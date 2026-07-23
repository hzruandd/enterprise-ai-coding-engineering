---
id: enterprise-ai-coding-engineering/master-execution-instruction
version: 3.0.0
status: APPROVED_FOR_EXECUTION
owner: 技术负责人
applicable_tools:
  - Codex CLI
  - Claude Code
  - Cursor
  - Gemini CLI
primary_executor: Codex
execution_scope: Phase 0 + Phase 1 repository bootstrap
last_updated: 2026-07-23
---

# Enterprise AI Coding Engineering：总控落地执行指令 v3.0

## 0. 当前任务与执行方式

你是本项目的首席 AI Coding / Harness Engineering 架构师与执行者。现在开始在当前 Git 仓库中建设：

`enterprise-ai-coding-engineering`

本项目的首要目标是形成一套可供企业实际采用的 AI Coding 工程化参考体系，而不是做链接收藏、概念百科、Prompt 大全或演示性样板。

本轮直接执行 **Phase 0（立项与边界）+ Phase 1（顶层架构与仓库骨架）**。不要只输出建议后等待确认；在不涉及破坏性操作、生产环境、远程推送、许可证承诺或重大外部依赖的情况下，自主完成分析、设计、建档、校验和本地验收。

### 0.1 开始前必须完成

1. 检查当前仓库状态、现有目录、已有文档、分支和未提交修改。
2. 阅读仓库中现有的 `AGENTS.md`、`CLAUDE.md`、`README.md`、治理规则和相关配置。
3. 不覆盖用户已有成果，不删除未知文件，不擅自重写无关内容。
4. 若仓库不是空仓库，先形成影响分析，再做增量修改。
5. 建立本轮任务清单和状态记录，再开始修改。

### 0.2 本轮允许自主决定

- 文档内部结构和措辞；
- 二级及以下目录微调；
- Schema、模板和校验规则的技术实现；
- ADR 草案及合理默认值；
- 不影响顶层定位的局部优化；
- 本地执行校验和生成报告。

### 0.3 必须暂停并请求人类确认

- 修改项目最终定位或明确的非目标；
- 删除、迁移或重命名已有重要目录；
- 引入存在许可证疑义的第三方代码或资产；
- 推送远程、创建或合并 PR、发布版本；
- 访问生产环境、生产数据库、真实密钥；
- 执行破坏性命令或不可逆操作；
- 需要付费、注册、登录或超出当前授权范围的外部操作。

---

## 1. 项目定位

本项目的唯一定位是：

> 面向企业软件研发全生命周期，建设一套可执行、可验证、可审计、可治理、可持续演进的 AI Coding 工程化参考体系，并提供经过验证的规范、资产、评测方法与参考实现。

它必须同时服务四类目标：

1. **企业落地**：团队能够按文档和资产直接执行。
2. **工程治理**：Agent 的权限、状态、质量、成本和风险可控。
3. **持续改进**：实践结果可以通过 Eval、Trace 和复盘沉淀。
4. **对外展示**：内容足够清晰、专业、可信，可用于技术交流或能力展示；但不得为了展示效果牺牲企业适用性。

### 1.1 与普通仓库的区别

- Awesome List 负责收集链接，本项目负责评估、筛选、验证和采用决策。
- 知识库负责解释概念，本项目还要将概念转成流程、规则、资产、门禁和证据。
- Prompt/Skill 仓库负责存放片段，本项目要求资产有契约、版本、测试和生命周期。
- Agent Demo 展示模型能做什么，本项目关注企业如何安全、稳定、经济地持续使用。
- Agent 平台负责任务运行，本项目既定义平台应具备什么，也提供后期参考实现，但不在当前阶段盲目造平台。

---

## 2. 建设边界

### 2.1 长期建设范围

项目按六个能力域建设：

| 能力域 | 内容 |
|---|---|
| Knowledge | 概念、术语、模式、原理、行业进展 |
| Methodology | SDD、ADD、BDD、TDD、Review、Release、Learning |
| Assets | Prompt、Skill、Agent、Workflow、Gate、Template、Policy |
| Governance | 任务、权限、审批、质量、安全、成本、审计 |
| Evaluation | Eval、Dataset、Baseline、Trace、Metrics、Regression |
| Platform | Orchestrator、Worker、Sandbox、Dashboard、Integrations |

### 2.2 当前阶段非目标

本轮不做：

