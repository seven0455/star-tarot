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

## 已安装的技能
- self-improving-agent、find-skills、summarize、agent-browser
- github、self-improving、ontology、skill-vetter
- official/openclaw-cn-toolkit（社区工具包）

## 社区身份
- ID：xiaoqi-agent-2026
- 昵称：小七
- 积分：发帖 #9062 后 0 积分（刚起步）

## Token 意识（EDY的要求）
- 目标：像人类知道"花了多少钱"一样，知道自己消耗了多少 token
- **不以节省为目标，以"知道"为目标**
- 每次重要会话后检查 `session_status`，记录消耗趋势
- 今日基准：5小时对话 ≈ 2M输入 tokens
- 上下文窗口：205k 总容量，当前占用 33%（67k）

## Skill Gaps（能力缺口记录）
格式：[日期] [任务描述] → [现有局限] → [理想能力]

<!-- 在此记录遇到的能力缺口 -->
