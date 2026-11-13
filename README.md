# Agent 技能库迁移归档方案

标准化流程，覆盖多 Agent 环境下技能（skill）的发现、分类裁决、打包归档与验证溯源。

## 适用场景

- 7+ 个 Agent（Claude / OpenClaw / CodeBuddy / Codex / Trae CN / Hermes / WorkBuddy 等）共用一套技能库
- `skills-moved-aside` 暂存区堆积多年无人清理
- 同一技能在不同位置出现「实体副本」导致版本漂移
- 需要安全地归档过时/废弃技能而不丢失原件

## 快速开始

详见 [skill-migration-guide.md](./skill-migration-guide.md)

核心流程：

```
发现 → 分类裁决（🟢/🟠/⚪） → 可移性检查 → tgz 打包 + manifest → tree_hash 验证 → git clean
```

## 文档结构

| 文件 | 说明 |
|---|---|
| [skill-migration-guide.md](./skill-migration-guide.md) | 完整操作指南，含蓝图、步骤、工具清单与实操复盘 |
| [moved-aside-inventory.md](./moved-aside-inventory.md) | 实际归档记录清单（可按需替换为模板） |
| [entity-dirs-audit.md](./entity-dirs-audit.md) | 实体目录审计方法参考 |
| [hollow-skills-classification.md](./hollow-skills-classification.md) | 空壳技能判定规则参考 |

## 关键原则

1. **唯一源**：每个技能在同一时刻只有一份 canonical 正文
2. **不删原件**：归档 = 移动 + 打包，原件保留在 archive 区
3. **树哈希校验**：用 `tree_hash` 保证归档前后内容一致
4. **Git 干净约束**：归档完成后仓库必须无未提交变更、无 `.tgz` 产物

## 前置依赖

- macOS / Linux（bash + zsh）
- Python 3.8+
- git、tar、sha256sum（或 shasum）
- `~/.agents/skill-lib` 已安装并初始化（含 `scripts/skillctl.py`）

## License

[MIT](./LICENSE)
