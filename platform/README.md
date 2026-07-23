---
id: enterprise-ai-coding-engineering/platform/readme
title: Platform 区说明
version: 0.1.0
status: REVIEWED
recommendation: NOT_APPLICABLE
owner: platform-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Architecture", "Operation"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# Platform 区

`platform/` 预留给经需求验证后的 Harness 参考实现，例如 Orchestrator、Worker、Sandbox、Dashboard 和 Integrations。

- 准入：必须有 Phase 5 试点需求、明确契约、威胁模型、运维边界和 build-vs-buy 决策。
- 禁止：Phase 0–1 造完整平台；连接生产；把特定供应商能力冒充通用架构；无测试的演示服务。
- 当前阶段：仅记录边界，对应 [ADR-0006](../adr/0006-defer-full-agent-platform.md)。
- 后续阶段：最早在 Phase 6 进入实现，且仍需人类批准具体范围。
