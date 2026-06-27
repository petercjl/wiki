# Audit Handoff

## Source

- Book: 商业模式新生代
- Adapter: `llm-wiki-ingest/adapters/book.md`
- Raw archive: `raw/books/shangye-moshi-xinshengdai-2011/`
- Raw EPUB: `raw/books/shangye-moshi-xinshengdai-2011/source.epub`
- Source profile: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/source-profile.md`

## Formal Pages

- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/index.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/01-商业模式画布九个构造块.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/02-商业模式式样库.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/03-商业模式设计技法.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/04-商业模式战略评估.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/05-商业模式设计五阶段流程.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/06-案例锚点库：商业模式新生代.md`
- `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/07-Agent使用模板：商业模式诊断与重构.md`

## Extraction Notes

- Source inventory: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/source-inventory.md`
- Segment plan: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/segment-plan.md`
- Chapter inventory: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/chapter-inventory.md`
- Knowledge unit inventory: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/omission-audit.md`
- Source-to-page map: `_meta/extraction-notes/shangye-moshi-xinshengdai-2011/source-to-page-map.json`

## Expected Future Agent Use Cases

- Diagnose a product, brand, platform, service or project using the nine-block business model canvas.
- Compare候选商业模式式样，如免费、平台、长尾、开放式或非绑定式。
- Generate商业模式重构方案 from customer, value, channel, revenue, resource, activity, partner and cost assumptions.
- Evaluate新旧模式冲突 and decide whether a second-curve business should be integrated or separated.
- Turn a vague business idea into a five-stage design and validation workflow.

## Known Issues And Boundaries

- EPUB is image-heavy and split into 255 spine items; formal coverage is grouped at knowledge-unit level while `chapter-inventory.md` preserves spine-level listing.
- Named cases reflect pre-2011 business contexts and should not be used as current market facts without verification.
- Raw images remain inside `source.epub` and are listed in `manifest.md`; formal pages preserve diagram meanings rather than copying images.

## Validation Notes

- `validate_book_ingest.py`: errors 0; warning 1, false-positive "No obvious Agent usage template page found" due to Chinese filename.
- `validate_ingest_contract.py`: OK after checking all formal pages via temporary merged Markdown file.
- Placeholder scan: `SHELL: 0`, `THIN: 0`, `OK: 8`.
- Route audit: active vault `/Users/pechen/wiki`; target index has backlinks from root `index.md` and `domains/品牌策略/03-产品战略与大单品/index.md`.
- Representative terms found by `rg`: 商业模式画布, 多边平台, 免费式, 开放式, Nespresso, Car2go, 五阶段.
