# Knowledge Unit Inventory

| knowledge_unit_id | source_units | knowledge_role | normalized_knowledge | status |
| --- | --- | --- | --- | --- |
| CH01-KU01 | CH01_SU03–SU06 | course contract | The course begins from a finished multi-world action short, then works backward into script, assets, prompts and scene generation. | formalized |
| CH01-KU02 | CH01_SU04 | success criteria | Success is not one attractive clip; it is cinematic shot quality, continuity from setup to twist, and controlled generation cost. | formalized |
| CH01-KU03 | CH01_SU05 | reusable resources | The official package includes script, exact prompts, asset sheets and a Claude Prompt-Builder Skill, making the course suitable for knowledge-to-Skill compilation. | formalized |
| CH01-KU04 | CH01_SU07 | asset QA rule | When a character sheet exposes multiple face anchors, Seedance may drift; use a single authoritative close-up face and remove duplicate faces from other panels. | formalized |
| CH01-KU05 | CH01_SU08–SU12 | narrative continuity pattern | A stable protagonist, recurring goal object and pursuit logic can bridge radical changes in location, costume, threat and action grammar. | formalized |
| CH01-KU06 | CH01_SU08–SU11 | production decomposition | The finished film can be decomposed into four production blocks: sea/cabin, desert, jungle and apartment twist; later lessons map directly to these blocks. | formalized |
| CH01-KU07 | CH01_SU13 | extraction QA | Music-heavy cinematic samples require visual-first validation; prompted ASR can leak prompt terms and unprompted ASR can still repeat short dialogue hallucinations. | raw-only in semantic validation |
| CH01-KU08 | CH01_SU02, SU08–SU11 | benchmark role | Chapter 1 is an acceptance benchmark and course map, not the detailed method itself; operational instructions must come from later lessons and companion assets. | formalized |
| BLOG-KU01 | BLOG-SU03–SU04 | production main line | Asset-first production precedes scene generation: broad asset ideation, controlled cleanup, named reusable elements, structured prompt generation, then video generation. | formalized |
| BLOG-KU02 | BLOG-SU06–SU10 | asset architecture | Character, location and prop sheets serve different control jobs: one authoritative identity face, navigable environment depth, and stable multi-angle prop geometry. | formalized |
| BLOG-KU03 | BLOG-SU07 | identity QA | More facial views can reduce consistency when they create competing identity anchors; retain one authoritative facial anchor while preserving non-face body/wardrobe coverage. | formalized |
| BLOG-KU04 | BLOG-SU10 | scoped image editing | Differentiate an asset by constraining the change set and positively locking all structural/background invariants. | formalized |
| BLOG-KU05 | BLOG-SU11–SU14 | Prompt-Builder contract | The human supplies script intent, scene beat, assets and corrections; the Skill translates them into a standalone structured scene document; the generator executes it. | formalized |
| BLOG-KU06 | BLOG-SU12–SU13 | cross-tool naming contract | Claude asset tags and Higgsfield Element names must match exactly so references bind deterministically. | formalized |
| BLOG-KU07 | BLOG-SU15–SU30 | prompt schema | Thirteen real prompts share a stable control spine with optional blocks selected by scene needs; the method is schema-driven rather than adjective-driven. | formalized |
| BLOG-KU08 | BLOG-SU15–SU30 | sealed-generation principle | Every generation must restate current references, geometry, timing, performance, physics, lighting, audio and likely failure locks because the model has no memory of prior shots. | formalized |
| BLOG-KU09 | BLOG-SU14 | iterative correction | Generation notes should describe visible failures precisely and feed back into the prompt builder, preserving successful locks while repairing only the failed relation. | formalized |
| BLOG-KU10 | BLOG-SU05, SU20, SU24, SU28, SU31 | reproducible evidence | The method ships with an inspectable Skill and per-scene asset packs, enabling later reproduction and forward testing instead of relying only on prose. | formalized |
