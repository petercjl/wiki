# Knowledge Unit Inventory

## API Documentation Units

- KU-001: Seed-Audio voice selection is driven by `audio_references`.
- KU-002: `audio_references` accepts preset `voice_type` or reference audio URL.
- KU-003: `@audioN` in prompt targets the Nth reference entry.
- KU-004: Preset voices support natural-language control of emotion, tone, and style.
- KU-005: Captured voice list includes 288 voices; list is time-sensitive.
- KU-006: Voice name `2.0` is library version, not model version.
- KU-007: Tested role voices include mother, father/uncle, girl, villain queen, CEO, and hot-blooded youth.

## Experiment Units

- KU-008: BGM consistency is better handled after video assembly than inside each generated segment.
- KU-009: Seed-Audio can generate useful BGM from a text prompt derived from video/story context.
- KU-010: Direct video-frame-understanding BGM generation was not verified in this run.
- KU-011: For videos with dialogue and BGM, source separation can preserve vocals before replacing BGM.
- KU-012: A single generic preset voice is not a strong route for multi-character identity.
- KU-013: Built-in role `voice_type` plus prompt micro-control is the stronger route for fictional character voice assets.
- KU-014: 3-5 second reference clips require line-length, speed, and crop control.
- KU-015: Future Agents need a dedicated query entry for AI video audio/voice consistency.

## Output Mapping

- KU-001 to KU-014: `domains/视觉制作/06-AI视频/07-声音设计与BGM/10-Seed-Audio短视频音频一致性工作流.md`
- KU-015: `queries/AI视频音频与声线一致性入口.md`

