---
id: enterprise-ai-coding-engineering/readme
title: Enterprise AI Coding Engineering
version: 1.0.0
status: REVIEWED
recommendation: RECOMMENDED
owner: Jake Ruan
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Idea", "Requirement", "Architecture", "Plan", "Verification", "Review", "Learning"]
applicable_tools: ["Codex", "Claude Code", "Cursor", "Gemini CLI"]
source_type: DECISION
evidence_level: DECISION
risk_level: LOW
supersedes: null
---

# Enterprise AI Coding Engineering

面向企业软件研发全生命周期的 AI Coding 工程化参考体系。本仓库交付可执行、可验证、可审计、可治理、可持续演进的规范、资产契约、评测方法与参考实现，而不是链接收藏、Prompt 大全或 Agent 演示。

## 当前状态

Phase 0（立项与边界）和 Phase 1（顶层架构与仓库骨架）已建立。当前内容定义项目边界、六个能力域、治理基线、三级资产准入、Schema、模板、ADR 和仓库校验；尚未开展 Phase 2 外部项目调研，也没有建设完整 Agent 平台。

## 唯一交付生命周期

`Idea → Requirement → PRD → Spec → Architecture → Plan → BDD → TDD → Implementation → Verification → Review → Security → Release → Acceptance → Operation → Learning`

## 六个能力域

| 能力域 | 交付重点 |
|---|---|
| Knowledge | 概念、术语、模式、原理与行业进展 |
| Methodology | SDD、ADD、BDD、TDD、Review、Release、Learning |
| Assets | Prompt、Skill、Agent、Workflow、Gate、Template、Policy |
| Governance | 任务、权限、审批、质量、安全、成本与审计 |
| Evaluation | Eval、Dataset、Baseline、Trace、Metrics、Regression |
| Platform | Orchestrator、Worker、Sandbox、Dashboard、Integrations |

## 仓库导航

- [项目章程](PROJECT_CHARTER.md)：定位、范围、成功标准和非目标。
- [治理规则](GOVERNANCE.md)：状态机、权限、证据、失败处理和审计。
- [路线图](ROADMAP.md)：各 Phase 的进入与退出条件。
- [贡献指南](CONTRIBUTING.md)：从研究到 Verified 资产的贡献流程。
- [Agent 约束](AGENTS.md)：AI Coding 工具在本仓库中的工作边界。
- [文档地图](docs/README.md)、[研究区](research/README.md)、[Catalog](catalog/README.md)、[正式资产](assets/README.md)、[评测](evals/README.md)。
- [架构决策记录](adr/README.md)。
- [Phase 0–1 验收报告](reports/phase-0-1-acceptance.md)。

研究事实放入 `research/`，通过 Triage 的 Candidate 放入 `staging/`，完成真实验证、独立审查和许可证核验后才进入 `assets/`。三个区域不得混用。

## 本地校验

要求 Python 3.9+，无第三方依赖：

```bash
python scripts/validate/validate_repository.py
```

Catalog 的 `.yaml` 文件采用 JSON 语法（JSON 是 YAML 1.2 的子集），由标准库解析。校验涵盖必要文件、Markdown 元数据、Schema、Catalog、ID/URL 去重、资产分层和本地相对链接。

## 许可证

仓库已有 [Apache License 2.0](LICENSE)。外部来源、代码和资产仍须逐项完成许可证核验，仓库许可证不代表第三方内容自动获准引入。
