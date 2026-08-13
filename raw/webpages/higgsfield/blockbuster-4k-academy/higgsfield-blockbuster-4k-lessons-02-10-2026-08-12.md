---
title: Higgsfield Blockbuster 4K Academy 第2至10课文字说明原文
type: source-summary
created: 2026-08-12
updated: 2026-08-12
domain: 视觉制作
tags: [visual-production, ai-video, higgsfield, raw-source]
sources:
  - https://higgsfield.ai/academy/courses/blockbuster-4k
status: active
---

# Higgsfield Blockbuster 4K Academy 第2至10课文字说明原文

> 采集日期：2026-08-12。以下为登录后课程页可见的教学文字与资源标签归档，不含视频转写。原始 DOM 快照见同目录 JSON。

## 2. Stage 1: Writing the Script with Claude

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/stage-1-writing-the-script-with-claude
- 页面资源：Download Full script (PDF)

Lesson resources
Full script (PDF)
application/full script (pdf)

Everything starts with the story. In this stage you take a one-line idea and turn it into a full script — not by asking Claude to write one for you, but by making Claude interview you about it.

The starting idea

The whole film grew out of a single premise: a guy gets trapped in his little sister's AI generations — and every time he dies, he wakes up in a new world. That's it. One sentence. No scenes, no dialogue, no structure yet.

Don't say "write me a script"

Here's the key move: the idea went to Claude, but the request was not "write me a script." That kind of one-shot request always turns out terrible — Claude fills every gap with generic choices, and the result feels like it. Instead, ask Claude to expand your idea. That single change of phrasing flips the dynamic: instead of guessing, Claude starts asking you questions.

The Q&A that shapes the script

Claude's questions pin down exactly the details a lazy request would skip:

What runtime are you aiming for? — 2 minutes.
Which settings do you want? — picked together: pirates, desert, jungle.
Want a couple of plot twist suggestions? — yes, please.

Each answer narrows the script toward your film. Once the details are locked in, Claude delivers the script — built step by step through that dialogue rather than dumped out in one guess.

Why this works

Nothing good comes out of one lazy request. The details are what make it work — runtime dictates pacing, the settings define your scenes and assets, and the twist gives the story a spine. That's how you get a script that gets millions of views.

Steal it

Two ways to use this lesson:

Steal the method — bring your own one-line idea to Claude, ask it to expand the idea, and answer its questions about runtime, settings, and twists.
Steal the script — the full text of this film's script is shared with the course, so you can follow along with the exact same story.

Next up: turning this script into assets — characters, locations, and props.

## 3. Stage 2: Building Character, Location, and Prop Assets

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/stage-2-building-character-location-and-prop-assets
- 页面资源：Open image: Real-photo reference sheet: front view plus profiles；Open image: Generated 3-view pirate sheet — costume solid, grime realistic；Open image: Erasing the face from the full-body panel；Open image: Final pirate sheet with a single close-up face；Open image: Rejected cabin: lighting off, two lamps, map barely visible；Open image: Rejected cabin: table shoved into the corner；Open image: Winning cabin: lantern plus daylight rays, map centered；Open image: Ship split-screen pick one；Open image: Ship split-screen pick two — the bigger enemy ship；Open image: Edited villain ship: black open sails with the skull emblem；Open image: Canvas with all locked assets and their @tags

Every scene is built from a small asset library — here's the routine, on Scene 1.

Project setup

In Higgsfield: Cinema Studio → New Project, named "Blockbuster". Create a folder per scene with a subfolder per asset — "two weeks and four hundred generations later, you'll be glad you did this."

The hero — Pirate

Start from a real reference sheet of yourself (front view plus profiles) so the model gets your face right.

Real-photo reference sheet: front view plus profiles

Drop it into Claude and ask for a character-sheet prompt (full request in the video cue): full body front and back plus a close-up, with preferences like the yellow bandana and shark-tooth necklace. The close-up locks the face; the full body sets height.