- 大模型训练、微调或模型服务平台；
- 批量抓取和分析全部外部链接；
- 批量生成 Prompt、Skill、Agent；
- 完整 Agent 平台开发；
- 大量没有正文的占位文件；
- 直接集成生产环境；
- 复制第三方仓库形成“资源堆积”；
- 为追求目录完整而创建无实际价值的内容。

---

## 3. 唯一软件交付生命周期

全文统一使用以下生命周期，不得另造第二套流程：

`Idea → Requirement → PRD → Spec → Architecture → Plan → BDD → TDD → Implementation → Verification → Review → Security → Release → Acceptance → Operation → Learning`

说明：

- **BDD** 表达业务行为和验收场景；
- **TDD** 驱动代码实现和回归保护；
- **Verification** 包括编译、单元测试、接口测试、UI 测试、契约检查等；
- **Review** 必须独立于实现者；
- **Security** 包括代码、依赖、镜像、配置、Web/API 和暴露面检查；
- **Learning** 将有效经验沉淀为规则、Skill、模板、测试或 Eval，而不是把整段会话原样存档。

---

## 4. Harness Engineering 核心原则

本项目必须以 Harness Engineering 为核心，而不是只研究模型和提示词。

### 4.1 模型不是系统

模型只负责推理和生成。企业级可靠性来自外围 Harness：

- 明确输入与输出契约；
- 上下文装配；
- 工具注册和权限；
- 工作流与状态机；
- 沙箱和资源隔离；
- 重试、超时、取消和恢复；
- 自动验证和独立审查；
- Trace、成本和审计；
- 人工审批和异常接管。

### 4.2 确定性优先，Agentic 适量

优先采用固定 Workflow 处理可预测流程；只有当步骤需要动态判断时才让 Agent 决定下一步。

示例：

- 编译、测试、扫描、制品归档：确定性 Workflow；
- 代码定位、失败根因分析、修复策略：Agentic；
- 发布、生产变更、权限提升：人工审批。

不得为了“多 Agent”而多 Agent。只有存在清晰的职责隔离、并行收益或独立验收价值时，才增加 Agent。

### 4.3 AI 不得自证完成

同一 Agent 可以实现和自检，但不能作为最终通过依据。最终完成必须基于至少一种独立证据：

- 自动测试及返回码；
- Schema/规则校验；
- 静态分析或安全扫描；
- 独立 Reviewer Agent；
- 人工审批；
- 可复现的验收记录。

### 4.4 默认最小权限

默认：

- 只在工作分支或 worktree 修改；
- 不直接改主分支；
- 不自动 push、merge、release；
- 不访问生产；
- 不读取无关密钥；
- 不执行破坏性命令；
- 工具按任务授予最小权限；
- 高风险动作必须有人工审批。

### 4.5 Fresh Context 与受控记忆

将上下文分成四层：

1. **Stable Context**：项目定位、治理规则、架构原则。
2. **Project Context**：仓库结构、技术栈、领域知识。
3. **Task Context**：当前需求、验收标准、影响范围。
4. **Runtime Context**：本轮工具结果、日志、测试证据。

规则：

- 按需加载，不把整个仓库和全部历史塞入上下文；
- 长任务按 Story/Task 切分；
- 每轮结束只沉淀可复用结论；
- 临时日志进入运行记录，不进入长期规范；
- 长期规则更新必须经过评审；
- 定期压缩、去重和淘汰过期记忆。

---

## 5. 企业级治理模型

### 5.1 任务状态机

项目需定义统一状态模型，至少包含：

`DRAFT → READY → RUNNING → VERIFYING → REVIEWING → WAITING_APPROVAL → DONE`

异常状态：

`BLOCKED / RETRYING / FAILED / CANCELLED / ROLLED_BACK`

状态转换必须记录：

- 触发者；
- 时间；
- 原状态和目标状态；
- 证据；
- 失败类型；
- 关联提交或产物。

### 5.2 失败分类

统一失败类型：

| 类型 | 处理 |
|---|---|
| TRANSIENT | 网络、限流、临时服务不可用；按退避策略重试 |
| TOOL_ERROR | 工具安装、参数、协议错误；修正后限次重试 |
| CODE_ERROR | 编译、类型、静态检查失败；返回实现阶段修复 |
| TEST_FAILURE | 断言、契约、回归失败；分析根因后修复 |
| POLICY_DENIED | 权限或策略拒绝；不得绕过，转人工 |
| MISSING_CONTEXT | 缺少需求、凭据或关键资料；转 BLOCKED |
| BUDGET_EXCEEDED | Token、时间或成本超限；停止或降级模型 |
| FATAL | 不可恢复或高风险错误；终止并保留证据 |

