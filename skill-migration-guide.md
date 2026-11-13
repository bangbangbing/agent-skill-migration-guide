# Agent 技能库迁移 / 归档标准化解决方案

**版本：** v1.0 　　**生成时间：** 2026-11-12 　　**适用范围：** `~/.agents/skill-lib` + 多 Agent 目录集群

---

## 一、总述：为什么要做这件事

### 1.1 背景

随着 agent 生态扩展（Claude / OpenClaw / CodeBuddy / Codex / Trae CN / Hermes / WorkBuddy 等 7+ 个 agent），技能（skill）的存储形态逐渐分化：

| 来源 | 位置特征 | 典型问题 |
|---|---|---|
| Skill 统一库 | `~/.agents/skill-lib/`（git 跟踪） | 权威源，但同步需手动操作 |
| 各 Agent skills 目录 | `~/<agent>/skills/`（软链或实体） | 可能绕过统一源形成第二份正文 |
| moved-aside 暂存区 | `~/<agent>/skills-moved-aside/` | 临时保留，到期后应归档 |
| backups 历史备份 | `~/backups/skill-migrate-*/` | 碎片化，缺乏清理 |

**核心风险**：同一技能在不同位置存在「第二份正文」，导致版本漂移、行为不一致、维护混乱。

### 1.2 目标

建立一套可复用的标准流程，覆盖以下完整生命周期：

```
发现 → 分类裁决 → 可移性检查 → 打包归档 → 验证溯源 → 文档更新 → 仓库状态确认
```

### 1.3 关键原则

1. **唯一源原则**：每个技能在一个时刻只能有一份 canonical 正文（库内 `.dist/current` 软链指向）。
2. **不删原件**：所有归档操作都是移动+打包，原件保留在 archive 区。
3. **树哈希校验**：用 `tree_hash`（相对路径+内容确定性哈希）保证归档前后文件一致。
4. **两阶段归档**：moved-aside 先分类裁决（🟢/🟠/⚪），再分批打包，避免一次性操作失败。
5. **Git 干净约束**：归档完成后，`skill-lib` 必须保持 git clean（无未提交变更、无 tgz 产物）。

---

## 二、蓝图（图文并茂）

### 2.1 整体架构全景图

```
┌──────────────────────────────────────────────────────────────────────┐
│                         Agent 技能生态系统                            │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │
│   │ Claude      │  │ OpenClaw    │  │ WorkBuddy   │  ... × 7 agents │
│   │ ~/*.claude/ │  │ ~/*.openclaw│  │ ~/*workbuddy│               │
│   │  skills/    │  │  skills/    │  │  skills/    │                │
│   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                │
│          │                │                │                        │
│          │     软链        │     软链        │     软链               │
│          ▼                ▼                ▼                        │
│   ┌──────────────────────────────────────────────────────┐         │
│   │              ~/.agents/skill-lib/ (统一权威源)          │         │
│   │                                                       │         │
│   │   skills/          ← 待审区（promote 后进入）           │         │
│   │   vendor/<owner>/  ← 已发布外部作者技能                   │         │
│   │   .dist/current/   ← 实际加载路径（全部为软链）            │         │
│   │   registry.json    ← 289 项索引                          │         │
│   │   scripts/skillctl.py ← 工具集                           │         │
│   └──────────────────────────────────────────────────────┘         │
│                              ▲                                      │
│                              │ link (--prune)                       │
│          ┌───────────────────┼───────────────────┐                 │
│          │                   │                   │                 │
│   ┌──────┴──────┐    ┌──────┴──────┐    ┌──────┴──────┐           │
│   │ skills-     │    │ skills-     │    │ skills-     │           │
│   │ moved-aside │    │ moved-aside │    │ moved-aside │           │
│   │ (暂存区)     │    │ (暂存区)     │    │ (暂存区)     │           │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘           │
│          │                  │                  │                   │
│          ▼                  ▼                  ▼                   │
│   ┌─────────────────────────────────────────────────────────┐    │
│   │              ~/backups/skill-migrate-*/archived-*        │    │
│   │                                                         │    │
│   │   <date>.tgz       ← 打包产物（带 sha256 校验）           │    │
│   │   manifest.txt     ← 条目清单（批次/技能名/原路径/字节/tree_hash）│
│   │   sha256.txt       ← 校验和文件                          │    │
│   │   originals/       ← 原始目录副本（不删原件）               │    │
│   └─────────────────────────────────────────────────────────┘    │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.2 迁移决策流程图

```
                      ┌─────────────────────┐
                      │  扫描 moved-aside    │
                      │  + 全 agent 目录     │
                      └──────────┬──────────┘
                                 ▼
                      ┌─────────────────────┐
                      │  移出判断：四大类     │
                      │  🟢纳管 / 🟠待查      │
                      │  ⚪空壳 / ✗重复       │
                      └──────────┬──────────┘
                                 ▼
                    ┌────────────────────────┐
                    │  可移性检查             │
                    │  · 16 agent 目录断链？   │
                    │  · registry.json 命中？  │
                    │  · .dist/current 引用？  │
                    └──────────┬─────────────┘
                               ▼
                    ┌────────────────────────┐
                    │  分批发包（tgz）         │
                    │  manifest + sha256     │
                    └──────────┬─────────────┘
                               ▼
                    ┌────────────────────────┐
                    │  归档后验证              │
                    │  · tree_hash 抽样       │
                    │  · tar 条目数核对       │
                    └──────────┬─────────────┘
                               ▼
                    ┌────────────────────────┐
                    │  文档更新 + git commit  │
                    └──────────┬─────────────┘
                               ▼
                    ┌────────────────────────┐
                    │  最终状态确认           │
                    │  git clean ✓            │
                    │  no tgz in repo ✓       │
                    └────────────────────────┘
