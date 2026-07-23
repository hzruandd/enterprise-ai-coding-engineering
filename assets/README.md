---
id: enterprise-ai-coding-engineering/assets/readme
title: Verified 资产区说明
version: 0.1.0
status: REVIEWED
recommendation: CONDITIONAL
owner: asset-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Implementation", "Verification", "Review", "Learning"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# Verified 资产区

`assets/` 只保存完成验证的 Prompt、Skill、Agent、Workflow、Gate、Policy 和 Template。

- 准入：资产契约完整，真实任务验证与 Eval 通过，独立审查完成，License 已核验，证据可复现。
- 禁止：Candidate、无 Owner 片段、未经测试的提示词、生产密钥、来源不明的第三方代码。
- 采用：`VERIFIED` 仅表示证据成熟度；是否推荐由独立的 `recommendation` 表达。
- 当前阶段：仅提供 [资产说明模板](templates/asset.md)，没有声称任何正式资产已验证。
- 后续阶段：Phase 4 通过 Gate 的 Candidate 才能进入正式子目录。
