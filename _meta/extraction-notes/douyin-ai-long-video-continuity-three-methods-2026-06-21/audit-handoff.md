# Audit Handoff

| Field | Value |
| --- | --- |
| Source slug | `douyin-ai-long-video-continuity-three-methods-2026-06-21` |
| Adapter | `llm-wiki-ingest/adapters/transcript.md` with video-course branch |
| Raw media | `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/source-0.mp4` |
| Raw transcript | `raw/transcripts/douyin-ai-long-video-continuity-three-methods-2026-06-21/source.raw.txt` |
| Raw visual evidence | `raw/assets/douyin-ai-long-video-continuity-three-methods-2026-06-21/keyframes/` and `keyframes-ocr.raw.txt` |
| Formal page | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` |
| Coverage matrix | `_meta/extraction-notes/douyin-ai-long-video-continuity-three-methods-2026-06-21/coverage-matrix.md` |
| Omission audit | `_meta/extraction-notes/douyin-ai-long-video-continuity-three-methods-2026-06-21/omission-audit.md` |
| Query entry | No new `queries/` file; existing `08-Agent使用模板：AI视频导演分镜.md` updated |
| Known unresolved items | Author-mentioned external document/prompt pack was not captured; exact scientific claim about visual persistence was not independently verified |

## Expected Future Agent Use

- Diagnose why an AI long video has visible jumps between generated segments.
- Convert a long-video idea into stable 15-second or shorter shot groups.
- Write prompts that preserve action overlap between segments.
- Decide when to use shot-size/angle changes, match-on-action, or storyboard grouping.

## Validation Notes

- `validate_ingest_contract.py`: OK. It reported verbatim-match warnings because the formal page reconstructs the spoken source into a reusable playbook instead of copying raw transcript sentences.
- `placeholder_scan.py`: OK for `domains/视觉制作/06-AI视频`, with `SHELL: 0`, `THIN: 0`.
- `wiki_cli_route_audit.py`: route from `08-Agent使用模板：AI视频导演分镜.md` includes the new long-video continuity page; global unresolved links reported by the script are pre-existing vault-wide noise.

Re-run:

```bash
python3 /Users/pechen/.codex/skills/llm-wiki-ingest/scripts/validate_ingest_contract.py --wiki-root /Users/pechen/wiki --notes-dir /Users/pechen/wiki/_meta/extraction-notes/douyin-ai-long-video-continuity-three-methods-2026-06-21 --formal /Users/pechen/wiki/domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md
python3 /Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/scripts/placeholder_scan.py /Users/pechen/wiki/domains/视觉制作/06-AI视频
```
