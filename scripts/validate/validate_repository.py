#!/usr/bin/env python3
"""Validate the Phase 0-1 repository contracts using only Python stdlib."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit, urlunsplit


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

REQUIRED_TOP_LEVEL = (
    "README.md",
    "PROJECT_CHARTER.md",
    "ROADMAP.md",
    "GOVERNANCE.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "CHANGELOG.md",
)

REQUIRED_AREA_READMES = (
    "docs/README.md",
    "research/README.md",
    "staging/README.md",
    "catalog/README.md",
    "assets/README.md",
    "evals/README.md",
    "platform/README.md",
    "examples/README.md",
)

REQUIRED_SCHEMAS = (
    "catalog/schemas/document-metadata.schema.json",
    "catalog/schemas/source-registration.schema.json",
    "catalog/schemas/project-triage.schema.json",
    "catalog/schemas/project-full-review.schema.json",
    "catalog/schemas/asset.schema.json",
    "catalog/schemas/task-run-state.schema.json",
)

REQUIRED_TEMPLATES = (
    "adr/template.md",
    "research/templates/source-registration.md",
    "research/templates/project-assessment.md",
    "assets/templates/asset.md",
    "reports/templates/phase-acceptance.md",
)

REQUIRED_ADRS = tuple(
    f"adr/{number:04d}-{name}.md"
    for number, name in (
        (1, "repository-positioning-and-capability-domains"),
        (2, "three-stage-asset-admission"),
        (3, "deterministic-workflow-first"),
        (4, "independent-completion-evidence"),
        (5, "schema-driven-metadata"),
        (6, "defer-full-agent-platform"),
    )
)

CATALOG_FILES = (
    "catalog/sources.yaml",
    "catalog/projects.yaml",
    "catalog/assets.yaml",
    "catalog/task-runs.yaml",
)

MARKDOWN_METADATA_EXCLUSIONS = {
    "enterprise-ai-coding-harness-master-instruction-v3.0.md",
    *REQUIRED_TEMPLATES,
}

VALID_JSON_SCHEMA_TYPES = {
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
}

MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.counts: dict[str, int] = {
            "markdown_documents": 0,
            "schemas": 0,
            "catalog_entries": 0,
            "local_links": 0,
        }

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def load_json(path: Path, report: ValidationReport) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"{relative(path)}: cannot parse JSON-compatible YAML/JSON: {exc}")
        return None


def parse_front_matter(path: Path, report: ValidationReport) -> dict[str, Any] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        report.error(f"{relative(path)}: cannot read Markdown: {exc}")
        return None

    if not lines or lines[0].strip() != "---":
        report.error(f"{relative(path)}: missing opening Markdown front matter delimiter")
        return None

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        report.error(f"{relative(path)}: missing closing Markdown front matter delimiter")
        return None

    metadata: dict[str, Any] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            report.error(
                f"{relative(path)}:{line_number}: front matter must use one key per line"
            )
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if key in metadata:
            report.error(f"{relative(path)}:{line_number}: duplicate metadata key {key!r}")
            continue
        try:
            if raw_value in {"null", "~"}:
                value: Any = None
            elif raw_value.startswith(("[", "{", '"')):
                value = json.loads(raw_value)
            elif raw_value in {"true", "false"}:
                value = raw_value == "true"
            else:
                value = raw_value
        except json.JSONDecodeError as exc:
            report.error(f"{relative(path)}:{line_number}: invalid metadata value: {exc}")
            continue
        metadata[key] = value
    return metadata


def matches_type(instance: Any, expected: str) -> bool:
    if expected == "null":
        return instance is None
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "object":
        return isinstance(instance, dict)
    return False


def validate_format(value: str, format_name: str) -> bool:
    try:
        if format_name == "date":
            date.fromisoformat(value)
            return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))
        if format_name == "date-time":
            datetime.fromisoformat(value.replace("Z", "+00:00"))
            return "T" in value
        if format_name == "uri":
            parsed = urlsplit(value)
            return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except ValueError:
        return False
    return True


def validate_instance(
    instance: Any,
    schema: dict[str, Any],
    location: str,
    report: ValidationReport,
) -> None:
    expected = schema.get("type")
    if expected is not None:
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(matches_type(instance, item) for item in expected_types):
            report.error(f"{location}: expected type {expected!r}, got {type(instance).__name__}")
            return

    if "const" in schema and instance != schema["const"]:
        report.error(f"{location}: expected constant {schema['const']!r}")

    if "enum" in schema and instance not in schema["enum"]:
        report.error(f"{location}: value {instance!r} is not in enum {schema['enum']!r}")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            report.error(f"{location}: string is shorter than minLength")
        pattern = schema.get("pattern")
        if pattern and re.search(pattern, instance) is None:
            report.error(f"{location}: value {instance!r} does not match {pattern!r}")
        format_name = schema.get("format")
        if format_name and not validate_format(instance, format_name):
            report.error(f"{location}: value {instance!r} is not a valid {format_name}")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            report.error(f"{location}: array is shorter than minItems")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                validate_instance(item, item_schema, f"{location}[{index}]", report)

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                report.error(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                validate_instance(value, properties[key], f"{location}.{key}", report)
            elif schema.get("additionalProperties") is False:
                report.error(f"{location}: unexpected property {key!r}")


def validate_schema_structure(
    schema: Any,
    location: str,
    report: ValidationReport,
) -> None:
    if not isinstance(schema, dict):
        report.error(f"{location}: schema must be an object")
        return

    expected = schema.get("type")
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        if not types or not all(item in VALID_JSON_SCHEMA_TYPES for item in types):
            report.error(f"{location}.type: invalid JSON Schema type declaration")

    required = schema.get("required")
    if required is not None and (
        not isinstance(required, list)
        or not all(isinstance(item, str) for item in required)
        or len(required) != len(set(required))
    ):
        report.error(f"{location}.required: must be a unique string array")

    properties = schema.get("properties")
    if properties is not None:
        if not isinstance(properties, dict):
            report.error(f"{location}.properties: must be an object")
        else:
            for key, child in properties.items():
                validate_schema_structure(child, f"{location}.properties.{key}", report)

    items = schema.get("items")
    if items is not None:
        validate_schema_structure(items, f"{location}.items", report)

    pattern = schema.get("pattern")
    if pattern is not None:
        try:
            re.compile(pattern)
        except (TypeError, re.error) as exc:
            report.error(f"{location}.pattern: invalid regular expression: {exc}")

    enum = schema.get("enum")
    if enum is not None and (not isinstance(enum, list) or not enum):
        report.error(f"{location}.enum: must be a non-empty array")


def validate_required_files(report: ValidationReport) -> None:
    required = (
        *REQUIRED_TOP_LEVEL,
        *REQUIRED_AREA_READMES,
        *REQUIRED_SCHEMAS,
        *REQUIRED_TEMPLATES,
        *REQUIRED_ADRS,
        *CATALOG_FILES,
        "docs/overview/metadata-standard.md",
        "reports/phase-0-1-task-status.md",
        "scripts/validate/validate_repository.py",
    )
    for item in required:
        if not (REPOSITORY_ROOT / item).is_file():
            report.error(f"{item}: required file is missing")


def load_schemas(report: ValidationReport) -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    schema_ids: dict[str, str] = {}
    for path in sorted((REPOSITORY_ROOT / "catalog/schemas").glob("*.schema.json")):
        loaded = load_json(path, report)
        if loaded is None:
            continue
        if not isinstance(loaded, dict):
            report.error(f"{relative(path)}: root schema must be an object")
            continue
        if not isinstance(loaded.get("$schema"), str):
            report.error(f"{relative(path)}: missing string $schema declaration")
        schema_id = loaded.get("$id")
        if not isinstance(schema_id, str):
            report.error(f"{relative(path)}: missing string $id")
        elif schema_id in schema_ids:
            report.error(
                f"{relative(path)}: duplicate schema $id also used by {schema_ids[schema_id]}"
            )
        else:
            schema_ids[schema_id] = relative(path)
        validate_schema_structure(loaded, relative(path), report)
        schemas[path.name] = loaded
        report.counts["schemas"] += 1
    return schemas


def validate_markdown(
    schemas: dict[str, dict[str, Any]],
    report: ValidationReport,
) -> None:
    metadata_schema = schemas.get("document-metadata.schema.json")
    if metadata_schema is None:
        return
    seen_ids: dict[str, str] = {}
    for path in sorted(REPOSITORY_ROOT.rglob("*.md")):
        item = relative(path)
        if item in MARKDOWN_METADATA_EXCLUSIONS or "/templates/" in f"/{item}":
            continue
        metadata = parse_front_matter(path, report)
        if metadata is None:
            continue
        validate_instance(metadata, metadata_schema, f"{item}:metadata", report)
        document_id = metadata.get("id")
        if isinstance(document_id, str):
            if document_id in seen_ids:
                report.error(
                    f"{item}: duplicate document id {document_id!r}; "
                    f"already used by {seen_ids[document_id]}"
                )
            else:
                seen_ids[document_id] = item
        report.counts["markdown_documents"] += 1


def validate_catalog_header(
    catalog: Any,
    path: Path,
    list_names: Iterable[str],
    report: ValidationReport,
) -> bool:
    if not isinstance(catalog, dict):
        report.error(f"{relative(path)}: catalog root must be an object")
        return False
    if not isinstance(catalog.get("schema_version"), str):
        report.error(f"{relative(path)}: schema_version must be a string")
    for list_name in list_names:
        if not isinstance(catalog.get(list_name), list):
            report.error(f"{relative(path)}: {list_name} must be an array")
            return False
    return True


def normalized_url(url: str) -> str:
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            path,
            parsed.query,
            "",
        )
    )


def validate_catalogs(
    schemas: dict[str, dict[str, Any]],
    report: ValidationReport,
) -> None:
    sources_path = REPOSITORY_ROOT / "catalog/sources.yaml"
    sources = load_json(sources_path, report)
    if validate_catalog_header(sources, sources_path, ("sources",), report):
        source_schema = schemas.get("source-registration.schema.json")
        seen_urls: dict[str, str] = {}
        for index, entry in enumerate(sources["sources"]):
            location = f"catalog/sources.yaml.sources[{index}]"
            if source_schema:
                validate_instance(entry, source_schema, location, report)
            if isinstance(entry, dict) and isinstance(entry.get("url"), str):
                normalized = normalized_url(entry["url"])
                if normalized in seen_urls:
                    report.error(
                        f"{location}: duplicate source URL; first seen at {seen_urls[normalized]}"
                    )
                else:
                    seen_urls[normalized] = location
            report.counts["catalog_entries"] += 1

    projects_path = REPOSITORY_ROOT / "catalog/projects.yaml"
    projects = load_json(projects_path, report)
    if validate_catalog_header(projects, projects_path, ("triage", "full_reviews"), report):
        mapping = (
            ("triage", "project-triage.schema.json"),
            ("full_reviews", "project-full-review.schema.json"),
        )
        for list_name, schema_name in mapping:
            schema = schemas.get(schema_name)
            for index, entry in enumerate(projects[list_name]):
                if schema:
                    validate_instance(
                        entry,
                        schema,
                        f"catalog/projects.yaml.{list_name}[{index}]",
                        report,
                    )
                report.counts["catalog_entries"] += 1

    assets_path = REPOSITORY_ROOT / "catalog/assets.yaml"
    assets = load_json(assets_path, report)
    if validate_catalog_header(assets, assets_path, ("assets",), report):
        asset_schema = schemas.get("asset.schema.json")
        for index, entry in enumerate(assets["assets"]):
            location = f"catalog/assets.yaml.assets[{index}]"
            if asset_schema:
                validate_instance(entry, asset_schema, location, report)
            if isinstance(entry, dict):
                lifecycle = entry.get("lifecycle_stage")
                asset_path = entry.get("path")
                if isinstance(asset_path, str):
                    normalized_path = asset_path.replace("\\", "/")
                    if not (REPOSITORY_ROOT / normalized_path).exists():
                        report.error(f"{location}.path: target does not exist: {asset_path}")
                    if lifecycle == "CANDIDATE" and not normalized_path.startswith("staging/"):
                        report.error(f"{location}: Candidate asset must be under staging/")
                    if lifecycle == "VERIFIED" and not normalized_path.startswith("assets/"):
                        report.error(f"{location}: Verified asset must be under assets/")
            report.counts["catalog_entries"] += 1

    runs_path = REPOSITORY_ROOT / "catalog/task-runs.yaml"
    runs = load_json(runs_path, report)
    if validate_catalog_header(runs, runs_path, ("runs",), report):
        run_schema = schemas.get("task-run-state.schema.json")
        seen_runs: set[str] = set()
        for index, entry in enumerate(runs["runs"]):
            location = f"catalog/task-runs.yaml.runs[{index}]"
            if run_schema:
                validate_instance(entry, run_schema, location, report)
            if isinstance(entry, dict) and isinstance(entry.get("run_id"), str):
                if entry["run_id"] in seen_runs:
                    report.error(f"{location}: duplicate run_id {entry['run_id']!r}")
                seen_runs.add(entry["run_id"])
            report.counts["catalog_entries"] += 1


def validate_asset_placement(report: ValidationReport) -> None:
    for base, forbidden in (("assets", "CANDIDATE"), ("staging", "VERIFIED")):
        base_path = REPOSITORY_ROOT / base
        for path in base_path.rglob("*"):
            if not path.is_file() or "/templates/" in f"/{relative(path)}":
                continue
            if path.name == "README.md":
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            patterns = (
                rf"(?im)^\s*lifecycle_stage\s*:\s*[\"']?{forbidden}[\"']?\s*$",
                rf'(?i)"lifecycle_stage"\s*:\s*"{forbidden}"',
            )
            if any(re.search(pattern, content) for pattern in patterns):
                report.error(
                    f"{relative(path)}: {forbidden} asset is in the wrong physical area"
                )


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target)


def validate_local_links(report: ValidationReport) -> None:
    for path in sorted(REPOSITORY_ROOT.rglob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            report.error(f"{relative(path)}: cannot read links: {exc}")
            continue
        for match in MARKDOWN_LINK_PATTERN.finditer(content):
            target = link_target(match.group(1))
            if (
                not target
                or target.startswith(("#", "{{"))
                or urlsplit(target).scheme in {"http", "https", "mailto"}
            ):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            if path_part.startswith("/"):
                candidate = REPOSITORY_ROOT / path_part.lstrip("/")
            else:
                candidate = path.parent / path_part
            try:
                candidate.resolve().relative_to(REPOSITORY_ROOT.resolve())
            except ValueError:
                report.error(
                    f"{relative(path)}: local link escapes repository: {target}"
                )
                continue
            if not candidate.exists():
                report.error(f"{relative(path)}: broken local link: {target}")
            report.counts["local_links"] += 1


def run_validation() -> ValidationReport:
    report = ValidationReport()
    validate_required_files(report)
    schemas = load_schemas(report)
    validate_markdown(schemas, report)
    validate_catalogs(schemas, report)
    validate_asset_placement(report)
    validate_local_links(report)
    return report


def print_report(report: ValidationReport, quiet: bool = False) -> None:
    if not quiet:
        print("Enterprise AI Coding Engineering repository validation")
        print(f"Root: {REPOSITORY_ROOT}")
        print(
            "Checked: "
            f"{report.counts['markdown_documents']} governed Markdown documents, "
            f"{report.counts['schemas']} JSON Schemas, "
            f"{report.counts['catalog_entries']} Catalog entries, "
            f"{report.counts['local_links']} local links"
        )
        for warning in report.warnings:
            print(f"WARNING: {warning}")
        for error in report.errors:
            print(f"ERROR: {error}")
    if report.errors:
        print(f"RESULT: FAIL ({len(report.errors)} error(s), {len(report.warnings)} warning(s))")
    else:
        print(f"RESULT: PASS (0 errors, {len(report.warnings)} warning(s))")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="only print the final result")
    args = parser.parse_args()
    report = run_validation()
    print_report(report, quiet=args.quiet)
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