Pro tip: ask for a grey background — zero clutter, much higher win rate.

Run Claude's detailed 3-view prompt in GPT Image 2.0 — the best model for photoreal character sheets and edits from a reference.

Generated 3-view pirate sheet — costume solid, grime realistic

Pro tip — one face to lock onto: multiple faces make Seedance drift ("by scene five your hero is a stranger"). The fix: "Erase the face from the full-body shot on the first panel."

Erasing the face from the full-body panel

Final pirate sheet with a single close-up face

Add him to the canvas — the workspace where all final assets live.

The location — the cabin

Locations carry the whole film. Ask Claude to enhance the request — captain's cabin, table, hanging lantern, map on the wall, daylight rays through the planks (see the video cue) — then batch it in Soul Cinema: 8 images per credit, great variety per prompt.

Pro tip: always ask for a 3/4 angle — it adds depth and win rate.

Rejected cabin: lighting off, two lamps, map barely visible

Rejected cabin: table shoved into the corner

Winning cabin: lantern plus daylight rays, map centered

The third wins — two light sources, map centered. Lighting sells realism.

The props — ships

Type a simple split-screen prompt straight into Soul Cinema (see the video cue) — the same ship, front and back 3/4 views — and pick two; the bigger becomes the enemy ship.

Ship split-screen pick one

Ship split-screen pick two — the bigger enemy ship

Make it intimidating with a Claude edit prompt — open the sails, turn them black, add a skull emblem in hex #D1FE17 — run in GPT Image 2.0.

Edited villain ship: black open sails with the skull emblem

Spyglass, parrot, cannon, map, cannonball — same routine: Soul Cinema for the raw pass, GPT Image 2.0 for edits and the final clean sheet.

Naming the assets

The boring step that pays off most. Name every asset with an @tag: @eduardo, @loc_cabin, @main_ship_sheet, @villain_ship_sheet, @spyglass_sheet, @parrot_sheet, @ship_cannon, @map_prop, @cannonball, @button, @eduardo_crew, @ocean_location, @island_location, @villain_captain, @helmsman_sheet, @loc_desert.

Canvas with all locked assets and their @tags

Introduce each asset to Claude by that name and add it to Higgsfield as an Element with the identical name — prompts auto-match inputs by tag during scene generation. Desert and jungle assets use the identical process, only the prompts change — all ship with the course.

## 4. Stage 3: Scene Generation with the Prompt-Builder Skill

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/stage-3-scene-generation-with-the-prompt-builder-skill
- 页面资源：Download higgsfield-seedance-prompt.skill；Download Scene 1 asset pack (zip)；Open image: The @eduardo character sheet used as a reference asset；Open image: The @map_prop treasure map asset uploaded with the request；Open image: The @eduardo_crew reference sheet — extras that match the scene

Lesson resources
higgsfield-seedance-prompt.skill
application/zip
Scene 1 asset pack (zip)
application/zip

Pre-production is done — now the shooting starts. Scene generation begins with Scene 1, and with the single most important tool in this workflow: a custom prompt-builder skill in Claude.

Scene 1: the setup

In the first scene, Eduardo digs through a cluttered cabin, finds the treasure map — and right at that moment one of his pirates bursts in: an island has been sighted.

The @eduardo character sheet used as a reference asset

Don't write prompts by hand

Seedance rewards long, precise, director-level prompts — and writing those manually is slow and inconsistent. Instead, use the prompt-builder skill built in Claude — higgsfield-seedance-prompt.skill is attached to this lesson, along with the Scene 1 asset pack so you can follow along with the exact same references. (Both also live in the Blockbuster 4K blog post, together with the full script and every prompt from this film.)

To load it:

Click Customize
Go to Skills
Hit the + button
Click Upload a skill — and that's it

The skill is loaded with director hacks and handles everything for you: it splits the scene into shots and writes detailed prompts that enhance your idea.

How to use it

The working loop for every shot is the same:

