# 75 条空壳技能分类报告

生成时间：2026-11-10　|　库：`/Users/zhougj/.agents/skill-lib`


## 总览

| 类别 | 数量 | 处置 |
|---|---|---|
| A 类（路由型短入口，保持原样） | 68 | 不动 |
| B 类（有完整源，已回填+升版） | 7 | 已回填，升 metadata.version，注明来源 |
| C 类（无源可查，待用户裁决） | 0 | 不补写，保留原样 |
| **合计** | **75** | 与 75 条口径一致 |


## 判定口径

**空壳定义**：frontmatter 后正文为空（`body_nonempty ≤ 1`，且排除仅「运行期状态」说明段）。

**A 类**：正文本身就该很短——frontmatter 的 description 即完整可执行指引，且技能目录下 scripts/references 等资源真实存在。保留原样。

**B 类**：在 16 个 agent 目录 / `skills-moved-aside` / `~/backups/skill-migrate-20260511/` 下找到同一技能、且实现一致的完整正文。保留现库 frontmatter、追加源正文、升 `metadata.version`（x.y.z→x.(y+1).0）、写入 `backfilled_from`/`backfilled_at: 2026-11-10`。

**C 类**：任何源池都找不到完整正文。不补写，列出清单等用户定。


## B 类（7 条，已回填）

| 技能 | 旧版→新版 | 正文行数 | 回填来源 | 被引用情况 |
|---|---|---|---|---|
| auto-monitor | 0.1.0 → 0.2.0 | 60 | `/Users/zhougj/.hermes/skills/.archive/openclaw-imports/auto-monitor/SKILL.md` | — |
| bailian-web-search | 0.1.0 → 0.2.0 | 15 | `/Users/zhougj/.hermes/skills/.archive/bailian-web-search/SKILL.md` | — |
| dsh-opencode-xdbridge | 0.1.0 → 0.2.0 | 75 | `/Users/zhougj/backups/skill-migrate-20260511/farms-A/moved-aside-dsh/dsh-opencode-xdbridge/SKILL.md` | dsh-opencode-free-models, opencode-free-models-workbuddy |
| macro-monitor | 0.1.0 → 0.2.0 | 163 | `/Users/zhougj/.hermes/skills/.archive/openclaw-imports/macro-monitor/SKILL.md` | — |
| mcporter | 0.1.0 → 0.2.0 | 108 | `/Users/zhougj/.hermes/skills/mcp/mcporter/SKILL.md` | tencent-docs |
| security-monitor | 0.1.0 → 0.2.0 | 70 | `/Users/zhougj/.hermes/skills/.archive/security-monitor/SKILL.md` | — |
| system-resource-monitor | 1.0.0 → 1.1.0 | 13 | `/Users/zhougj/.hermes/skills/.archive/system-resource-monitor/SKILL.md` | auto-monitor |

### B 类资源自洽性说明

- auto-monitor：另复制 `scripts/monitor.sh`（源与库内同源 openclaw-imports，自洽）。
- bailian-web-search：`scripts/mcp-websearch.sh` 已存在。
- dsh-opencode-xdbridge：正文 75 行，自洽。
- macro-monitor：正文 163 行，自洽。
- mcporter：正文 108 行；已知缺口 `config/mcporter.json` 源侧不存在（正文引用，待补，属后续项）。
- security-monitor：`scripts/monitor.cjs` 已存在。
- system-resource-monitor：`scripts/monitor.sh` 已存在，自洽。

## A 类（68 条，保持原样）

说明：这 68 条均为路由型短入口，description 即完整指引、资源齐备。其中 `docx`/`pdf` 两条经核实改判 A（见下）。

### docx / pdf 改判说明

库内 docx/pdf 为 store 安装的 Z.AI 版（`_store_meta.json` version 1.0.2/1.0.4，`source: store`）。候选源为 `.hermes/skills/.archive` 下 Nous Research 版（docx v1.1.0 / pdf v1.0.0），**两者是不同实现**——回填正文引用的 12/7 个脚本在库内不存在，回填会造成正文与资源不匹配，属「判不了」情形。已停止回填、git checkout 还原 SKILL.md、4 个误复制脚本（docx_create/docx_edit/docx_read/docx_template.py）已移入 `~/backups/skill-migrate-20260511/backfill-rollback-20261110/docx/scripts/`（未删除）。判定为 A 类，保留原样。

