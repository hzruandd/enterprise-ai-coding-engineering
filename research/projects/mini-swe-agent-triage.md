---
id: enterprise-ai-coding-engineering/research/projects/mini-swe-agent
title: mini-SWE-agent Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Architecture", "Verification", "Acceptance"]
applicable_tools: ["mini-SWE-agent"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: MEDIUM
supersedes: null
---

# mini-SWE-agent Triage

## 结论

进入 `POC_CANDIDATE`，仍保留在 Research 层。它的 Agent Loop 较小、模型与执行环境可替换，适合作为可观察、可重复的实验基线。

## 已核验事实

- [官方仓库](https://github.com/SWE-agent/mini-swe-agent)定位为解决 GitHub Issue 或辅助命令行工作的最小软件工程 Agent，支持本地、Docker/Podman 等执行环境。
- [许可证](https://github.com/SWE-agent/mini-swe-agent/blob/main/LICENSE.md)为 MIT。
- 项目 README 的 SWE-bench 分数属于项目方声明；本轮没有下载数据集或复现实验。

## 企业适用性假设

适合研究 Agent Loop、模型路由、环境隔离和 Trace，而不是直接作为企业生产平台。

## 主要风险

- “代码少”不等于默认安全；Shell、网络、模型和环境权限仍需外部 Harness。
- Benchmark 成绩不代表企业任务质量。
- 模型供应商和 LiteLLM/OpenRouter 等可选路径会改变依赖与数据边界。

## 下一 Gate

固定模型、版本、测试仓库和预算，先运行无密钥模拟/最小任务，再设计 SWE-bench 子集；记录完整命令、补丁、测试和成本。