Activate the skill in the Claude bar.
Upload all the assets the shot needs from the canvas — plus the script.
Describe what happens in the scene in plain language.

For Scene 1, part 1, that means our hero digs through the cabin, finds the map, and a crew member bursts in with the news. The exact request is in the video cue — use it as written. Notice how it works: every element that must stay consistent is tagged with an asset handle — @eduardo for the hero, @loc_cabin for the room, @map_prop for the map — while the action itself is described freely, like a scene note to a director.

The @map_prop treasure map asset uploaded with the request

The extra asset: @eduardo_crew

Besides props like the map, the request pulls in one additional asset — @eduardo_crew. This is the crew reference sheet, and it gives you extras that actually match the scene: the pirate who bursts through the door looks like he belongs on Eduardo's ship, not like a random generated character.

The @eduardo_crew reference sheet — extras that match the scene

With the assets attached and the request sent, Claude gets to work — in the next lesson we'll take the detailed prompt it produces into Seedance and set the generation parameters.

## 5. Scene 1: Cabin Shot and Talking Parrot

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/scene-1-the-cabin-shot-and-the-talking-parrot
- 页面资源：Open image: parrot_sheet — scarlet macaw asset；Open image: spyglass_sheet — brass spyglass asset；Open image: main_ship_sheet — Eduardo's galleon；Open image: villain_ship_sheet — the enemy black-sailed galleon；Open image: button — the glowing green-button treasure case；Open image: ocean_location — locked ocean reference；Open image: island_location — the island in the spyglass POV

Two full director's feedback loops in this chapter: fixing the cabin shot, then adding comedy to the deck shot.

Run prompt 1a in Seedance

Claude's prompt is fully structured: SCENE CONTEXT, ACTIVE REFERENCES (each asset locked — "100% matches the reference"), numbered CUTS, OPTICS, LIGHTING, AUDIO with the crewman's line "Cap'n — island sighted, dead ahead!", and POSITIVE LOCKS like "the door stays closed until CUT 4". Paste it into Seedance: cinematic 21:9, 4K, 15 seconds, 4 batches.

Critique the first batch

Four problems: too much random stuff on the table (bottles, rags, ropes merging into each other); the pacing drags; it looks like night behind the open door, but the story is daytime; and the clip ends with Eduardo just staring — the hero should react the instant he hears the news.

Take the comments back to Claude

Send the notes straight to Claude (the exact fix request is in the video cue): scattered papers instead of clutter, a smile when he realizes he found the map, the line "You think you can outsmart me? Nice try", the map slammed down when the door opens, daytime behind the door, a run for the door at the end. Plain-language notes — Claude turns them into cut-level detail.

Prompt 1b — the small details do the work

Same settings, four new batches — much better. The smile, the map slam, the move toward the door: when the character reacts to his world, the shot feels real. One batch goes straight to the final edit.

Part 2 — out of the cabin

Eduardo runs out and spots the treasure. Give Claude the script plus all named assets, asking for a sharp zoom-in on the faraway case:

Write a prompt for scene 1, part 2 - @eduardo walks out of the cabin, @parrot_sheet lands on his shoulder. He runs up to the helm, where a pirate @eduardo_crew is looking through the @spyglass_sheet — Eduardo walks over, takes it from him and looks himself. He sees a distant island. SHARP ZOOM IN: on the beach lies @button.

This shot pulls in a whole set of props:

parrot_sheet — scarlet macaw asset

spyglass_sheet — brass spyglass asset

main_ship_sheet — Eduardo's galleon

villain_ship_sheet — the enemy black-sailed galleon

And the star of the show — @button, a mysterious little case with a glowing green button: the treasure Eduardo is hunting.

button — the glowing green-button treasure case

@ocean_location locks the ocean so the water looks identical in every batch; @island_location fixes the island seen through the spyglass.

ocean_location — locked ocean reference

island_location — the island in the spyglass POV

