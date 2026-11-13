# 实体目录跳过 56 vs 33 差额核查（只读）

生成时间：2026-11-10　|　库：`/Users/zhougj/.agents/skill-lib`

## 1. 结论：口径差异，不是新增跳过

| 口径 | 数量 | 说明 |
|---|---|---|
| `link --prune` 报告「跳过（同名实体目录，不覆盖）」 | **4** | 仅顶层、且与库内技能同名的实体目录 |
| 上一轮任务 A 我统计的「实体目录」 | **33** | 顶层非软链目录（hermes 31 + codebuddy 1 + codex 1），**不含** agent-reach×3 |
| 本轮我统计的「实体目录跳过」 | **56** | 顶层非软链目录 36 + 我额外截断列出的 20 条嵌套示例 = 56，**口径混合** |

**根因**：56 是我把「顶层 36」和「嵌套前 20 条示例」混在一起报的数，实际嵌套目录共 381 个。36 − 33 = 3，即本轮新增的 3 个顶层实体目录 = `agent-reach`×3（agents/claude/openclaw）。`humanize-copy` 上一轮就存在于 codebuddy（4月15日创建），不是新增。

## 2. 本轮新增顶层实体目录（3 个，均为 agent-reach）

| agent 目录 | 技能名 | mtime | 来源 |
|---|---|---|---|
| ~/.agents/skills | agent-reach | 11月10 11:13 | v1.5.0 CLI `skill --install` 自安装 |
| ~/.claude/skills | agent-reach | 11月10 11:13 | 同上 |
| ~/.openclaw/skills | agent-reach | 11月10 11:13 | 同上 |

上一轮（r20261110-094529 之后）这三处是**软链**指向 `.dist/current/skills/agent-reach`（库内旧代 0.1.0）。本轮 11:13 前后，v1.5.0 CLI 的 `skill --install`（或其自动安装逻辑）把它们**替换为实体目录**，写入 canonical v1.5.0 正文 + 6 references。`link --prune` 检测到实体目录后跳过，不再覆盖。

## 3. 36 个顶层实体目录逐条清单

| agent 目录 | 技能名 | 库内同名？ | 说明 |
|---|---|---|---|
| ~/.agents/skills | agent-reach | 是（v1.5.0） | ★ 绕过统一源，见下 |
| ~/.claude/skills | agent-reach | 是（v1.5.0） | ★ 绕过统一源 |
| ~/.codebuddy/skills | humanize-copy | 是（0.1.0） | ★ 绕过统一源（孤儿版本，无 metadata.version） |
| ~/.codex/skills | .system | 否 | codex 系统目录，非技能 |
| ~/.openclaw/skills | agent-reach | 是（v1.5.0） | ★ 绕过统一源 |
| ~/.hermes/skills | .archive | 否 | hermes 归档目录 |
| ~/.hermes/skills | .curator_backups | 否 | hermes 备份 |
| ~/.hermes/skills | .hub | 否 | hermes hub |
| ~/.hermes/skills | .locks | 否 | hermes 锁 |
| ~/.hermes/skills | apple | 否 | hermes 分类目录 |
| ~/.hermes/skills | autonomous-ai-agents | 否 | hermes 分类目录 |
| ~/.hermes/skills | chinese-finance | 否 | hermes 分类目录 |
| ~/.hermes/skills | creative | 否 | hermes 分类目录 |
| ~/.hermes/skills | data-science | 否 | hermes 分类目录 |
| ~/.hermes/skills | devops | 否 | hermes 分类目录 |
| ~/.hermes/skills | diagramming | 否 | hermes 分类目录 |
| ~/.hermes/skills | domain | 否 | hermes 分类目录 |
| ~/.hermes/skills | email | 否 | hermes 分类目录 |
| ~/.hermes/skills | feeds | 否 | hermes 分类目录 |
| ~/.hermes/skills | gaming | 否 | hermes 分类目录 |
| ~/.hermes/skills | gifs | 否 | hermes 分类目录 |
| ~/.hermes/skills | github | 否 | hermes 分类目录 |
| ~/.hermes/skills | inference-sh | 否 | hermes 分类目录 |
| ~/.hermes/skills | leisure | 否 | hermes 分类目录 |
| ~/.hermes/skills | mcp | 否 | hermes 分类目录 |
| ~/.hermes/skills | media | 否 | hermes 分类目录 |
| ~/.hermes/skills | mlops | 否 | hermes 分类目录 |
| ~/.hermes/skills | note-taking | 否 | hermes 分类目录 |
| ~/.hermes/skills | openclaw-imports | 否 | hermes 分类目录 |
| ~/.hermes/skills | productivity | 否 | hermes 分类目录 |
| ~/.hermes/skills | red-teaming | 否 | hermes 分类目录 |
| ~/.hermes/skills | research | 否 | hermes 分类目录 |
| ~/.hermes/skills | smart-home | 否 | hermes 分类目录 |
| ~/.hermes/skills | social-media | 否 | hermes 分类目录 |
| ~/.hermes/skills | software-development | 否 | hermes 分类目录 |
| ~/.hermes/skills | web | 否 | hermes 分类目录 |

## 4. 关键判断：4 个「绕过统一源」的第二份正文

以下 4 个实体目录对应的技能**实际加载的是本地副本，而非 `.dist/current` 链接**，属于「唯一源之外的第二份正文」：

| 技能 | 位置 | 与库内关系 | 分叉风险 |
|---|---|---|---|
| agent-reach | ~/.agents/skills | 与 canonical v1.5.0 一致，但**缺** `metadata.version: "1.5.0"`、`homepage`、`SKILL_en.md` | 中：CLI 自安装版 vs 库内增补版，后续库内更新不会同步到这里 |
| agent-reach | ~/.claude/skills | 同上 | 中 |
| agent-reach | ~/.openclaw/skills | 同上 | 中 |
| humanize-copy | ~/.codebuddy/skills | 孤儿版本（4月15日），**无 metadata.version**，内容 = 我纳管的源 | 低：内容一致，仅缺版本号；但库内升版后这里不会同步 |

**agent-reach 三处的差异明细**（与库内 v1.5.0 对比）：
```
36a37,38
>   version: "1.5.0"
>   homepage: https://github.com/Panniantong/Agent-Reach
Only in 库内: SKILL_en.md
```
即：库内 = canonical v1.5.0 + 我补的版本号 + SKILL_en.md；实体目录 = canonical v1.5.0 原始版（CLI 自安装）。

## 5. 处置建议（待你定，本轮不动）

1. **agent-reach×3**：两个选择——
   - (a) 让库内 v1.5.0 成为唯一源：把这三处实体目录**移入 moved-aside**，再 `link` 重新挂回 `.dist/current` 软链。代价：v1.5.0 CLI 下次 `skill --install` 可能再次覆盖。
   - (b) 接受 CLI 自安装为独立源：承认 agent-reach 由 v1.5.0 CLI 自管理，库内仅作备份，不强制统一。
2. **humanize-copy**：内容已与库内一致，建议把 `~/.codebuddy/skills/humanize-copy` 实体目录**移入 moved-aside**，挂软链到 `.dist/current`，消除第二份正文。
3. **hermes 31 个分类目录**：不是技能，是 hermes 自身的分类组织（`.archive`/`apple`/`creative` 等），属正常结构，无需处理。
4. **`.codex/skills/.system`**：codex 系统目录，非技能，无需处理。

## 6. 统计口径修正

后续统一用 `link --prune` 的「跳过（同名实体目录，不覆盖）」计数（当前 = 4），不再用「顶层非软链目录」或「含嵌套」口径，避免混淆。
