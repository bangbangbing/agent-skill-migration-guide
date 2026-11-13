#!/usr/bin/env python3
"""Regenerate 6 rednote post PNGs using Pillow with hardcoded Chinese font."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1440
FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"

def lf(size):
    return ImageFont.truetype(FONT_PATH, size)

def rgb(h):
    h = h.lstrip('#')
    if len(h) == 3: h = h[0]*2 + h[1]*2 + h[2]*2
    return tuple(int(h[i:i+2], 16) for i in (0,2,4))

OUT = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT, exist_ok=True)

# ── Color palette ────────────────────────────────────────────────
BG       = "#FDFBF7"
WHITE    = "#FFFFFF"
BLACK    = "#1A1A1A"
GRAY     = "#666666"
DARK     = "#333333"
ORANGE   = "#FF6B35"
GREEN    = "#2D6A4F"
BLUE_C   = "#1565C0"
PURPLE   = "#6A1B9A"
RED      = "#C62828"
LIGHT_ORG= "#FFF3E0"
LIGHT_GRN= "#E8F5E9"
LIGHT_BLU= "#E3F2FD"
LIGHT_PUR= "#F3E5F5"
ACCENT_G = "#A5D6A7"
ACCENT_B = "#90CAF9"

# ══════════════════════════════════════════════════════════════════
# PAGE 0 — COVER
# ══════════════════════════════════════════════════════════════════
def gen_cover():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    # Decorative circles
    d.ellipse((880,100,1040,260), fill=rgb("#FF6B3520"))
    d.ellipse((40,1180,200,1340), fill=rgb("#FF6B3515"))
    d.ellipse((840,1040,960,1160), fill=rgb("#2D6A4F15"))
    # Main card
    d.rounded_rectangle((60,100,1020,800), radius=32, fill=WHITE)
    # Top orange stripe
    d.rectangle((60,100,1020,124), fill=ORANGE)
    # Tag
    d.rounded_rectangle((120,180,340,228), radius=24, fill="#FFF0E8")
    f = lf(22); d.text((230,204), "技术干货 · 亲测", anchor="mm", font=f, fill=ORANGE)
    # Title
    f = lf(64); d.text((120,310), "多个 Agent", anchor="lm", font=f, fill=BLACK)
    f = lf(64); d.text((120,395), "共用技能库？", anchor="lm", font=f, fill=BLACK)
    # Subtitle
    f = lf(36); d.text((120,500), "一套可复用的迁移归档方案", anchor="lm", font=f, fill=GRAY)
    # Highlight blocks
    for i, (txt, col) in enumerate([("唯一源原则",ORANGE),("树哈希校验",GREEN),("139项无删档",BLACK)]):
        bx = 120 + i*200
        d.rounded_rectangle((bx,560,bx+180,620), radius=12, fill=col)
        f = lf(26); d.text((bx+90,598), txt, anchor="mm", font=f, fill=WHITE)
    # Bottom note
    f = lf(22); d.text((120,720), "📌 附：实操步骤图 + 决策流程图", anchor="lm", font=f, fill="#999999")
    # Illustration area
    d.rounded_rectangle((60,850,1020,1250), radius=24, fill=WHITE)
    f = lf(28); d.text((540,910), "多 Agent → 统一权威源 → 安全归档", anchor="mm", font=f, fill=ORANGE)
    # Agent boxes
    for name, tx in [("Claude",140),("OpenClaw",320),("WorkBuddy",500),("+ 其他 agent",680)]:
        d.rounded_rectangle((tx,970,tx+140,1050), radius=16, fill=rgb(LIGHT_ORG), outline=rgb(ORANGE), width=2)
        f = lf(20); d.text((tx+70,1010), name, anchor="mm", font=f, fill=rgb(ORANGE))
    # Arrow down
    d.line([(540,1070),(540,1130)], fill=rgb(GREEN), width=4)
    d.polygon([(520,1110),(540,1140),(560,1110)], fill=rgb(GREEN))
    # Unified source box
    d.rounded_rectangle((340,1140,740,1230), radius=20, fill=rgb(GREEN))
    f = lf(24); d.text((540,1180), "~/.agents/skill-lib/", anchor="mm", font=f, fill=WHITE)
    f = lf(18); d.text((540,1210), "统一权威源（软链加载）", anchor="mm", font=f, fill=rgb("#C8E6C9"))
    # Right result box
    d.rounded_rectangle((800,1070,1000,1230), radius=16, fill=rgb("#F1F8E9"), outline=rgb(GREEN), width=2)
    f = lf(18); d.text((900,1110), "✅ 实际效果", anchor="mm", font=f, fill=rgb(GREEN))
    f = lf(16); dy = 1145
    for ln in ["139 项全部归档","registry 零命中","原件完整保留","git 仓库干净"]:
        d.text((900,dy), ln, anchor="mm", font=f, fill="#555555"); dy += 25
    # Footer
    f = lf(18); d.text((540,1360), "⬇️ 下页：完整解决方案 & ⬅️ 点赞收藏备用", anchor="mm", font=f, fill="#AAAAAA")
    return img

# ══════════════════════════════════════════════════════════════════
# PAGE 1 — PAIN
# ══════════════════════════════════════════════════════════════════
def gen_page1():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    f = lf(32); d.text((80,70), "① 痛点：技能漂移是怎么发生的", anchor="lm", font=f, fill=rgb(ORANGE))
    # Card
    d.rounded_rectangle((60,100,1020,660), radius=24, fill=WHITE, outline=rgb("#E8E8E8"), width=2)
    # Description
    f = lf(24); d.text((100,160), "同一个 skill 在不同 Agent 目录下出现多份实体拷贝：", anchor="lm", font=f, fill=rgb(DARK))
    # Four agent boxes
    agents = [("~/.claude/skills/", "#E65100"), ("~/.workbuddy/skills/", "#2E7D32"),
              ("~/.openclaw/skills/", "#E65100"), ("+ 其余 4 个 agent", "#888888")]
    cols_f = ["#FFF3E0", "#E8F5E9", "#FFF3E0", "#F5F5F5"]
    cols_s = ["#FF9800", "#4CAF50", "#FF9800", "#BBBBBB"]
    xs, ws = [100,340,580,820], [200,200,200,160]
    for i,(name,col) in enumerate(agents):
        x, w = xs[i], ws[i]
        d.rounded_rectangle((x,220,x+w,320), radius=12, fill=rgb(cols_f[i]), outline=rgb(cols_s[i]), width=2)
        f = lf(20); d.text((x+w//2,260), name, anchor="mm", font=f, fill=rgb(col))
        sub = "(实体)" if i != 3 else "..."
        sc = "#888888" if i != 3 else "#AAAAAA"
        f = lf(16); d.text((x+w//2,290), sub, anchor="mm", font=f, fill=rgb(sc))
    # Unified source box
    d.rounded_rectangle((290,430,790,540), radius=20, fill="#FFF8E1", outline="#FFB300", width=3)
    f = lf(22); d.text((540,475), "~/.agents/skill-lib/.dist/current/", anchor="mm", font=f, fill="#F57F17")
    f = lf(18); d.text((540,505), "← 所有软链最终应指向这里（唯一 true source）", anchor="mm", font=f, fill="#888888")
    f = lf(16); d.text((540,530), "⚠️ 实体目录绕过了这个约束 = 版本漂移源头", anchor="mm", font=f, fill="#E65100")
    # Consequence box — 底边下移使第3条后果（760+2×30=820）完整包含
    d.rounded_rectangle((60,670,1020,850), radius=16, fill="#FFEBEE")
    f = lf(22); d.text((100,720), "后果", anchor="lm", font=f, fill=rgb(RED))
    f = lf(18); items = ["· 改一处要同步 N 遍，漏一处 = 行为不一致",
                         "· moved-aside 堆积数年无人清理",
                         "· 归档时担心误删正在使用的技能"]
    for j, item in enumerate(items):
        d.text((100,760+j*30), item, anchor="lm", font=f, fill="#888888")
    # Page number
    f = lf(18); d.text((540,1390), "上一页 ⬅ · 第 2 页 / 共 6 页 · ➡️ 下一页", anchor="mm", font=f, fill="#BBBBBB")
    return img

# ══════════════════════════════════════════════════════════════════
# PAGE 2 — FLOW
# ══════════════════════════════════════════════════════════════════
def gen_page2():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    f = lf(32); d.text((80,70), "② 解法：标准化归档六步流程", anchor="lm", font=f, fill=rgb(GREEN))
    steps = [
        ("1","扫描 + 全量清点","find ~/skills-moved-aside + 各 agent 目录"),
        ("2","分类裁决（四色标记）","🟢纳管 · 🟠待查 · ⚪空壳 · ✗重复"),
        ("3","可移性三重检查","断链复核 + registry.json 命中检测 + .dist/current 引用确认"),
        ("4","打包归档（manifest + sha256 + tgz）","两阶段：WB/OC 第一批 → rest 第二批，各自独立 manifest"),
        ("5","tree_hash 抽样验证","解压后比对 ≥ 5 项原始 tree_hash，确保一致性"),
        ("6","更新文档 + git commit + 仓库清洁确认","moved-aside-inventory.md + git ls-files '*.tgz' 为空"),
    ]
    y0, gap = 120, 195
    for i,(num,title,desc) in enumerate(steps):
        y = y0 + i*gap
        cc = GREEN if num=="6" else ORANGE
        d.ellipse((80,y,152,y+72), fill=rgb(cc))
        f = lf(28); d.text((116,y+36), num, anchor="mm", font=f, fill=WHITE)
        f = lf(22); d.text((200,y+25), title, anchor="lm", font=f, fill=rgb(BLACK))
        f = lf(16); d.text((200,y+52), desc, anchor="lm", font=f, fill="#666666")
        if i < 5:
            d.line([(116,y+76),(116,y+gap-10)], fill="#DDDDDD", width=2)
    # Tip bar
    d.rounded_rectangle((80,1280,1000,1340), radius=12, fill=rgb(LIGHT_GRN), outline=rgb(ACCENT_G), width=1)
    f = lf(18); d.text((540,1314), "💡 每步都有对应 bash 脚本片段，见完整指南", anchor="mm", font=f, fill=rgb("#2E7D32"))
    f = lf(18); d.text((540,1395), "第 3 页 / 共 6 页", anchor="mm", font=f, fill="#BBBBBB")
    return img

# ══════════════════════════════════════════════════════════════════
# PAGE 3 — RESULTS
# ══════════════════════════════════════════════════════════════════
def gen_page3():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    f = lf(32); d.text((80,70), "③ 实操结果：真实数据复盘", anchor="lm", font=f, fill=rgb(BLUE_C))
    # Overview — expanded to accommodate all text
    d.rounded_rectangle((60,100,1020,320), radius=20, fill=rgb(LIGHT_BLU), outline=rgb(ACCENT_B), width=2)
    pairs = [((100,160),"归档日期","2026-11-10"),((100,220),"归档总量","139 项"),
             ((540,160),"第一批（WB+OC）","132 项"),((540,220),"第二批（rest）","7 项")]
    for (x,y),label,val in pairs:
        f = lf(22); d.text((x,y), label, anchor="lm", font=f, fill=rgb(BLUE_C))
        f = lf(28); d.text((x+(180 if "日期" in label or "第一批" in label else 240),y), val, anchor="lm", font=f, fill=rgb(DARK))
    # Classification table
    d.rounded_rectangle((60,350,1020,710), radius=20, fill=WHITE, outline="#E0E0E0", width=2)
    f = lf(22); d.text((540,395), "分类裁决结果", anchor="mm", font=f, fill=rgb(BLACK))
    d.line([(100,415),(980,415)], fill="#EEEEEE", width=1)
    for txt,x in [("类别",120),("数量",360),("处置方式",560),("状态",820)]:
        f = lf(18); d.text((x,455), txt, anchor="mm", font=f, fill="#888888")
    d.line([(100,475),(980,475)], fill="#EEEEEE", width=1)
    rows = [
        ("🟢 已确认纳管","92","随 tgz 一并归档，标记为重复副本处理","✓ 已归档",GREEN),
        ("🟢 重复副本","40","与库内技能正文一致或子集","✓ 已归档",GREEN),
        ("🟠 已裁决不收编待查","1","版本冲突，保留至归档原地不动","保留中","#E65100"),
        ("⚪ 已判定空壳","2","frontmatter 后正文为空，不收编","已归档","#888888"),
    ]
    for i,(cat,qty,disp,status,sc) in enumerate(rows):
        y = 520+i*60
        f = lf(18); d.text((120,y), cat, anchor="lm", font=f, fill=rgb(sc))
        f = lf(18); d.text((360,y), qty, anchor="mm", font=f, fill="#333333")
        f = lf(16); d.text((560,y), disp, anchor="mm", font=f, fill="#666666")
        f = lf(16); d.text((860,y), status, anchor="mm", font=f, fill=rgb(sc))
    # Validation card — taller, text padded from edges
    d.rounded_rectangle((60,740,1020,1100), radius=20, fill=rgb(LIGHT_GRN), outline=rgb(ACCENT_G), width=2)
    f = lf(22); d.text((100,790), "校验结果 · 全部通过 ✅", anchor="lm", font=f, fill=rgb(GREEN))
    vlines = ["· WB tgz 顶层目录数：125 ✓ | OC tgz：7 ✓ | rest tgz：7 ✓",
              "· manifest 数据行总数：139（含注释头分别对齐）",
              "· tree_hash 抽样（≥5项）：全部一致 ✓ | registry.json 命中：0 ✓",
              "· git clean：无意外变更 ✓ | tgz 未混入仓库 ✓",
              "· 原件：全程未删除任何文件 ✓"]
    f = lf(18); dy = 840
    for ln in vlines:
        d.text((100,dy), ln, anchor="lm", font=f, fill="#333333"); dy += 48
    f = lf(18); d.text((540,1390), "第 4 页 / 共 6 页", anchor="mm", font=f, fill="#BBBBBB")
    return img

# ══════════════════════════════════════════════════════════════════
# PAGE 4 — TRAPS
# ══════════════════════════════════════════════════════════════════
def gen_page4():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    f = lf(32); d.text((80,70), "④ 关键陷阱 & 避坑指南", anchor="lm", font=f, fill=rgb(PURPLE))
    # Trap 1+2 — 合并为一张橙色卡，底边包住陷阱二的全部描述（y≈435）
    d.rounded_rectangle((60,100,1020,440), radius=20, fill="#FFF3E0", outline="#FFCC80", width=2)
    f = lf(24); d.text((100,155), "⚠️ 陷阱一：manifest 口径易混", anchor="lm", font=f, fill="#E65100")
    f = lf(18)
    for i,ln in enumerate(["把「顶层实体目录」和「嵌套示例」混在一起报数，导致 56 vs 33 数字对不上。",
                            "→ 修正：统一用 link --prune 的「跳过」计数，只统计顶层 skill 目录。"]):
        d.text((100,200+i*40), ln, anchor="lm", font=f, fill="#555555")
    # Trap 2
    f = lf(24); d.text((100,310), "⚠️ 陷阱二：docx/pdf 误判为可回填", anchor="lm", font=f, fill="#E65100")
    f = lf(18)
    for i,ln in enumerate(["初期以为找到 hermes/archive 下的 Nous Research 版即可回填，但 diff 后发现脚本集合不同，回填会断链。",
                            "→ 修正：CLI 契约冲突场景一律判不了→保留在 archive，不动。"]):
        d.text((100,355+i*40), ln, anchor="lm", font=f, fill="#555555")
    # Lessons — 卡片顶部紧跟陷阱卡下方（440+15=455），底部扩展至y=855保证间距
    d.rounded_rectangle((60,455,1020,855), radius=20, fill="#F3E5F5", outline="#CE93D8", width=2)
    f = lf(24); d.text((100,480), "💡 三个核心教训", anchor="lm", font=f, fill=rgb(PURPLE))
    # 使用 14pt 字体 + 主动换行，避免长行溢出右边界（原 18pt 导致 lesson1=1177px、lesson2=1084px 均超出）
    f = lf(14); dy = 530
    # Lesson 1（拆两行避免超宽）
    d.text((100,dy), "1.agent-reach 两代 CLI v1.5.0 vs router 模式命令体系不兼容，", anchor="lm", font=f, fill="#333333")
    d.text((120,dy+24), "强行合并会输出不一致。策略：库内升 v1.5.0 权威版，旧代留在 archived/不动。", anchor="lm", font=f, fill="#555555")
    dy += 58
    # Lesson 2（拆两行）
    d.text((100,dy), "2.v1.5.0 CLI skill --install 会把技能写成实体目录（绕过统一源），", anchor="lm", font=f, fill="#333333")
    d.text((120,dy+24), "link --prune 因此跳过。必须在归档报告中标注这类「双源」风险项。", anchor="lm", font=f, fill="#555555")
    dy += 58
    # Lesson 3（单行足够短）
    d.text((100,dy), "3.归档后第一时间跑 skillctl validate + git ls-files *.tgz，比事后排查省力十倍。", anchor="lm", font=f, fill="#333333")
    dy += 40
    # CTA — 紧接lessons卡下方，留15px间隙
    d.rounded_rectangle((60,870,1020,990), radius=20, fill="#E3F2FD", outline="#90CAF9", width=2)
    f = lf(22); d.text((540,915), "你的 Agent 目录下有移动硬盘般的 moved-aside 吗？", anchor="mm", font=f, fill=rgb(BLUE_C))
    f = lf(18); d.text((540,960), "这套方案已在 139 项真实场景中验证过，可直接套用", anchor="mm", font=f, fill="#666666")
    # Footer
    f = lf(18); d.text((540,1410), "第 5 页 / 共 6 页 · 完整版见 skill-migration-guide.md", anchor="mm", font=f, fill="#BBBBBB")
    return img

# ══════════════════════════════════════════════════════════════════
# PAGE 5 — BENEFITS
# ══════════════════════════════════════════════════════════════════
def gen_page5():
    img = Image.new('RGB', (W, H), rgb(BG))
    d = ImageDraw.Draw(img)
    # Main green card — expanded so CTA fits inside
    d.rounded_rectangle((60,80,1020,780), radius=28, fill=rgb(LIGHT_GRN), outline=rgb(ACCENT_G), width=2)
    f = lf(32); d.text((540,150), "为什么你需要关注这件事？", anchor="mm", font=f, fill=rgb("#2E7D32"))
    benefits = [
        (("🔒 数据安全",[
            "所有归档均有 sha256 + manifest",
            "原件全程保留，可随时回滚提取",
            "不会误删任何正在使用的技能",
        ]), 100, 200),
        (("⚡ 效率提升",[
            "139 项技能，一天内完成归档",
            "tree_hash 自动校验免去人工核对",
            "skillctl.py 工具链支持批量操作",
        ]), 520, 200),
        (("🧹 仓库整洁",[
            "git clean 零意外变更是硬指标",
            "tgz 产物绝不出现在仓库内",
            "每次归档后立即写文档并 commit",
        ]), 100, 370),
        (("🔄 标准复用",[
            "本方案已提炼为可复用 SOP 文档",
            "适合 3+ 个 Agent 并存的技术用户",
            "直接拷贝 bash 片段即可开始",
        ]), 520, 370),
    ]
    for (title, lines), tx, ty in benefits:
        d.rounded_rectangle((tx,ty,tx+380,ty+140), radius=16, fill=WHITE)
        f = lf(22); d.text((tx+30, ty+45), title, anchor="lm", font=f, fill=rgb("#2E7D32"))
        f = lf(16); dy = ty+80
        for ln in lines:
            d.text((tx+30, dy), ln, anchor="lm", font=f, fill="#555555"); dy += 25
    # CTA button — inside the green card now (top=620, bottom=700)
    d.rounded_rectangle((240,620,840,700), radius=40, fill=rgb(ORANGE))
    f = lf(26); d.text((540,672), "收藏本文 + 查看完整指南 ↓", anchor="mm", font=f, fill=WHITE)
    # Doc link card — below CTA, outside green card
    d.rounded_rectangle((60,720,1020,820), radius=16, fill=WHITE, outline="#E0E0E0", width=2)
    f = lf(20); d.text((100,770), "📄 完整方案文档", anchor="lm", font=f, fill=rgb(BLACK))
    f = lf(16); d.text((100,805), "skill-migration-guide.md · v1.0 · 2026-11-12 · 628 行实战提炼", anchor="lm", font=f, fill="#888888")
    # Footer
    f = lf(18); d.text((540,1390), "第 6 页（终页）· 有问题欢迎评论区交流", anchor="mm", font=f, fill="#BBBBBB")
    return img

# ── Generate all ─────────────────────────────────────────────────
gens = [
    ("cover.png",          gen_cover),
    ("page1-pain.png",     gen_page1),
    ("page2-flow.png",     gen_page2),
    ("page3-results.png",  gen_page3),
    ("page4-traps.png",    gen_page4),
    ("page5-benefits.png", gen_page5),
]

for fname, fn in gens:
    print(f"Generating {fname} ...", flush=True)
    img = fn()
    path = os.path.join(OUT, fname)
    img.save(path, "PNG")
    print(f"  → {path} ({img.size})", flush=True)

print("\nDone!")
