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
- **Every cut does something.** A speed ramp, a flash, a shake, an RGB split, a crop punch-in, a split screen, type or an overlay. One at least, unless the cut is a plain wide left bare as a breath after a busy run, like 20h. An effect the viewer can't read is left out, not added to fill the rule.
- **No filler.** A clip is never swapped or inserted only to fill time. A second clip breaks what the first set up: the drone vanishes, the city changes. Stretch the clip that is there with a speed ramp or a freeze, or move the next shot.
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
| 1 | 0:00–0:06 | The singer's eye in the rain, cut on the beat against 1b, faster bar by bar into "(Ha!)". Two 4-frame glimpses of what's coming: blades and sparks (1d), then the master's red eye (36b; 1c until it's made). White flash into 2 | Q4, made, plus 1c, 1d | G6, F1, F19 |
| 1b | 0:00–0:06 | The rival's eye under a hood, harbour lights behind | Q4, rival hood, harbour | G6 |
| 2 | 0:05:23–0:08:11 | "(Ha!)": after the white flash, `STEEL IN BLOOM` slams in and the dive (3) plays inside the letters, black around them. The drone rises inside the letters at about 0:07, so the eye looks for what is moving; then the camera flies into the letters and the drone is in the middle of the frame at 0:08:11 | Edit | F4, M7, F14 |
| 3 | 0:08:11–0:13:16 | The FPV dive, following the agency drone: it hangs in the middle of the frame as the letters cut away, the camera tips over and dives, then races down the neon street. A drone HUD in the top right counts the altitude down through the dive and holds about 5m on the street. From 0:10:00 a lower third types `NEO-EDO` / `SHOGUNATE YEAR 2083`. Ends on the accent at 0:13:16 | Q3C, rooftop, made | G5, M1 |
| 4 | 0:13:16–0:26:11 | Character select, then the VS screen, from the plates. The singer gets `P1`, the rival `P2`; the cursor on a black `???` (the master) is thrown off by red noise, `LOCKED`, and the screen snaps in on her card. Then the fronts slide in, `AGENT` and `SMUGGLER`, `VS` slams on the loudest bar, and star ratings fill row by row; the rival's `ZUNDA` runs past five stars off the screen. The screen snaps in on it, switches off like a CRT, and `MISSION START` types out into verse 1 | Edit, the plates | M8, M2, F19 |

## Verse 1 · 0:26–0:46 · the case, and the message

The two are never in one place. The singer is at the agency at night, the rival at the tea stall at dawn, alone, and the edit cuts between them. She still sets out two cups and pours the singer's first. Two women in one frame with a small exchange came out robotic in every roll, so the talk at the stall became a message.

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 5 | 0:26–0:31 | "Morning steam above the stall": the stall wide running into the steaming cups (6-2), the singer at the agency with her back to us (5), the hologram in her sunglasses (5b) | Q3C 5, Q4 5b, made | F1, M1 |
| 6 | 0:31–0:36 | "Two cups waiting by the wall": two cups in the rain (6), the rival's file on the agency screens, with a glowing green mochi turning, `CONTRABAND`, and the drone's feed from shot 3 | Q3C, made, plus edit | F24, M4 |
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

### Cutting 0:26–0:56

