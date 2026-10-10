# 0006 shot list

The edit carries it. Every shot is simple, and the cutting, the speed, the type and the effects make it busy. Excitement first, story second, the lyric only where it helps. The story is in [`README.md`](README.md#story). Times come from [`captions/en.vtt`](captions/en.vtt) and the WAV. Technique numbers are the ones in [`README.md`](README.md#techniques).

The song runs about 192 BPM. One beat is about 0.31s, one bar about 1.25s, and one sung line is two bars, about 2.5s. Final Cut Pro's Beat Detection gives the exact frames.

Loud landmarks in the WAV:

- 1:32.1–1:44.4: the first instrumental, after chorus 1
- 2:30–2:32: a dip before the bridge
- 2:42.25: the densest stretch of the song starts here and runs 19s to the last chorus
- 3:03–3:09: the first half of the last chorus is pulled back, and the band comes back in at 3:10
- 3:36.25: the sound drops out for a moment. The last hit is at 3:37.0, and it's silent by 3:37.5

## Rules

- **Cut length.** Verses: a cut a bar, about 1.25s. Choruses and fights: a cut every one or two beats, 0.3–0.6s. Nothing holds longer than 2.5s except the freezes before a drop.
- **Every cut does something.** A speed ramp, a flash, a shake, an RGB split, a crop punch-in, a split screen, type or an overlay. One at least.
- **One clip, many cuts.** A clip is cut into three to five pieces and used in different places, cropped, flipped or at another speed. Generate simple shots.
- **One place per scene, used once.** The bridge is the only Japanese place, and the only scene in the old clothes apart from the tea stall. Everything else is the near-future city in modern clothes.
- **A costume per scene.** Each scene has its own costume plate, so a scene's cuts match. An extra that only one cut needs (a cap, an earpiece) goes in that cut's prompt. Everyone but the three leads is used once and thrown away. The hair never changes, except in the memories: with a new costume every scene, the hair is how the viewer tells the two apart.
- **The fight-game layer.** The VS screen, `ROUND 1` and `ROUND 2`, a boss health bar, arrow inputs and a combo counter, `K.O.` Built in Motion (M8).

## Who goes in each generation

- **Q3C:** Vidu Q3 Cinematic, 8s, one action per clip. Full body, wide shots, the fighting, the city
- **Q4:** Vidu Q4, 5s. Face and hand close-ups

References, in this upload order: each person's costume front, then their face (`singer-face.png`, `rival-face.png`, `master-face.png`), then blades or props, then one place. Seven at most, Q3's limit. A shot with three people has no room for the blades: name them in the prompt. Guns, bikes, the wooden swords, the flask and the photo have no plates: Vidu invents them. Each is on screen for a cut or two, so they don't have to match from shot to shot, and a plate for each would take a slot from a face.

The plates are listed in [`prompts.md`](prompts.md#files). Full-body shots stay in rain and city light, never on a bare stage. On an empty stage both models drew a 3D game render. The training room is the one place that look is wanted.

## Intro · 0:00–0:26 · the hook

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 1 | 0:00–0:06 | The singer's eye in the rain, cut on the beat against 1b and one-frame flashes of what's coming: the master's red eye (36b), a muzzle flash, crossed blades (22). Faster and faster into "(Ha!)" | Q4, made | G6, F1, F19 |
| 1b | 0:00–0:06 | The rival's eye under a hood, harbour lights behind | Q4, rival hood, harbour | G6 |
| 2 | 0:06 | "(Ha!)": white flash, the title slams in, the dive plays inside the letters | Edit | F4, M7, F14 |
| 3 | 0:08–0:17 | FPV dive down the towers into the city, following an agency drone. Lower third types out the place and the year | Q3C, rooftop | G5, F2, M1 |
| 4 | 0:17–0:26 | VS screen. The two front plates slide in, `AGENT` under one, `SMUGGLER` under the other, `VS` slams on the beat, then the back plates as each turns away | Edit, the plates | M8, M2 |

## Verse 1 · 0:26–0:46 · the case, and the message

The two are never in one place. The singer is at the agency at night, the rival at the tea stall at dawn, alone, and the edit cuts between them. She still sets out two cups and pours the singer's first. Two women in one frame with a small exchange came out robotic in every roll, so the talk at the stall became a message.

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 5 | 0:26–0:31 | "Morning steam above the stall": the stall wide (first half of 6-2), the singer at the agency with her back to us (5), the hologram in her sunglasses (5b) | Q3C 5, Q4 5b, made | F1, M1 |
| 6 | 0:31–0:36 | "Two cups waiting by the wall": two cups (6), the cups again (second half of 6-2), the rival's file on the agency screens, with a glowing green mochi turning, `CONTRABAND`, and the drone's feed from shot 3 | Q3C, made, plus edit | F24, M4 |
| 7 | 0:36–0:41 | "You pour mine before your own": the rival's hand pours the singer's cup first. Framed to match the flipped 17. Then her eyes on her tea (8b) | Q3C, rival, stall, plus 8b made | G1, first half |
| 8 | 0:41–0:46 | "Same as every day we've known": the message lands as a hologram over her cup, an old photo of the two apprentices and their master. She doesn't look at it. Split screen, the agency and the stall, then the singer turns to camera (the end of 5). Freeze, and her intro card builds | Edit, from 5, 8b and the plates | F9, M4, M3, F3 |

The photo is built in the edit from `singer-gi.png`, `rival-gi.png` and `master-front.png`, with grain and a film burn so it reads as old.

## Verse 2 · 0:46–0:56 · the deal

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 9 | 0:46–0:49 | "Petals stick": the harbour at night, the rival in a hood hands a case to two thugs | Q3C, rival hood, harbour | F21, M1 |
| 9b | 0:46–0:49 | The open case: rows of glowing green mochi, a flash on the cut | Q3C, case, harbour | F21 |
| 10 | 0:49–0:52 | "Whetstones": split screen, the singer on a crane watching through a scope, and the scope's view of the rival | Q3C, singer suit, harbour | F9, M4 |
| 11 | 0:52–0:54 | "Neither of us says the word": the rival's face over the harbour | Edit, 12 and 9 | F15 |
| 12 | 0:54–0:56 | "Both of us already heard": the rival turns and looks straight up at the scope. Freeze, and her intro card builds | Q4, rival hood, harbour | M3, F3, F25 out |

### Edit notes for 1–12

What the clips need on the timeline, worked out when they were picked. The step-by-step comes at the edit.

- **1 and 1b.** Alternate on the beat, faster towards "(Ha!)". Rain on the lens and the focus pull (Gaussian Blur, full to zero) on 1.
- **3.** The drone rises from the foot of the tower into frame: a flash or a type hit there. Speed up the dive back down (about 150%), and ease back to 100% as it levels out over the street.
- **5.** Ends facing the camera, centred. Freeze the last frame (`Option+F`) for about 1.5s to 0:46.6, and the intro card slides in from the left: her name big, `AGENT` under it, the last letter on the beat.
- **5b.** `5b-2.mp4` has bigger glasses than the plate. A one-frame flash at most.
- **6-2.** Vidu cut inside the clip, from the stall wide to the cups. Blade it at the change (`Cmd+B`): the first half is the wide, the second half a second angle on the cups.
- **7.** If it came out mirrored against 17, flip it (Effects → Distortion → Flipped). The cut to 17 lands on "Draw!", on the hand gripping the handle.
- **8.** No clip. The old photo is built from `singer-gi.png`, `rival-gi.png` and `master-front.png`, with grain and a film burn, and floats over the cup in 8b as a hologram.
- **9.** Use from 3s on; the case warps before that. `9-2.mp4` has her hood down, so the tufts say who it is: one bar after a hooded cut.
- **9b.** Only the last three seconds. Put a white flash on the first frame used, so the warp just before it doesn't show.
- **10.** The suit shines like rubber. Half size in the split screen, a grain overlay, lowered highlights. `10-2.mp4` is the wide on the crane, one bar before the split.
- **12.** `12-2.mp4` first (her face hidden in the hood), then `12.mp4` (she looks up, the eyes catch the light), jump cut on the beat. Freeze the last frame of 12 and her intro card builds. Check the eyes are amber, not red.

## Pre-chorus · 0:56–1:08 · the ambush on the bridge

The one slow stretch, and it stays slow: the stillness is what makes the drop hit.

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 13 | 0:56.01–0:58.56 | "One more bell": a red lantern on the bridge, swinging in the rain | Q3C, made | F21 |
| 14 | 0:58.56–1:01.14 | "One more breath": the singer breathes out, rain on her face | Q4, made | F24 |
| 15 | 1:01.14–1:06.86 | "Then the street goes still": waist up, she lifts her eyes. Slowed to a stop, the frame closes to 2.39:1 | Q3C, made | F2, F8 |
| 16 | 1:06.86–1:08.78 | Freeze on 15. Two health bars slide in and fill, `ROUND 1` | Edit | F3, M8 |

## Chorus 1 · 1:08.8–1:32 · the duel

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 17 | from 1:08.78, up to about 1s | "Draw!": match cut from the pouring hand of 7 to the hand on the hilt. Negative frames, white flash | Q3C, made | G1, F4, M2 |
| 18 | to 1:11.28 | "Steel in bloom" in big type behind the singer | Q3C, made | F12 |
| 19 | 1:11.28–1:13.70 | "Red against the rain": all grey except the red | Q3C, made | F11 |
| 20 | 1:13.70–1:18.75 | "Only one walks off… Only one goes home": eight cuts, not one wide. The wide, crops of each woman, flipped crops, i1 and i2, 1-frame tower cutaways, `ONLY` and `ONE` slamming in | Q3C, made, plus inserts | F1, M2, F5 |
| 21 | 1:18.75–1:21.16 | "Draw!": the rival draws. After the draw, i3: her grip tightens on the drawn blade, about 0.5s, into the charge | Q3C, made, plus i3 | F4, F2 |
| 22 | 1:21.16–1:23.67 | "Faster than the light": the charge, afterimage, flash on the hit, sparks. Already full, so no insert | Q3C, made | F4, F16, F20, F7 |
| 23 | 1:23.67–1:26.13 | "Smile at me": the lock, held. A crop of 22's crossed blades, the rival's face (i2-2), the singer's eyes (i1), a punch-in on the blades. No smile: she is still the smuggler here, and her smile is kept for the reveal in 34 | Edit, from 22, i1, i2-2 | F5, F24, F20 |
| 24 | 1:26.13–1:32.1 | "Then cut me down tonight": the backflip and the rising cut. Strobe on the hit, sparks, a crop punch-in on each speed change | Q3C, made | F2, F7, F18, F20, F21 |

Inserts for the chorus 1 re-edit, made:

| # | Shot | Gen |
| --- | --- | --- |
| i1 | The singer's eyes narrowing, rain, lanterns behind | Q4, singer, bridge |
| i2 | The rival's eyes narrowing | Q4, rival, bridge |
| i3 | Her hand tightening on the green-wrapped hilt of the drawn blade, extreme close-up | Q4, rival, her blade, bridge |

### Cutting 0:56–1:32

The rough cut, as placed on the timeline. The project runs at 23.976 fps, so Final Cut Pro shows times as minutes:seconds:frames, 24 frames to a second.

| # | Starts | Length | Seconds |
| --- | --- | --- | --- |
| 13 | 0:55:23 | 2:13 | 0:55.96–0:58.50 |
| 14 | 0:58:12 | 2:14 | 0:58.50–1:01.08 |
| 15 | 1:01:02 | 5:17 | 1:01.08–1:06.79 |
| 16, freeze | 1:06:19 | 1:22 | 1:06.79–1:08.71 |
| 17 | 1:08:17 | 1:00 | 1:08.71–1:09.71 |
| 18 | 1:09:17 | 1:12 | 1:09.71–1:11.21 |
| 19 | 1:11:05 | 2:10 | 1:11.21–1:13.63 |
| 20 | 1:13:15 | 5:01 | 1:13.63–1:18.67 |
| 21 | 1:18:16 | 2:10 | 1:18.67–1:21.08 |
| 22 | 1:21:02 | 2:12 | 1:21.08–1:23.58, the hit about a second before "light" |
| 23 | 1:23:14 | 2:11 | 1:23.58–1:26.04 |
| 24 | 1:26:01 | 6:00 | 1:26.04–1:32.04 |

Shot 15 is an 8s clip, trimmed and slowed to fit 5:17. Shot 16 is a freeze of its last frame. Every cut sits one to two frames before its caption starts. That is on purpose: the picture leads the voice slightly.

The times above are the caption starts in [`captions/en.vtt`](captions/en.vtt), which are the purple caption bars on the Final Cut Pro timeline. Each cut lands where a sung line starts, so it lands on the left edge of a purple bar. Where a bar and the ear disagree, trust the ear and move the cut. A frame or two early reads tighter than late.

- **13 · "One more bell".** Cut in on "One." The lantern swings like a bell being rung. It is the calm before the fight, so there is no fast movement.
- **14 · "One more breath".** Cut on "One." Her breath comes out on "breath." Slide the clip until the mist leaves her lips on that word.
- **15 · "Then the street goes still".** Cut on "Then." The line holds a long note, and the picture slows to a stop over it: 100%, then 50%, then 25%, into the freeze of 16. The black bars close in to 2.39:1 over the same note: Crop (Trim) on the clip itself, Top and Bottom 0 at 1:01:02 to 138 at 1:06:18, then 138 held on the freeze in 16. Final Cut Pro 12 has only a 360° solid, which crops wrongly in a 16:9 project. The crop shows whatever is under the clip, so the lyric title there is disabled.
- **16 · the gap.** The bar ends at 1:06.86 and there is no singing until "Draw!" Freeze on the last frame of 15 and let the music build under a still picture. The stillness is what makes the next cut hit.
- **17 · "Draw!".** The first frame lands exactly on "Draw!" The hand grips and a little steel shows. The two frames before the white flash are a negative (Color Curves, Luma curve flipped end to end; FCP has no Invert effect), and the flash then carries it into 18. The clip is flipped horizontally (Effects → Distortion → Flipped) so the rival faces screen left, as she does in 20 and 21. Shot 7, the pouring hand, is framed to match the flipped version.
- **18 · "Steel in bloom".** 17 and 18 share one caption, "Draw! Steel in bloom," about 2.5s, so the split between them is free. 17 can run a second. 18 only has to start before "bloom," because the big type behind her pops on that word. Three layers: 18 as is, the title `STEEL IN BLOOM` (Impact, white, at face and shoulder height, the full frame wide), and 18 again on top with a Magnetic Mask on her and the blade. `IN` hides behind her, and `STEEL` and `BLOOM` show over the lanterns. The title pops in on "bloom": Scale 140% to 100% over 3 frames, Opacity 0 to 100% over 2, then Scale drifts to 110% by the end. A red Glow on the text (Opacity 60%, Radius 20, Blur 8) ties it to the lanterns.
- **19 · "Red against the rain".** Cut on "Red." The colour isolation starts on the cut, everything grey but the red. One Color Board: a Color Mask on the red of her hair cord (Add), then a Shape Mask around her and the cord's sweep (Intersect, last), so the red lanterns and railing stay out. Outside the mask, Saturation Global −100%. Auto Mask mis-detected her, and a second Color Mask for the cord's dark underside also caught her hair, so neither is used. Masks combine top to bottom.
- **20 · "Only one walks off this bridge / Only one goes home again".** Cut on the first "Only." The shot runs under both lines, with no gap between them. The clip pushes in slowly by itself, and nothing is added. A zoom punch on top of a moving camera reads as a bad cut, so it was taken out.
- **21 · "Draw!".** Cut on the second "Draw!" Her right hand goes to the hilt and the draw starts on the word. The bit of steel showing in 17 is ignored. In 20 her blade is sheathed and her hand is off it, so 21 starts from there. The line goes on to "Steel in bloom" and the shot runs under all of it.
- **22 · "Faster than the light".** One clip, no cut inside it. It starts on "Faster" with the two running in; the clip's first second, an empty bridge, is cut. The blades hit about a second before "light." Moving the hit onto "light" would need that empty second back or a slowed run, so the hit stays where it falls. The afterimage covers the 8 frames before the hit, and the white flash starts on the hit frame. The lock runs on through "light" until "Smile."
- **23 · "Smile at me the way you do".** Cut on "Smile." The lock, four cuts of about 0.6s: a crop of 22's crossed blades with sparks, i2-2, i1, a punch-in on the blades, into 24. `23.mp4`, the rival's smile, is out: at this point she is the smuggler, and the smile belongs to the reveal in 34. The vignette moves to i2-2: Vignette (not Vignette Mask), Darken 0.65, Falloff 0.3, Size 1.03, Blur 0. Judge it with the viewer at Fit.
- **24 · "Then cut me down tonight".** Cut on "Then," during the short lock. The rising cut lands on the rival's block on "tonight," at 1:29:00 on the timeline. Putting it on "down" would need the run-up at 224%, which reads as fast-forward. With the hit on "tonight," everything before it plays at 160%. The clip already goes into slow motion after the blades cross, but at 100% it runs out at 1:31:02, so the rest is slowed further to 68% with Optical Flow to reach 1:32:01. The two swap sides during the attack, so from 25 on the singer is on the right and the rival on the left. Camera shake on that hit, the only shake in 13–24: Scale 104% on the whole clip, then Position keyframes over the 6 frames after the hit, X/Y 18/−12, −14/10, 10/−6, −6/4, 3/−2, 0/0. The picture ends at 1:32.1, where the instrumental starts.

The cutting above is the rough cut, and the effects on 15–24 stay. The re-edit cuts into it: 20 becomes eight cuts, and i1 and i2 go into 20 and i3 into 21.

## Instrumental · 1:32–1:44 · the chase

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 25a | 1:32–1:44 | The rival on a motorbike down the empty highway | Q3C, rival hood, highway | F2, F1 |
| 25b | | The singer on a bike behind her, firing a pistol one-handed | Q3C, singer suit, highway | F7, F20 |
| 25c | | The rival turns in the saddle and knocks a bullet away with her blade, sparks | Q3C, rival hood, her blade, highway | F2, F18 |

## Verse 3 · 1:44–2:06 · the master

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 26 | 1:44–1:49 | "Sleeves torn open, sandals gone": three manga panels. The singer's torn sleeve, her pistol on the wet road, a tail light vanishing | Q3C ×2 and a crop of 25a, highway | F10 |
| 27 | 1:49–1:54 | "Lanterns swinging, steel on stone": memory. The two as apprentices with wooden swords in the white training room, laughing, the master watching. Their hair is the old hair: the singer's long and loose, the rival's in two low pigtails. 4:3, grain, film burn | Q3C, both in training clothes, master, training room | F8, F20 |
| 28 | 1:54–1:59 | "Every step we ever trained": the master shows a stance, the two copy her. Her eye flashes red for one frame | Q3C, the same | F2, F11 |
| 29 | 1:59–2:06 | "Every scar we never named": now. The singer alone at the agency at night, the rival alone on a rooftop looking at a photo of the three of them. Cut faster and faster | Q4 ×2 | F24, F1 |

## Chorus 2 · 2:06–2:30 · the raid

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 30 | 2:06.5 | `ROUND 2`, then "Draw!": the warehouse doors blow in, the singer in tactical gear comes through gun first, and her body wipes to the next shot | Q3C, singer tactical, warehouse | M8, F13, F4 |
| 31 | 2:09–2:11 | "Red against the rain": red alarm lights over stacks of glowing crates, muzzle flashes | Q3C, singer tactical, warehouse | F11, F20 |
| 32 | 2:11–2:16 | "Only one walks off": the two face to face between the crates, her gun at the rival, the rival's blade at her | Q3C, both, warehouse | F5, F2 |
| 33 | 2:16–2:21 | "Draw!", "Faster than the light": the rival swings at her and cuts down the thug behind her. Trails | Q3C, both, warehouse | F16, F7 |
| 34 | 2:21–2:24 | "Smile at me": the rival smiles and flips open a badge. On the VS card, `SMUGGLER` is struck out and `UNDERCOVER` slams in | Q4, rival hood, warehouse | F24, M8, M2 |
| 35 | 2:24–2:30 | "Then cut me down tonight": back to back, the two of them cut and shoot their way through the thugs, crash zoom on the last | Q3C, both, warehouse | F6, F7, F21 |

## Bridge · 2:30–2:42 · the boss

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 36 | 2:30–2:32 | The dip: on the rooftop, the master steps out of the dark. The koi hologram behind her turns from cyan to red. A boss health bar fills the top of the frame | Q3C, master, rooftop | G7, M8 |
| 36b | 2:30–2:32 | Her eyes glow red, a dark red aura rises off her | Q4, master, rooftop | F21 |
| 37 | 2:32–2:35 | "Left, right, low, high": four strikes, one a word, on twos. The two block. Arrow inputs on screen | Q3C ×2, all three, rooftop | F17, M4, M8 |
| 38 | 2:35–2:37 | "Blade on blade": the clash, sparks | Q3C, all three, rooftop | F7, F21 |
| 39 | 2:36.6 | "(Ha!)": she throws a wave of red energy and both are thrown back. White flash, negative frame | Q3C, master, rooftop | F4 |
| 40 | 2:37–2:39 | "Left, right, low, high" again, faster | From 37 | F17, M4 |
| 41 | 2:39.7–2:42 | "Draw it like you mean it": the two get up side by side, blade and gun raised. Crash zoom | Q3C, both, rooftop | F6 |

## Break · 2:42–3:01 · two against one

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 42 | 2:42.25–2:59 | The team-up at full speed: she shoots while the rival cuts in, a combo counter climbing, strobe on the hardest hits, one fake take through the joins | Q3C ×4, all three, rooftop | G8, F18, F20, M8 |
| 43 | 2:59–3:01.6 | RGB split builds, then one frame of black | Edit | F19, F26 |

## Last chorus · 3:01.6–3:26.7 · K.O., and tea

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 44 | 3:01.6 | "Draw!": the type tears and re-forms | Edit, over 45 | M5, F4 |
| 45 | 3:01.6–3:06.7 | "Petals in the rain": both leap at her together, slowed almost to a stop, petals overlaid | Q3C, all three, rooftop | F2, F20 |
| 46 | 3:06.7–3:09 | "Both of us still…": two slashes cross through her | Q3C, all three, rooftop | F21, F4 |
| 47 | 3:09–3:11.6 | "Both of us the same": the band is back. She falls, a glowing outline traces the two, `K.O.` | Edit, over 46 | M6, M8 |
| 48 | 3:11.6–3:16.6 | "Breathing in the light": dawn on the roof, the two faces | Q4 ×2, rooftop dawn | F24 |
| 49 | 3:16.6–3:19 | "Pour me tea tomorrow": a hand sheathing a blade cuts to a hand pouring tea, same framing | Q3C ×2, rooftop dawn | G1, reversed |
| 50 | 3:19–3:26.7 | "We'll draw again at night": both on the roof edge with tea and the confiscated case, eating the evidence | Q3C, both, case, rooftop dawn | F23 |

## Outro · 3:26.7–3:38 · the last hit

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 51 | 3:26.7–3:36.25 | The dive of shot 3 in reverse, up from the two of them into the dawn sky. End card | Q3C, both, rooftop dawn | M7, G5 |
| 52 | 3:36.25 | The sound drops out: black | Edit | |
| 53 | 3:37.0 | The last hit: `CONFISCATED` stamps down on one mochi, then the title | Edit, a frame of 50 | F4, M2 |

## What gets generated

Outside 1 and 13–24, the shot list needs 35 Q3C clips and 13 Q4 clips, the made ones included. Made so far: 1b, 3, 5b, 6, 6-2, 8b, 9, 9b, 10 and 12.

## Order

1. Midjourney: the master, the costumes, the case and the places, in that order
2. Shots 1–12 and the inserts i1–i3. Done. Next: the chorus 1 re-edit, to test the busy cut before the second half is generated
3. The second half in song order, shots 25–53

Everywhere: F1 beat cuts, F23 one grade over the whole song, F24 on every close-up, F26 at each section change.