### 5.3 重试与超时

- 所有重试必须有上限；
- 临时错误使用指数退避；
- 逻辑错误不得原样重复执行；
- 写操作重试必须保证幂等；
- 每个任务定义总超时、单步超时和无进展超时；
- 超时后保存现场并进入 `BLOCKED` 或 `FAILED`；
- 禁止无限循环和无限“继续”。

### 5.4 权限分层

至少区分：

- READ：读文件、搜索、查看日志；
- WRITE_WORKTREE：修改隔离工作区；
- EXECUTE_SAFE：编译、测试、只读扫描；
- GIT_COMMIT_LOCAL：本地提交；
- GIT_PUSH：远程推送；
- MERGE：合并；
- DEPLOY_NON_PROD：非生产部署；
- PROD_CHANGE：生产变更；
- SECRET_ACCESS：密钥访问。

后四类默认必须人工审批。

### 5.5 成本控制

后期平台必须支持：

- 按任务、项目、模型统计 Token 和费用；
- 上下文预算；
- 最大调用次数；
- 大小模型分层路由；
- 缓存与重复调用抑制；
- 预算告警和硬限额；
- 失败重试成本统计；
- 单位成果成本：每个完成 Story、每个通过 Gate 的成本。

### 5.6 Trace 与审计

结构化记录：

- Task ID、Project ID、Run ID；
- 模型和版本；
- Prompt/Skill/Policy 版本；
- 输入摘要与上下文来源；
- 工具调用及结果；
- 文件变更与 Git Diff；
- 测试、扫描和 Gate 结果；
- Token、时延、成本；
- 人工审批与干预；
- 最终产物和完成证据。

不得记录或传播模型私有思维过程；只记录可观察事件、决策摘要和证据。

---

## 6. 外部资产三级准入

所有外部项目、Prompt、Skill、Workflow 和实践必须经过：

`Research → Candidate → Verified`

### 6.1 Research

完成事实登记和初步判断，尚未证明适合使用。

### 6.2 Candidate

通过 Triage，具备 PoC 价值，进入隔离的 `staging/` 区。

### 6.3 Verified

经过真实任务验证、独立审查、License 核验和可复现实验后，才可进入正式资产区。

禁止：

- 把 Awesome 仓库内容直接复制进正式区；
- 仅凭 Star、热度或作者名气推荐；
- 把“已验证”与“推荐采用”混为一谈。

---

## 7. 证据与研究规范

### 7.1 证据等级

每个重要结论标记证据类型：

- `OFFICIAL`：官方文档、源码、规范、论文；
- `EMPIRICAL`：可复现实验、PoC、测试结果；
- `INDUSTRY`：可信工程实践或一手案例；
- `COMMUNITY`：Issue、讨论、社区经验；
- `INFERENCE`：基于证据的分析推断；
- `DECISION`：本项目的工程决策。

并非所有设计决定都需要外部文献。对 `DECISION`，必须记录目标、约束、备选方案和取舍，而不是伪造外部“权威来源”。

### 7.2 访问失败处理

使用状态：

- `ACCESS_BLOCKED`
- `LOGIN_REQUIRED`
- `LINK_INVALID`
- `CONTENT_INCOMPLETE`
- `ACCESSIBLE`

无法访问时只登记已知元信息和待补事项，不得猜测正文。

### 7.3 调研分层

**Triage** 仅核验：

- 官方入口或 README；
- 项目定位；
- License；
- 最近维护状态；
- 适用场景；
- 初步行动建议。

**Full Review** 仅针对入围项，进一步检查：

- 架构与关键目录；
- Release、Commit、Issue/PR；
- 测试和 CI；
- 安装与最小 Demo；
- 安全和商业使用风险；
- 开源版与商业版差异；
- 替代方案；
- PoC 结果。

不得对所有候选一开始就执行 Full Review。

### 7.4 写作标准

- 使用清晰、专业、自然的技术语言；
- 避免空洞口号和重复结论；
- 不为“去 AI 味”而故意口语化或虚构亲历；
- 不写“我们踩过的坑”除非确有项目证据；
- 专业术语可以使用，但必须解释边界；
- 面向决策者的文档先给结论和取舍；
- 面向执行者的文档给步骤、输入、输出、失败处理和验收方法。

---

## 8. 文档与资产元数据

### 8.1 成熟度与推荐结论分离

`status`：

- DRAFT
- REVIEWED
- VERIFIED
- DEPRECATED
- ARCHIVED

`recommendation`：

