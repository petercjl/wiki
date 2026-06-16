# Omission Audit

## No Text Node Omission

All 101 unique XMind nodes are present in `source-inventory.md` and `coverage-matrix.md`.

## Merged Nodes

Most text nodes are marked `merged` because XMind fragments were compiled into a continuous domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook rather than copied one node per paragraph. This is intentional: the formal page preserves the accounting logic, branch hierarchy, platform-specific distinctions, and examples while avoiding a raw node dump.

## Unresolved Image Nodes

28 screenshot/diagram nodes are marked `unresolved` in the coverage matrix because exact UI path text was not OCR-transcribed during this run. They are not omitted:

- The original XMind files are archived.
- The extracted image assets are archived under `raw/data/ecommerce-platform-settlement-accounting-xmind-2026-02-06/resources/`.
- `image-asset-inventory.md` maps each image node to its source unit and asset path.

Future audit can OCR or visually inspect those screenshots to promote the exact platform UI paths from `unresolved` to `formalized`.
