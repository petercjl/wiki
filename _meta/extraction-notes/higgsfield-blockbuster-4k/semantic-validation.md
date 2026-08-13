# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: complete official Blog + exact prompt panels + downloadable Skill + scene packages, plus ASR/visual frames from the showcase video
- Evidence sources: raw Blog HTML/Markdown, article images, downloaded Skill, four ZIP-validated scene packs, raw video, raw ASR, selective no-prompt re-ASR and keyframes
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 00:24–00:28 | product/model | Seed Dance | Seedance | official lesson title/context + official blog | high | corrected | use `Seedance`; model version must be time-stamped when used operationally |
| A02 | 00:24–00:28 | resolution | 4K | 4K | two ASR passes + official course title/blog | high | accepted-as-is | preserve as source claim, not independent quality certification |
| A03 | 00:47–00:58 | artifact | Claude scale / plot skill | Claude Skill | official companion blog explicitly identifies a Claude Skill | high | corrected | use `Claude Skill` |
| A04 | 00:47–00:58 | deliverable | script, prompts, asset sheets | script, exact prompts, asset sheets | narration + official companion blog | high | accepted-as-is | preserve as course package deliverables |
| A05 | 00:32–00:47 | ordered objective | cinematic shots → story continuity → twist → avoid random credit burn | same sequence | both ASR passes agree; visual montage supports settings | high | accepted-as-is | compile as course success criteria |
| A06 | 00:52 visual insert | asset rule | “sheet has more than one face…video model drift” | multi-face character sheets can cause identity drift; retain one face anchor | clear keyframe text + official blog lines explaining the edit | high | accepted-as-is | treat as platform-specific working rule; validate on current model before generalizing |
| A07 | 01:05–04:27 | dialogue | repeated `behind us` across almost entire film | only early sea-battle dialogue is supported; later repetitions are hallucinated | waveform context + two ASR outputs + visual evidence of long music/action stretches | high | excluded-from-formal | do not use repeated transcript after 01:26 as dialogue evidence |
| A08 | 01:57–04:27 | hallucinated anchors | repeated Seedance/Captain Rackham/parrot/desert/jungle | unsupported prompt leakage/hallucination | exact repetition matches ASR prompt and conflicts with audiovisual structure | high | excluded-from-formal | preserve only in raw ASR and document as extraction failure |
| A09 | entire film | story identity | inferred character names beyond visible/narrated evidence | unresolved in this chapter alone | names are supplied by companion blog/later lessons, not reliably by this chapter soundtrack | medium | unresolved | exclude unverified character names from chapter-1 claims; names may enter only when cited to the Blog or course assets |
| A10 | Blog metadata/body | model/version | Seedance 2.0, GPT Image 2, Claude Skill, Soul Cinema | source-specific July 2026 tool chain | official Blog text and downloaded Skill | high | accepted-as-is | preserve as the demonstrated July 2026 tool chain, not a timeless requirement |
| A11 | Blog Stage 2 | UI path | `Customize → Skills → +` | Claude Skill upload path shown by source | official Blog | high | accepted-as-is | verify the current UI before operational execution |
| A12 | Blog Hero edit | causality | multiple faces confuse Seedance and cause drift | one-face identity-anchor working rule scoped to this workflow | article text + before/after assets + video overlay | medium | corrected | phrase as a Higgsfield/Seedance practice and test on the current model before generalizing |
| A13 | Blog prompt corpus | model behavior | prompt block structure controls shots | thirteen exact source prompts share a stable spine with optional blocks | verbatim prompt corpus + downloaded Skill | high | accepted-as-is | compile as a reusable schema while preserving exceptions and optionality |
| A14 | downloadable Skill | directive conflict | Skill says positive phrasing only; some examples/locks contain negative wording such as `no drift` or `does not cut` | positive-first rule with explicit control exceptions demonstrated by the source | downloaded `SKILL.md` and prompt corpus | high | corrected | do not turn “positive only” into an absolute parser rule; preserve source-tested control phrases where needed |
| A15 | scene ZIPs | asset completeness | each scene pack is self-contained | later packs omit recurring button/parrot assets and depend on earlier/global assets | ZIP contents + visual inspection + prompt tags | high | corrected | future manifest must model global reusable assets and per-scene dependencies separately |

## Validation Notes

- The first ASR run used a course-specific initial prompt. During low-speech music/action passages, Whisper copied prompt terms repeatedly. This is systematic prompt leakage, not spoken content.
- A second no-prompt run removed the leaked terms but hallucinated repeated “behind us” across the remainder of the film. Visual review shows distinct desert, jungle and apartment sequences without corresponding repeated dialogue.
- Only the instructor narration through roughly 01:06 is reliable enough for direct semantic use. The showcase film is analyzed primarily as visual evidence and story structure.
- Raw transcript files remain unchanged.
- The official Blog's exact prompts remain unchanged in the raw Markdown; structural analysis is stored separately.
- The downloaded Skill was inspected but not installed or executed.
- All four scene ZIPs passed archive validation; 34 extracted images were visually matched to prompt tags with confidence notes.