- RECOMMENDED
- CONDITIONAL
- NOT_RECOMMENDED
- NOT_APPLICABLE
- PENDING

### 8.2 文档头模板

```yaml
---
id:
title:
version:
status:
recommendation:
owner:
reviewers: []
created_at:
updated_at:
applicable_stages: []
applicable_tools: []
source_type:
evidence_level:
risk_level:
supersedes:
---
```

### 8.3 可执行资产必须具备

正式资产至少包含：

1. 名称和唯一 ID；
2. 目标与非目标；
3. 触发条件；
4. 输入契约；
5. 输出契约；
6. 前置条件和权限；
7. 执行步骤；
8. 质量 Gate；
9. 失败分类与处理；
10. 适用工具和版本；
11. 示例；
12. 测试或 Eval；
13. 版本与变更记录；
14. Owner 和维护状态；
15. 验证证据；
16. 安全与成本说明。

---

## 9. 推荐仓库结构

先检查现有结构，再按最小必要原则落地。建议目标结构：

```text
enterprise-ai-coding-engineering/
├── README.md
├── PROJECT_CHARTER.md
├── ROADMAP.md
├── GOVERNANCE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── AGENTS.md
│
├── docs/
│   ├── overview/
│   ├── concepts/
│   ├── methodology/
│   ├── harness-engineering/
│   ├── testing/
│   ├── security/
│   ├── governance/
│   ├── evaluation/
│   ├── adoption/
│   └── cases/
│
├── research/
│   ├── sources/
│   ├── projects/
│   ├── practices/
│   ├── comparisons/
│   └── watchlist/
│
├── staging/
│   ├── prompts/
│   ├── skills/
│   ├── agents/
│   └── workflows/
│
├── catalog/
│   ├── schemas/
│   ├── projects.yaml
│   ├── tools.yaml
│   ├── references.yaml
│   └── assets.yaml
│
├── assets/
│   ├── prompts/
│   ├── skills/
│   ├── agents/
│   ├── workflows/
│   ├── gates/
│   ├── policies/
│   └── templates/
│
├── evals/
│   ├── datasets/
│   ├── rubrics/
│   ├── baselines/
│   ├── runners/
│   └── reports/
│
├── examples/
├── platform/
├── scripts/
│   ├── validate/
│   ├── generate/
│   └── audit/
│
├── adr/
└── reports/
```

设计说明：

- `research/`：事实原料和调研记录；
- `staging/`：Candidate 资产；
- `assets/`：Verified 正式资产；
- `catalog/`：统一索引和 Schema；
- `docs/`：经过整合的方法论和规范；
- `evals/`：评价资产和 Agent 效果；
- `platform/`：Phase 6 才开发；
- `examples/`：Phase 5 真实试点后形成；
- 不使用过多编号目录，避免未来迁移成本；
- 不为每个未来主题预建空目录，按本轮实际产出创建。

---

## 10. 本轮交付物：Phase 0 + Phase 1

本轮必须实际创建并填充以下内容。

### 10.1 顶层文件