The rough cut, as placed. Line starts are the caption starts less one frame; cuts inside a line sit on bars, to be checked by ear. The build work (6's screens, 8's photo, split screens, 11's face, the intro cards) comes on top of these.

| Time | Clip |
| --- | --- |
| 26:11–29:22 | 6-2 from its start: the stall, then steaming cups |
| 29:22–31:01 | 5 from its start, her back to us |
| 31:01–31:08 | 5b, one beat |
| 31:08–33:16 | 6, two cups in the rain |
| 33:16–35:19 | Placeholder: the rival's file on the agency screens |
| 35:19–38:16 | 7, the pour |
| 38:16–43:16 | 8b, the whole clip; the photo hologram goes over it |
| 43:16–45:00 | The end of 5, the turn |
| 45:00–46:12 | Freeze on 5's last frame, for the intro card |
| 46:12–47:10 | 9 from 3s |
| 47:10–48:22 | 9b from 5s, a 2-frame white flash on its first frame |
| 48:22–51:14 | 10 from its start; the split screen from 49:22 |
| 51:14–53:19 | 9 from 4s, the harbour under 11's face |
| 53:19–54:07 | 12-2, eyes down |
| 54:07–55:00 | 12 from about 1.5s, the eyes rising |
| 55:00–55:23 | Freeze, eyes up, for the intro card. 23 frames is short for a card; where the time comes from is decided with the card |


### Edit notes for 1–12

What the clips need on the timeline, worked out when they were picked. The step-by-step comes at the edit.

- **1 and 1b.** The beat grid, counted back from "(Ha!)" at 0:05:23: 0:23, 1:07, 1:14, 1:22, 2:05, 2:13, 2:20, 3:04, 3:11, 3:19, 4:02, 4:10, 4:17, 5:01, 5:08, 5:16. 1 is the base, retimed to 5:23 (`Cmd+R`, Custom, duration), with Gaussian Blur 50 to 0 over 0:00–0:16: her eye snaps sharp on the beat at 0:16 and holds sharp for 7 frames before 1b, and every later cut of 1 is sharp. 1b has none. 1b sits above from 0:23, bladed and with the pieces in 1's slots deleted:

    | Bar | Time | Cuts |
    | --- | --- | --- |
    | Open | 0:00–0:23 | 1, out of the blur |
    | 1 | 0:23–2:05 | 1b, 1, two beats each |
    | 2 | 2:05–3:11 | 1b, 1, two beats each |
    | 3 | 3:11–4:17 | 1b, 1, 1b, 1, a beat each |
    | 4 | 4:17–5:23 | Half beats: 1b, 1d, 1, 1b, 1c, 1, 1b, then the white flash from 17 at 5:19 |

    A one-frame glimpse didn't read, so these are four. Two glimpses of the same moment at different zooms read as one, so 1c and 1d are different moments.
- **2.** Two copies of the 18 title (the pop comes with them), X 5.72, Y lowered by eye to centre, Glow off, two bars long (`Control+D`, `212`), sized so `S` and `M` sit inside the Action Safe line: on black the title is the whole picture and needs a margin. The lower copy is Blend Mode Stencil Alpha, so 3 shows only inside the letters. The upper one is Normal, Face off, a white Outline of 3–4, so the letters read where the buildings inside them are dark. One bar was too short to read. Transform Scale on both: 140% at 5:23 and 100% three frames later (the pop), 105% at 7:23, 2000% at 8:10, so the letters creep in and then the camera flies through them. The zoom centre is the `I` of `IN`: centred on a gap between letters, the black grows instead. The lower copy is keyed and the upper one gets it by Paste Attributes, Transform only.
- **3.** At 100% the whole way, no ramp and no second roll: a second dive roll would drop the drone and change the city. Its end is trimmed to 0:13:16, a bar with an accent by ear. Lower third: FCP's Typewriter title, 0:10:00–0:13:16 (`Control+D`, `316`), Menlo 72, white, left-aligned, X −860, Y −400, Drop Shadow 60% / Blur 3 / Distance 3, no outline, Duration 60 so it finishes typing with time to read. `YEAR` over `ERA`: no real calendar counts years that way, which is the point, and Japanese viewers know the word. HUD, top right, inside Action Safe: two Counting generators (Menlo, Monospace, Minimum Digits 3, Thousands Separator off, sized with Transform Scale, smaller than the lower third), 412 to 5 over 8:11–10:00, then Random 4–6 with Random Hold Frame 48 over 10:00–13:16, since a drone holds its height. A Basic Title `ALT (m)` above them over 8:11–13:16, about half their height, right edges lined up; the unit is on its own line so it doesn't shift when the digits change. All text on this project sits inside the Action Safe line; Title Safe is a TV rule and crowds it on a phone. A full-bleed word behind a subject, as in 18, can run to the edge.
- **4.** Bars by ear from 0:13:16, 30 frames each: 13:16 select screen and `P1`, 14:22 `P2`, 16:04 `???` rejected and `LOCKED`, 17:10 push-in on the master's card, 18:16 singer and `AGENT`, 19:22 rival and `SMUGGLER`, 21:04 `VS`, 22:02 stat panels, 22:10 / 22:17 / 23:01 the three rows, 23:16 push-in on the rival's stats, 24:00 the overflow, 25:00–25:05 CRT off, 25:05–26:11 `MISSION START`. The music is loudest over 21:04–23:16 and drops a level at 23:16, where the push-in lands. The bar grid counted from the WAV ran 5 frames early against the ear here (it gave 10:23 and 13:11 for 11:04 and 13:16), so every time is checked by ear. Every event holds about a second or more, except the three star rows, which build a beat apart. The leftover bars after the stats were first given to a dialogue and to the two backs; both were filler, and the time went to the holds instead.

    The select screen, 13:16–18:16, as built. A Custom generator (not the 360° one) at RGB 4/5/11 on the 0–100 scale runs under all of shot 4 and is never in a compound clip. The three face plates are cards: Crop Bottom 360 so they show chest up, Scale 70%, X −554 / 0 / +554, Y −110, the same on all three so the edges line up; the eyes are left unaligned, since moving one plate moves its card. The master's card is Color Board Saturation −100%, Exposure −70%, a figure you can't name, with a red Impact `???` over it. `SELECT YOUR FIGHTER`, Impact 90, Y +330. Simple Border 12 marks a pick, in the colours of 20: purple on the singer from 13:16 with a purple `P1` under her card (Y −420), green on the rival from 14:22 (bladed there) with a green `P2`. At 16:04 the master's card is bladed for 8 frames: Exposure −10%, Tint red, a red Simple Border, Bad TV, and Position X shaking 554/574/534/564/554 every 2 frames, so her face shows red for an instant. Then a red `LOCKED` under it to 18:16. Everything but the base is one compound clip, Transform 100% at 17:10 to 160%, Position −576/+300, at 17:12: a snap on the bar, then held, with her card and `LOCKED` large on the right. Ken Burns would push in slowly over the bar instead.

    The VS screen, 18:16–25:05, as built, all of it one compound clip over the base. Two Custom generators split the frame: dark purple `#1F0829` with Crop Right 960, dark green with Crop Left 960. The front plates cut out with Magnetic Mask (re-analysed to the end after lengthening: the mask only covers analysed frames), Scale 95%, slide in over 6 frames: the singer from X −1500 to −480 at 18:16, the rival from +1500 to +480 at 19:22. `AGENT` in light purple `#CC73FF` (the plate purple sank into its half) and `SMUGGLER` in green, Impact 120, Y −420, with a drop shadow (60%, Blur 8, Distance 0), in as each fighter lands. `VS`: the 18 title copied, Size 400, on a lane above the stat panels, the pop's first keyframe raised to 300%, a 2-frame white flash at 21:04, and a Transform Position shake from 21:06: 0/0, then one per frame 18/−12, −14/10, 10/−6, −6/4, 3/−2, 0/0.

    Stats, from 22:02. Fighting games show stats on the select screen; here they go on the VS screen, since the select screen already carries the master. Black Custom panels at 60%, Crop singer Left 200 / Right 1180, rival Left 1210 / Right 170, both Top 620 / Bottom 240, clear of the `S` of the shaking `VS`. Labels `SPEED` / `POWER` / `ZUNDA` in one title per side, DIN Condensed Bold 56, Tracking 8%, Line Spacing 20, `#CCCCCC`, left-aligned, X −730 / +280. Stars one title per row, Hiragino Sans W6 48, Tracking 5%, left-aligned, X −500 / +510, Y −125 / −193 / −261, purple and green; an outline ☆ reads as empty, so one colour per row. Singer ★★★★☆ / ★★★★★ / ☆☆☆☆☆, rival ★★★★★ / ★★★★☆ / ★★★★★: she is stronger, the rival faster, and the singer's `ZUNDA` is empty. Letter grades were tried first and left the panel half empty. Panels and labels pop in at 22:02, the rows at 22:10, 22:17 and 23:01, each with the 18 pop cut down to its arrival: the pop's slow push after landing scales a title around the frame centre, so a row off-centre drifts away from its label. At 24:00 the rival's `ZUNDA` row is bladed and the rest is nine stars, Glow `#7CFF3A` radius 20, the `VS` shake, and a 2-frame green flash (a Custom generator `#7CFF3A` at 50%, kept outside the compound so the zoom doesn't move it). Fourteen stars were planned; nine already run off the edge.

    The camera on the compound: 100% at 23:16, 150% at Position −480/+270 at 23:18 (the rival's panel and `SMUGGLER`, no black at the edges), held to 25:00. CRT off: Scale X/Y 150/150 at 25:00, 150/3 with Position 0/0 at 25:02, 0/3 at 25:04 (the clip's last frame), so it collapses to a line and then a point in the middle; Color Board Exposure 0% at 25:01 and +60% at 25:02 for the flare. `MISSION START`: the `NEO-EDO` Typewriter title, 25:05–26:11, Menlo 100, centred, typed out in about 10 frames, on the base.
