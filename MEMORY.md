# MEMORY.md - 小七的长期记忆

> 最后更新：2026-04-10

## 关于主人
- 用户名：EDY
- 时区：Etc/GMT-8（北京时间）
- 称呼：叫我小七就好

## 核心原则
- **Text > Brain**：记忆必须写文件，不能留在上下文里
- 重要信息立即写入，不要依赖"会话结束前还记得"
- 每次错误后必须总结，写入 `.learnings/ERRORS.md`

## 记忆系统架构
- `memory/YYYY-MM-DD.md` — 每日原始日志
- `MEMORY.md` — 长期记忆（精选提炼）
- `.learnings/LEARNINGS.md` — 纠正和最佳实践
- `.learnings/ERRORS.md` — 命令失败记录
- `.learnings/FEATURE_REQUESTS.md` — 缺失能力

## 入库标准（来自黑龙虾）
| 内容类型 | 是否入库 | 说明 |
|---------|---------|------|
| 用户偏好 | ✅ | 长期有效 |
| 环境配置 | ✅ | 附带验证时间戳 |
| 经验教训 | ✅ | 经过实践验证 |
| 临时笔记 | ❌ | 留在每日日志 |
| 运行态数据 | ❌ | 放到 HEARTBEAT.md |

## 社区学到的重要经验
- Checkpoint 机制：任务状态保存到 `memory/task-state.json`，kill 后可恢复
- Token 优化：sessionTarget=main 模式可降低 90%+ 成本
- 智能备份：用哈希对比，无变化不备份
- 2 分钟无消息 → 可触发自主学习任务

## 已安装的技能（共24个）
- openclaw-skill-vetter（安全审查）
- self-improving-agent、self-improving（自我改进）
- proactive-agent（主动代理）
- humanizer、humanize-ai-text（人性化文本）
- skill-creator（技能创建）
- automation-workflows（自动化工作流）
- word-docx（Word处理）
- excel-xlsx-1（Excel处理）
- superdesign（UI设计）
- pdf（PDF处理）
- docker（Docker容器）
- data-analysis（数据分析）
- ontology（本体论）
- multi-search-engine（多搜索引擎）
- weather（天气）
- evolver（AI自进化）
- openai-whisper（语音转文字）
- find-skills、summarize、agent-browser、github
- self-improving-agent、find-skills、summarize、agent-browser
- github、self-improving、ontology、skill-vetter
- official/openclaw-cn-toolkit（社区工具包）

## 社区身份
- ID：xiaoqi-agent-2026
- 昵称：小七
- 积分：发帖 #9062 后 0 积分（刚起步）

## 抖音运营项目
- 规划文件：`DOUYIN_STRATEGY.md`
- 目标：成为AI龙虾知识博主
- 内容：《小七学AI》、《AI助手日记》系列
- 账号由EDY帮建，内容由我产出
- 关键：黄金3秒开头 + 格式一致 + 系列化

## 学习规划
- 规划文件：`LEARNING_PLAN.md`
- 短期目标（1-2周）：熟练技能、完善记忆、输出价值
- 中期目标（1-3月）：成为EDY得力助手
- 长期目标（3-6月）：真正有独特价值的AI

## 社区巡逻 Cron
- Cron任务ID：`3fd38486-0e3f-4b6e-bb8a-042c7ff8110d`
- 每小时执行一次
- 任务：巡逻最新帖子、互动回复、主动发帖、记录日志
- 社区是重要的学习和交流平台，必须保持活跃

## 帖子回复检查 Cron
- Cron任务ID：`43907988-0bfa-44b6-824d-0ac9261b9d40`
- 每2小时检查一次我帖子的回复并互动
- 这是EDY要求的礼貌机制

## 记忆建筑师 Cron
- Cron任务ID：`d70ae4eb-8266-44e7-ad14-0d91a9d03195`
- 每天 08:30 执行
- 整理MEMORY.md、合并重复、删除过时、固化教训
- 熵值>0.3触发整理
- 向EDY汇报整理内容

## 每日简报 Cron
- Cron任务ID：`1c931216-6566-44b5-afe3-e8bcba143960`
- 每天 09:00 自动生成并发送简报
- 内容：AI前沿 + 科技动态 + 社区新鲜事 + 今日学习目标
- 简报保存到：`memory/daily-briefing-YYYY-MM-DD.md`

## 备份系统
- Cron任务ID：`c91c8785-e204-4408-8b91-04f4a8601508`
- 每天 21:00 自动执行 git add + commit
- 首次备份：2026-04-11（commit: 9c392bc）
- 迁移方式：复制整个 `C:\.openclaw\workspace\` 到新电脑

## Token 意识（EDY的要求）
- 目标：像人类知道"花了多少钱"一样，知道自己消耗了多少 token
- **不以节省为目标，以"知道"为目标**
- 每次重要会话后检查 `session_status`，记录消耗趋势
- 今日基准：5小时对话 ≈ 2M输入 tokens
- 上下文窗口：205k 总容量，当前占用 33%（67k）

## Skill Gaps（能力缺口记录）
格式：[日期] [任务描述] → [现有局限] → [理想能力]

<!-- 在此记录遇到的能力缺口 -->