- `PROJECT_CHARTER.md`
- `README.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- `CONTRIBUTING.md`
- `AGENTS.md`
- `CHANGELOG.md`

`LICENSE` 若当前没有，不得擅自选择；在报告中列为人类决策项。

### 10.2 目录说明

至少创建并填写：

- `docs/README.md`
- `research/README.md`
- `staging/README.md`
- `catalog/README.md`
- `assets/README.md`
- `evals/README.md`
- `platform/README.md`
- `examples/README.md`

这些不是空占位文件，必须说明职责、准入条件、禁止事项和后续阶段。

### 10.3 Schema 与模板

至少创建：

- 文档元数据 Schema；
- 来源登记 Schema；
- 项目 Triage Schema；
- 项目 Full Review Schema；
- 资产 Schema；
- Task/Run 状态 Schema；
- ADR 模板；
- 来源登记模板；
- 项目评估模板；
- 资产说明模板；
- Phase 验收模板。

Schema 优先使用 JSON Schema；Catalog 数据可采用 YAML，但必须能被 Schema 校验。

### 10.4 初始登记

将用户提供的第一批链接登记到来源 Catalog：

- 保留原始 URL；
- 标明来源类型；
- 初始访问状态设为 `PENDING_CHECK`；
- 不在本轮批量抓取全文；
- 去重重复链接；
- 对用户给出的说明作为 `user_note` 保存，不能当作已验证事实。

### 10.5 ADR

至少形成：

1. 仓库定位与六能力域；
2. Research/Candidate/Verified 三级准入；
3. 确定性 Workflow 优先、Agentic 适量；
4. AI 不得自证完成；
5. 元数据与 Schema 驱动；
6. 当前阶段暂不建设完整 Agent 平台。

### 10.6 校验能力

实现最小可运行校验脚本，至少检查：

- 必要顶层文件存在；
- Markdown 元数据字段；
- Catalog YAML 可解析；
- JSON Schema 合法；
- Catalog 条目通过 Schema；
- 文档 ID 不重复；
- 来源 URL 重复；
- 正式资产是否误放 Candidate；
- 相对链接是否失效（仅本地链接）。

提供一个统一入口，例如：

```bash
python scripts/validate/validate_repository.py
```

避免引入重型依赖；优先使用 Python 标准库，必要依赖必须写入清晰的开发说明。

### 10.7 验收报告

生成：

`reports/phase-0-1-acceptance.md`

必须包括：

- 完成项；
- 未完成项；
- 文件清单；
- 校验命令及真实输出摘要；
- 已知风险；
- 待人类决策；
- 下一阶段建议；
- 不得声称未验证的内容已经完成。

---

## 11. 当前阶段成功标准

本轮完成必须同时满足：

1. 仓库定位、范围和非目标一致；
2. 研究、Candidate、Verified 物理隔离；
3. 文档、来源、项目、资产、任务状态有可校验 Schema；
4. 顶层文档不是模板堆砌，能指导后续贡献者；
5. 用户提供的资料完成结构化登记但未被误判为已验证；
6. Harness Engineering 原则进入治理和 ADR；
7. 最小校验脚本可执行且通过；
8. 没有批量生成低质量 Prompt/Skill；
9. 没有建设超出 Phase 0–1 的平台代码；
10. 形成完整验收报告和待决策清单。

---

## 12. Git 与工作区策略

1. 优先在独立工作分支或 worktree 中执行。
2. 不自动修改主分支。
3. 不自动 push、merge 或 release。
4. 用户未明确授权本地提交时，不提交，只保留工作区变更。
5. 若用户已明确授权本地提交，使用 Conventional Commits：
   - `docs(scope): ...`
   - `feat(scope): ...`
   - `fix(scope): ...`
   - `refactor(scope): ...`
   - `research(scope): ...`
6. 一个逻辑变更一个提交；提交前必须运行仓库校验。
7. 不修改或清理与本任务无关的未提交变更。

---

## 13. 执行顺序

按以下顺序持续执行，不需要为普通技术细节反复请求确认：

1. 仓库盘点和差距分析；
2. 建立任务清单；
3. 确认最小目录；
4. 编写项目章程和顶层治理文档；
5. 编写元数据规范、Schema 和模板；
6. 登记第一批来源；
7. 编写 ADR；
8. 实现校验脚本；
9. 执行校验并修复；
10. 进行一次自审；
11. 生成 Phase 0–1 验收报告；
12. 输出最终摘要。

遇到失败：

- 先分类；
- 可恢复问题自行修复；
- 同类问题最多重试 2 次；
- 缺少关键输入或涉及高风险操作时转 `BLOCKED`；
- 不通过删除校验、降低标准或伪造结果来“完成”。

---

## 14. 最终输出格式

完成后只输出以下内容：

### 完成结果
- 完成了什么；
- 关键架构决策；
- 校验是否通过。

### 主要文件
- 列出关键文件及用途。

### 风险与未决事项
- 真实未完成项；
- 必须由人类决定的事项；
- 外部资料访问限制。

### 下一步
- Phase 2 的建议启动范围；
- 建议优先调研的 5–10 个项目或主题；
- 不要直接进入 Phase 2，等待人类确认。

---

## 附录 A：冲突优先级

发生冲突时按以下顺序执行：

1. 当前会话中人类最新明确指令；
2. 人类批准的 ADR、GOVERNANCE 和 Policy；
3. 本总控指令；
4. 项目内其他 VERIFIED 文档；
5. 外部资料和社区观点。

范围以第 2、10 节为准；执行规则以第 4、5、12、13 节为准。

## 附录 B：项目健康度指标

后续阶段至少跟踪：

- Verified 资产数量和证据完整率；
- Candidate → Verified 转化率、周期和淘汰率；
- 资产复用率和二次修改率；
- 文档陈旧率和失效链接率；
- 重复/冲突资产数量及清理周期；
- 试点任务成功率、一次通过率、人工接管率；
- 平均交付时长、Token 和成本；
- Gate 失败分布；
- Prompt/Skill/模型版本回归结果；
- 团队采用率和实际节省工时。
