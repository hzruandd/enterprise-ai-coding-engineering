---
id: enterprise-ai-coding-engineering/research/sources/phase-2-initial
title: Phase 2 首批来源登记说明
version: 1.0.0
status: REVIEWED
recommendation: NOT_APPLICABLE
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Idea", "Requirement", "Architecture"]
applicable_tools: []
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: LOW
supersedes: null
---

# Phase 2 首批来源登记说明

## 范围与方法

本批选择 8 个对象，覆盖本地 CLI、托管异步 Agent、可组合 Agent Runtime、最小研究 Agent 和 AI Gate。选择依据是对 Harness 能力的覆盖与比较价值，不以 Star、媒体热度或供应商知名度作为采用证据。

Triage 只核验：

1. 官方入口与当前定位；
2. 源码许可证或托管服务条款；
3. 2026-07-23 可观察的维护信号；
4. 与权限、沙箱、验证、审计相关的公开能力；
5. 下一步行动和必须补齐的证据。

没有下载、安装、登录、付费、运行 PoC 或复制第三方内容。Catalog 中 20 个来源均保留原始 URL，访问状态为 `ACCESSIBLE`，用户原注为 `null`。

## 来源分布

| 对象 | 官方来源数 | 证据重点 |
|---|---:|---|
| OpenAI Codex CLI | 2 | 仓库、Apache-2.0、沙箱与自动化入口 |
| Anthropic Claude Code | 3 | 产品定位、商业许可、安装与认证 |
| GitHub Copilot cloud agent | 3 | 托管执行、风险控制、产品条款 |
| Google Gemini CLI | 3 | Apache-2.0、服务条款、2026 服务迁移 |
| OpenHands | 2 | 混合许可证、Sandbox Provider |
| mini-SWE-agent | 2 | 最小 Agent、MIT、执行环境 |
| Aider | 3 | Apache-2.0、Repo Map、Lint/Test |
| Continue | 2 | Apache-2.0、源码化 AI Checks |

结构化记录见 [来源 Catalog](../../catalog/sources.yaml)；项目结论见 [首批比较矩阵](../comparisons/phase-2-initial-coding-agent-triage.md)。

## 证据边界

- `ACCESSIBLE` 只表示本轮能访问相应页面，不表示内容永久可用。
- 官方 README 中的性能或能力声明仍是项目方声明；未运行 PoC 前不提升为 `EMPIRICAL`。
- 维护状态根据官方仓库、发布或文档近期活动判断，不等同于长期支持承诺。
- License 核验是工程登记，不构成法律意见；商业采用仍需组织内 License Reviewer。