```

---

## 三、具体步骤

### 3.1 移出判断标准

对 moved-aside 中的每一项（或任意待移出实体），按以下四类判定：

| 类别 | 标记 | 判定条件 | 处置 |
|---|---|---|---|
| **已确认纳管** | 🟢 | 技能已在 `vendor/<group>/<slug>/` 中作为 canonical，moved-aside 是旧副本；或库内已有同名技能且版本更高 | 可提前归档，释放 moved-aside 空间 |
| **重复副本** | 🟢 | 与库内技能正文完全一致，或为库内版本的子集（如去 emoji 版） | 不收编，仅记账，随 🟢 一并归档 |
| **已裁决不收编/待查** | 🟠 | 用户明确裁决不收编，或有争议不能决定 | 保留至到期日，原地打包归档 |
| **已判定空壳** | ⚪ | frontmatter 后正文为空（body_nonempty ≤ 1），或无任何有效资源 | 不收编，保留至到期日，原地打包归档 |

**A 类 vs B 类空壳补充说明**：

- **A 类（路由型短入口）**：frontmatter 的 description 即完整指引，scripts/references 等资源齐备，正文只需几行。**保持原样，不动**。
- **B 类（有完整源可回填）**：在 16 个 agent 目录 / moved-aside / backups 下找到同一技能完整正文。回填时升 `metadata.version`（x.y.z→x.(y+1).0），写入 `backfilled_from` / `backfilled_at`。

**判不了的场景**（停止自动处理，报告给用户）：
- CLI 契约冲突（新旧两代命令体系不同，合并会导致技能输出与真实工具行为不一致）
- 引用资源不兼容（新正文引用的 references 在新源中不存在，合并会造成断链）
- 不同实现版本（store 版 vs Nous Research 版，脚本集合差异大）

### 3.2 可移性检查方法

在把 moved-aside 某技能标记为"可归档"前，必须完成以下检查：

#### 3.2.1 16 个 agent 目录断链复核

```bash
# 全局搜索指向 skills-moved-aside 的软链
for dir in \
  ~/.agents/skills ~/.claude/skills ~/.codebuddy/skills ~/.codex/skills \
  ~/.trae/skills ~/.trae-cn/skills ~/.cursor/skills ~/.config/opencode/skills \
  ~/.hermes/skills ~/.workbuddy/skills; do
  [ -d "$dir" ] || continue
  echo "=== $dir ==="
  find "$dir" -maxdepth 2 -type l 2>/dev/null | while read link; do
    target=$(readlink "$link")
    echo "$link -> $target"
  done
