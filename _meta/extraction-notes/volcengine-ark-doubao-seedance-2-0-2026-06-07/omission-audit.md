# Omission Audit

## Raw-Only Items

| source_unit_id | reason |
| --- | --- |
| SD20-NAV-001 | Console navigation and Doubao icon duplicate the formal model identity. Raw archive preserves the UI context and image URL. |
| SD20-NOISE-001 | Blank iframe and global assistant elements are dynamic console UI artifacts with no knowledge value for later agents. |

## Unresolved Items

| source_unit_id | unresolved question | handling |
| --- | --- | --- |
| SD20-NUM-001 | The bare values `3` and `0.18k` appear near model limits but have no labels in the clipping. They might be UI counters, token estimates, or display artifacts. | Preserved in raw and flagged as unresolved. Do not use for decisions without checking the live console. |

## No Intentional Knowledge Omission

All capability claims, task types, model ID, API route, pricing figures, resolution/framerate limits, source-date metadata, and the three demo prompts are represented in the formal page or marked above.
