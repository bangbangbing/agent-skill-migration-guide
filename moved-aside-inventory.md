# skills-moved-aside 保留清单

## 头部规则

**保留到期日：2026-12-10 —— 已提前完成，不再有待到期项。**

原规则为「保留 30 天后按清单归档」。实际上 2026-11-10 一天内分两批全部归档完毕：
- 第一批（132 项，🟢 已确认纳管 92 + 🟢 重复副本 40）
- 第二批（剩余 7 项：🟠 1 + ⚪ 2 + 任务 E 的 4 个实验备份）

`~/.workbuddy/skills-moved-aside/` 顶层**已清空**（空目录保留），无需再等到 2026-12-10 处理。

## 归档状态（2026-11-10 全部完成）

**135 项已全部归档 + 4 个任务 E 实验备份一并归档，WB 侧 moved-aside 顶层清空。** 全程未删除任何原件。

归档区：`~/backups/skill-migrate-20260511/archived-20261110/`

| 内容 | 包 / 位置 | 数量 | 校验 |
|---|---|---|---|
| 第一批 WB | `moved-aside-wb-20261110.tgz`（23 MB） | 125 项 | tar 顶层 125，抽检 5 项 tree_hash 一致 |
| 第一批 OC | `moved-aside-oc-20261110.tgz`（32 KB） | 7 项 | tar 顶层 7，抽检一致 |
| 第一批清册 | `manifest.txt` + `sha256.txt` | 132 行 | 与 tar 条目 125 + 7 = 132 对齐 |
| 第二批（剩余） | `moved-aside-rest-20261110.tgz`（38 KB） | 7 项 | tar 顶层 7；抽检 `agent-reach-agents-20261110`、`skill_2053082421296758784` 解包后 tree_hash 与 manifest 完全一致 |
| 第二批清册 | `manifest-rest.txt` + `sha256-rest.txt` | 7 行 | 移动后原地复算 7/7 一致 |
| 原件（第一批 WB 125 项） | `originals-132/` | 125 项 | 保留原目录名 |
| 原件（第二批 7 项） | `originals/` | 7 项 | 保留原目录名 |

- 第二批 tgz sha256：`97b2786d83bf16d9cf832ab31b6b4a40c7057ecbae676d66f3de1945956b92ad`
- `manifest.txt` 末尾已追加「路径变更说明」：原「原路径」列保留归档时的位置，供追溯；文件名与 tree_hash 未改动。
- 第一批 OC 侧 7 项原件仍在 `~/.openclaw/skills-moved-aside/_archived-20261110/`（对应包已生成，未再迁移）。

**可移性检查（2026-11-10 实测）**：8 项均为实体目录；16 个 agent 目录内**无任何软链**指向 `skills-moved-aside`（全 home 扫描命中 0）；`registry.json` 289 项、`.dist/current/skills`、WB 技能列表缓存均**零命中**这些项目名。

**四类标记**：
- 🟢 **已确认纳管、可提前归档**：技能已在 `vendor/<group>/<slug>/` 中存在（git 跟踪），moved-aside 里是旧副本，可提前归档释放空间。
- 🟢 **重复副本、不收编（已裁决）**：2026-11-10 第 1 步逐项体检后判定为库内已有技能的重复副本，按「确实重复的不重复收编」原则不收编，可随 🟢 一并提前归档。
- 🟠 **已裁决不收编、原地保留待查**：用户明确裁决不收编，但保留 moved-aside 原件供将来核查（到期后随规则归档，不删除）。
- ⚪ **已判定空壳、不收编**：无实质正文或无任何有效资源，不收编，保留至到期日随规则归档。

## 总览

| 分类 | 数量 | 当前状态 |
|---|---|---|
| 🟢 已确认纳管 | 92 | **已归档 2026-11-10**（`originals-132/` + `moved-aside-wb-20261110.tgz`） |
| 🟢 重复副本、不收编（已裁决） | 40 | **已归档 2026-11-10**（同上） |
| 🟠 已裁决不收编、保留待查 | 1 | **已归档 2026-11-10**（`originals/` + `moved-aside-rest-20261110.tgz`） |
| ⚪ 已判定空壳、不收编 | 2 | **已归档 2026-11-10**（同上） |
| **合计** | **135** | **已归档 135 / 剩余 0，moved-aside 顶层已清空** |