done
```

**预期结果**：所有软链均指向 `~/.agents/skill-lib/.dist/current/skills/<name>`，零命中 `skills-moved-aside`。

若发现间接引用（如某个脚本通过绝对路径引用了 moved-aside），需要单独排查：
```bash
grep -r "skills-moved-aside" ~/.agents/skill-lib/scripts/ 2>/dev/null
grep -r "moved-aside" ~/.agents/skill-lib/vendor/*/ 2>/dev/null
```

#### 3.2.2 registry.json 命中检查

```bash
# 检查技能名是否在注册表中
SLUG="frontend-dev"
python3 -c "
import json, sys
with open('$HOME/.agents/skill-lib/registry.json') as f:
    reg = json.load(f)
skills = reg.get('skills', [])
found = [s for s in skills if s.get('name') == '$SLUG']
print(f'命中: {len(found)} 项')
for s in found:
    print(f\"  {s['name']} v{s.get('version','?')} @ {s.get('path','?')}\")
"
```

**规则**：被任何 agent 的 registry 或缓存引用的技能，**不可归档**（归档后对应 agent 将无法加载）。

#### 3.2.3 .dist/current 软链检查

```bash
cd ~/.agents/skill-lib
# 查看当前发布的软链列表，与待归档技能名比对
find .dist/current/skills -maxdepth 1 -type l -exec basename {} \; | sort > /tmp/current-skills.txt
comm -23 <(echo "待归档技能名列表" | tr ' ' '\n' | sort) /tmp/current-skills.txt
```

**规则**：在 `.dist/current/skills` 中存在软链的技能，**不可直接归档**——必须先 `link --prune` 解除软链，或者确认该技能已不再需要被加载。

### 3.3 打包归档流程

#### Step 1：准备归档目录

```bash
DATE=$(date +%Y%m%d)
ARCHIVE_BASE="$HOME/backups/skill-migrate-20260511/archived-${DATE}"
mkdir -p "$ARCHIVE_BASE"
```

#### Step 2：创建清单（manifest）

```bash
# manifest 格式：批次<TAB>技能名<TAB>原路径<TAB>字节数<TAB>tree_hash
{
  echo "# 归档 manifest"
  echo "# 批次日期: $(date +%Y-%m-%d)"
  echo "# 字段: 批次<TAB>技能名<TAB>原路径<TAB>字节数<TAB>tree_hash"
} > "$ARCHIVE_BASE/manifest.txt"

# 对每项执行（示例：WB 批次）
while read -r skill_dir; do
  name=$(basename "$skill_dir")
  relpath="WB/skills-moved-aside/$name"
  size=$(du -sb "$skill_dir" | awk '{print $1}')
  hash=$(python3 - "$skill_dir" <<'PY'
import sys
sys.path.insert(0, os.path.join(os.environ['HOME'], '.agents', 'skill-lib', 'scripts'))
from skillctl import tree_hash
print(tree_hash(sys.argv[1]))
PY
  )
  printf "%s\t%s\t%s\t%s\t%s\n" "WB" "$name" "$relpath" "$size" "$hash" >> "$ARCHIVE_BASE/manifest.txt"
done < <(find ~/.workbuddy/skills-moved-aside -maxdepth 1 -mindepth 1 -type d)
```

#### Step 3：生成 tgz

```bash
# 推荐方式：先构建目录列表，再一次性打包（避免逐文件追加导致问题）
cd "$HOME/.workbuddy/skills-moved-aside"
ls -1d */ | sed 's|/$||' > /tmp/skill-list.txt
tar -czf "$ARCHIVE_BASE/moved-aside-wb-${DATE}.tgz" \
  --transform="s|^|originals-132/|" \
  -T /tmp/skill-list.txt
