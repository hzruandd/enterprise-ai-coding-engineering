---
id: enterprise-ai-coding-engineering/adr/0004
title: ADR-0004 AI 不得自证完成
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: governance-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Verification", "Review", "Security", "Acceptance"]
applicable_tools: []
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# ADR-0004：AI 不得自证完成

- 决策状态：ACCEPTED
- 决策者：项目技术负责人（由总控指令授权）

## 背景

生成结果的 Agent 容易遗漏自身假设或把未运行的检查描述为完成。企业交付需要可观察、可复现且与实现者判断相分离的证据。

## 备选方案

1. Agent 自述完成：成本低但不可采信。
2. 全部人工复核：可靠但吞吐有限。
3. 风险分级的自动证据、独立 Reviewer 与人工审批组合。

## 决策

实现者可以自检，但 `DONE` 至少需要自动测试返回码、Schema/Policy 校验、静态/安全扫描、独立 Reviewer 或人工审批之一。高风险发布和生产动作始终需要人工审批。

## 后果

- 验收报告必须记录真实命令与输出摘要。
- 未运行或失败的 Gate 必须显式列为未完成。
- 需要维护测试、Schema、Reviewer 角色和证据引用。

## 验证与复审

审计 Task/Run 的 `DONE` 转换是否都有证据。出现虚假完成或不可复现结果时，提高相应任务的独立 Gate。
