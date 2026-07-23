---
id: enterprise-ai-coding-engineering/research/projects/aider
title: Aider Triage
version: 1.0.0
status: REVIEWED
recommendation: PENDING
owner: research-owner
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Implementation", "Verification"]
applicable_tools: ["Aider"]
source_type: OFFICIAL
evidence_level: OFFICIAL
risk_level: MEDIUM
supersedes: null
---

# Aider Triage

## 结论

进入 `POC_CANDIDATE`，仍保留在 Research 层。其 Repo Map、Git 工作方式和可配置 Lint/Test 适合验证“人类交互 + 确定性反馈”的组合。

## 已核验事实

- [官方仓库](https://github.com/Aider-AI/aider)定位为终端 AI Pair Programming 工具，许可证为 Apache-2.0，2026 年仍有仓库活动。
- [Lint/Test 文档](https://aider.chat/docs/usage/lint-test.html)支持编辑后运行确定性命令，并以非零退出码反馈失败。
- [许可证原文](https://github.com/Aider-AI/aider/blob/main/LICENSE.txt)可访问；本轮没有安装依赖或连接任何模型。

## 企业适用性假设

适合验证受控文件集、上下文压缩、自动 lint/test 和 Git 证据；相比全自动 Agent，更适合作为低自治对照。

## 主要风险

- 默认 Git 自动提交和 pre-commit 行为必须与组织策略对齐。
- Shell/Test 命令与模型 Key 仍需要沙箱和密钥隔离。
- Repo Map 的有效性和 Token 成本需要在本项目样本上测量。

## 下一 Gate

在隔离仓库禁用非必要自动提交，固定文件范围、测试命令和模型预算，对照手工上下文与 Repo Map 的质量/成本。
