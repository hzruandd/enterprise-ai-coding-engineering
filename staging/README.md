---
id: enterprise-ai-coding-engineering/staging/readme
title: Candidate 暂存区说明
version: 0.1.0
status: REVIEWED
recommendation: CONDITIONAL
owner: asset-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Plan", "Implementation", "Verification"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: MEDIUM
supersedes: null
---

# Candidate 暂存区

`staging/` 只保存已通过 Triage、等待隔离 PoC 或独立审查的 Candidate Prompt、Skill、Agent 和 Workflow。

- 准入：有 Triage 记录、Owner、验证计划、风险、许可证初判和淘汰条件。
- 禁止：把 Candidate 放入 `assets/`；连接生产或真实密钥；未经审查直接向团队推荐采用。
- 退出：验证失败则记录原因并淘汰；完成真实任务验证、独立审查、License 核验和可复现证据后才可进入 Verified。
- 后续阶段：Phase 3 才按真实候选建立子目录；Phase 0–1 不生成低质量占位资产。