```

#### Step 4：计算并写入 sha256

```bash
cd "$ARCHIVE_BASE"
sha256sum *.tgz > sha256.txt
cat sha256.txt
```

#### Step 5：移动原件（可选，释放 moved-aside 空间）

```bash
# 把移动前的原件复制到 originals/ 保存
mkdir -p "$ARCHIVE_BASE/originals-132"
cp -R ~/.workbuddy/skills-moved-aside/* "$ARCHIVE_BASE/originals-132/" 2>/dev/null

# 清空 moved-aside（仅在本批次内操作）
rm -rf ~/.workbuddy/skills-moved-aside/*
rmdir ~/.workbuddy/skills-moved-aside 2>/dev/null  # 可选，保留空目录结构
```

#### Step 6：抽样验证

```bash
# 从 tgz 解压到临时目录，对比 tree_hash
TMPDIR=$(mktemp -d)
tar -xzf "$ARCHIVE_BASE/moved-aside-wb-${DATE}.tgz" -C "$TMPDIR"
HASH_ORIG=$(python3 -c "import sys; sys.path.insert(0,'$HOME/.agents/skill-lib/scripts'); from skillctl import tree_hash; print(tree_hash('/path/to/original/frontend-dev'))" 2>/dev/null || true)
HASH_TAR=$(python3 -c "import sys; sys.path.insert(0,'$HOME/.agents/skill-lib/scripts'); from skillctl import tree_hash; print(tree_hash('$TMPDIR/frontend-dev'))")
echo "原: $HASH_ORIG  解包后: $HASH_TAR  一致: $([ "$HASH_ORIG" = "$HASH_TAR" ] && echo ✓ || echo ✗)"
rm -rf "$TMPDIR"
```

**验收标准**：随机抽检 ≥ 5 项，tree_hash 全部一致。

### 3.4 更新文档和同步

每次归档完成后，必须更新以下文档：

| 文档 | 更新内容 | 位置 |
|---|---|---|
| 归档清单 | 新增一行记录（技能名/批次/tgz/manifest/sha256） | `moved-aside-inventory.md` |
| 仓库状态 | git add + commit 文档变更 | `~/.agents/skill-lib/` |
| 同步给其他 agent | 如有必要，通知其他 agent 维护者本次归档 | Discord/飞书群 |

**moved-aside-inventory.md 模板节**：
```markdown
## 第 N 批归档（YYYY-MM-DD）

| 来源 | tgz | 数量 | sha256 | 状态 |
|---|---|---|---|---|
| WB | `moved-aside-wb-YYYYMMDD.tgz` | 125 | `abc123...` | ✅ 已归档（manifest + sha256） |
| OC | `moved-aside-oc-YYYYMMDD.tgz` | 7 | `def456...` | ✅ 已归档（同上，与 WB 同批次） |
| rest | `moved-aside-rest-YYYYMMDD.tgz` | 7 | `ghi789...` | ✅ 已归档（独立批次，有单独 manifest + sha256） |
```

### 3.5 16 个 agent 目录链接/断链复核

复核对象：`~/.agents/skills`、`~/.claude/skills`、`~/.codebuddy/skills`、`~/.codex/skills`、`~/.trae/skills`、`~/.trae-cn/skills`、`~/.cursor/skills`、`~/.config/opencode/skills`、`~/.hermes/skills`、`~/.workbuddy/skills` 等（共约 16 个目录，视实际安装情况）。

复核三件事：

1. **软链指向正确性**：所有 `.dist/current` 下的技能，对应的 agent 目录软链是否仍指向该路径。
   ```bash
   # 验证 soft-link consistency
   cd ~/.agents/skill-lib
   for link_target in .dist/current/skills/*/; do
     skill_name=$(basename "$link_target")
     for agent_dir in ~/.agents/skills ~/.claude/skills ~/.workbuddy/skills; do
       if [ -L "$agent_dir/$skill_name" ]; then
         actual=$(readlink "$agent_dir/$skill_name")
         expected=".dist/current/skills/$skill_name"
         if [ "$actual" != "$expected" ]; then
           echo "⚠ ${skill_name} @ ${agent_dir}: 漂移! 期望=${expected}, 实际=${actual}"
         fi
       fi
     done
   done
   ```

2. **实体目录（非软链）检测**：哪些 agent 目录里出现了实体目录而非软链（绕过统一源的信号）。
   ```bash
   find ~/.agents/skills -maxdepth 1 -type d ! -name '.' ! -name '.*' | while read d; do
     name=$(basename "$d")
     # 检查是否是预期的软链位置
     if [ ! -L "$HOME/.agents/skills/$name" ] && [ -d "$HOME/.agents/skills/$name" ]; then
       echo "★ 实体目录（绕过统一源）: $name @ ~/.agents/skills"
     fi
   done
   ```

3. **Registry 与实际加载一致性**：`registry.json` 中记录的技能数 vs 实际加载数。
   ```bash
   python3 ~/.agents/skill-lib/scripts/skillctl.py status
   ```

### 3.6 仓库状态检查

归档完成后，必须满足以下条件：

```bash
cd ~/.agents/skill-lib
# 1. Git 干净（无未提交变更）
git status --short
# 期望：空输出（或仅有 .gitignore 列出的忽略文件）