The comedy pass

Run prompt 1-2a in Seedance — same settings, 4 batches. Not bad, but a bit boring. Back to Claude (full request in the video cue): make his run weird and funny — tiptoes, hands slightly raised; give the parrot a voice; end on the enemy ship reveal — a crewman says "Captain, behind us" and the parrot screams it twice. A parrot screaming the bad news twice is instantly funny.

Prompt 1-2b — the parrot changes everything

The talking parrot changes the whole vibe — the scene feels alive. The opening comes from one clip, the rest from another: both go to the final edit.

## 6. Scene 1: Sea Battle and Escape Overboard

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/scene-1-the-sea-battle-and-escape-overboard
- 页面资源：Open image: Villain captain character sheet；Open image: Ship cannon asset sheet；Open image: Cannonball asset sheet；Open image: Helmsman character sheet；Open image: Hand-drawn diagram showing where the cannonball hits and where the characters stand；Open image: Desert location reference；Open image: Main character desert wardrobe sheet

The map is found, the case is spotted, the enemy is astern. Now Scene 1 turns into a full sea battle: the villain's reveal, a cannonball chase shot, and the hero's leap overboard that carries us straight into the desert.

Part 3 — the villain's introduction

The enemy captain deserves an epic entrance, so tell Claude exactly what you picture:

Write a prompt for an epic reveal of the enemy pirates: the camera moves from bottom to top along the ship @villain_ship_sheet. When we reach the deck, we see @villain_captain looking toward Eduardo's ship @main_ship_sheet. He quietly says to himself: 'Didn't see this coming, did ya?' The camera shows the bow of the ship — a fuse is lit, a cannon @ship_cannon fires. Cut to Eduardo's ship: cannonballs @cannonball fly past, hitting the water nearby. Total chaos.

Add the new assets to Claude and label them, just like before:

Villain captain character sheet
Ship cannon asset sheet
Cannonball asset sheet