- **5.** Ends facing the camera, centred. Freeze the last frame (`Option+F`) for about 1.5s to 0:46.6, and the intro card slides in from the left: her name big, `AGENT` under it, the last letter on the beat.
- **5b.** `5b-2.mp4` has bigger glasses than the plate. One beat at most: a single frame doesn't read. Dropped if the glasses show.
- **6-2.** Vidu cut inside the clip, from the stall wide (under a second) to steaming cups. Used whole from its start: the steam is the first line. 6's cups have no steam and a different angle, and the agency sits between them.
- **7.** If it came out mirrored against 17, flip it (Effects → Distortion → Flipped). The cut to 17 lands on "Draw!", on the hand gripping the handle.
- **8.** No clip. The old photo is built from `singer-gi.png`, `rival-gi.png` and `master-front.png`, with grain and a film burn, and floats over the cup in 8b as a hologram.
- **9.** Use from 3s on; the case warps before that. `9-2.mp4` has her hood down, so the tufts say who it is: one bar after a hooded cut.
- **9b.** Only the last three seconds. Put a white flash on the first frame used, so the warp just before it doesn't show.
- **10.** The suit shines like rubber. Half size in the split screen, a grain overlay, lowered highlights. One piece from its start: the camera zooms the whole clip, so a cut inside it adds nothing. `10-2.mp4` is not used: she faces the other way, and the cut would flip the screen direction.
- **12.** Two takes of one action at two distances. `12-2.mp4` only while her eyes are down (it has them up by 2s), then cut in to `12.mp4` as the eyes start to rise (about 1.5s in). Freeze where the eyes are fully up (about 2.5s in), not on the last frame, and her intro card builds. The eyes are amber.

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
| 20 | 1:13.70–1:18.75 | "Only one walks off… Only one goes home": eight cuts of two beats. The first line is the stare-down, the second builds to the rival's draw: the wide, the singer, i1, the rival, the wide, i2, her eyes and the green hilt, the wide. `ONLY` and `ONE` land on each sung word, purple on the first line for the singer, green on the second for the rival | Q3C, made, plus inserts | F1, M2, F5, F11 |
| 21 | 1:18.75–1:21.16 | "Draw!": the rival draws fast and swings, straight into the charge. No insert: a quiet grip breaks its speed | Q3C, made | F4, F2 |
| 22 | 1:21.16–1:23.67 | "Faster than the light": the charge, afterimage, flash on the hit, sparks. Already full, so no insert | Q3C, made | F4, F16, F20, F7 |
| 23 | 1:23.67–1:26.13 | "Smile at me": the lock, held. A crop of 22's lock, the rival's face (i2-2), the singer's eyes (i1), then tight on the point where the blades meet. No smile: she is still the smuggler here, and her smile is kept for the reveal in 34 | Edit, from 22, i2-2, i1 | F5, F24, F20 |
| 24 | 1:26.13–1:32.1 | "Then cut me down tonight": the backflip and the rising cut. Strobe on the hit, sparks, a crop punch-in on each speed change | Q3C, made | F2, F7, F18, F20, F21 |

