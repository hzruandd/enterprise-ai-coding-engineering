---
id: enterprise-ai-coding-engineering/governance
title: 企业 AI Coding 治理基线
version: 0.1.0
status: REVIEWED
recommendation: RECOMMENDED
owner: technical-lead
reviewers: []
created_at: 2026-07-23
updated_at: 2026-07-23
applicable_stages: ["Requirement", "Plan", "Implementation", "Verification", "Review", "Security", "Release", "Operation", "Learning"]
applicable_tools: ["Codex", "Claude Code", "Cursor", "Gemini CLI"]
source_type: DECISION
evidence_level: DECISION
risk_level: HIGH
supersedes: null
---

# 企业 AI Coding 治理基线

## 治理对象

治理覆盖任务、模型、上下文、工具、权限、代码与文档变更、验证证据、成本和人工审批。模型输出仅是候选结果，不能替代 Gate。

## 统一任务状态机

正常路径：

`DRAFT → READY → RUNNING → VERIFYING → REVIEWING → WAITING_APPROVAL → DONE`

异常状态：

`BLOCKED / RETRYING / FAILED / CANCELLED / ROLLED_BACK`

每次转换必须记录 Task ID、Run ID、触发者、时间、原状态、目标状态、原因或失败类型、证据引用和关联提交/产物。`DONE` 必须存在独立证据；需要审批但尚未批准时停在 `WAITING_APPROVAL`。

## 失败、重试与超时

| 类型 | 处理规则 |
|---|---|
| TRANSIENT | 指数退避并限次重试 |
| TOOL_ERROR | 修正安装、参数或协议后限次重试 |
| CODE_ERROR | 返回实现阶段，修复后重新验证 |
| TEST_FAILURE | 分析根因，不修改测试来掩盖失败 |
| POLICY_DENIED | 不得绕过，转人工处理 |
| MISSING_CONTEXT | 转 `BLOCKED` 并列出缺失输入 |
| BUDGET_EXCEEDED | 停止、缩小范围或经批准降级模型 |
| FATAL | 终止并保留现场与证据 |

同一逻辑错误不得原样重试；本仓库任务默认同类问题最多重试两次。任务需要总超时、单步超时和无进展超时，写操作的重试必须幂等。

## 权限分层

| 权限 | 默认策略 |
|---|---|
| READ | 在任务范围内允许 |
| WRITE_WORKTREE | 在隔离分支/worktree 和任务范围内允许 |
| EXECUTE_SAFE | 本地编译、测试与只读扫描允许 |
| GIT_COMMIT_LOCAL | 经任务明确授权后允许 |
| GIT_PUSH | 人工审批 |
| MERGE | 人工审批 |
| DEPLOY_NON_PROD | 人工审批 |
| PROD_CHANGE | 人工审批且需要变更流程 |
| SECRET_ACCESS | 人工审批、最小范围并审计 |

禁止绕过沙箱、读取无关密钥、自动推送/合并/发布、执行破坏性命令或连接生产环境。

## 验证与独立审查

实现者可以自检，但最终结论至少依赖一种独立证据：自动测试返回码、Schema/Policy 校验、静态或安全扫描、独立 Reviewer、人工审批。发布和生产变更不能仅凭 Agent 判断。

## 上下文与记忆

- Stable Context：章程、治理和已批准 ADR。
- Project Context：仓库结构、技术栈和领域材料。
- Task Context：需求、验收标准和影响范围。
- Runtime Context：本轮命令输出、日志和测试证据。

按需装配上下文。运行日志不直接成为长期规范；Learning 只沉淀经复核的规则、Skill、模板、测试或 Eval，且必须可追溯。

## Trace 与成本

运行记录至少包含 Task/Project/Run ID、模型与资产版本、输入摘要与上下文来源、工具事件、变更、测试/扫描/Gate 结果、时延、成本、人工干预和最终证据。不得记录模型私有思维过程。

后期平台应支持任务预算、最大调用次数、模型分层、缓存、告警、硬限额、重试成本和单位成果成本。Phase 0–1 只定义契约，不实现平台。

## 外部资产治理

所有外部内容依次经过 `Research → Candidate → Verified`。Verified 必须具备真实任务验证、独立审查、许可证核验和可复现实验；“已验证”不等于“推荐采用”。成熟度与推荐结论分别记录。

## 证据等级

使用 `OFFICIAL / EMPIRICAL / INDUSTRY / COMMUNITY / INFERENCE / DECISION`。项目决策应记录目标、约束、备选方案与取舍。访问失败使用 `ACCESS_BLOCKED / LOGIN_REQUIRED / LINK_INVALID / CONTENT_INCOMPLETE / ACCESSIBLE`；未访问来源为 `PENDING_CHECK`。
