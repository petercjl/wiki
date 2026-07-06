---
title: Seed-Audio短视频音频一致性工作流
type: playbook
created: 2026-07-04
updated: 2026-07-04
domain: 视觉制作
tags: [visual-production, ai-video, workflow, api]
sources:
  - raw/api/evolink/seed-audio-voice-docs-2026-07-04/doubao-seed-audio-1-0-voices.md
  - raw/experiments/seed-audio-short-video-audio-workflow-2026-07-04/source-notes.md
  - _meta/extraction-notes/seed-audio-short-video-audio-workflow-2026-07-04/coverage-matrix.md
status: active
---

# Seed-Audio短视频音频一致性工作流

这页解决 AI 短视频里的两个音频一致性问题：

1. 多段视频连接成完整短视频后，BGM 如何保持统一。
2. 多段视频里同一个人物说话时，人物声线如何保持统一。

它和 [[domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法|AI长视频连续性组接方法]] 是同一类问题：不要强求单个生成模型一次解决全部连续性，而是把连续性拆成可控资产、剪辑和后期流程。

## 核心判断

短视频分段生成时，不要让每段视频各自生成 BGM。每段自带 BGM 会导致音乐风格、节拍、情绪和混音不一致，而且 BGM 一旦与环境音、人声耦合，后期很难干净移除。

更稳的路径是：

1. 分段生成视频时，尽量不要生成背景音乐。
2. 如果需要环境声或动作音效，可以单独设计，但要避免与 BGM 混在一起。
3. 所有视频片段剪接成完整短视频后，再为整条片子生成统一 BGM。
4. 如果原视频已有对白和 BGM，要先做源分离，保留对白轨，再重新配乐。

本机实验中，用 Seed-Audio 给 63 秒无声故事视频生成 BGM，效果可用；又对一段含对白和原 BGM 的短视频做 Demucs 人声分离，再用 Seed-Audio 生成新 BGM，Peter 听后认为新 BGM 甚至优于原片。

## BGM工作流

### 无原始对白

当目标是为整条短视频配乐：

1. 先完成所有 10-15 秒视频片段的画面生成。
2. 用剪辑工具或 ffmpeg 合成无 BGM 版本。
3. Agent 观察成片内容，把剧情、节奏、情绪曲线、品类气质转写成音乐 prompt。
4. 用 Seed-Audio 生成整条片子的 instrumental BGM。
5. 在剪映、Premiere、ffmpeg 或其他工具里混入整条 BGM。

Prompt 应包含：

- 总时长，例如 `60-second`。
- `instrumental`。
- `No vocals, no speech, no lyrics`。
- 情绪曲线，而不只是单个风格词。
- 乐器、密度、节奏。
- 结尾方式，例如 clean fade out。
- 是否要给对白留空间。

### 有原始对白

当输入视频已有对白和 BGM：

1. 抽取音频。
2. 用 Demucs 等源分离工具分出 `vocals` 和 `no_vocals`。
3. 保留 `vocals` 作为对白轨。
4. 丢弃或降低原 `no_vocals`。
5. 用 Seed-Audio 生成新 BGM。
6. 混合视频画面、对白轨、新 BGM。

这个流程的边界是：对白和 BGM 如果频段严重重叠，源分离可能留下音乐残影或损伤人声。它是一个实用后期方案，不是无损还原。

## Seed-Audio声线文档事实

EvoLink 的 Seed-Audio 1.0 voices 文档说明，声音选择通过 `audio_references` 完成，每个 entry 可以是两类：

- 系统内置的 preset voice ID，即 `voice_type`。
- reference audio URL，用于参考音频/声音克隆路径。

在 prompt 中用 `@audioN` 引用第 N 个 `audio_references` 条目。文档还说明，所有预设声音都支持通过自然语言 prompt 控制 emotion、tone、style；中文 voice 也可以读英文文本。

文档页在 2026-07-04 抓取时列出 288 个 voices，主要是中文 voice，另有 15 个 ICL 英语角色 voice。这个数量和 voice ID 是时间敏感信息，生产前要回查当前 EvoLink 文档。

注意：voice name 里的 `2.0` 表示 voice library version，不等于 Seed-Audio 模型版本。

## 人物声线生成方法

人物声音参考资产的正确主线不是“从空白 prompt 里凭空生成某个身份的声音”，而是：

1. 先按人物身份、年龄、性别、职业、气质选择合适的内置 `voice_type`。
2. 再用 prompt 微调这句台词里的情绪、语气、力度、速度和状态。
3. 生成 3-5 秒干净人声，不带 BGM，不带音效。
4. 把这段音频作为后续视频模型的人物声音参考资产。