Inserts for the chorus 1 re-edit, made:

| # | Shot | Gen |
| --- | --- | --- |
| i1 | The singer's eyes narrowing, rain, lanterns behind | Q4, singer, bridge |
| i2 | The rival's eyes narrowing | Q4, rival, bridge |
| i3 | Her hand tightening on the green-wrapped hilt of the drawn blade, extreme close-up. Not used: her arm hangs and the blade points down, a standoff pose, and the bridge scene has no standoff with her blade out. 21 is a fast draw, 23 a lock | Q4, rival, her blade, bridge |

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
- **19 · "Red against the rain".** Cut on "Red." The colour isolation starts on the cut, everything grey but the red. One Color Board: a Color Mask on the red of her hair cord (Add), then a Shape Mask around her and the cord's sweep (Intersect, last), so the red lanterns and railing stay out. Outside the mask, Saturation Global −100%. Inside, Saturation +40% and Exposure +10–15%, so the red glows to match the green of 20g. Auto Mask mis-detected her, and a second Color Mask for the cord's dark underside also caught her hair, so neither is used. Masks combine top to bottom.
- **20 · "Only one walks off this bridge / Only one goes home again".** Cut on the first "Only." Eight cuts of 15 frames, bladed at 1:14:06, 1:14:21, 1:15:12, 1:16:04 (the second "Only", by ear), 1:16:19, 1:17:10 and 1:18:01. All but c and f are pieces of `20-2.mp4`, the singer on the left and the rival on the right.

    | Cut | Picture | On it |
    | --- | --- | --- |
    | a | The wide | `ONLY` |
    | b | The singer, left third, looking down-right | Scale 250%, X 1000, Y −600. `ONE` |
    | c | i1, the singer's eyes as she glares from under her brow | Connected over the third piece of 20-2 |
    | d | The rival, right third, eyes a step lower than the singer's, looking up-left | Scale 250%, X −800, Y −600 |
    | e | The wide | `ONLY` |
    | f | i2, the rival's glare, between the big raindrops | Connected over the sixth piece. `ONE` |
    | g | The rival, eyes cut at the top, the green hilt across her coat | Scale 300%, X −1200, Y −300. Color Board: Color Mask on the hilt's green only (its black dots left out) and a keyframed Shape Mask (Intersect) following it. Outside, Saturation −100%. Inside, Saturation +60%, Exposure +15% |
    | h | The wide, into 21 | Nothing. After seven busy cuts, the plain wide is the breath before the draw |

    The four titles are the 18 title copied with `Option+V`, so the pop comes with them, at Position X 0. They follow the voice, not the cuts: `ONLY` starts on "Only", and `ONE` on "one" about 8 frames later and runs to the end of the next cut. Shortening a title's tail keeps the pop; trimming its head cuts it, so a title is moved with `+` and a frame count. White fill, with the outline and glow picked with the eyedropper from the hilts: the singer's purple on the first line, the rival's green on the second. The fill stays white to read against the night. One `ONE` on the second "Only" read as a mistake; two of each matches the lyric.

    Sharpen 5 on b, d and g. It doesn't fix the softness of a 250–300% crop, but it doesn't make it worse, and the cuts are 15 frames. The crops aren't flipped: flipping swaps who is on which side. The clip pushes in by itself, so there is no zoom punch on top.