### A 类名单（68 条）

| 技能 | 行数 | 字节 | 资源文件数 | 最后修改 | 被引用 |
|---|---|---|---|---|---|
| a-stock-analysis | 7 | 459 | 5 | 2026-11-09 21:16 | — |
| accio-mcp-cli | 8 | 442 | 0 | 2026-11-09 21:16 | lark-tools |
| aesthetic-preset-library | 7 | 493 | 1 | 2026-11-09 21:16 | — |
| alipay-authenticate-wallet | 19 | 2142 | 10 | 2026-11-09 21:16 | alipay-payment-skill |
| alipay-payment-skill | 25 | 1800 | 12 | 2026-11-09 21:16 | alipay-authenticate-wallet |
| authoring-skills | 14 | 483 | 0 | 2026-11-09 21:16 | — |
| autoclaw-billing | 8 | 1065 | 20 | 2026-11-09 21:16 | — |
| autoclaw-design-capability | 7 | 490 | 698 | 2026-11-09 21:16 | autoclaw-design-capability-noqa |
| autoclaw-design-capability-noqa | 8 | 612 | 698 | 2026-11-09 21:16 | — |
| autoclaw-im-cron | 10 | 306 | 2 | 2026-11-09 21:16 | — |
| autoclaw-pdf-ocr | 8 | 497 | 3 | 2026-11-09 21:16 | — |
| autoglm-asr-translate | 15 | 668 | 3 | 2026-11-09 21:16 | — |
| autoglm-browser-agent | 18 | 667 | 3 | 2026-11-09 21:16 | — |
| autoglm-deepresearch | 13 | 693 | 4 | 2026-11-09 21:16 | — |
| autoglm-file-upload | 12 | 422 | 3 | 2026-11-09 21:16 | — |
| autoglm-generate-image-seedream | 16 | 902 | 4 | 2026-11-09 21:16 | — |
| autoglm-image-edit | 14 | 628 | 6 | 2026-11-09 21:16 | — |
| autoglm-image-recognition | 13 | 571 | 4 | 2026-11-09 21:16 | autoglm-stock-analysis |
| autoglm-open-link | 9 | 385 | 4 | 2026-11-09 21:16 | deep-research-orchestrator |
| autoglm-remove-bg | 13 | 465 | 2 | 2026-11-09 21:16 | — |
| autoglm-search-image | 12 | 428 | 3 | 2026-11-09 21:16 | — |
| autoglm-stock-analysis | 7 | 1019 | 4 | 2026-11-09 21:16 | — |
| beida-fabao | 7 | 259 | 3 | 2026-11-09 21:16 | — |
| bestseller-pattern-decoder | 15 | 758 | 0 | 2026-11-09 21:16 | — |
| clawhub | 24 | 690 | 0 | 2026-11-09 21:16 | skillhub-preference, majia-chatcut-koubo, seo-content-writer, skill-vetter… |
| company-research | 9 | 342 | 0 | 2026-11-09 21:16 | — |
| competitive-landscape | 8 | 330 | 0 | 2026-11-09 21:16 | — |
| content-breakdown | 16 | 803 | 40 | 2026-11-10 10:32 | — |
| create-website | 16 | 502 | 0 | 2026-11-09 21:16 | — |
| ddg-search | 7 | 403 | 2 | 2026-11-09 21:16 | — |
| delivery-artifact | 16 | 740 | 126 | 2026-11-09 21:16 | frontend-page-design, deep-research-orchestrator |
| docx | 9 | 414 | 42 | 2026-11-10 11:03 | lark-unified, doc-page, wps, skill-creator… |
| feishu-chat-history | 13 | 493 | 3 | 2026-11-09 21:16 | — |
| feishu-cron-reminder | 10 | 304 | 2 | 2026-11-09 21:16 | — |
| feishu-doc | 12 | 542 | 21 | 2026-11-10 10:29 | feishu-chat-history, feishu-doc-to-xhs-poster |
| finance-search | 13 | 597 | 3 | 2026-11-09 21:16 | — |
| financial-suite | 7 | 709 | 51 | 2026-11-09 21:16 | — |
| frontend-page-design | 7 | 563 | 2 | 2026-11-09 21:16 | — |
| gildata-finance-data | 18 | 1055 | 5 | 2026-11-09 21:16 | — |
| hermes-evolution | 7 | 325 | 2 | 2026-11-09 21:16 | — |
| image-prompt-guide | 21 | 1378 | 8 | 2026-11-09 21:16 | logo-design |
| infinite-canvas-output | 10 | 312 | 2 | 2026-11-09 21:16 | — |
| jianwei | 7 | 748 | 6 | 2026-11-09 21:16 | — |
| lark-tools | 14 | 486 | 0 | 2026-11-09 21:16 | — |
| logo-design | 15 | 624 | 8 | 2026-11-09 21:16 | — |
| market-research | 9 | 238 | 4 | 2026-11-09 21:16 | — |
| marketing-ideas | 8 | 434 | 0 | 2026-11-09 21:16 | — |
| memory | 11 | 428 | 7 | 2026-11-09 21:16 | self-improving-agent, daily-classical-poem, qmd, codebase-memory… |
| news-aggregator-skill | 7 | 444 | 50 | 2026-11-09 21:16 | — |
| pdf | 13 | 426 | 41 | 2026-11-10 11:03 | agent-browser, md-to-html-pdf, a-stock-data, visualization-standards… |
| pdf-text-extractor | 17 | 451 | 10 | 2026-11-09 21:16 | — |
| people-research | 9 | 328 | 0 | 2026-11-09 21:16 | — |
| pptx | 9 | 182 | 3 | 2026-11-09 21:18 | nlm-skill, skill-creator-codex, wps, skill-creator… |
| product-attribute-analyzer | 16 | 1011 | 1 | 2026-11-09 21:16 | — |
| product-description-generator | 8 | 405 | 5 | 2026-11-09 21:16 | — |
| product-selection | 9 | 469 | 1 | 2026-11-09 21:16 | — |
| qichacha | 7 | 298 | 4 | 2026-11-09 21:16 | — |
| remotion-best-practices | 9 | 206 | 42 | 2026-11-09 21:16 | — |
| sec-search | 13 | 580 | 3 | 2026-11-09 21:16 | — |
| skill-finder | 9 | 575 | 4 | 2026-11-09 21:16 | — |
| skill-writer | 8 | 308 | 0 | 2026-11-09 21:16 | — |
| skillhub-preference | 7 | 251 | 0 | 2026-11-09 21:16 | — |
| social-network-mapper | 21 | 611 | 0 | 2026-11-09 21:16 | — |
| trend-stage-timing-analyzer | 16 | 802 | 4 | 2026-11-09 21:16 | — |
| ui-ux-pro-max | 7 | 642 | 57 | 2026-11-09 21:16 | — |
| website-builder | 8 | 206 | 3 | 2026-11-09 21:16 | — |
| wps | 24 | 899 | 4 | 2026-11-09 21:16 | — |
| xiaohongshu-content-creator | 7 | 206 | 0 | 2026-11-09 21:16 | — |