单一 voice 硬调多角色不是主方法。本机第一次实验只用 `zh_female_vv_uranus_bigtts`，通过 prompt、`speech-rate`、`pitch-rate` 尝试模拟母亲、领导、少女、反派和父亲导师。结果说明：它可以改变一点情绪和音高，但不适合承担多角色声线差异。

第二次实验改用内置角色型 `voice_type`，效果更符合工作流：

| 人物方向 | voice_type | 适用判断 |
| --- | --- | --- |
| 温柔母亲 | `zh_female_wenroumama_uranus_bigtts` | 母亲、姐姐、照顾者、保护型角色。 |
| 成熟父亲/叔叔 | `zh_male_baqiqingshu_uranus_bigtts` | 父亲、叔叔、导师、成熟男性旁白。 |
| 明亮少女 | `ICL_uranus_zh_female_chunzhenshaonv_tob` | 年轻、纯真、轻快、兴奋型角色。 |
| 邪魅反派女王 | `ICL_uranus_zh_female_xiemeinvwang_tob` | 危险、压迫、优雅、反派女性。 |
| 高冷总裁 | `ICL_uranus_zh_male_gaolengzongcai_tob` | 克制、果断、商业决策者、权力角色。 |
| 热血少年 | `ICL_uranus_zh_male_rexueshaonian_tob` | 少年主角、热血、坚定、不服输。 |

## 声线Prompt骨架

```text
@audio1 用[年龄感/身份/性格/情绪状态/说话力度]的声音说：
[台词]。
只输出这句话，不要背景音乐，不要音效。
```

示例：

```text
@audio1 用高冷、克制、果断、像商业决策者一样的男性声音说：
现在不是犹豫的时候，按计划执行，所有后果我来承担。
只输出这句话，不要背景音乐，不要音效。
```

参数上，可以微调用：

- `speech-rate`：控制说话速度。沉稳角色通常略慢，年轻活泼角色略快。
- `pitch-rate`：控制音高，但不要指望它把女声可靠变男声。
- `loudness-rate`：控制音量和力度，更多用于混音前的素材平衡。

## 3-5秒参考音频规则

如果后续视频模型只需要 3-5 秒声音参考，台词要反向设计：

- 活泼角色语速快，台词可以稍长，否则容易短于 3 秒。
- 沉稳角色语速慢，台词要短，否则容易超过 5 秒。
- 台词最好包含角色最典型的发声状态，而不是普通陈述句。
- 生成结果略长时，可以截取中间最有代表性的 3-5 秒。
- 参考音频应干净，避免 BGM、混响、音效、多人重叠。

## 决策表

| 目标 | 推荐路径 | 不推荐路径 |
| --- | --- | --- |
| 整条短视频统一 BGM | 成片后生成整段 BGM | 每个视频片段各自带 BGM |
| 保留原片对白、替换 BGM | 源分离保留 vocals，再混新 BGM | 直接在原混音上叠新 BGM |
| 生成虚构角色声线 | 选 `voice_type` 后 prompt 微调 | 一个通用声线靠 pitch/speed 硬调所有角色 |
| 复刻特定真人/品牌声线 | reference audio URL 路径，并检查授权 | 用相似 `voice_type` 冒充精确复刻 |
| 为视频模型准备声音参考 | 3-5 秒干净单人台词 | 带 BGM、多角色、混响重的片段 |

## 与视频分段的一致性关系

60 秒短视频拆成 6 段左右生成时，音频一致性应拆成三个后期资产：

1. BGM 资产：整条片子统一生成。
2. 人物声音资产：每个核心人物生成并固定 3-5 秒 voice reference。
3. 环境声/音效资产：按镜头需要局部补充，不要和 BGM 耦合。

这样，视频片段生成只负责画面和动作；声音一致性由剪辑和音频资产层统一控制。

## 未验证边界

- 本次没有证明 Seed-Audio 能直接读取视频画面并自动配乐；实验中是 Agent 先理解视频，再写文本 prompt。
- 本次没有验证 Seedance 或其他视频模型对 3-5 秒 voice reference 的保持能力。
- 本次只实测了部分 `voice_type`，没有逐一验证 288 个内置 voice 的可用性。
- API、voice list、模型能力都可能变化，正式生产前要复核 EvoLink 当前文档。

## 相关记忆

- [[domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡|Doubao-Seedance-2.0 视频生成模型卡]]
- [[domains/视觉制作/06-AI视频/02-AI商业短视频规划方法|AI商业短视频规划方法]]
- [[domains/视觉制作/06-AI视频/07-故事板铁三角AI视频控制法|AI视频控制资产系统：身份板、故事板、导演台与素材库]]
- [[domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法|AI长视频连续性组接方法]]