> 2026-11-10 更新：原「🟡 待定性 43 项」已全部裁决完毕（41 有干货 / 2 空壳）。43 项的去向见文末三节，不再有「待定性」条目。
>
> 2026-11-10 二次更新：剩余 7 项（🟠 1 + ⚪ 2 + 任务 E 实验备份 4）已打包归档并移入 `archived-20261110/originals/`；`_archived-20261110/` 的 125 项 WB 原件移入 `archived-20261110/originals-132/`。`~/.workbuddy/skills-moved-aside/` 顶层为空。


## 🟢 已确认纳管、已归档（92 项）

> 表中 12 位 `tree_hash` 为早期扫描口径的取值，与归档实测值存在 19 项差异（字节数一致，判定为口径/时点不同而非文件改动）；当前以 `archived-20261110/manifest.txt` 中的实测值为准。

| 技能名 | 原路径 | 最后修改时间 | 大小(B) | tree_hash |
|---|---|---|---|---|
| agent-reach | OC/skills-moved-aside | 2026-07-29 11:11 | 20758 | `79d798b8df5b` |
| summarize | OC/skills-moved-aside | 2026-03-31 23:02 | 1694 | `36512e1f3286` |
| summarize-pro | OC/skills-moved-aside | 2026-03-31 22:52 | 18020 | `81cafa318a78` |
| a-share-capital-flow-video | WB/skills-moved-aside | 2026-09-22 15:25 | 119536 | `d77e23c155e4` |
| a-share-ipo-first-day | WB/skills-moved-aside | 2026-09-01 09:59 | 11567 | `34e65e86166a` |
| a-share-premarket-forecast | WB/skills-moved-aside | 2026-09-22 08:41 | 41561 | `76644359dedb` |
| a-share-stock-forecast | WB/skills-moved-aside | 2026-09-17 10:48 | 206640 | `5ad58107cee0` |
| academic-research | WB/skills-moved-aside | 2026-09-09 21:35 | 93656 | `503b55ebe237` |
| ai-question-learning | WB/skills-moved-aside | 2026-09-20 16:33 | 53475 | `8a7a0b133589` |
| ai-replace-me-check | WB/skills-moved-aside | 2026-08-31 19:20 | 75090 | `f292ba052873` |
| apple-notes | WB/skills-moved-aside | 2026-08-31 19:20 | 1750 | `cb668054a4a7` |
| archify | WB/skills-moved-aside | 2026-09-10 09:42 | 7936482 | `6a4e2c446872` |
| ashare-report-audit | WB/skills-moved-aside | 2026-10-26 10:20 | 92104 | `3cf8007dbd48` |
| baoyu-cover-image | WB/skills-moved-aside | 2026-08-31 19:20 | 92095 | `be46888d9e15` |
| baoyu-infographic | WB/skills-moved-aside | 2026-08-31 19:20 | 69074 | `53412a4acc66` |
| baoyu-xhs-images | WB/skills-moved-aside | 2026-08-31 19:20 | 94754 | `b5c17a991be6` |
| book-teardown | WB/skills-moved-aside | 2026-10-03 18:17 | 36286 | `af578a493473` |
| book-writer | WB/skills-moved-aside | 2026-10-24 12:33 | 73516 | `2bec33a74ec1` |
| cc-switch-skills-migrate | WB/skills-moved-aside | 2026-10-03 15:35 | 8842 | `0fb6975717f5` |
| central-news-finance-digest | WB/skills-moved-aside | 2026-10-07 20:48 | 12725 | `4a1218b41a44` |
| cloudflare-tunnel-diagnose | WB/skills-moved-aside | 2026-09-27 16:20 | 7649 | `f9f2cc139c5e` |
| cls-intel-radar | WB/skills-moved-aside | 2026-11-10 06:59 | 492072 | `966c1deed502` |
| code-generation-standards | WB/skills-moved-aside | 2026-09-09 20:58 | 3321 | `d5743f7d1a57` |
| code-vuln-miner | WB/skills-moved-aside | 2026-09-10 09:42 | 16724 | `2c6a656fc987` |
| content-performance-analysis | WB/skills-moved-aside | 2026-08-31 19:21 | 12364 | `befa68fda98f` |
| content-safety-guardrails | WB/skills-moved-aside | 2026-08-11 12:58 | 4299 | `030f69249f9d` |
| content-topic-generator | WB/skills-moved-aside | 2026-08-31 19:21 | 25236 | `2f70fd8873bc` |
| copyright-compliance | WB/skills-moved-aside | 2026-08-11 12:58 | 1997 | `3c41f62a22b5` |
| copywriter | WB/skills-moved-aside | 2026-08-31 19:21 | 10940 | `7950838c4b29` |
| deepseek-harness-dsh | WB/skills-moved-aside | 2026-08-27 23:26 | 18964 | `bba51d17f5d5` |
| dsh-audiogen | WB/skills-moved-aside | 2026-09-15 11:25 | 5609 | `1564bacca15c` |
| dsh-imported-skills-hub | WB/skills-moved-aside | 2026-08-28 10:49 | 3064 | `1e3831c46a27` |
| dsh-opencode-free-models | WB/skills-moved-aside | 2026-09-30 20:33 | 13937 | `b24d39d44b6d` |
| dsh-plugin-bridge | WB/skills-moved-aside | 2026-08-28 10:48 | 5907 | `ff07380e006f` |
| expert-roundtable | WB/skills-moved-aside | 2026-09-09 21:36 | 7694 | `4f52ab82fb85` |
| feishu-doc-to-xhs-poster | WB/skills-moved-aside | 2026-09-14 20:26 | 4858 | `9c69189c2264` |
| ffmpeg-video-editor | WB/skills-moved-aside | 2026-08-31 19:21 | 10185 | `f4ae1d8a981b` |
| find-skills | WB/skills-moved-aside | 2026-04-04 10:21 | 11655 | `919282ffcc93` |
| gold-deep-research | WB/skills-moved-aside | 2026-09-09 21:36 | 18777 | `344ce335f97a` |
| guizang-ppt-skill | WB/skills-moved-aside | 2026-08-30 09:05 | 11766076 | `5bf96fca0ed6` |
| guofeng-video-static-activate | WB/skills-moved-aside | 2026-08-18 22:37 | 6191 | `894f7827dcd1` |
| h3-prompt-writing | WB/skills-moved-aside | 2026-09-23 22:46 | 82963 | `1615b6f20832` |
| harness-optimizer | WB/skills-moved-aside | 2026-09-09 21:30 | 4735 | `7cc56c1e072e` |
| history-today-tech-article | WB/skills-moved-aside | 2026-11-10 07:58 | 10643 | `838c89173cb2` |
| hook-and-headline-writing | WB/skills-moved-aside | 2026-08-31 19:21 | 144249 | `544c86f92286` |
| hot-topics | WB/skills-moved-aside | 2026-08-31 19:21 | 8785 | `7e6a8cbd85c8` |
| humanizer-zh | WB/skills-moved-aside | 2026-10-24 12:33 | 9115 | `1da41dbe1701` |
| ima-skills | WB/skills-moved-aside | 2026-09-23 22:46 | 25795 | `920825276183` |
| interaction-design-review | WB/skills-moved-aside | 2026-08-11 11:44 | 6982 | `140036e0535a` |
| jackyshen-gen-short-video-script | WB/skills-moved-aside | 2026-08-31 19:21 | 8499 | `3e16a0d8b7f0` |
| karpathy-guidelines | WB/skills-moved-aside | 2026-09-10 10:39 | 3226 | `b2aae8198f56` |
| long-horizon-harness | WB/skills-moved-aside | 2026-08-30 09:40 | 3598 | `2d7793407432` |
| majia-chatcut-koubo | WB/skills-moved-aside | 2026-09-13 18:23 | 2549743 | `33549d278ca2` |
| md-to-html-pdf | WB/skills-moved-aside | 2026-10-13 16:12 | 15579 | `db72366cbba7` |
| minimind | WB/skills-moved-aside | 2026-09-09 21:31 | 4258 | `f6c15d9d1abd` |
| multi-agent-orchestration | WB/skills-moved-aside | 2026-09-09 21:36 | 6196 | `7339c59525d3` |
| mybase-nyf-export | WB/skills-moved-aside | 2026-09-30 13:03 | 4002 | `105d7d14c1f6` |
| nano-banana-pro | WB/skills-moved-aside | 2026-08-31 19:21 | 6403 | `6bc7814a54a2` |
| obsidian | WB/skills-moved-aside | 2026-09-23 22:46 | 85210 | `83d54a20d814` |
| obsidian-kb | WB/skills-moved-aside | 2026-10-14 19:12 | 18234 | `a472f3cfbe79` |
| omnivoice | WB/skills-moved-aside | 2026-09-09 21:29 | 4422 | `cb9385215491` |
| openclaw-starter-guide | WB/skills-moved-aside | 2026-10-24 12:33 | 12670 | `208ca425331d` |
| opencode-free-models-workbuddy | WB/skills-moved-aside | 2026-10-25 23:58 | 473869 | `39ef7e969e41` |
| openmaic | WB/skills-moved-aside | 2026-09-09 21:34 | 42182 | `d539f49d0655` |
| patent-disclosure | WB/skills-moved-aside | 2026-09-09 21:35 | 5725 | `e3eafc906f7f` |
| pdf-to-interactive-web | WB/skills-moved-aside | 2026-10-25 09:40 | 36679 | `0521b5a5e206` |
| pdf-web-export | WB/skills-moved-aside | 2026-10-15 08:09 | 140220 | `a42756855721` |
| poem-verify | WB/skills-moved-aside | 2026-10-19 12:24 | 3265 | `921b1eeca99d` |
| ponytail | WB/skills-moved-aside | 2026-09-10 10:45 | 10096 | `4642350fee59` |
| port-agent-skill | WB/skills-moved-aside | 2026-09-09 20:37 | 4198 | `e5c5b6ddb40b` |
| pptx-generator | WB/skills-moved-aside | 2026-09-23 22:46 | 37459 | `714c6f719ec6` |
| prompt-precision-vocab | WB/skills-moved-aside | 2026-10-26 22:28 | 39136 | `68c2e0d78e97` |
| research-report-html-builder | WB/skills-moved-aside | 2026-09-30 12:09 | 38220 | `23d2b0859888` |
| reverse-engineer-anything | WB/skills-moved-aside | 2026-10-21 15:27 | 89939 | `11fd82285da0` |
| seedance-2-5 | WB/skills-moved-aside | 2026-10-20 19:52 | 44093 | `5b9d5bf8b165` |
| self-improving-agent | WB/skills-moved-aside | 2026-08-31 19:21 | 55145 | `21535302812b` |
| sensenova-image-sync | WB/skills-moved-aside | 2026-10-18 20:38 | 21659 | `5fcce04364c4` |
| seo-content-writer | WB/skills-moved-aside | 2026-08-31 19:21 | 54736 | `83e789ccd6d3` |
| shotcut-headless-editor | WB/skills-moved-aside | 2026-09-16 14:22 | 16433 | `442048e492a8` |
| skill-auditor | WB/skills-moved-aside | 2026-08-11 13:27 | 4601 | `582a7c8b10e6` |
| summarize | WB/skills-moved-aside | 2026-04-03 19:59 | 3228 | `481fd6c95727` |
| summarize-pro | WB/skills-moved-aside | 2026-08-31 19:21 | 19131 | `672f0e1980cc` |
| table-to-chart | WB/skills-moved-aside | 2026-08-31 19:21 | 4577323 | `de4d3cc78931` |
| timesfm-forecasting | WB/skills-moved-aside | 2026-09-09 22:42 | 32182 | `767c61d1cd5b` |
| tool-discovery-orchestration | WB/skills-moved-aside | 2026-08-11 12:58 | 2841 | `95cade15377e` |
| toutiao-draft-publisher | WB/skills-moved-aside | 2026-10-29 10:43 | 13749391 | `7605506c84c2` |
| trae-launch | WB/skills-moved-aside | 2026-10-12 13:41 | 2423 | `76694db88454` |
| video-shotcraft | WB/skills-moved-aside | 2026-08-30 09:16 | 19046 | `a3cc71f30b99` |
| visualization-standards | WB/skills-moved-aside | 2026-09-10 09:42 | 7761 | `9b169403dae4` |
| wb-task-inbox | WB/skills-moved-aside | 2026-09-21 21:09 | 6283 | `fc43a2ff1a35` |
| whisper-transcription | WB/skills-moved-aside | 2026-08-31 19:21 | 14760 | `965cc1ac1561` |
| yt-dlp-downloader | WB/skills-moved-aside | 2026-08-31 21:12 | 51289 | `692bcb2c6f15` |

