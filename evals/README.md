---
id: enterprise-ai-coding-engineering/evals/readme
title: Evaluation 区说明
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: evaluation-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["BDD", "TDD", "Verification", "Acceptance", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# Evaluation 区

`evals/` 保存 Dataset、Rubric、Baseline、Runner 和 Report，用于独立判断 Agent 与资产是否满足质量、成本和安全目标。

- 准入：任务代表性、预期结果、评分规则、版本和运行环境可复现。
- 禁止：只展示成功案例、泄露敏感数据、用实现者主观评价替代 Gate、覆盖失败基线。
- 当前阶段：只定义职责，不虚构 Dataset 或基线。
- 后续阶段：Phase 3 设计 Eval，Phase 4 建立基线和回归，Phase 5 增加企业试点指标。
