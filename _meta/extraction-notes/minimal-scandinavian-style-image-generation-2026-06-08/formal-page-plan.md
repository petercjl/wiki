---
title: 极简北欧风生图风格库 Formal Page Plan
type: source-summary
created: 2026-06-08
updated: 2026-06-08
domain: meta
tags: [domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index, knowledge-base, research]
sources:
  - raw/webpages/visual-style/domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/domains/视觉制作/05-小红书风格AI生图/index-style-image-generation-2026-06-08.md
  - raw/webpages/visual-style/domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/domains/视觉制作/05-小红书风格AI生图/index-web-research-2026-06-08.md
status: active
---

# Formal Page Plan

## Architecture

The formal output is a small AI image-generation style library:

| Page | Type | Role |
| --- | --- | --- |
| `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index.md` | concept | Define visual style boundaries: palette, materials, light, spatial language, composition, adjacent style distinctions. |
| `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/01-极简北欧风AI生图Playbook.md` | domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook | Provide prompt skeletons, scene recipes, negative constraints, reference weighting, and QA checklist. |
| `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/02-极简北欧风参考图索引.md` | source-summary | Index user references and ZCOOL assets with reusable points and risk controls. |
| `queries/domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/04-AI生图风格库/01-极简北欧风/domains/视觉制作/05-小红书风格AI生图/index-image-generation.md` | query | Provide Agent routing entry for future generation, rewrite, and audit requests. |

## Routing intent

- Agents answering “极简北欧风是什么” should read the concept page.
- Agents writing prompts should read the domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook.
- Agents selecting reference images should read the gallery.
- Agents receiving vague generation requests should start from the query page.

## Thin-page risk control

The plan intentionally avoids creating separate pages for palette, material, lighting, and composition because that would produce thin pages. Those concepts remain integrated in the main style page and domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook.
