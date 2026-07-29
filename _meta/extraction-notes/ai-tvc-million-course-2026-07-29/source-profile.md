# Source profile

- Package ID: `ai-tvc-million-course-2026-07-29`
- Source: 170-minute Chinese livestream course with screen sharing, slides,
  tool demonstrations, embedded examples, instructor camera and course sales.
- Primary evidence: source video, timestamped Whisper ASR, 15-second keyframes,
  Chinese/English OCR and four contact sheets.
- Companion source: the previously ingested Feishu page
  `feishu-ai-tvc-three-step-2026-07-29`.
- Intended compilation: durable TVC creative decisions, product-reference
  preparation and controlled generation gates.
- Excluded from durable claims: current model rankings, platform UI details,
  prices, quoted market rates, promotional claims and student testimonials.
- Rights handling: retain the user-supplied source locally; do not reproduce
  long transcript passages, slides or example films in formal pages.

## Extraction

- Whisper: `large-v3-turbo`
- Keyframes: one frame every 15 seconds, 1280 px wide
- OCR: Tesseract `chi_sim+eng`
- Semantic validation: ASR ↔ OCR ↔ keyframes ↔ contact sheets ↔ Feishu source
- ASR corrections are recorded only in semantic validation; raw outputs are
  not edited.
