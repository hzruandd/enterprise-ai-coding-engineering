---
id: enterprise-ai-coding-engineering/catalog/readme
title: Catalog 区说明
version: 0.2.0
status: REVIEWED
recommendation: RECOMMENDED
owner: governance-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Requirement", "Verification", "Review", "Learning"]
applicable_tools: ["Python"]
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# Catalog 区

`catalog/` 是来源、项目、资产和任务运行记录的机器可校验索引，`schemas/` 保存 JSON Schema。

- 准入：唯一 ID、明确 Schema 版本、合法枚举、可追溯证据和责任人。
- 禁止：未验证事实、明文密钥、私有思维过程、与正文冲突的生命周期状态。
- 格式：`.yaml` 采用 JSON 语法兼容的 YAML 1.2，以便仅用 Python 标准库确定性解析。
- 当前数据：[来源](sources.yaml)含 20 个官方来源，[项目](projects.yaml)含 8 个 Triage，[资产](assets.yaml)仍为空，[任务运行](task-runs.yaml)记录 Phase 执行。
- 后续阶段：来源进入 Phase 2 后逐条更新访问状态；Catalog 变化必须与对应记录同一提交。