## 🟢 重复副本、不收编、已归档（已裁决，40 项）

2026-11-10 逐项体检：去掉 frontmatter 后统计非空行/实质行（排除纯 `#` 标题），并与库内同名技能逐行比对。以下 40 项正文一致、或为库内旧版子集，按「确实重复的不重复收编」原则**不收编，仅记账**，已随 🟢 一并提前归档。

| 技能名 / 目录名 | 原路径 | 库内对应 slug | 实质行（moved / 库内） |
|---|---|---|---|
| find-skills-skill | OC/skills-moved-aside | find-skills | 66 / 168（本地为旧代，库内已升级） |
| openclaw-agent-browser | OC/skills-moved-aside | agent-browser | 84 / 84（正文逐行一致） |
| openclaw-skill-vetter | OC/skills-moved-aside | skill-vetter | 192 / 194（仅去 emoji、ClawHub→community 的净化差异） |
| openclaw-tavily-search | OC/skills-moved-aside | tavily-search | 16 / 16（正文完全一致） |
| A股四类主体资金区分 | WB/skills-moved-aside | ashare-four-participant-capital-flow | 104 / 104 |
| A股洗筹出货判别 | WB/skills-moved-aside | ashare-washout-vs-distribution | 71 / 71 |
| A股资金流向分析技能 | WB/skills-moved-aside | ashare-capital-flow-analysis | 73 / 73 |
| openclaw-tavily-search | WB/skills-moved-aside | tavily-search | 16 / 16 |
| skill_2052764137292271616（frontend-dev） | WB/skills-moved-aside | frontend-dev | 366 / 366 |
| skill_2053081352079101952（apple-reminders） | WB/skills-moved-aside | apple-reminders | 47 / 47 |
| skill_2053081792154468352（browser-use） | WB/skills-moved-aside | browser-use | 146 / 146 |
| skill_2053081855772266496（earnings-tracker） | WB/skills-moved-aside | earnings-tracker | 115 / 115 |
| skill_2053082074731966464（habit-tracker） | WB/skills-moved-aside | habit-tracker | 36 / 36 |
| skill_2053082097175687168（humanizer） | WB/skills-moved-aside | humanizer | 214 / 249（库内多「中文适配」章节） |
| skill_2053082253572640768（lark-unified） | WB/skills-moved-aside | lark-unified | 381 / 381 |
| skill_2053082332061896704（llm-wiki） | WB/skills-moved-aside | llm-wiki | 92 / 92 |
| skill_2053082413554933760（multi-search-engine） | WB/skills-moved-aside | multi-search-engine | 95 / 95 |
| skill_2053082438073974784（news-summary） | WB/skills-moved-aside | news-summary | 58 / 58 |
| skill_2053082521955860480（openai-whisper） | WB/skills-moved-aside | openai-whisper | 15 / 15 |
| skill_2053082622976532480（qmd） | WB/skills-moved-aside | qmd | 67 / 67 |
| skill_2053082773933727744（skill-scanner） | WB/skills-moved-aside | skill-scanner | 202 / 246（库内多「中文风险分级」章节） |
| skill_2053083202046337024（xurl） | WB/skills-moved-aside | xurl | 7 / 7 |
| skill_2053083649073352704（wechat-miniprogram） | WB/skills-moved-aside | wechat-miniprogram | 202 / 202 |
| skill_2053084036212973568（tencent-docs） | WB/skills-moved-aside | tencent-docs | 120 / 120 |
| skill_2057443722237636608（knowledge-framework-builder） | WB/skills-moved-aside | knowledge-framework-builder | 283 / 283 |
| skill_2059464154913587200（a-stock-data） | WB/skills-moved-aside | a-stock-data | 1709 / 1709 |
| skill_2059984290577739776（tencentcloud-ocr-questionmarkagent） | WB/skills-moved-aside | tencentcloud-ocr-questionmarkagent | 183 / 183 |
| skill_2076628582742429696（a-share-daily-review） | WB/skills-moved-aside | a-share-daily-review | 332 / 332 |
| skill_2091018464477057024（westock-data） | WB/skills-moved-aside | westock-data | 119 / 119 |
| 代码审查 | WB/skills-moved-aside | code-review | 97 / 97 |
| 前端原型交付验证 | WB/skills-moved-aside | frontend-prototype-delivery-verification | 88 / 88 |
| 复杂任务推进 | WB/skills-moved-aside | complex-task-execution | 55 / 55 |
| 安全审计 | WB/skills-moved-aside | security-audit | 49 / 49 |
| 小红书视频内容研究 | WB/skills-moved-aside | xhs-video-content-research | 134 / 134 |
| 技能设计规范 | WB/skills-moved-aside | skill-design-standards | 114 / 114 |
| 政策文章市场影响研究 | WB/skills-moved-aside | policy-article-market-impact-research | 40 / 40 |
| 每天一首古诗词 | WB/skills-moved-aside | daily-classical-poem | 278 / 278（库内多 1 个附属文件） |
| 每日记忆蒸馏 | WB/skills-moved-aside | daily-memory-distillation | 114 / 114 |
| 竞赛通知解析与备考规划 | WB/skills-moved-aside | competition-notice-to-study-plan | 79 / 79 |
| 结果校验 | WB/skills-moved-aside | delivery-result-verification | 26 / 26 |

