---
id: enterprise-ai-coding-engineering/research/projects/openhands
title: OpenHands Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Architecture", "Implementation", "Verification"]
applicable_tools: ["OpenHands"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: HIGH
supersedes: null
---

# OpenHands Triage

## 结论

进入 `FULL_REVIEW`。其 SDK、CLI、Sandbox Provider 和部署形态对 Harness 架构研究价值高，但核心与 `enterprise/` 的许可证边界、网络和挂载风险必须先拆清。

## 已核验事实

- [官方仓库](https://github.com/OpenHands/OpenHands)提供 Agent SDK、CLI 与企业产品；README 声明核心为 MIT，而 `enterprise/` 目录使用独立商业 source-available 许可。
- [Sandbox 文档](https://docs.openhands.dev/openhands/usage/sandboxes/overview)列出推荐 Docker、无容器隔离的 Process 以及 Remote Provider。
- 官方文档明确网络、凭据和挂载目录会扩大风险边界；本轮未部署任何模式。

## 企业适用性假设

适合研究 Runtime/Sandbox 抽象、Agent SDK 与自托管边界，而不是直接采用完整产品。

## 主要风险

- 混合许可证要求按目录与制品核验，不能用“仓库是 MIT”概括。
- Process 模式不提供容器隔离；挂载与网络策略需要额外 Gate。
- 自托管会引入镜像、模型、密钥、监控和升级责任。

## Full Review 问题

形成组件级 SBOM/许可证清单，检查 Sandbox 默认值、网络与挂载、资源限额、Trace、身份认证和部署运维成本。
