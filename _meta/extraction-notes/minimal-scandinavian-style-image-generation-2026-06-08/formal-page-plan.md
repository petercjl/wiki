---
title: 极简北欧风生图风格库 Formal Page Plan
type: source-summary
created: 2026-06-08
updated: 2026-06-08
domain: meta
tags: [visual-production, knowledge-base, research]
sources:
  - raw/webpages/visual-style/minimal-scandinavian-style-image-generation-2026-06-08.md
  - raw/webpages/visual-style/minimal-scandinavian-web-research-2026-06-08.md
status: active
---

# Formal Page Plan

## Architecture

The formal output is a small AI image-generation style library:

| Page | Type | Role |
| --- | --- | --- |
| `domains/visual-production/visual-styles/minimal-scandinavian/index.md` | concept | Define visual style boundaries: palette, materials, light, spatial language, composition, adjacent style distinctions. |
| `domains/visual-production/visual-styles/minimal-scandinavian/playbook.md` | playbook | Provide prompt skeletons, scene recipes, negative constraints, reference weighting, and QA checklist. |
| `domains/visual-production/visual-styles/minimal-scandinavian/reference-gallery.md` | source-summary | Index user references and ZCOOL assets with reusable points and risk controls. |
| `queries/minimal-scandinavian-image-generation.md` | query | Provide Agent routing entry for future generation, rewrite, and audit requests. |

## Routing intent

- Agents answering “极简北欧风是什么” should read the concept page.
- Agents writing prompts should read the playbook.
- Agents selecting reference images should read the gallery.
- Agents receiving vague generation requests should start from the query page.

## Thin-page risk control

The plan intentionally avoids creating separate pages for palette, material, lighting, and composition because that would produce thin pages. Those concepts remain integrated in the main style page and playbook.