## C 类（0 条）

经完整源池检索（16 agent 目录 + skills-moved-aside + backups），**无源可查的技能为 0 条**——所有空壳要么是路由型短入口（A），要么已找到一致实现源（B）。无需用户裁决项。

---

# 任务 C 第 2 项：agent-reach 合并 — 判不了，停下报告

## 结论（修正版）

**已按 v1.5.0 权威包对齐。** 初判「两代不同设计」后进一步核实发现：本机安装的 `agent-reach` CLI 为 **v1.5.0**（`~/.agents/skill-lib` 库内 version 0.1.0 为旧代）。v1.5.0 包自带 `agent_reach/skill/SKILL.md` 与 6 个 references（search/social/career/dev/web/video），**与 openclaw/skills-moved-aside 的 6 个 references 逐字节一致**；其正文即「路由表 + 零配置快速命令 + 需登录态平台 + 环境检查 + 工作区规则 + 详细文档 + 配置渠道」完整结构。库内旧代引用命令（`agent-reach channels`/`read <url>`/`add`/`remove` 等）在本机 v1.5.0 CLI 上**不存在**（`--help` 实测仅 setup/install/configure/doctor/uninstall/skill/format/transcribe/check-update/watch/version）。判定：**旧代正文失配，不可留在库内作为主文档**。

