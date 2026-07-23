---
id: enterprise-ai-coding-engineering/research/comparisons/phase-2-initial-coding-agent-triage
title: Phase 2 首批 Coding Agent Triage 比较
version: 1.0.0
status: REVIEWED
recommendation: CONDITIONAL
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Requirement", "Architecture", "Plan"]
applicable_tools: []
source_type: INFERENCE
evidence_level: OFFICIAL
risk_level: MEDIUM
supersedes: null
---

# Phase 2 首批 Coding Agent Triage 比较

## 决策摘要

本轮不选“统一标准工具”，而是形成两条后续验证队列：

- 可直接设计隔离 PoC：Codex CLI、mini-SWE-agent、Aider、Continue。
- 先做 Full Review：Claude Code、GitHub Copilot cloud agent、Gemini CLI、OpenHands。

这只是 Triage 行动结论，不是 `Candidate`、`Verified` 或企业采用推荐。

## 比较矩阵

| 对象 | 执行形态 | License/条款 | Harness 观察点 | 维护 | 初步行动 |
|---|---|---|---|---|---|
| Codex CLI | 本地 CLI/自动化 | Apache-2.0；模型服务另计 | Sandbox、Approval、Headless | ACTIVE | POC_CANDIDATE |
| Claude Code | 本地/IDE/GitHub 商业产品 | Commercial Terms | Gateway、权限、版本与数据 | ACTIVE | FULL_REVIEW |
| Copilot cloud agent | GitHub 托管异步 Agent | GitHub Copilot 产品条款 | 单分支、PR、扫描、审计、人工合并 | ACTIVE | FULL_REVIEW |
| Gemini CLI | 开源 CLI + Google 服务 | Apache-2.0；服务条款另计 | Tool Policy、Sandbox、企业认证 | ACTIVE | FULL_REVIEW |
| OpenHands | SDK/CLI/自托管/托管 | 核心 MIT；enterprise/ 商业许可 | Runtime、Sandbox Provider、网络/挂载 | ACTIVE | FULL_REVIEW |
| mini-SWE-agent | 最小研究 Agent | MIT | Agent Loop、环境、Benchmark Trace | ACTIVE | POC_CANDIDATE |
| Aider | 交互式本地 CLI | Apache-2.0 | Repo Map、Git、Lint/Test | ACTIVE | POC_CANDIDATE |
| Continue | CLI + PR AI Checks | Apache-2.0 | Reviewer、Rubric、CI Status | ACTIVE | POC_CANDIDATE |

## 共同结论

1. 开源 Harness 与模型/托管服务条款必须分开核验。
2. “有沙箱”不足以证明安全；网络、挂载、密钥、操作系统和默认策略同样决定边界。
3. 托管 Agent 的原生审计和分支控制更完整，但需要租户 Policy、成本和数据合同。
4. 最小 Agent 便于研究可解释性，不代表具备企业权限、恢复和运维能力。
5. AI Review 适合补充独立证据，不能替代确定性 Gate。

## Phase 3 输入建议

若进入下一阶段，先为四个 `POC_CANDIDATE` 设计同一组非生产任务与 Rubric，不立即安装或运行。四个 `FULL_REVIEW` 对象先补齐条款、数据流、版本、管理面和组件 License，未过 Gate 不进入 PoC。
