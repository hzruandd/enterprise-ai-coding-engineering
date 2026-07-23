---
id: enterprise-ai-coding-engineering/adr/readme
title: 架构决策记录索引
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: architecture-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Architecture", "Review", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: LOW
supersedes: null
---

# 架构决策记录

ADR 记录对长期结构、治理或成本有影响的决策。`ACCEPTED` 表示当前基线，不代表永不变化；变化通过新的 ADR 替代，历史记录不删除。

| ADR | 决策 | 状态 |
|---|---|---|
| [0001](0001-repository-positioning-and-capability-domains.md) | 仓库定位与六能力域 | ACCEPTED |
| [0002](0002-three-stage-asset-admission.md) | Research/Candidate/Verified 三级准入 | ACCEPTED |
| [0003](0003-deterministic-workflow-first.md) | 确定性 Workflow 优先、Agentic 适量 | ACCEPTED |
| [0004](0004-independent-completion-evidence.md) | AI 不得自证完成 | ACCEPTED |
| [0005](0005-schema-driven-metadata.md) | 元数据与 Schema 驱动 | ACCEPTED |
| [0006](0006-defer-full-agent-platform.md) | 当前阶段暂不建设完整 Agent 平台 | ACCEPTED |

新决策使用 [ADR 模板](template.md)，编号单调递增。
