# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: ASR + burned-in subtitles + video frames + spoken context
- Evidence sources: original.mp4, transcript.raw.srt, transcript.raw.json, 59 keyframes
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 00:13–00:22 / 06:16 | entity | 海地 / 小海莉 | 海蒂 | 烧录字幕与角色名 | high | corrected | 正式页统一用“海蒂” |
| A02 | 00:13–00:17 | title | 《海地和爷爷》 | 《海蒂和爷爷》 | 烧录字幕与影片名 | high | corrected | 正式页用规范片名 |
| A03 | 00:17–00:22 | place | 团团里 | 村庄里 | 烧录字幕 | high | corrected | 校订稿写“村庄” |
| A04 | 01:23–01:26 | camera term | 景别的所放 | 景别的缩放 | 字幕与语义 | high | corrected | 不保留错词 |
| A05 | 01:42–01:46 | narrative term | 平铺直竖 | 平铺直叙 | 烧录字幕 | high | corrected | 正式页保留原意 |
| A06 | 03:22–03:25 | craft term | 分型设计 | 分镜设计 | 烧录字幕 | high | corrected | 统一用“分镜” |
| A07 | 05:13–05:18 | camera term | 景别私似的锁在 | 景别死死地锁在 | 烧录字幕 | high | corrected | 正式页写“锁在近景” |
| A08 | 05:30–05:40 | shot size | 小玄境 / 玄境 | 小全景 / 全景 | 331秒画面字幕 | high | corrected | 正式页用“小全景” |
| A09 | 05:53–05:58 | causal phrase | 场景在全世界的过程中 | 场景在诠释的过程中 | 354秒画面字幕 | high | corrected | 用规范词形 |
| A10 | 06:04–06:08 | colloquial noun | 老泡 | 老炮 | 字幕与口语语义 | high | corrected | 不进入正式方法正文 |
| A11 | 06:13–06:16 / 07:42 | structure | 最后的一杆利 / 这杆里 | 最后的一个案例 / 这个案例 | 上下文与字幕 | high | corrected | 按案例组织 |
| A12 | 09:21–09:24 | ordered path | 由简路凡 | 由简入繁 | 烧录字幕 | high | corrected | 训练路径保留 |

## Systematic Variant Search

- 已检索上述全部 raw 变体；错词只在机器识别文件中保留，校订稿与正式页未遗留。
- “导演思维＝导演动机＋导演工具”是来源观点。
- 视频没有直接给出 AI Prompt 模板；正式页中的 Prompt 映射明确标为知识库应用编译。