处置：
- 库内 `SKILL.md`/`SKILL_en.md` 替换为 v1.5.0 权威正文，`metadata.version` 升为 `"1.5.0"`（含 triggers 中文路由表）。
- 6 个 references 以 v1.5.0 包为准对齐（与 moved-aside 相同内容）。
- 旧代 3 个 references（capabilities/sessions/maintenance）与旧 SKILL.md/SKILL_en.md 移入 `~/backups/skill-migrate-20260511/agent-reach-lib-outdated-20261110/`（未删除，可复核）。
- openclaw/skills-moved-aside/agent-reach 保留原样（已与 v1.5.0 一致）。

## 逐段比对

| 章节 | openclaw/skills-moved-aside（旧代 router 设计） | 库内 vendor/panniantong_agent-reach（新代统一 CLI） |
|---|---|---|
| 核心模型 | 13 平台多后端路由：mcporter call exa / curl r.jina.ai / gh / yt-dlp / bili / opencli xiaohongshu search | 统一命令 `agent-reach <channel> <action> [args]`、`agent-reach read <url>`，`--backend public-web` 兜底 |
| 环境检查 | `agent-reach doctor --json` | `agent-reach doctor --text`（统一 CLI 变体） |
| Routing table | 平台 → references/search.md、social.md、career.md、dev.md、web.md、video.md | 无此表；选路逻辑由 `agent-reach channels` 动态给出 + capabilities.md 边界表 |
| Zero-config quick commands | mcporter/curl jina/gh/yt-dlp/bili 一组旧代命令 | 无此节；公开内容优先自带工具，缺的由 `agent-reach` 补 |
| Login-backed platforms | opencli/rdt/twitter-cli 一组旧代命令 | 统一 `agent-reach login <channel>` + 专用浏览器章节 |
| Workspace rules | /tmp 与 ~/.agent-reach | 状态外置到 `~/.agents/skill-lib/state/`（任务 A 做法） |
| Detailed references | 6 个引用文件（search/social/career/dev/web/video） | 3 个引用文件（capabilities/sessions/maintenance） |
| Configure a channel | fetch install.md + 用户给 cookie | `agent-reach add/setup` + 安装报告原样展示 |

## 为什么不能合

1. **CLI 契约冲突**：moved-aside 的 Routing table / Zero-config quick commands 命令（`mcporter call exa…`、`curl r.jina.ai`、`gh search`、`yt-dlp`、`bili`、`opencli`）不属于库内新代 `agent-reach` 统一 CLI 的接口，塞进新正文会造成技能输出与真实工具行为不一致（违反「不编造技能内容」）。
2. **引用资源不兼容**：Routing table / Detailed references 指向的 6 个引用文件在库内版本不存在；强行合并会制造断链，违背「合并后确认技能在库内自洽可读」。
3. **已确认更新的部分不可覆盖**：库内 v0.1.0 是较新的一代（`{{CHANNEL_TABLE}}` 模板 + 统一 CLI，mtime 11-06；旧代 mtime 07-29），其 选路/错误码表/登录专用浏览器/渠道/管理表 章节比旧代更贴合上游现状，不应被旧代内容回退。

## 现状

- 库内 agent-reach（v0.1.0，`vendor/panniantong_agent-reach/agent-reach/`）git 状态干净，自洽可读。
- 旧代完整正文保留在 `~/.openclaw/skills-moved-aside/agent-reach/`（含 6 个 references），不删除。

## 待用户裁决

- 若坚持合并：需明确采用哪一代的 CLI 契约。若采用旧代，则引用资源也需整组迁入并改 `agent-reach channels` 相关段落，属于整体换代而非补缺。
- 若无此意图，本项判定为「判不了，保留现状」，不升版本、不动资源。
