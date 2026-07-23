---
id: enterprise-ai-coding-engineering/research/projects/github-copilot-cloud-agent
title: GitHub Copilot cloud agent Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Implementation", "Verification", "Review", "Security"]
applicable_tools: ["GitHub Copilot"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: HIGH
supersedes: null
---

# GitHub Copilot cloud agent Triage

## 结论

进入 `FULL_REVIEW`。它与 GitHub 分支、Pull Request、Actions、安全扫描和审计日志深度集成，最接近托管式企业 Harness，但需要付费租户、仓库授权和组织 Policy 才能验证。

## 已核验事实

- [产品说明](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)描述异步任务执行并创建 Pull Request 的工作方式。
- [风险控制说明](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations)列出单分支写入、人工合并、Actions 审批、网络防火墙、安全扫描、Session/Audit Log 等控制。
- [GitHub 附加产品条款](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features)说明 Copilot Business/Enterprise 受产品专用条款约束；这不是可再分发源码许可证。

## 企业适用性假设

适合验证“托管 Agent + 原生 SCM Gate + 人工合并”的参考流程，并与本地 CLI 模式比较权限和审计责任。

## 主要风险

- 评估需要组织租户、计费额度和管理员配置，本阶段未访问。
- 防火墙允许项、MCP、Setup Steps 和专用 Secrets 会改变数据暴露面。
- 内置扫描降低风险但不能替代独立 Review 与组织 Gate。

## Full Review 问题

确认租户数据政策、区域、预算、管理员 Policy、日志保留、MCP/Secrets 边界和自动化触发规则，再申请非生产仓库试点。
