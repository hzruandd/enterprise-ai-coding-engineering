---
id: enterprise-ai-coding-engineering/adr/0002
title: ADR-0002 Research Candidate Verified 三级准入
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: governance-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Requirement", "Verification", "Review", "Acceptance"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# ADR-0002：Research/Candidate/Verified 三级准入

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

外部项目的热度、作者声誉或 README 声明不能证明企业适用性。未经隔离的第三方资产还可能带来许可证、安全和维护风险。

## 备选方案

1. 直接收录：速度快，但成熟度和推荐结论混乱。
2. 二级草稿/正式：无法区分事实研究与已具备 PoC 价值的候选。
3. Research/Candidate/Verified：多一道 Gate，但证据链清晰。

## 决策

采用三级准入并物理隔离：`research/` 保存事实与评估，`staging/` 保存通过 Triage 的 Candidate，`assets/` 只保存 Verified。Verified 需要真实任务验证、独立审查、License 核验和可复现实验。

## 后果

- Candidate 不得因“看起来可用”进入正式区。
- 验证完成也不自动等于推荐采用，继续使用独立 `recommendation`。
- 淘汰结果保留原因和证据，避免重复评估。

## 验证与复审

仓库校验器检查正式区中的 Candidate 标记。Phase 4 后按转化率、淘汰率和验证周期复审 Gate 成本。