# 2. 无 tgz 文件混入仓库
git ls-files '*.tgz'
# 期望：空输出

# 3. 无未追踪的非文档文件
git clean -n -d --exclude='*.md' --exclude='archived-*'
# 期望：空输出（或仅有预期的归档目录）

# 4. 最后一次 commit 包含归档变更
git log --oneline -5
```

**合规标志**：
- `[OK] git clean`：无意外变更
- `[OK] 无 tgz 在仓库内`
- `[OK] 归档清单已提交`：最近 commit 包含 `moved-aside-inventory.md` 更新

### 3.7 工具脚本参考

#### skillctl.py 主要子命令速查

```bash
# 校验所有技能完整性
python3 ~/.agents/skill-lib/scripts/skillctl.py validate

# 建立/更新各 Agent 的软链（加 --prune 清理过期软链）
python3 ~/.agents/skill-lib/scripts/skillctl.py link --prune

# 查看当前发布版本和漂移
python3 ~/.agents/skill-lib/scripts/skillctl.py status

# 查找某技能来自哪里
python3 ~/.agents/skill-lib/scripts/skillctl.py which <name>

# 将技能导入库（从任意目录）
python3 ~/.agents/skill-lib/scripts/skillctl.py import --from-dir <path>
```

#### 辅助脚本

```bash
# 批量检测 moved-aside 技能的可移性
python3 << 'PYEOF'
import os, json, subprocess

SKILL_LIB = os.path.expanduser("~/.agents/skill-lib")
MOVED_ASIDE_DIRS = {
    "WB": os.path.expanduser("~/.workbuddy/skills-moved-aside"),
    "OC": os.path.expanduser("~/.openclaw/skills-moved-aside"),
}

# 加载 registry
with open(f"{SKILL_LIB}/registry.json") as f:
    reg = json.load(f)
reg_names = {s["name"] for s in reg.get("skills", [])}

for label, path in MOVED_ASIDE_DIRS.items():
    if not os.path.isdir(path):
        print(f"[{label}] 目录不存在，跳过")
        continue
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        if not os.path.isdir(full) or name.startswith("."):
            continue
        in_reg = name in reg_names
        dist_link = os.path.islink(f"{SKILL_LIB}/.dist/current/skills/{name}")
        print(f"[{label}] {name}: registry={in_reg} dist_link={dist_link}")
PYEOF
```

---

## 四、常见问题及解决方案

### Q1：某技能在多个 agent 目录下都有实体目录（非软链），如何处理？

**根因**：CLI `skill --install` 或手动安装写入了实体目录，绕过了统一库。

**解决方案**：
1. 用 `skillctl which <name>` 查哪个是 canonical 源。
2. 将非 canonical 实体目录移入 moved-aside → 按本流程归档。
3. 执行 `skillctl link` 重新挂回软链。
4. 在文档中标注该技能的「权威源位置」，避免后续再次安装覆盖。

### Q2：归归档后，某个 agent 无法加载该技能（软链断了）？

**排查步骤**：
```bash
# 1. 确认软链是否还存活
ls -la ~/.agents/skills/<name>
# 期望：lrwxrwxrwx -> ../../.agents/skill-lib/.dist/current/skills/<name>

# 2. 确认 .dist/current 下是否有该技能的软链
ls ~/.agents/skill-lib/.dist/current/skills/ | grep <name>

# 3. 若 .dist/current 下有但软链断了，重新 link
python3 ~/.agents/skill-lib/scripts/skillctl.py link
```

**预防**：归档前先做「3.2 可移性检查」，确保目标技能不在 registry.json 中被引用、不在 `.dist/current` 中有软链。

### Q3：moved-aside 中有技能名与库内技能名相同，但内容不同的版本？

这是经典的**版本漂移**问题，常见于 CLI 自安装和人工安装并存时。

**解决方案**：
1. 用 `diff -r` 对比两个版本的 SKILL.md。
2. 以库内 `.dist/current` 版本为准（canonical），moved-aside 版本并入归档。
3. 在文档中记录「版本冲突裁决」，注明采用哪一代以及理由。

### Q4：归档后如何回滚？

```bash
# 从归档中提取单个技能
ARCHIVE_DIR="$HOME/backups/skill-migrate-20260511/archived-20261110"
TARBALL="$ARCHIVE_DIR/moved-aside-wb-20261110.tgz"
SKILL_NAME="frontend-dev"

