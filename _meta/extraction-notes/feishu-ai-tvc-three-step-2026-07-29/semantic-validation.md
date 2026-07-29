# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: mixed Feishu text, images, videos and selective ASR
- Evidence sources: full Docx outline, media block inventory, visual inspection, video metadata, contact sheets, scene probes and selective Whisper ASR
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | TXT-01–04; staged media | ordered-method | 气质 → 视觉符号 → 产品延迟登场 | 产品/人群气质 → 可见证据 → 条件式产品登场 | headings + body + image/video sequence | high | corrected | keep sequence but make reveal conditional |
| A02 | VID-01; VID-02; VID-07; VID-18 | comparison | early product is weak | direct exposition is weak only when it displaces the intended brand world | visual comparison | high | corrected | do not prohibit early product exposure |
| A03 | VID-08–11 | causal-claim | freedom symbols | running, birds, waves and companionship as candidate freedom cues | labels + visual inspection | high | accepted-as-is | require product causality before reuse |
| A04 | VID-12–15 | causal-claim | healing symbols | pet, wood interior, moving sunlight and curtain as candidate healing cues | labels + visual inspection | high | accepted-as-is | treat as candidates, not formula |
| A05 | IMG-19–22 | ordered-sequence | perfume sequence | gallery → person/material → blurred product cue → packshot | image order + visual inspection | high | accepted-as-is | use as reveal analysis |
| A06 | IMG-23–27 | ordered-sequence | car sequence | road → person → embodied emotion → driver → vehicle | image order + visual inspection | high | accepted-as-is | use as stronger causal analysis |
| A07 | VID-32 | duration/count | complete perfume film | 48.25-second film with approximately fifteen visual transitions | metadata + scene probe + contact sheet | high | accepted-as-is | describe structure without copying film |
| A08 | VID-32 | speech | music-region ASR text | only clearly intelligible closing English voice-over is usable | selective Whisper + manual listening | high | corrected | paraphrase; reject other hallucinated speech |
| A09 | image alt text | media-label | perfume images described as automobile | perfume imagery | visual inspection + section position | high | corrected | ignore generated alt-text error |
| A10 | source heading | rights-boundary | no-copy/no-derivative notice | do not redistribute media binaries or long prompts | page heading | high | accepted-as-is | retain pointers and transformative analysis only |
| A11 | TXT-02 | aesthetic-claim | open/strange spaces are more premium | a course aesthetic preference | text + examples only | medium | corrected | do not state as category-independent fact |

## Corrections and cautions

- Product reveal in the perfume film is gradual rather than absolutely withheld:
  product cues and use appear before the final packshot.
- Music-only regions generated obvious ASR hallucinations; those strings are
  excluded from formal knowledge.
- Source symbols are analyzed for their function and limits, not prescribed as
  reusable luxury imagery.
