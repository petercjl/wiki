# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: mixed ASR, OCR, keyframes and screen-recorded slides
- Evidence sources: timestamped ASR, 15-second keyframes, OCR, four contact sheets, repeated spoken context and the companion Feishu source
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 40:24–60:39 | ordered-method | 气质锚定、视觉符号、产品延迟登场 | 气质协调、可见证据、条件式产品登场 | ASR + slides + examples + Feishu source | high | corrected | retain sequence but make reveal conditional |
| A02 | 47:05–48:21 | causal-claim | 高级场景 | 目标人群向往的生活状态 | ASR + slide context + family example | high | corrected | explicitly reject luxury-decoration shortcut |
| A03 | 49:03–57:41 | ordered-method | 视觉符号 | 抽象价值的可见/可听证据 | ASR + running/wave/perfume examples | high | corrected | add product causality and replaceability tests |
| A04 | 57:49–60:39 | comparison | 产品最后出现 | 短广告可早露出，较长品牌片可渐进延迟主亮相 | ASR + 49-second perfume film | high | corrected | use duration/objective decision table |
| A05 | 60:40–75:00 | tool-name | LibbTV / life TV | LibTV | screen UI + repeated context | high | corrected | omit tool-specific operation from durable method |
| A06 | transcript-wide | tool-name | 寂寞 / 急梦 | 即梦 | screen UI + repeated context | high | corrected | normalize only in interpreted notes |
| A07 | 75:00–88:48 | asset-name | 30图 | 三视图 / 多角度图 | screen demonstration + repeated visual angles | high | corrected | formalize as approved multi-angle reference |
| A08 | transcript-wide | tool-name | GBT | GPT | repeated context + screen text | high | corrected | normalize only in interpreted notes |
| A09 | transcript-wide | product-name | 养生糊 | 养生壶 | repeated category context + OCR | high | corrected | normalize only in interpreted notes |
| A10 | 85:38–86:40 | threshold | 超过三张都没有生成成功 | three-failure rewrite heuristic | ASR + screen context | medium | accepted-as-is | qualify as instructor budget heuristic, not universal law |
| A11 | 94:17–105:06 | causal-claim | Skill自动完成流程 | fixed workflow regenerated redundant assets and clips in this run | canvas nodes + ASR | high | corrected | retain as one observed failure case |
| A12 | 106:28–125:45 | ordered-steps | manual Agent workflow | analysis → approvals → one asset/clip → local repair | ASR + on-screen working document | high | accepted-as-is | generalize beyond platform UI |
| A13 | 118:24–127:00 | sound-boundary | shot plan includes BGM | generated segments contain no BGM; final music added in edit | source + current validated project rule | high | corrected | current project method supersedes source |
| A14 | 127:09–128:43 | causal-claim | successful conversation becomes a Skill | conversation may seed a Skill but needs contracts and clean-context tests | ASR + project Skill design protocol | high | corrected | add validation caution |
| A15 | multiple | money/model-comparison | prices, rates and model rankings | dated instructor claims | ASR only; no current primary-source verification | low | excluded-from-formal | preserve raw-only and require fresh verification |

## Corrections and cautions

- The speaker's broad use of “TVC” across screens is retained as course usage,
  not asserted as the only industry definition.
- Model comparisons, platform functions, pricing, market quotes and success
  claims are time-sensitive or anecdotal.
- AI-generated “product information” cannot create factual claims. Material,
  performance, dimensions, certification and similar facts require user or
  authoritative evidence.
- Product-understanding images are not automatically production references.
  The later workflow must deliberately approve identity references and reject
  structurally drifting derivatives.
- “Three failed generations, then rewrite” is a useful budget heuristic, not a
  universal numerical law.
