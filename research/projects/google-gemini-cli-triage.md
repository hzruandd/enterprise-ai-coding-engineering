---
id: enterprise-ai-coding-engineering/research/projects/google-gemini-cli
title: Google Gemini CLI Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Implementation", "Verification", "Review"]
applicable_tools: ["Gemini CLI"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: HIGH
supersedes: null
---

# Google Gemini CLI Triage

## 结论

进入 `FULL_REVIEW`。CLI 源码和工具控制适合研究，但 2026 年服务接入迁移使认证路径和长期支持边界成为进入 PoC 前的必查项。

## 已核验事实

- [官方仓库](https://github.com/google-gemini/gemini-cli)将其定位为开源终端 Agent，许可证为 Apache-2.0。
- [条款说明](https://github.com/google-gemini/gemini-cli/blob/main/docs/resources/tos-privacy.md)明确 CLI 软件许可证与其访问的 Google 服务条款相互独立，并列出多种认证方式。
- 官方仓库的[迁移公告](https://github.com/google-gemini/gemini-cli/discussions/27274)说明 2026-06-18 后消费者免费/Pro/Ultra 路径转向 Antigravity CLI，而 Enterprise 和付费 API 路径继续受支持。

## 企业适用性假设

适合作为 Apache-2.0 CLI 与 Google Cloud 企业服务组合的对照，但 PoC 必须以明确仍受支持的企业认证路径为前提。

## 主要风险

- 开源 CLI 可用不代表任何后端服务免费或长期可用。
- 认证方式决定数据、配额、隐私和合同边界。
- 迁移期功能差异可能导致文档、版本和实际行为漂移。

## Full Review 问题

确认企业支持矩阵、Vertex AI/Enterprise 认证、数据驻留、遥测、沙箱强度、版本路线图与 Antigravity 的职责边界。
