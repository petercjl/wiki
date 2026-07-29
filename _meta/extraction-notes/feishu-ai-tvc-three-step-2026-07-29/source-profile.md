# Source profile

## Source

- Type: Feishu Wiki backed by Docx
- Title: AI TVC 广告三步法
- Source manifest:
  `raw/webpages/feishu-ai-tvc-three-step-2026-07-29/source-manifest.md`
- Revision inspected: 364
- Language: Chinese, with one short English voice-over in the complete perfume
  film

## Content shape

This is a compact course handout that combines:

- a three-stage creative proposition;
- reusable formulas and long prompt templates;
- short AI-generated video demonstrations;
- two image-sequence product-entry cases;
- one approximately 48-second perfume film;
- a final-film checklist.

The media is evidentiary rather than decorative. It demonstrates contrasts,
visual-symbol categories, shot progression, and a complete-film result.

## Reliability and interpretation

- The three-stage structure is a useful creative heuristic, not a universal
  law of advertising.
- “Do not show the product first” is treated as a conditional strategy for
  brand/world-building TVCs, not a hard rule for every ecommerce or
  performance ad.
- “High-end” is frequently operationalized through open landscapes, restrained
  acting, low-saturation lighting, slow camera motion, reflective materials,
  and delayed product reveal. This can become formulaic when detached from a
  product-specific truth.
- Media examples confirm the intended visual grammar, but some symbols are
  generic and weakly attributable to the featured product.

## Rights and privacy

- The document contains an explicit no-copy/no-derivative notice.
- No course prompt is reproduced verbatim as a reusable template.
- No media binary, QR code, contact detail, or promotional collage is retained
  in the wiki.
- Formal pages should paraphrase methods, critique cases, and link to the
  original Feishu document for authorized viewing.

## Tools and evidence

- The Feishu document was resolved and inspected through the authorized user
  session; private node and document identifiers are not retained publicly.
- `lark-cli docs +fetch` retrieved the full XML structure and media block IDs.
- `lark-cli docs +media-download` downloaded temporary working copies solely
  for inspection.
- `ffprobe` verified duration, dimensions, frame rates, and audio streams.
- `ffmpeg` produced temporary contact sheets and scene-change probes.
- `whisper-cli` with `ggml-large-v3-turbo.bin` checked audio. Most clips contain
  music/ambience and produce hallucinated filler; only the complete perfume
  film has a clearly intelligible English closing voice-over.
- Temporary media is outside the wiki and is not part of the retained source
  package.
