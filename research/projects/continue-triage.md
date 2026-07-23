---
id: enterprise-ai-coding-engineering/research/projects/continue
title: Continue Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Verification", "Review", "Security"]
applicable_tools: ["Continue CLI"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: MEDIUM
supersedes: null
---

# Continue Triage

## 结论

进入 `POC_CANDIDATE`，仍保留在 Research 层。当前公开定位是源码化、可在 Pull Request 上执行的 AI Checks，适合验证 Agent Review 与确定性 CI Gate 的组合。

## 已核验事实

- [官方仓库](https://github.com/continuedev/continue)将项目定位为 source-controlled AI checks，并通过 CLI 形成 Pull Request 状态检查。
- [许可证](https://github.com/continuedev/continue/blob/main/LICENSE)为 Apache-2.0，仓库在 2026 年有持续提交与发布。
- README 示例中的检查由 Markdown 定义，但本轮没有安装 CLI、调用模型或验证检查是否可重复。

## 企业适用性假设

适合作为独立 Reviewer/Gate 的候选，而不是主要代码实现 Agent；可与传统 lint、test、security scan 做职责分离。

## 主要风险

- LLM 判断具有非确定性，不能取代必需的编译、测试和安全扫描。
- 模型、权限、上下文与状态检查失败语义需要实测。
- 产品定位近年来变化，资产格式和兼容性需要锁定版本。

## 下一 Gate

选取 2–3 个明确 Rubric，在固定 PR Dataset 上测量一致性、误报、漏报、时延和成本，并验证失败是否能被 CI 确定性阻断。