## 🟠 已裁决不收编、已归档（1 项）

| 技能 | 原路径 | 判定 | 说明 |
|---|---|---|---|
| nano-banana-pro（`skill_2053082421296758784`） | WB/skills-moved-aside/skill_2053082421296758784 | **已裁决不收编（用户决定，2026-11-10）** | moved-aside 这份是完整实现：52 行正文 + `scripts/generate_image.py`（调 Gemini 3 Pro Image，支持 1K/2K/4K 与图生图），另有 `_skillhub_meta.json`，共 7.8 KB。库内 `vendor/*/nano-banana-pro` 是**有意退役的 stub**（12 行，正文指向主版本 `AI绘图`，退役理由=内容重复）。用户裁定不复活、不收编、不覆盖 stub，库内继续维持退役状态；**moved-aside 原件未删除**，2026-11-10 已打包进 `moved-aside-rest-20261110.tgz` 并移入 `archived-20261110/originals/skill_2053082421296758784/`。<br>功能重叠关系：`AI绘图` 是当前唯一图片生成/编辑入口；本件的独立价值仅在那个 `generate_image.py`（直连 Gemini 3 Pro Image 的裸脚本）。将来若需要「不依赖 Skill 体系、直接跑脚本出图」的路径，可单独把这个脚本迁出复用，无需复活整个技能。 |

## ⚪ 已判定空壳、不收编、已归档（2 项）

| 技能名 / 目录名 | 原路径 | 判定 | 理由 |
|---|---|---|---|
| a-share-participant-flow-video | WB/skills-moved-aside | **已判定空壳、不收编** | 无 SKILL.md，目录内只有一个空的 `scripts/`，0 文件 0 字节（2026-08-06 创建后未填充） |
| openclaw-agent-browser | WB/skills-moved-aside | **已判定空壳、不收编** | `name: retired-openclaw-agent-browser`、`version: 9999.0-retired`、`user-invocable: false`，正文 6 行实质内容全为退役声明，实际能力已由 `agent-browser` 承接（库内 84 实质行） |

> 以上 3 节共 43 项，全部裁决完毕。2026-11-10 两批归档完成后，43 项对应原件均已移入 `archived-20261110/`（第一批入 `originals-132/`，第二批入 `originals/`），**全程未删除任何文件**；`~/.workbuddy/skills-moved-aside/` 顶层已清空，原定 2026-12-10 到期处理不再需要。