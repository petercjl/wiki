# Seed-Audio 短视频音频工作流实验记录

Capture date: 2026-07-04

## Source Scope

本 raw 记录来自 2026-07-04 与 Peter 的工作会话，围绕 AI 短视频音频一致性拆解两类问题：

1. 多段视频合成为整条短视频时，如何保证 BGM 一致。
2. 生成短视频人物对话时，如何准备 3-5 秒的人物声线参考音频。

配套官方/中转 API 文档已归档：

- `raw/api/evolink/seed-audio-voice-docs-2026-07-04/doubao-seed-audio-1-0-voices.md`
- `raw/api/evolink/seed-audio-voice-docs-2026-07-04/doubao-seed-audio-1-0-voices.html`

## Local Tool

- CLI: `/Users/pechen/.local/bin/seedaudiocli`
- Model: `doubao-seed-audio-1-0`
- Skill: `/Users/pechen/.local/share/seedaudiocli/SKILL.md`
- Config: `/Users/pechen/.config/seedaudiocli/seedaudiocli.env`

Do not preserve API keys in wiki raw.

## BGM Experiment 1

Goal: 验证 Seed-Audio 能否根据短视频剧情/气质提示，为无声视频生成整段统一 BGM。

Files:

- Silent video: `/Users/pechen/AI/Research/seed_audio_bgm_test/christmas_63s_silent.mp4`
- Generated BGM: `/Users/pechen/AI/Research/seed_audio_bgm_test/seed_audio_downloads/christmas-ghost-story-bgm.mp3`
- Final video: `/Users/pechen/AI/Research/seed_audio_bgm_test/christmas_63s_seed_audio_bgm.mp4`

Observed conclusion:

- Seed-Audio 可以根据文本化剧情、画面气质、情绪曲线生成完整 BGM。
- 本次不是“直接看视频自动配乐”，而是 Agent 先把画面/剧情转成音乐 prompt，再由 Seed-Audio 生成。

## BGM Experiment 2

Input video: `/Users/pechen/Downloads/测试短视频.mp4`

Goal: 原视频中同时有 BGM 和人物对话，测试能否去除原 BGM、保留人物对白，再重新生成统一 BGM。

Pipeline:

1. 用 ffmpeg 抽取原始音频。
2. 用 Demucs 分离 `vocals.wav` 和 `no_vocals.wav`。
3. 保留 `vocals.wav` 作为对白轨。
4. 用 Seed-Audio 根据视频情节生成新 BGM。
5. 用 ffmpeg 把视频画面、对白轨、新 BGM 混合。

Files:

- Extracted audio: `/Users/pechen/AI/Research/bgm_replace_test/original_audio.wav`
- Dialogue track: `/Users/pechen/AI/Research/bgm_replace_test/demucs_out/htdemucs/original_audio/vocals.wav`
- Removed-BGM track: `/Users/pechen/AI/Research/bgm_replace_test/demucs_out/htdemucs/original_audio/no_vocals.wav`
- Generated BGM: `/Users/pechen/AI/Research/bgm_replace_test/seed_audio_downloads/pursuit-dialogue-new-bgm.mp3`
- Final fixed version: `/Users/pechen/AI/Research/bgm_replace_test/final_dialogue_with_new_seed_bgm_v2.mp4`

Observed conclusion:

- Peter 听后认为新 BGM 非常好，甚至优于原片。
- 关键不是让每段生成视频自带 BGM，而是把 BGM 后置到最终剪辑阶段。
- 对白与原 BGM 耦合时，可先做源分离；但质量取决于原片混音与人声/BGM 重叠程度。

## Voice Experiment 1: Single Preset Voice

Goal: 测试仅用一个系统女声 `zh_female_vv_uranus_bigtts`，是否能靠 prompt、语速、音高模拟多种人物。

Output directory:

- `/Users/pechen/AI/Research/voice_consistency_test/`

Files:

- `01_warm_mother.mp3`, 3.918s
- `02_calm_leader.mp3`, 3.239s
- `03_bright_girl.mp3`, 2.142s
- `04_dark_villain.mp3`, 5.799s
- `05_father_mentor_attempt.mp3`, 5.982s

Observed conclusion:

- 这种方式可以改变部分情绪、节奏和音高，但不适合作为“多角色声线”主方法。
- 用同一个女声硬调男性/父亲/导师声线，边界明显。

## Voice Experiment 2: Built-in Character Voice Types

Goal: 按 EvoLink 文档中正确方法，先选择内置 `voice_type`，再用 prompt 微调性格、情绪和说话状态。

Output directory:

- `/Users/pechen/AI/Research/voice_consistency_test_builtin/`

Generated samples:

| Role | voice_type | File | Duration |
| --- | --- | --- | --- |
| 温柔母亲 | `zh_female_wenroumama_uranus_bigtts` | `01_warm_mother_builtin.mp3` | 5.799s |
| 成熟父亲/叔叔 | `zh_male_baqiqingshu_uranus_bigtts` | `02_mature_father_builtin.mp3` | 7.706s |
| 明亮少女 | `ICL_uranus_zh_female_chunzhenshaonv_tob` | `03_bright_girl_builtin.mp3` | 3.605s |
| 邪魅反派女王 | `ICL_uranus_zh_female_xiemeinvwang_tob` | `04_dark_queen_builtin.mp3` | 5.538s |
| 高冷总裁 | `ICL_uranus_zh_male_gaolengzongcai_tob` | `05_cold_ceo_builtin.mp3` | 4.571s |
| 热血少年 | `ICL_uranus_zh_male_rexueshaonian_tob` | `06_hot_blood_boy_builtin.mp3` | 3.605s |

Observed conclusion:

- 这批比单一女声硬调更接近真实工作流。
- 角色身份、年龄感、性别和基础气质应主要由 `voice_type` 决定。
- Prompt 负责微调当前台词里的情绪、状态、力度和节奏。
- 3-5 秒参考音频需要控制台词长度；沉稳/慢速角色容易超过 5 秒，可以缩短台词或后期截取最具代表性的 3-5 秒。

## Current Working Hypothesis

短视频音频一致性的主线：

1. 分段生成视频时，不让每段自带 BGM。
2. 最终剪辑阶段统一加整段 BGM。
3. 有原始对白时，先用源分离保留人声，再替换 BGM。
4. 人物声线参考资产不要只靠 prompt 从空白生成；应优先选择匹配人物身份的内置 `voice_type`，再用 prompt 做性格/情绪微调。
5. 如果需要复刻某个具体演员/主播/品牌声线，再考虑 reference audio URL 的声音克隆路径。

