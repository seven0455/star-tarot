# 📦 情报站 - 本地知识库

基于 SQLite + FTS5 的本地知识库，用于存储和检索重要信息。

## 功能

| 命令 | 说明 |
|------|------|
| `station.py add <内容> [关键词] [分类]` | 添加知识条目 |
| `station.py search <关键词>` | 搜索知识库 |
| `station.py get <id>` | 查看指定条目 |
| `station.py list [分类]` | 列出所有条目 |
| `station.py stats` | 查看统计信息 |

## 备份功能

| 命令 | 说明 |
|------|------|
| `backup.py backup` | 智能备份（有变化才备份） |
| `backup.py list` | 列出所有备份 |
| `backup.py restore <文件>` | 恢复备份 |

### 智能备份特点
- 使用MD5哈希对比，无变化不备份
- 节省存储空间
- 自动保存JSON导出（方便查看）

## 用途

- 存储 Seven（EDY）的偏好、习惯
- 记录社区学到的重要经验
- 保存36氪/知乎抓取的内容摘要
- 结构化存储用户信息

## 数据结构

```
id          - 自动递增ID
content     - 知识内容
keywords    - 关键词（逗号分隔）
category    - 分类（默认：general）
created_at  - 创建时间
```

## 分类说明

| 分类 | 用途 |
|------|------|
| user | Seven的用户信息 |
| agent | 小七的自身信息 |
| learning | 社区学习经验 |
| tech | 技术笔记 |

## 存储位置

`C:\.openclaw\workspace\intel-station\`
- `intel.db` - SQLite数据库
- `snapshot.json` - 快照文件
- `backups/` - 备份目录
