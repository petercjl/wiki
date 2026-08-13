# Blog Prompt Structure Analysis

## Corpus

- Five asset-building/edit prompts.
- Thirteen complete Seedance scene prompts.
- Scene-prompt text volume: approximately 135,000 characters.
- The downloadable Skill is a single `SKILL.md` and was inspected without execution.

## Stable Scene-Prompt Spine

All 13 scene prompts contain:

1. `SCENE CONTEXT`
2. `ACTIVE REFERENCES`
3. `FORMAT MODE`
4. camera direction (some prompts place `CAMERA` before or after `OPTICS`)
5. `PHYSICS`
6. `LIGHTING`
7. `AUDIO`
8. `POSITIVE LOCKS`

Most also contain `LOCATION MAP`, `FIRST FRAME / BLOCKING`, `OPTICS`, `ACTION`, `PERFORMANCE`, and `STYLE`. Specialized blocks appear only where necessary: `OUTPUT SETTINGS` in four prompts, `COLOR GRADE` in one, and `WARDROBE` in one.

This establishes a key design rule: the system is a fixed ordered spine with optional control blocks, not a universal giant template that must always include every section.

## Skill-Level Rules Recovered

- Write the visible and measurable; translate mood into blocking, muscle movement, light, timing and physical behavior.
- Each generation is a sealed document with no memory of earlier shots.
- An image tag fixes identity/appearance; text specifies action and locks the few critical details the model may drop.
- Keep appearance descriptions minimal when a reference image already carries identity.
- Never include an asset tag in a shot where the object is absent.
- Distribute style into the block that controls it: light in `LIGHTING`, acting/skin in `PERFORMANCE`, physics in `PHYSICS`, optics in `OPTICS`; keep technical format in the suffix.
- Choose control resolution by need: oner, sequential cuts without timecodes, timed multishot, or freestyle b-roll.
- Use explicit FOV anchors rather than arbitrary lens wording when precise optics matter.
- Use positive locks to restate likely failure points; avoid uncontrolled negative-prompt lists.
- Final prompt output is English, even when the user briefs the scene in another language.

## Blog-Level Operating Loop

1. Build and clean reusable assets.
2. Register every asset as a named Higgsfield Element.
3. Give Claude the same element names and only the assets needed by the current scene.
4. Describe the dramatic beat in plain language.
5. Let the Skill produce one standalone structured Seedance prompt.
6. Generate the scene.
7. Diagnose visible failures and return concrete notes to Claude.
8. Regenerate the affected scene while preserving unchanged locks.

## Distinction From the Showcase Video

The Academy video answers “what result are we targeting?” The Blog and downloadable package answer “what assets, prompt protocol, naming contract and feedback loop produce it?” The knowledge base should therefore cite the video as acceptance evidence and the Blog/Skill/assets as operational evidence.