- **21 · "Draw!".** Cut on the second "Draw!" Her right hand goes to the hilt and the draw starts on the word. The bit of steel showing in 17 is ignored. In 20 her blade is sheathed and her hand is off it, so 21 starts from there. The line goes on to "Steel in bloom" and the shot runs under all of it.
- **22 · "Faster than the light".** One clip, no cut inside it. It starts on "Faster" with the two running in; the clip's first second, an empty bridge, is cut. The blades hit about a second before "light." Moving the hit onto "light" would need that empty second back or a slowed run, so the hit stays where it falls. The afterimage covers the 8 frames before the hit, and the white flash starts on the hit frame. The lock runs on through "light" until "Smile."
- **23 · "Smile at me the way you do".** Cut on "Smile." 22 runs on under it, bladed at 1:23:14, 1:24:05, 1:24:20 and 1:25:11, and the old `23.mp4` above it is disabled. Four cuts: 22's lock with a Ken Burns from the full frame to about 80% on the crossed blades (15 frames, the tips may touch the top), i2-2 (15), i1, a part after the glare used in 20c (15), then 250–300% on the point where the blades meet and spark, Sharpen 5 (14), into 24, where the singer breaks the lock. Wide first and tight last, so the lock closes in. The fourth cut stays a crop of 22 despite the softness: 22's lock runs straight on into 24, and a sharper close-up from another roll would break it. `23.mp4`, the rival's smile, is out: at this point she is the smuggler, and the smile belongs to the reveal in 34. The vignette moves to i2-2 with Paste Attributes (`Shift+Cmd+V`), unchanged: the inner ellipse holds both eyes and the hair and mouth go dark: Vignette (not Vignette Mask), Darken 0.65, Falloff 0.3, Size 1.03, Blur 0. Judge it with the viewer at Fit.
- **24 · "Then cut me down tonight".** Cut on "Then," during the short lock. The current `24.mp4` lands its hit on "tonight" by placement alone and carries one effect, the shake. It is to be replaced from 24b–24d, which all start locked so 22 and 23 run into it. On the new clip:

    1. **Place it.** Its head at 1:26:01, on "Then." The blades meeting on "tonight," about 1:29:00: trim the head of the lock to bring the hit forward. Change the speed only if trimming can't get it there.
    2. **Shake on the hit.** Scale 104% on the whole clip, so the moves never show an edge. Position keyframes over the 6 frames from the hit: X/Y 18/−12, −14/10, 10/−6, −6/4, 3/−2, 0/0. The only shake in 13–24.
    3. **Strobe on the hit.** Three one-frame white flashes, a frame apart, from the hit: copy the white flash from 17 and trim each copy to one frame.
    4. **Sparks.** If Vidu's sparks are faint, a Bloom effect over the 6 frames from the hit, keyframed up and back down.
    5. **Punch-in on the slow motion.** Vidu slows the clip by itself after the blades cross. Blade the clip where it slows, and set the second piece to Scale 115%, so the change of speed lands as a cut.
    6. **End at 1:32:01,** where the instrumental starts. If the clip runs short, stretch its slow part. Nothing else goes in to fill it.
    7. **Hit stop.** Hold the hit frame for 4 frames, the freeze fighting games use to make a blow land (Retime → Hold, `Shift+H`). It pushes everything after it 4 frames later, so trim the clip's end back to 1:32:01 straight after. The strobe and the shake start when the picture moves again.
    8. **RGB split on the strobe.** The Prism effect (Blur category) on the three strobe frames only, so the colour tears apart on the hit.
    9. **The rival's health bar drops.** The two health bars from 16 flash back in on the hit, and the rival's loses a big chunk. It pays off the bars from 16 and says who won the first exchange. Build it with 16's bars, which aren't made yet.

    Who ends on which side doesn't matter: the second half isn't generated yet.

The cutting above is the rough cut, and the effects on 15–24 stay. The re-edit cuts into it: 20 becomes eight cuts with i1 and i2, and 23 is rebuilt from 22, i2-2 and i1.

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