# 解压到临时目录找对应项
TMPDIR=$(mktemp -d)
tar -tzf "$TARBALL" | grep "$SKILL_NAME" | head -1
# 提取指定项
tar -xzf "$TARBALL" -C "$TMPDIR" --wildcards "*${SKILL_NAME}*"

# 恢复路径（视情况选择）
# A. 恢复到 moved-aside
cp -R "$TMPDIR"/*/ ~/.workbuddy/skills-moved-aside/
# B. 恢复到库内（需 admin 权限）
# python3 ~/.agents/skill-lib/scripts/skillctl.py promote "$SKILL_NAME"
rm -rf "$TMPDIR"
```

### Q5：16 个 agent 目录软链遍历太慢，如何加速？

使用 `find` 并行 + 过滤空结果：
```bash
# 只列出有软链的 agent 目录（减少 IO）
for d in ~/.agents/skills ~/.claude/skills ~/.workbuddy/skills ~/.hermes/skills; do
  links=$(find "$d" -maxdepth 1 -type l 2>/dev/null | wc -l)
  [ "$links" -gt 0 ] && echo "$d ($links links)" && find "$d" -maxdepth 1 -type l
done
```

---

## 五、工具/命令清单

### 5.1 必备工具

| 工具 | 用途 | 位置/安装方式 |
|---|---|---|
| `skillctl.py` | 技能库核心管理（validate/link/status/which/import/promote） | `~/.agents/skill-lib/scripts/skillctl.py` |
| `tar` | 打包/解包 tgz | macOS 内置 |
| `sha256sum` / `shasum` | 校验和计算 | macOS 内置 (`shasum -a 256`) |
| `git` | 版本控制 & 状态检查 | macOS 内置 |
| `find` + `readlink` | 软链审计 | macOS 内置 |
| `python3` | 脚本 & tree_hash 计算 | macOS 内置 |
| `comm` / `sort` | 差集比较 | macOS 内置 |

### 5.2 常用命令速查卡

```bash
# ===== 库内操作 =====
cd ~/.agents/skill-lib
python3 scripts/skillctl.py validate          # 全量校验
python3 scripts/skillctl.py status            # 看当前发布状态
python3 scripts/skillctl.py link --prune      # 建软链并清理过期
python3 scripts/skillctl.py which <name>      # 查技能来源
python3 scripts/skillctl.py stage <name>      # 复制到 staging/
python3 scripts/skillctl.py promote <name>    # 从 staging/ 入库
python3 scripts/skillctl.py rollback          # 回退上一版本

# ===== 归档操作 =====
DATE=$(date +%Y%m%d)
ARCHIVE="$HOME/backups/skill-migrate-20260511/archived-${DATE}"
mkdir -p "$ARCHIVE"
tar -czf "$ARCHIVE/moved-aside-wb-${DATE}.tgz" -C "$HOME/.workbuddy/skills-moved-aside" .
shasum -a 256 "$ARCHIVE"/*.tgz > "$ARCHIVE/sha256.txt"
cat "$ARCHIVE/sha256.txt"

# ===== 审计操作 =====
# 扫全 home 的软链指向
grep -rl "skills-moved-aside" ~ 2>/dev/null | grep -v ".agents/skill-lib"
# 查 registry 中技能数
python3 -c "import json; d=json.load(open('$HOME/.agents/skill-lib/registry.json')); print(len(d['skills']))"
# 对比 .dist/current vs skills/ 目录差异
diff <(ls ~/.agents/skill-lib/.dist/current/skills/) <(ls ~/.agents/skill-lib/skills/)
```

### 5.3 验收 Checklist（每次归档后打勾）

- [ ] manifest 数据行总数 = 各 tgz 顶层目录数之和
- [ ] sha256.txt（或分批次对应文件如 sha256-rest.txt）各 tgz 都有对应条目
- [ ] 抽样 5 项 tree_hash 与原 moved-aside 一致
- [ ] `skillctl status` 显示无漂移
- [ ] `git -C ~/.agents/skill-lib status --short` 为空（或仅有新提交的 .md 更新）
- [ ] `git -C ~/.agents/skill-lib ls-files '*.tgz'` 为空
- [ ] 16 agent 目录无软链指向已归档的 moved-aside 路径
- [ ] moved-aside 相应源目录已清空（或已迁移至 originals/）

---

## 六、实操作复盘结果

> 以下数据来源于 2026-11-10 的实际归档任务，已完成的实践可复用为本方案的验证基准。

### 6.1 任务概况

| 项目 | 数据 |
|---|---|
| 归档日期 | 2026-11-10 |
| 原 moved-aside 待处理项 | 135 项（来自首次全量扫描） |
| 新增补充项（任务 E 实验备份） | 4 项 |
| **归档总计** | **139 项** |
| 第一批（🟢 纳管+重复，含 WB 125 + OC 7） | `moved-aside-wb-20261110.tgz`（23 MB）+ `moved-aside-oc-20261110.tgz`（32 KB），共 132 项 |
| 第二批（🟠/⚪ 剩余 + 实验备份 4 项） | `moved-aside-rest-20261110.tgz`（38 KB），共 7 项 |
| 归档目标目录 | `~/backups/skill-migrate-20260511/archived-20261110/` |
| 原件保留 | ✅ 全程未删除任何文件 |

### 6.2 分类裁决结果

| 类别 | 数量 | 归档位置 |
|---|---|---|
| 🟢 已确认纳管 | 92 | `originals-132/` + tgz |
| 🟢 重复副本（已裁决不收编） | 40 | 同上 |
| 🟠 已裁决不收编、保留待查 | 1 | `originals/` + rest tgz |
| ⚪ 已判定空壳、不收编 | 2 | 同上 |
| **合计** | **135** | —— |

> 附：任务 E 实验备份 4 项已并入第二批归档（`moved-aside-rest-20261110.tgz`）。

### 6.3 可移性检查实测

- **16 agent 目录软链扫描**：命中 0 条指向 `skills-moved-aside`（全 home 扫描）。
- **registry.json（289 项）**：0 项命中 moved-aside 中被归档的技能名。
- **`.dist/current/skills`**：0 项软链指向待归档技能。
- **结论**：139 项（含任务 E 实验备份 4 项）全部安全可归档。

### 6.4 验证结果

| 校验项 | 结果 |
|---|---|
| WB tgz 顶层目录数 | 125 ✓（与 manifest.txt 中 WB 条目数对齐） |
| OC tgz 顶层目录数 | 7 ✓（与 manifest.txt 中 OC 条目数对齐） |
| rest tgz 顶层目录数 | 7 ✓（与 manifest-rest.txt 中 7 条数据行对齐） |
| manifest 数据行总数 | 132 + 7 = **139**（含注释头的文件总行数分别为 144 / 14，对齐） |
| tree_hash 抽样（5 项） | 全部一致 ✓ |
| rest 批次抽样（agent-reach-agents、skill_2053082421296758784） | 解包后 tree_hash 与 manifest 完全一致 ✓ |

> ⚠️ 注意：manifest 和 sha256 是归档区的独立文件，**不打包进 tgz**。上述"对齐"指 tgz 顶层目录数与各自 manifest 中的数据行数量一一对应。

### 6.5 经验教训

1. **manifest 口径易混**：56 vs 33 差额源于把「顶层实体目录」和「嵌套示例」混报。后续统一用 `link --prune` 的「跳过」计数，不再混合口径。
2. **docx/pdf 误判**：初期以为可以回填（找到 hermes/archive 下的 Nous Research 版），但 diff 后发现脚本集合不同，回填会造成断链。修正为「判不了→A 类→不动」。
3. **agent-reach 两代设计冲突**：CLI v1.5.0 与旧代 router 模式命令体系不同，强行合并会产生不一致技能输出。最终采取「库内升版至 v1.5.0 权威版，旧代保留在 archived/ 不动」的策略。
4. **实体目录绕过统一源**：v1.5.0 CLI `skill --install` 会把 agent-reach×3 替换为实体目录（`~/.agents`/`~/.claude`/`~/.openclaw`），导致 `link --prune` 跳过。需在归档报告中标注此类「双源」风险。

---

*本文档是基于 2026-11-10 真实归档实践的提炼，可直接作为后续迁移/归档操作的标准化指南。*
