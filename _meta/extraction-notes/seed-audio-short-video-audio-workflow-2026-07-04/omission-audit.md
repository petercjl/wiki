# Omission Audit

## Raw-only

- Full 288-row EvoLink voice table remains in `raw/api/evolink/seed-audio-voice-docs-2026-07-04/doubao-seed-audio-1-0-voices.md`.
  - Reason: the formal page needs a selection method and tested role examples, not a duplicated long table that may drift as provider docs update.

## Omitted with Reason

- Temporary failed or superseded intermediate BGM mix.
  - Reason: final fixed version `final_dialogue_with_new_seed_bgm_v2.mp4` is the relevant experiment artifact.

## Unresolved

- Whether Seed-Audio can directly analyze video frames and auto-score BGM without an Agent-written textual prompt.
  - Reason: local experiment used text prompt derived from video/story, not direct video input.
- Whether every documented `voice_type` is accepted by the current EvoLink endpoint at generation time.
  - Reason: only six role voice IDs were live-tested in this batch.
- Whether Seedance/other video models preserve the reference voice consistently across generated clips.
  - Reason: this ingest only covers generation of the reference audio asset, not downstream video-model voice adherence.