The first run has a problem: the third shot (the captain's POV of the distant ship) ruins the visual flow. Ask Claude to delete it so cut 2 flows straight into cut 4 and nothing blends together — the fixed prompt is in the video cue. It turns the captain's beat into ONE unbroken take: the line, two steps to the cannon, fuse down, fire. Now the sequence makes perfect sense — light the fuse, fire, feel the impact on our side.

Shot 4 — follow the cannonball

Upload a new asset, @helmsman_sheet, and pay attention to the camera notes — they're the whole point of this shot:

Helmsman character sheet

Write a prompt for scene 1, part 4. The scene starts with the wide shot. @eduardo yells 'HARD A-PORT!' to @helmsman_sheet, who spins the wheel hard to the left. BAM — a muffled cannon shot. The camera follows the cannonball @cannonball up close. It hits the hero's ship @main_ship_sheet in slow motion.

Why follow the cannonball? Drama — it's way more impressive when you actually see it flying right at the ship. If you have a clear picture in your head, just tell Claude.

The batches reveal two problems: the cannonball lands in a different spot every time, and it shouldn't hit the heroes right away — a big water splash next to the ship in the first frame instantly says "active sea battle."

Pro tip: upload a drawing. Instead of explaining geometry in words, literally draw where the cannonball should hit and where everyone stands. One drawing tells the model what ten sentences can't — and every failed batch you avoid saves credits.

Hand-drawn diagram showing where the cannonball hits and where the characters stand

The fix request (near miss, explosion at the back of the ship per the green circle, blast throwing Eduardo forward, first wide cut removed) is in the video cue. And here 4K earns its cost: the explosion is sharp and heavy, not the usual blurry slop. Since several batches ran, combine the best parts — opening shot from batch one, the rest from batch two. That's the real lesson: run it, look at it, ask for exact changes, run it again. It's a skill that gets better with practice.

Shot 5 — abandon ship

The blast throws the hero down to the burning deck; his only way out is the water. Describe the jump to Claude AND how to transition in-camera straight from the ocean into the next scene — attach @location_desert and the desert character sheet @main_character_desert so the dust whiteout can swap both world and wardrobe.

Desert location reference
Main character desert wardrobe sheet

Two iterations finish the shot. First, the opening camera angle doesn't work — flip it to look toward the bow, with a worm's-eye first cut so the hero lands into frame from above. Then one last fix, from the video cue: add water splashes and make him look wet, because a ship under fire shouldn't have a dry deck. He falls hard, the limp reads real, and the wet deck makes the whole setting feel true.

Scene 1 — locked

Cut it all together. The 4K keeps the picture completely sharp instead of turning to mush, and the fall into the water looks straight-up cinematic. Three settings to go.

## 7. Scene 2: Desert Chase

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/scene-2-the-desert-chase
- 页面资源：Open image: Canvas with the desert-scene assets；Open image: The desert location asset；Open image: The ostrich riders asset sheet；Open image: The @oasis as its own location asset

New setting — the desert. This scene comes together in three parts. On the canvas we have everything Scene 2 needs: the desert location, the binoculars, and the ostrich riders.

Canvas with the desert-scene assets

The desert location asset

Part 1 — the scream

There is a lot happening in this beat — the hero's entrance from behind a dune, the "CINDYYYY!" scream, a dramatic ultra-wide pull-back, and the ostrich riders reacting — so drop all the assets into Claude and give it every detail at once. The ostriches are the comic relief, so their reaction has to be funny, and the riders shout in their own strange language:

Write a prompt for scene 2, part 1 — The hero @main_character_desert climbs out from behind a dune in @location_desert. The camera sits close to the top of the dune, so at first we don't see him. He coughs, a little sand spilling off him — keep it subtle. He looks around, sees nothing but dunes, and screams 'CINDYYYY!' On the scream, pull the camera away into a dramatic ultra-wide shot — one tiny guy alone in the middle of the desert. Make the ostriches' @ostrich reaction comedic — and the riders @rider shout something in their own strange language as they ride toward the sound.

The ostrich riders asset sheet

Paste the prompt and batch several. From one batch, take the ostrich reaction; from another, the riders taking off toward the hero. Both go to the edit.

The opening shot still feels a bit off, so ask Claude for the tweak from the video cue: give the camera a moment to breathe before the hero climbs out, and make the dust thicker so it takes longer to clear. That breathing room at the start is what sells the cut from the pirate scene — and the massive zoom-out just looks expensive.

Part 2 — spotting the case (pro tip: asset inside an asset)

Our story needed an oasis, but the desert location didn't have one. The fix: treat the oasis as its own separate location asset. Now the model knows the spot AND the landscape around it, so the oasis looks the same in every generation.

The @oasis as its own location asset

Drop the oasis image into Claude and ask for the beat:

Write a prompt for scene 2, part 2. He looks through the binoculars @binoculars toward the oasis @oasis and spots the device with the button @button. He lowers the binoculars and starts running toward the oasis. Cut: a static camera at ground level — a sandstorm is rolling in, and the riders @rider are chasing him.

First result: he runs the wrong way. Tell Claude what's wrong (the prompt is in the video cue): he must always run toward the oasis, the storm needs more scale, and when he looks back we should see the riders. Second result: the desert finally feels endless and the storm looks real — but the riders are right on top of him. Push them far behind so there's actually room for a chase, then run a few batches for options.

Then mix and match across the three batches: the wide shot of the storm rolling in for the moment he sees the case, the most natural binocular-lowering reaction from batch two, and the run with the storm right there in frame from batch three.

Part 3 — the chase

The whole chase goes in one prompt, with specific camera cuts written in:

Write a prompt for scene 2, part 3. He's running toward the device @button, already close to the oasis @oasis. The riders @rider are chasing him and the storm is closing in. 1 — medium shot, camera in front: main character @main_character_desert runs from the riders, a huge sandstorm behind him. Cut: reverse shot — we see the riders chasing him, the oasis nearby, the riders shouting phrases in their own language. Cut: the hero is in the oasis, jumping toward the device between the palms — and the sandstorm swallows the whole frame.

Good — but he shouldn't actually reach the case. Ask Claude for the story fix from the video cue: he jumps for it, falls just a little short, and the sandstorm swallows the frame at that exact moment. He almost makes it — and almost is what makes it hurt.

Since it's batched, choose again: the jump toward the device from one batch, the rear angle on the riders plus the run through the palms from another. Stitch it all together and watch the full scene.

## 8. Scene 3: Jungle

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/scene-3-the-jungle
- 页面资源：Open image: @main_character_jungle asset sheet；Open image: @machete asset sheet；Open image: @spider asset sheet；Open image: Character sheet re-attached for the chase；Open image: @mandrill monkey asset sheet；Open image: @location_jungle2 jungle path location；Open image: The white @macaque replacement sheet；Open image: @jaguar asset sheet；Open image: @location_jungle3 ridge and cliff location；Open image: Character sheet attached with the jaguar-scene assets；Open image: @main_character_jungle_torn — the torn-pants sheet

Here's the joke of Scene 3: the hero is afraid of monkeys, and his little sister drops him into a thick jungle full of them. She has a wicked sense of humor. Honest framing up front — this scene took the most batches and tries in the whole film: lots of jump cuts, and assets even got swapped mid-process. This lesson covers the 3 most important shots; the rest use the exact same logic — use the skills, describe the scene, drop in your assets.

Shot 1: Waking Up (POV)

The hero wakes up hanging upside down by his legs and sees a massive spider right in front of his face — shown through his eyes. Assets for this shot (all sheets are shared in the description):

@main_character_jungle asset sheet

@machete asset sheet

@spider asset sheet

The first request to Claude:

Write a prompt — the hero's POV, subjective camera. He's waking up in @location_jungle1: the hero @main_character_jungle hangs upside down, tied by his feet. The eye opens in frame and sees a spider right in front of it. Then the hero @main_character_jungle screams in fear and swats the spider @spider away with his hand. The camera IS the hero's eye — when the eye opens from defocus, the focus shifts onto the spider. He then draws his machete @machete and cuts the vine.

The first try failed completely: instead of making the camera act like his eye, the model pushed the spider inside the character's eyes. The fix is to simplify — drop the multi-shot and ask for one thing: "Give me just one continuous POV shot. The eye opens slowly like shutters, and we see the spider."

Better, but still not it — the camera zoomed out of the eye like a physical lens, and the spider sat mid-frame. The final round of fixes is in the video cue prompt: no eyelashes or skin, static camera, black eye-slit shutters that blink, spider fixed at one distance at the edge of the frame, and the location flipped upside down and blurred — because the hero is hanging upside down. Four batches later — nailed it: a real POV where the eyes struggle open, and the off-center spider makes the jump-scare feel natural.

Shot 2: The Chase

The hero trips, falls flat on his stomach, covers his head, and the monkeys flood over him while he screams: "Okay. Okay. Fine. I'm done! I'll do it! You win! Just make it stoooop!" This is a multi-shot, because the comedy is in the cuts.

Character sheet re-attached for the chase

@mandrill monkey asset sheet

@location_jungle2 jungle path location

The two-cut request:

Write me a prompt for a multishot, two cuts, on the path in @location_jungle2. Cut 1: the explorer @main_character_jungle runs, trips, and falls flat on his stomach, quickly covers his head with his hands and squeezes his eyes shut, expecting the monkeys @mandrill to attack. He screams and begs: 'Okay. Okay. Fine. I'm done! I'll do it! You win! Just make it stoooop!' The camera starts wide and pushes in to a close-up — we don't need to see his face, the important thing is we hear him. Cut 2: a medium top shot — he's lying there while the whole troop runs over him. Someone steps on him, some monkeys are up in the trees, and by the end not a single monkey is left. His screams run under all of it.

The mandrills rendered way too cartoonish — the bright noses made it look like an animated movie. The fix: swap @mandrill for a white @macaque, something simpler and more realistic. Changing assets mid-iteration is completely normal when you need to avoid a plastic look — keep a few asset variations ready for moments like this.

The white @macaque replacement sheet

The rewrite (see the video cue) also fixes timing and camera: the monkeys should already be flooding past during his monologue — otherwise it looks like he could escape but chooses to lie down; Cut 1 gets a crane-down on the fall, and Cut 2 becomes a side profile, because the flat top-down hides all the chaos. From the four new batches: the fall comes from batch 1, and the macaques running over him from batch 2.

Part 3: The Jaguar

The final part shows what to do when something on your character changes mid-story. One continuous take: the hero runs down the path, a jaguar swipe rips his pants — revealing red underwear with white hearts — he keeps running, grabs the button at the tree, and the jaguar shoves him off the cliff.

@jaguar asset sheet

@location_jungle3 ridge and cliff location

Character sheet attached with the jaguar-scene assets

Write a prompt for the guy @main_character_jungle runs along the path in @location_jungle3, and out of the grass a jaguar @jaguar attacks him — one swipe rips his pants, and we see red underwear with white hearts. The guy doesn't stop — he screams and keeps running toward the tree. The moment he reaches the tree and grabs the button @button, the jaguar catches up and shoves him into the chasm. Handheld camera: when the guy runs, it rises from his feet upward. No cuts.

The continuous camera move looked amazing — but classic AI glitch: the pants tear, then a second later magically stitch themselves back together.

The workaround: generate a mid-story character sheet — a brand-new sheet of the hero already wearing the torn pants (@main_character_jungle_torn). Feed the model this second sheet and it always knows what the torn state looks like.

@main_character_jungle_torn — the torn-pants sheet

The rewritten prompt (video cue) plugs in the new @main_character_jungle_torn asset immediately after the claw swipe. It also fixes the ending physics — the device stays in his hands as he falls, and the jaguar stays at the cliff edge, watching him go down instead of falling with him.

Four batches with the new setup, and the logic held together perfectly. The winning take goes straight into the final edit — watch the full jungle sequence at the end of the clip.

## 9. Scene 4: Twist and Dialogue Scenes

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/scene-4-the-twist-and-dialogue-scenes
- 页面资源：Open image: Living-room location asset used as @room1；Open image: Scene 4 asset sheet sent to Claude；Open image: Cindy character sheet — the sister behind the twist；Open image: @room2 — reverse angle of the same room, the fourth wall；Open image: @room3 — frontal angle of the desk wall

Time for the big twist. Our hero wasn't dropping into all these crazy worlds by accident — his little sister Cindy was intentionally sending him there. In this scene we finally see her and get a dialogue going. Dialogue scenes are incredibly important, and this lesson shows how to shoot a classic over-the-shoulder sequence that won't fall apart or glitch out.

Part 1: the couch landing and the reveal

According to the script, the main character drops out of nowhere and slams onto a living-room couch — matching his fall from the cliff, so the two shots stitch together. Then, behind him, a sly giggle. He turns around and finds his sister.

Send all the scene assets to Claude — the character sheets, the room location, the parrot — and describe the beat: the hero falls in from off-screen onto the couch in @room1, the parrot @parrot_sheet gets scared and squawks on landing, and over his disorientation comes Cindy's (@cindy) sly giggle from behind.

Living-room location asset used as @room1

Scene 4 asset sheet sent to Claude

Cindy character sheet — the sister behind the twist

Watch the first generations and you'll see the problem: Cindy's background changes from generation to generation. If the background shifts when you cut between characters, the scene will never piece together in the edit. The model simply needs more information about the room.

Pro tip: reverse-angle environment references

When making a dialogue scene with reverse angles, you must generate reverse-angle environment references of the same room. Feed the model images of what both sides of the room look like — that gives it a blueprint of the set, and the background stops jumping between cuts.

@room2 — reverse angle of the same room, the fourth wall

@room3 — frontal angle of the desk wall

Two smaller fixes go into the same rewrite: the green @button device kept changing size, so its exact dimensions get locked, and the parrot kept getting trapped inside its cage — it should sit on top. Use the rewrite request from the video cue: it adds @room2 and @room3 as extra references, pins the button at a fixed size, and puts the parrot back on the cage dome.

The result is night and day. Because the model has both sides of the room, the set stays completely consistent when we cut back and forth, the parrot is right where it needs to be, and the device holds the exact same size. This clip goes into the edit.

Part 2: the dialogue

Per the script, the hero and Cindy try to make a deal but can't agree, so Cindy sends him back — he clearly hasn't learned his lesson. The exchange: "Make it two months." He refuses. She shrugs — "Okay. You said you hate monkeys?" — and presses the button without looking. He dissolves into green light, screaming. Ask Claude for a shot-reverse-shot between the couch and the desk (the request is in the video cue).

The first generations fail in three ways: the camera randomly broke the axis and started zooming in on the hero, he didn't fully disappear, and Cindy's physical position shifted with every single cut.

Locking the 180-degree rule

The fix is to lock down the rules. Tell Claude to keep the camera completely static: Cindy from the exact same angle on every one of her lines, and the hero over her LEFT shoulder on every one of his — identical framing each time. That's the 180-degree rule: break it, and the audience stops knowing who's standing where. Two more notes go into the rewrite (see the video cue): "HELL NAHHH" should read as dismissive, annoyed disbelief — refusal with contempt, not volume — and the dissolve must finish completely.

Run a couple of batches. The first still drifts — acting is fine, but the camera doesn't lock and Cindy shifts between takes. Then one lands: rock-solid framing, spot-on acting, and it goes into the final edit almost completely intact.

And with that, Scene 4 is locked.

## 10. Full Film and Workflow Recap

- URL: https://higgsfield.ai/academy/courses/blockbuster-4k/full-film-and-workflow-recap

With Scene 4 locked, the film is done. This final chapter plays the whole thing back one more time — and now that you've built it shot by shot, you can watch it the way the presenter does: as a finished production, not a pile of generations.

Watch the full film again

The clip runs the complete film from start to finish. Watch it with fresh eyes — you now know exactly where every character sheet, location asset, and reverse angle is doing its job.

The big takeaway

We approached this like actual filmmakers. Nobody threw a random one-line prompt at the model and hoped for the best. We built a script first, then used the prompt-building framework to turn that script into highly detailed, working shots. That order — story first, prompts second — is the whole method.

The pro tips, in one place

The presenter calls out three techniques by name in this clip:

Single-face character sheets so the model always locks onto one identity.
Separate location assets for complex scenes — the oasis trick: generate the environment as its own asset instead of asking one prompt to invent everything at once.
Reverse-angle references to keep dialogue scenes consistent when the camera flips sides.

And from earlier chapters, the rest of the toolkit that got the film here:

The iteration loop: run it, look at it, ask for exact changes, run it again — treat the model like a crew member, not a slot machine.
Drawings as geometry instructions when words can't pin down a layout.
Mid-story character sheets whenever wardrobe changes.
The 180-degree rule so cuts between characters never feel disorienting.
Why 4K matters

Because it's all in 4K, it looks like money. You watched the explosions — nothing melted. Resolution is what keeps fast, detailed action reading as cinema instead of mush.

Everything is yours

The presenter learned a ton making this film, and all of it comes with the course: the full script, every single prompt, the asset sheets, and the prompt guide. You don't have to reverse-engineer anything — steal it directly.

Go make something

The best part: this exact workflow works for anything. Commercials, short films, or any random idea in your head — it's the exact same approach. Script, framework, assets, iterate. So steal these tools and go create something great.
