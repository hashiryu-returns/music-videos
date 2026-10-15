# 0006 shot list

The generation carries the motion and the edit carries the rhythm. Every clip moves on its own, the camera or the body, and the cutting, the speed, the type and the effects build on that: a still picture cut faster reads busy, not dynamic. Excitement first, story second, the lyric only where it helps. The story is in [`README.md`](README.md#story). Times come from [`captions/en.vtt`](captions/en.vtt) and the WAV. Technique numbers are the ones in [`README.md`](README.md#techniques).

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
- **No two cuts in a row from the same camera.** Each sung line changes the angle (straight down, at deck level, side-on, a point of view, a close detail) or the way the frame is shown (split, panels, a cut-in, a colour change). Every prompt names its camera and how it moves: circling, tracking, tilting, pulling back, whipping after the action. A still camera is chosen for one cut, never the default. Chorus 1 was first nine cuts of one picture, eye level down the deck with the lanterns running away on both sides, and cutting faster didn't hide it.
- **Two women share a frame when they touch.** Before the first clash the two are never in one frame: two women apart in one frame is where the models broke (15b, 20-1). Once they clash, locked or trading blows, they share it, as the fights in the reference MVs do, and the camera moves around them. The run-ins are each woman's own move, cut against the other's. The fighting-game layer goes on the hits: a super-move cut-in (a black frame with a slanted band and her eyes in it), a 2–3 frame black-and-white impact frame, a hit stop, the health bars.
- **What the first half sets up, the second half pays back.** The CRT that switched off comes back on for the reveal, the `LOCKED` card opens for the master, the singer's empty `ZUNDA` fills at the end.
- **One clip, many cuts.** A clip is cut into three to five pieces and used in different places, cropped, flipped or at another speed. Never the same picture twice within a few seconds: the second cut reads as a rewind. Generate one action and one camera move a clip.
- **A close-up has to do something.** Type over it (18), a move (the camera pushing, the face changing), or one beat as punctuation between two moves (22c, 22d). A held face with none of these is a stop. The song already opens on alternating eyes, so eyes alternating again is a repeat.
- **A roll is judged on the frames that go on screen.** A shot that is 8 frames long needs 8 good frames, not a good 8 seconds.
- **One place per scene, used once.** The bridge is the only Japanese place in the present, and the only scene in the old clothes apart from the tea stall. The memories are in an old dojo. Everything else is the near-future city in modern clothes.
- **A costume per scene, dressed for what she does in it.** Each scene has its own costume plate, so a scene's cuts match, and the clothes fit the action: the suit and sunglasses at the agency and on the crane, riding gear on the bike, tactical gear for the raid. A plate is not carried into a scene it doesn't fit to save a roll. The second half wears nothing from the first: new plates from the chase on (`singer-ride-helmet.png`, `rival-ride.png`, `singer-tactical.png`, `rival-raid.png`, `master-boss.png`), except the memories. The bikes are plates too (`bike-rival.png`, `bike-singer.png`), so each is the same bike in every cut. An extra that only one cut needs (a cap, an earpiece) goes in that cut's prompt. Everyone but the three leads is used once and thrown away. The hair never changes, except in the memories: with a new costume every scene, the hair is how the viewer tells the two apart.
- **The fight-game layer.** The pixel select screen (the joke, 4), the VS screen (the real thing, 16), `ROUND 1` and `ROUND 2`, a boss health bar, arrow inputs and a combo counter, `K.O.` Drawn by `fight_hud.py` and `pixel_select.py` (M8).

## Who goes in each generation

- **Q4:** Vidu Q4, 5s, or 8s where one clip carries two shots. Almost every shot, the fights and the chase included: it keeps the faces
- **Q3C:** Vidu Q3 Cinematic, 8s, one action per clip. Only a run straight at the lens and the dojo, where Q4 goes flat 2D. The second-half rows below still say Q3C from the first plan; each is moved to Q4 when its prompt is written

References, in this upload order: each person's costume front, then their face (`singer-face.png`, `rival-face.png`, `master-face.png`), then blades or props, then one place. Seven at most, Q3's limit. A shot with three people has no room for the blades: name them in the prompt. The blades, the bikes and the case have plates. Guns, the wooden swords, the flask and the photo don't: Vidu invents them. Each is on screen for a cut or two, so they don't have to match from shot to shot, and a plate for each would take a slot from a face.

The plates are listed in [`prompts.md`](prompts.md#plates). Full-body shots stay in rain and city light, never on a bare stage. On an empty stage both models drew a 3D game render. 

## Intro · 0:00–0:26 · the hook

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 1 | 0:00–0:06 | The singer's eye in the rain, cut on the beat against 1b, faster bar by bar into "(Ha!)". Two 4-frame glimpses of what's coming: blades and sparks (1d), then the master's red eye (36b; 1c until it's made). White flash into 2 | Q4, made, plus 1c, 1d | G6, F1, F19 |
| 1b | 0:00–0:06 | The rival's eye under a hood, harbour lights behind | Q4, rival hood, harbour | G6 |
| 2 | 0:05:23–0:08:11 | "(Ha!)": after the white flash, `STEEL IN BLOOM` slams in and the dive (3) plays inside the letters, black around them. The drone rises inside the letters at about 0:07, so the eye looks for what is moving; then the camera flies into the letters and the drone is in the middle of the frame at 0:08:11 | Edit | F4, M7, F14 |
| 3 | 0:08:11–0:13:16 | The FPV dive, following the agency drone: it hangs in the middle of the frame as the letters cut away, the camera tips over and dives, then races down the neon street. A drone HUD in the top right counts the altitude down through the dive and holds about 5m on the street. From 0:10:00 a lower third types `NEO-EDO` / `SHOGUNATE YEAR 2083`. Ends on the accent at 0:13:16 | Q3C, rooftop, made | G5, M1 |
| 4 | 0:13:16–0:26:11 | A 16-bit arcade character select screen, the joke version; no VS here, the real one is 16. The singer gets `P1` and her stats fill row by row, `ZUNDA` empty. `P2` tries the black `???` (the master): red noise, `LOCKED`, and the screen snaps in on her card. `P2` takes the rival, and on the loudest bar her `ZUNDA` runs past five stars off the screen. The screen snaps in on it, switches off like a CRT, and `MISSION START` comes up into verse 1 | `pixel_select.py`, from the plates | M8, M2, F19 |

## Verse 1 · 0:26–0:46 · the case, and the message

The two are never in one place. The singer is at the agency at night, the rival at the tea stall at dawn, alone, and the edit cuts between them. She still sets out two cups and pours the singer's first. Two women in one frame with a small exchange came out robotic in every roll, so the talk at the stall became a message.

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 5 | 0:26–0:31 | "Morning steam above the stall": the stall wide from the street, the rival alone at the counter with her back to us, the stool beside her empty, steam off the kettle (6-2); the singer at the agency with her back to us (5), the hologram in her sunglasses (5b) | Q3C 6-2, Q3C 5 and Q4 5b made | F1, M1 |
| 6 | 0:31–0:36 | "Two cups waiting by the wall": two empty dark bowls on the wet counter, from straight above (6), the rival's file on the agency screens, with a glowing green mochi turning, `CONTRABAND`, and the drone's feed from shot 3 | Q3C, made, plus edit | F24, M4 |
| 7 | 0:36–0:41 | "You pour mine before your own": the rival's hand pours the singer's cup first. Framed to match the flipped 17. Then her eyes on her tea (8b) | Q3C, rival, stall, plus 8b made | G1, first half |
| 8 | 0:41–0:46 | "Same as every day we've known": split screen, the agency and the stall. The singer sends the message, an old photo of the two apprentices and their master; it flies across the split and lands as a hologram over the rival's cup. She sighs the steam through it and doesn't look. Then the singer turns to camera (the end of 5). Freeze, and her intro card builds | Edit, from 5, 8b and the plates | F9, M4, M3, F3 |

The photo is built in the edit from `singer-gi.png`, `rival-gi.png` and `master-front.png`, with grain and a film burn so it reads as old.

## Verse 2 · 0:46–0:56 · the deal

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 9 | 0:46–0:49 | "Petals stick": the harbour at night, the rival in a hood hands a case to two thugs | Q3C, rival hood, harbour | F21, M1 |
| 9b | 0:46–0:49 | The open case: rows of glowing green mochi, a flash on the cut | Q3C, case, harbour | F21 |
| 10 | 0:49–0:52 | "Whetstones": split screen, the singer on a crane watching through a scope, and the scope's view of the rival | Q3C, singer suit, harbour | F9, M4 |
| 11 | 0:52–0:54 | "Neither of us says the word": the rival's face, eyes down, then the singer's eye at the scope. Neither speaks | Q4, made, plus 12-2 | |
| 12 | 0:54–0:56 | "Both of us already heard": the rival turns and looks straight up at the scope. Freeze, and her intro card builds | Q4, rival hood, harbour | M3, F3, F25 out |

### Cutting 0:26–0:56

The rough cut, as placed. Line starts are the caption starts less one frame; cuts inside a line sit on bars, to be checked by ear. The build work (6's screens, 8's photo, 10's scope, the intro cards) is on top of these.

| Time | Clip |
| --- | --- |
| 26:11–28:16 | 6-2 from its start, the stall from the road, the rival alone, the stool beside her empty; the camera pushes in |
| 28:16–30:04 | 5 from its start to 1:11, her back to us before the screens. It stops before 1:12, where the split's piece of 5 starts |
| 30:04–31:08 | 5b, the screens in her glasses |
| 31:08–33:16 | 6 from 0:06, two empty bowls from straight above, Scale 115% at Y +70 to push the floor at the top edge out. Its first six frames are the `tea-stall.png` plate, so it never starts before 0:06 |
| 33:16–35:19 | The rival's file on the agency screens, one item a beat: `hq.png` blurred and darkened behind, her face in a cyan frame with `SUBJECT 02` (33:16), the case's mochi flipping in by Scale X (33:23), a red `CONTRABAND` stamp with the 18 title's pop (34:07), the drone's feed from 3 with `● LIVE` (34:22) |
| 35:19–38:16 | 7, the pour. Over 38:06–38:14 it is pushed right (X 0→+800) as the split opens, so the cup and the teapot stay in the right half |
| 38:06–39:18 | Split screen: 5 from 1:12 on the left, slid in from the left edge with the line over 38:06–38:14. On the right the end of 7, then 8b from its start at 38:16 at X +250 so the cup stays in. From 38:14 the photo and a blinking `SENDING ▶▶▶` (4 frames on, 4 off, to 39:06) are beside her; the photo flies across the line over 39:06–39:11 and lands on the cup. Over 39:12–39:17 the line slides back out to the left and the stall fills the frame, the photo riding on the cup to +350/−280 by 39:18. 8b has only 26 frames before her eyes drop, so the split starts over the pour rather than after 8b |

Built so that nothing has to be kept in step by hand. The singer's half (5 at Crop L480 R480, X −480) and the line are one compound clip, moved by Position X alone: −960 at 38:06, 0 at 38:14 and 39:12, −800 at 39:17. Nothing under it is cropped; it covers the left side. Every moving layer is moved by Position only, with keyframes on the same frames: 7 (0 → +800 over 38:06–38:14); 8b (+250 at 39:12, +41.7 at 39:17, 0 at 39:18); the photo (+600 at 39:12, +391.7 at 39:17, +350 at 39:18). With one kind of parameter and the same frames, every layer gets the same ease, so no gap opens at the line. A first build animated 8b by Crop and Position together, and Crop and Position eased differently: the edges met on the middle frame of each move and showed a black gap on the others.
| 39:18–42:10 | 8b full frame. Her eyes drop to the photo at 39:20, hold, and close from 40:19 on "Same as every day"; the breath shows at 41:10 and drifts right through the photo. The photo becomes a hologram where it lands (cut at 39:11): Aged Film and Sepia off, Colorize white `#33E0FF` / black `#002A40` at 100, Opacity 80, a cyan border, Flipped horizontal because we see it from behind (she sees the singer on the left, we see her on the right), and a trapezoid by Distort (Top Right −120/−27, Bottom Right −120/+27), its far right edge shorter as it turns to face her. It rests at +350/−220. It opens from a line (Scale Y 3%→45% over 39:11–39:14), drops out for one frame at 39:13 as it boots, and squashes back to a line over 42:06–42:09. Bad TV gives the scan lines and the shake: Amount 25 through the opening, down to 10 by 39:18, back up to 25 over 42:06–42:08 as it goes out (Roll 0); Bloom at Amount 9.3. A cyan beam from the bowl to its lower edge (`Beam`: a Custom generator cropped and distorted into a trapezoid, moved with 8b, inside a compound so Gaussian 8 and Add apply to the cut shape; Opacity 0→35% over 39:11–39:12, 35→0% over 42:06–42:09) sinks back into the bowl as it goes out (Crop Top 855→998 on `Beam`, 42:06–42:09). The cut at 42:10 follows |
| 42:10–44:22 | The end of 5 from 5:10, at the window in profile, turning to camera |
| 44:22–46:12 | Freeze on the frame at 44:21, from the browser (`Shift+F`, then `Option+F`) so it connects over the gap and nothing ripples; for the intro card |
| 46:12–47:10 | 9 from 3s |
| 47:10–48:22 | 9b from 5s, a 2-frame white flash on its first frame |
| 48:22–51:14 | 10-3 from its start, full frame. On the bar at 50:04 the scope opens below her barrel (Scale 0→100% over 4 frames, X +480, Y −230). The scope is a compound of two layers. On top, the view: 9 from 5s at 200%, X −720 / Y −320 so the crosshair sits on the rival's face (at 200% the circle holds only her head; she drifts right and up about 65 and 50 over the shot), with a red `#FF2A2A` crosshair 3px wide (an illuminated reticle: a black one vanishes on her black hood), cut to a circle of radius 250 by a Shape Mask. Under it, a black circle of radius 270 as the rim |
| 51:14–52:14 | 12-2 from its start, eyes down |
| 52:14–53:19 | 11 from its start, the singer's eye at the scope |
| 53:19–54:12 | 12 from 1:12, the eyes rising |
| 54:12–55:23 | Freeze on 12's 2:04 frame, eyes up, for the intro card (35 frames; `WIFE`'s had 38) |


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
- **4.** A 16-bit arcade select screen, cheap on purpose: the joke version of the fighting-game layer, where 16 is the real one. No VS in 4: two VS screens a minute apart read as a repeat, and the first was the weaker. Every state is a full-frame PNG from `_tools/image/pixel_select.py`, drawn at 320×180 and scaled up 6× with scan lines. The portraits are sprites the script makes from the face plates (backdrop cut off, a 22-colour palette, dark pixel outlines), and the background is `rooftop.png` cut to 24 colours: nothing is generated. The PNGs, in `graphics/select/`, go one after another on a lane above the base, each until the next starts, and the lane becomes one compound clip that carries every move, so nothing is positioned by hand.

    Bars by ear from 0:13:16, 30 frames each. The bar grid counted from the WAV ran 5 frames early against the ear here (it gave 10:23 and 13:11 for 11:04 and 13:16), so every time is checked by ear. The music is loudest over 21:04–23:16 and drops a level at 23:16.

    | Time | PNG | What happens |
    | --- | --- | --- |
    | 13:16 | `px-01-singer-0` | The screen comes on like a CRT: Scale Y 3% to 100% over 2 frames. `P1` on the singer, `AGENT` in the panel |
    | 14:22, then a beat apart | `px-02`, `px-03`, `px-04` | Her stats, a row a beat: `SPEED` 4, `POWER` 5, `ZUNDA` empty |
    | 16:04 | `px-05-master-0` | `P2` jumps to `???`: 8 frames of Bad TV and the Position X shake 0/20/−20/10/0 every 2 frames, then `LOCKED` |
    | 17:10 | the same | Snap in on her card: the lane in one compound, 100% at 17:10 to 160% at 17:12, Position −576/−182 (as far as it goes without showing an edge), held to 18:15 |
    | 18:16 | `px-06-rival-0` | Back to 100%. `P2` on the rival, `SMUGGLER` |
    | 19:22, then a beat apart | `px-07`, `px-08` | `SPEED` 5, `POWER` 4 |
    | 21:04 | `px-09-rival-3` and `px-zunda-overflow` | `ZUNDA` 5, and on the same frame the overflow runs on past the panel and off the right edge: Crop Right from 540 to 0 over 21:04–22:02 (its stars start at x 1386). A 2-frame green flash (`#7CFF3A` at 50%) and the shake 18/−12, −14/10, 10/−6, −6/4, 3/−2, 0/0 a frame each from 21:04 |
    | 23:16 | the same | Snap in on the row: 100% to 150% over 2 frames, Position −480/270, the bottom-right corner |
    | 25:00 | the same | CRT off: Scale X/Y 150/150 at 25:00, 150/3 with Position 0/0 at 25:02, 0/3 at 25:04, so it collapses to a line and then a point; Color Board Exposure 0% at 25:01 and +60% at 25:02 for the flare |
    | 25:05–26:11 | `px-mission-start` | `MISSION START` in the same pixel font, blinking 4 frames on, 4 off, as an arcade does: bladed at 25:09, 25:13, 25:17, 25:21, 26:01 and 26:05, with the pieces at 25:09, 25:17 and 26:01 disabled so the black shows. It ends lit, 26:05–26:11, into verse 1 |

    The stats are on the select screen, where fighting games put them, and the singer's empty `ZUNDA` pays off in 50. The cursors are the singer's purple and the rival's green, the colours of 20; `P2` goes red on the locked card.
- **5.** The agency gets more time than the stall: 26:11–31:08 splits on the bar at 28:16, 53 frames for the stall and 64 for the agency. The mission room is dense and needs reading time; the stall is one woman on a stool and reads at once. Ends facing the camera, centred. The freeze runs 44:22–46:12 and the intro card slides in from the left, clear of her shoulder. Names are codenames: no real name goes on screen. Hers is `WIFE`, under a small `CODENAME`, over `AGENT`; the rival's card in 12 is `ZUNDAMON` over `SMUGGLER`, the same labels as the select screen. A dark purple band (`#1F0829`, 85%, Crop Right 1180, Top 336, Bottom 330) carries `CODENAME` (Menlo 36, `#CC73FF`, Tracking 20%, X −590, Y +135) and `AGENT` (DIN Condensed Bold 56, `#CCCCCC`, Tracking 30%, X −590, Y −165, from 45:12), all one compound clip sliding X −800 → 0 over 44:22–45:02. `WIFE` is the 18 title copied for its purple glow (it has no outline), Size 152 so it matches `ZUNDAMON`, which needs 152 to leave 43 each side in the band, the same as above and below, its pop removed: it slides in by Position alone, X −1500 → −590 over 45:02–45:05, landing on the beat, at Y −106, which leaves equal gaps (65) above and below it, with 42 between the text and the band's top and bottom. The 18 title's text sits above its Position by about 0.7 of its Size (140 at 200, 112 at 160); and its pop scales around the frame centre, which pulled an off-centre title across her face.
- **The two freezes under the cards (44:22, 54:12).** On the freeze the picture drains to grey and darkens a little, so the band's purple or green is the only colour left. The same move as a character card in an anime opening; held in colour, the band sinks into the picture.
- **1c and 1d, the glimpses.** Black and white with a zoom blur. 1d is `22e-4.mp4` 2:00–2:16 at 400% (Retime Custom, Ripple, Video Quality Normal), 4 frames: the blades touch, the flash bursts and the sphere of light grows to its full size, so the opening flashes forward to the hit that 22 pays off. At normal speed 4 frames hold only the start of the flash.
- **5b.** `5b-2.mp4` has bigger glasses than the plate. One beat at most: a single frame doesn't read. Dropped if the glasses show.
- **6-2, 6, 7.** The cups go empty, then poured, then drunk: the stall with her alone and the empty stool (6-2), two empty bowls (6), she pours the singer's first (7), her own in front of her (8b). Cups shown full before the pour read as a mistake. The two cups were set up for a scene of the two side by side at the counter, which was dropped; they now pay off at 49–50, where she pours again and the singer is there to drink it.
- **7.** If it came out mirrored against 17, flip it (Effects → Distortion → Flipped). The cut to 17 lands on "Draw!", on the hand gripping the handle.
- **8.** No clip. The old photo is built from `singer-gi.png`, `rival-gi.png` and `master-front.png`, with grain and a film burn, and floats over the cup in 8b as a hologram.
- **9.** Use from 3s on; the case warps before that. `9-2.mp4` has her hood down, so the tufts say who it is: one bar after a hooded cut.
- **9b.** Only the last three seconds. Put a white flash on the first frame used, so the warp just before it doesn't show.
- **10.** `10-3.mp4`, side-on along the girder, aiming right, the suit matte. It is wide, so it stays full frame and the scope opens over the girder and the water below her barrel; shrunk to half she would be too small to read. One piece from its start: the camera trucks the whole clip, so a cut inside it adds nothing. `10.mp4` is not used because the suit shines like rubber, and `10-2.mp4` because she faces the other way and the cut would flip the screen direction.
- **11 and 12.** No second deal: 9 already shows the hand-over and 9b the case opened, so handing the case again straight after reads as a repeat. The line goes to the two women instead. `12-2.mp4` only while her eyes are down (they start to rise at 1s), then the singer's eye at the scope, a Q4 close-up of 10-3's girder and pose (`10.mp4` is a different crane and pose). Then `12.mp4` as the eyes rise, so she looks up into the scope just after we have seen who is behind it. Freeze where the eyes are up, not on the last frame, and her intro card builds. The eyes are yellow-green. The card is `WIFE`'s, copied and turned green, in the same place. The band's right end touches only a little of her cheekbone, and green hair under it is fine since her face is already out. Band `#0D2410`, 85%, Crop Right 1180, Top 336, Bottom 330; `CODENAME` `#A6FF4D` and `SMUGGLER` `#CCCCCC` at X −590; `ZUNDAMON` Size 152 so eight letters fit the band, with a `#A6FF4D` glow, X −1500→−590 over 54:20–54:23 at Y −106. The band compound slides over 54:12–54:20, `SMUGGLER` from 55:06, everything ends at 55:23.

## Pre-chorus · 0:56–1:08 · the ambush on the bridge

The one slow stretch, and it stays slow: the stillness is what makes the drop hit.

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 13 | 0:56.01–0:58.56 | "One more bell": a red lantern on the bridge, swinging in the rain | Q3C, made | F21 |
| 14 | 0:58.56–1:01.14 | The singer in profile facing right against the neon city across the canal, no lanterns, cold purple light on her face, the camera arcs round from behind her shoulder in a gust, one slow breath out, the wind tearing the mist away | Q4, made: `14.mp4` | F24 |
| 15 | 1:01.14–1:03.6 | The rival in three-quarter facing left, the focus pulling from the dripping railing to her face, her eyes sliding left to something far off | Q4, made: `15.mp4` | F24 |
| 16 | 1:03.6–1:07.7 | The VS screen, the only one, played straight: 4 is a pixel-art select screen with no VS, in the order a fighting game uses. A slanted split slides in over 15, off the bridge, each in her own colour. Top left in purple fire, the singer from far below, looking down her nose at the camera; bottom right in green lightning, the rival from above, a sideways grin. As the two halves meet, a white line on the seam, `VS` slams onto it and `WIFE` and `ZUNDAMON` slide in, each on her own side. On the gap both freeze. Then the stage: 17 comes in a second early under `ROUND 1`, and "Draw!" is the "FIGHT!". No health bars: they belong to the fight, and first come in on the hit in 24b. The type is PNGs in `graphics/`, made by `_tools/image/fight_hud.py` | Q4, made (16a, 16b) | F3, F9, M8 |

## Chorus 1 · 1:08.8–1:32 · the duel

The chorus is being rebuilt. The cut below is the plan; the rough cut further down is the timeline as it stands until the new clips are in.

- **The light changes on "Draw!"** Up to 17 the bridge is lantern-lit and calm. From 17's white flash on the blades carry the light: each swing leaves a glowing arc, purple for the singer and green for the rival, the colours of `ONLY` and `ONE`. The glow comes from the generation. The clips stay as generated, with no darkening grade: a Color Board on the shadows and midtones made the night scenes muddy, and one setting can't even out clips this different.
- **One woman a cut until the hit.** The run-in is one woman a cut. From the hit (22e) the two share the frame while they are locked or trading blows (23a, 24a), and at the end, far apart (24d). Every cut changes the camera, and every camera moves but 24d's.
- **Cut to the music, not the words.** The cuts land on the beats; what is sung doesn't decide what is shown. The stillness and the distance are in the pre-chorus, the singer alone and then the two at the two ends; from "Draw!" nothing stops until the hit, which lands on the second "Draw!" at 1:18.75, the loudest downbeat of the chorus.
- **Now and then, cut against each other.** The past comes once, out of the lock: the lock now, the same clash ten years before (20e), her knocked down by it and laughing on the floor after losing it (23b), then back in the bind as it breaks (24a). Her face now comes after the blow, as she lifts her eyes at the end of 24c. The two as apprentices with wooden swords in the old dojo, 4:3 with grain. The master is never in these cuts; she first shows in verse 3, where the room widens to take her in. The memory clips are cut again in 27.
- **Models.** Q4 first: it keeps the faces, and Q3 Cinematic changes them. One woman a cut keeps Q4 out of the complex multi-plate moves that break it, and it carried the clash too, where Q3 failed every roll. A blade runs out past the frame edge: with the tip in the frame Q4 draws it short and thick. Q3 Cinematic only for a run straight at the lens (20c, 20d) and the dojo, where Q4 draws flat 2D anime at any size. A shot that keeps failing on Q3 moves to Q4.

Lengths in beats, about 0.31s each, eight to a sung line.

| # | Start | Beats | Shot | Camera | Gen |
| --- | --- | --- | --- | --- | --- |
| 17 | 1:07.7 | to "Draw!" | The rival's hand grips the hilt, the stage: from a second before "Draw!" under `ROUND 1`, then on the "D" of "Draw!", the "FIGHT!", two negative frames and the white flash | Hand close-up | Q3C, made |
| 18 | | 5 | The singer lifts her eyes to the camera, lit only from behind, no blade in sight. `STEEL`, `IN` and `BLOOM` come in one at a time, on 18 only: It starts out of 17's flash on "Draw!". The words are sung one by one, and each comes in on its own: `STEEL` on "Steel", `IN` on "in", `BLOOM` on "bloom". Each is cut together: its top half slides in from the left and its bottom half from the right, they meet with a one-frame white flash, and the seam stays a few pixels out of line, a word cut by a blade. `STEEL` big over her hair at the top, `IN` small to the right of her face over the blurred lanterns, `BLOOM` biggest across her chest, left of centre, as her eyes meet the camera, with a shake. The eyes and mouth are never covered. Each half is a copy of the title cut by Crop and moved by Position only: the title's pop scales around the frame centre and drags an off-centre word across her face | Front, chest up | Q4, made |
| 21a | 1:11.28 | 4 | The rival finishes the draw 17 started, a green arc | Side-on, low | Q4, made |
| 21b | | 4 | The singer's blade, seen for the first time: the whole blade comes up purple as she snaps it level. Her face only in soft profile at the top, so it doesn't repeat 18's front face, and so Q4 keeps her look | Blade close-up at chest height, tracking left along the blade to her hand on the hilt | Q4, made: `21b.mp4` |
| 20a | 1:13.70 | 2 | The singer's sandal stamps into a puddle | On the deck | Q4, made |
| 20b | | 2 | The rival's sandal, from the other side | On the deck, reversed | Q4, made |
| 20c | | 2 | The singer runs straight at the camera, a purple ribbon of light off her blade. Cut before she veers past the lens: two beats are too short for the swerve, and a swerve contradicts a charge at the rival | From the planks, tilting up, down the deck | Q3C, made |
| 20d | | 2 | The rival runs straight at the camera, a green ribbon of light off her blade, cut before she veers, as 20c | From the planks, down the deck | Q3C, made |
| 22a | 1:16.16 | 2 | The singer's charge, the purple trail behind her | Tracking beside her, waist height | Q4, made |
| 22b | | 2 | The rival's charge, green | Tracking beside her, reversed | Q4, made |
| 22c | | 1 | The singer's eyes, lit purple | Eyes | Q4, made |
| 22d | | 1 | The rival's eyes, lit green, the irises yellow-green | Eyes | Q4, made |
| 22e | 1:18:01–1:19:07 | 4 | `22e-4.mp4` from 1:09 to 2:15: the two charge in from the two sides and clash, the flash at 2:02 on the downbeat of the second "Draw!" (1:18:18), the sphere of light, purple on her side and green on hers. Impact frame on the contact, 2 frames | Wide, from the side | Q4, made |
| 23a | 1:19:07 | 4 | The lock: the two chest to chest, the blades crossed at the guards, shoving, a fountain of sparks. Used once: a second cut of it after the memory came back to the same picture a few seconds later, and stopped the fight just before 24a | Pushing in on their faces over the crossed guards | Q4 5s, the start of the 24a roll (`23a.mp4`, over her shoulder, for now) |
| 20e | | 2 | The past, out of a white flash: the young singer drives in with one hard, trained cut, long loose hair | Side-on | Q3C, made |
| 23b | 1:20:13 | 6 | The past, straight after 20e's cut: the young rival takes it, is knocked down onto the dojo floor, laughs up at her friend, "you're too strong!". Ten years before the singer throws her in 24a–24c | Following her down, ending low on her face; the clip is wide, so the push-in is made in the edit inside the memory's compound clip | Q3C, made |
| 24a | 1:23:02, to 1:25:19 | 9 | Out of the memory, back in the bind, their faces a hand's width apart: the singer throws the rival off, spins and cuts, a ribbon of purple light round her, mirrored in the wet deck; the rival blocks and is thrown out of the right. The memory cuts back to the present in a new clip and a moving camera, not to the lock again. Cut on the swing, before the blades meet: the contact is first seen in 24b | Close on the bind, then pulling back and dropping low through the spin | Q4 5s, the same roll as 23a, from the shove that breaks the bind (`24a.mp4` for now) |
| 24b | 1:25:19 | 2 | The rival takes the blow on her blade and recoils: the hit only, the flight is 24c. It starts on the contact frame at 1:25:19, where 24a ends, held 2 frames for the hit stop (1:25:19–1:25:21), so the cut is the impact. The strobe and the shake start at 1:25:21, as the picture moves again. 4 frames of hold on top of a cut on the impact stalled the spin's speed; 2 frames read as weight. The hit: hit stop, strobe, RGB split, shake, her health bar drops | Front, chest up, jolting with the impact | Q4, made |
| 24c | 1:26:04, on "Then", to 1:29:09 | 10 | Thrown in from the left, she lands and skids back, jamming her blade into the planks to stop, and lifts her eyes. In `24c.mp4` she is already down on one knee and is dragged backward, the reverse of a carving turn: no landing, so no shake; 24b's hit carries it. It runs to the end of the clip: from where the camera starts pushing in on her face, at 200%, so the push-in moves. Her hard face now is this end, the payoff of the laugh in 23b, so 23c is out | Whipping in low with her, jolting to a stop, then in on her face | Q4, made |
| 24d | 1:29:09 | to 1:32.1 | The glow fades off both blades. The rival, still down on one knee from 24c, pulls her blade out of the planks, gets up and runs off the right | High above, the deck filling the frame, held: the one still camera after "Draw!". Once she is gone it tilts up into the rainy sky, the turn away from the bridge before the chase. The sky fades to black over its last 12 frames, 1:31:13–1:32:01, and 25a cuts in hard on the downbeat: no dissolve, which would blend the rain into the dry road | Q4, made: `24d.mp4`, tilting up into the rain |

The `ONLY` / `ONE` titles stay, recoloured and moved (see 20 under the rough cut). The smuggler's smile (`23.mp4`) stays kept for the reveal in 34. Out of the cut: `23c.mp4` and the eyes `22c-2.mp4` / `22d-2.mp4` (one face close-up too many each: 23c needed 300% to fit and sent the memory back to the lock; the eyes repeated 22c–22d and the opening of the song), `20f.mp4` (23b holds the blow, and the same woman twice in a row broke the cut), `18-old.mp4`, `20-2.mp4`, `21.mp4`, `22.mp4`, `24.mp4`, `19-1.mp4`, `15b.mp4`, i3, the super-move cut-in in 21 (the split in 16 is the same device five seconds earlier), and the falling lantern.

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
- **19 · "Red against the rain".** Cut on "Red." The colour isolation starts on the cut, everything grey but the red. One Color Board: a Color Mask on the red of her hair cord (Add), then a Shape Mask around her and the cord's sweep (Intersect, last), so the red lanterns and railing stay out. Outside the mask, Saturation Global −100%. Inside, Saturation +40% and Exposure +10–15%, so the red glows. Auto Mask mis-detected her, and a second Color Mask for the cord's dark underside also caught her hair, so neither is used. Masks combine top to bottom.
- **20 · "Only one walks off this bridge / Only one goes home again".** Cut on the first "Only." Four new clips replace the stare-down: 20a 1:13:15–1:16:04, 20b 1:16:04–1:17:10, 20c 1:17:10–1:18:04, 20d 1:18:04–1:18:16, each cut on a bar, to be checked by ear. 20c gets a 4-frame hit stop where the two cross (`Shift+H`) and a 2-frame impact frame on it (Color Board Saturation −100%, contrast pushed). The old cut, eight pieces of `20-2.mp4` with i1 and i2, was a stare-down in the same picture as the shots around it; its titles stay.

    The four titles are the 18 title copied with `Option+V`, so the pop comes with them, at Position X 0. They follow the voice, not the cuts: `ONLY` starts on "Only", and `ONE` on "one" about 8 frames later. Shortening a title's tail keeps the pop; trimming its head cuts it, so a title is moved with `+` and a frame count. White fill, with the glow (no outline) picked with the eyedropper from the hilts. The fill stays white to read against the night. One `ONE` on the second "Only" read as a mistake; two of each matches the lyric.

    With one woman a cut, `ONLY` always lands on the singer (20a, 22a) and `ONE` on the rival (20b, 22b), so the colour follows who is on screen: `ONLY` purple, `ONE` green. Colour by line put green on the singer. The two lines differ in how they come instead. The first line is one word at a time at the top centre (X 0), each word's top on the title-safe line, clear of the feet in 20a–20b. The second is at the bottom, 1.2 times the size, `ONLY` at X −320 held on as `ONE` joins it at X 320, so the two colours read `ONLY ONE` side by side before the clash; their bottoms on the title-safe line, clear of the faces in 22a–22b, and both end where 22c starts, since the eyes' close-up has the nose and mouth low. The title is set above the centre of its box, so the two lines' Y values are not mirror numbers: place them by the safe-zone lines (View → Show Title/Action Safe Zones). Each pops 140% to 100% (168% to 120% on the second line) over 3 frames, Opacity 0 to 100% over 2; no drift after it, since a scale on an off-centre title slides it.

- **21 · "Draw!".** Cut on the second "Draw!" Her right hand goes to the hilt and the draw starts on the word. The bit of steel showing in 17 is ignored. In 20 her blade is sheathed and her hand is off it, so 21 starts from there. The line goes on to "Steel in bloom" and the shot runs under all of it.
- **22 · "Faster than the light".** One clip, no cut inside it. It starts on "Faster" with the two running in; the clip's first second, an empty bridge, is cut. The blades hit about a second before "light." Moving the hit onto "light" would need that empty second back or a slowed run, so the hit stays where it falls. The afterimage covers the 8 frames before the hit, and the white flash starts on the hit frame. The lock runs on through "light" until "Smile."
- **23 · "Smile at me the way you do".** Cut on "Smile." 22 runs on under it, bladed at 1:23:14, 1:24:05, 1:24:20 and 1:25:11, and the old `23.mp4` above it is disabled. Four cuts: 22's lock with a Ken Burns from the full frame to about 80% on the crossed blades (15 frames, the tips may touch the top), 23b, the apprentice on the floor laughing, 4:3 with grain (10), i2-2, her face now (15), then 250–300% on the point where the blades meet and spark, Sharpen 5 (19), into 24, where the singer breaks the lock. The bright white memory between two dark cuts is the one change of light in the chorus. Wide first and tight last, so the lock closes in. The fourth cut stays a crop of 22 despite the softness: 22's lock runs straight on into 24, and a sharper close-up from another roll would break it. `23.mp4`, the rival's smile, is out: at this point she is the smuggler, and the smile belongs to the reveal in 34. The vignette moves to i2-2 with Paste Attributes (`Shift+Cmd+V`), unchanged: the inner ellipse holds both eyes and the hair and mouth go dark: Vignette (not Vignette Mask), Darken 0.65, Falloff 0.3, Size 1.03, Blur 0. Judge it with the viewer at Fit.
- **24 · "Then cut me down tonight".** Cut on "Then," during the short lock. The current `24.mp4` lands its hit on "tonight" by placement alone and carries one effect, the shake. It is to be replaced from 24b–24d, which all start locked so 22 and 23 run into it. On the new clip:

    1. **Place it.** Its head at 1:26:01, on "Then." The blades meeting on "tonight," about 1:29:00: trim the head of the lock to bring the hit forward. Change the speed only if trimming can't get it there.
    2. **Shake on the hit.** Scale 104% on the whole clip, so the moves never show an edge. Position keyframes over the 6 frames from the hit: X/Y 18/−12, −14/10, 10/−6, −6/4, 3/−2, 0/0. The only shake in 13–24.
    3. **Strobe on the hit.** Three one-frame white flashes, a frame apart, from the hit: copy the white flash from 17 and trim each copy to one frame.
    4. **Sparks.** If Vidu's sparks are faint, a Bloom effect over the 6 frames from the hit, keyframed up and back down.
    5. **Punch-in on the slow motion.** Vidu slows the clip by itself after the blades cross. Blade the clip where it slows, and set the second piece to Scale 115%, so the change of speed lands as a cut.
    6. **End at 1:32:01,** where the instrumental starts. If the clip runs short, stretch its slow part. Nothing else goes in to fill it.
    7. **Hit stop.** Hold the hit frame for 2 frames (4 stalled the cut on the impact in 24b), the freeze fighting games use to make a blow land (Retime → Hold, `Shift+H`). It pushes everything after it 4 frames later, so trim the clip's end back to 1:32:01 straight after. The strobe and the shake start when the picture moves again.
    8. **RGB split on the strobe.** The Prism effect (Blur category) on the three strobe frames only, so the colour tears apart on the hit.
    9. **The rival's health bar drops.** The two health bars flash in on the hit, their first time on screen, and the rival's loses a big chunk from its outer end, toward the middle, as the bars in Street Fighter 6 drain: it says who won the first exchange. The HUD is drawn after Street Fighter 6 by `_tools/image/fight_hud.py`. It is one clip, `graphics/hud-fight-chorus1.mov`, over 24a to 24c, 1:23:02 to 1:29:09, so the bars are seen full through the spin before the hit takes them down: the timer counting down from 99 at "FIGHT!" (1:08:17), 85 at 1:23:02; `PUNISH COUNTER` sliding in on the singer's side on the contact at 1:25:19; the blow landing as three hits, one on each white strobe frame (1:25:21, 1:25:23, 1:26:01), the rival's bar dropping a step on each, 40% in all, from its outer end, and a combo counter under `PUNISH COUNTER` climbing `1 HIT`, `2 HITS`, `3 HITS`; the red chip draining after the last hit, 1:26:09 to 1:26:19.

    Who ends on which side doesn't matter: the second half isn't generated yet.

The cutting above is the rough cut as it stands. The rebuild in the table at the top of this chorus replaces 18–24 and cuts 15 down for 15b; the hit checklist under 24 moves to the hit in 24b. The prompts are in [`prompts.md`](prompts.md#chorus-1). The `ONLY` / `ONE` titles stay, laid out as in 20 below.

## Instrumental · 1:32–1:44 · the chase

12.3s, 1:32:01–1:44:07 as cut: six cuts, each on a beat, straight from 24d on the downbeat. The clips run at 150–200%, to use as much of each clip as fits, so there is no hit stop anywhere in the chase: in sped-up footage a held frame reads as the video stalling. The hits are white flashes, shakes and the HUD. Built like chorus 1: one woman a cut, each cut its own camera, the motion in the clip. Plain cuts between the shots: no slash wipe, since the clips already carry the flashes and there is no room for one. It is the rival's bonus stage, between `ROUND 1` and `ROUND 2` where Street Fighter puts one: the singer is the car. Everything she does scores for the rival, on P2's side of the screen: `BONUS STAGE` at 1:34:01, on the cut to 25b, once 25a's typed lines clear, with a stage timer and P2's score at 0, `PERFECT PARRY +10000` on the bullet cut out of the air at 1:36:06, `+50000` for the gantry on its biggest burst of sparks at 1:39:16, `+30000` for the singer's crash as her sparks stop at 1:42:11, and `PERFECT` with the total over the tail light at 1:43:04. One ProRes clip with alpha from `fight_hud.py`, as the HUD of 24b: `graphics/hud-bonus-stage.mov`, 1:34:01–1:44:07, the timer counting down from 30 and stopping on `PERFECT`, P2's score top right rolling up on each award, the awards sliding in from the right edge (`PERFECT PARRY`, `GANTRY DOWN`, `CRASH`), `PERFECT` and `BONUS 90000` high in the frame, clear of the tail light. The rival is `SMUGGLER` on the select screen, and acing her bonus stage hints she is the better fighter before the badge in 34; straight after, 26 shows what it cost the singer. Another night, as the costumes say: her white racing suit and white helmet (`singer-ride-helmet.png`) and the rival's black riding gear, bare-headed, her katana across her back (`rival-ride.png`), not the bridge's old clothes. Purple says which rider is the singer with her face hidden: the stripe on her helmet, the strip on her bike, and her rounds, which glow purple and burst purple and green on the rival's blade. The rival rides to the right, the way she ran off in 24d, so the cut still flows; the singer chases from the left. The bikes have plates (`bike-singer.png`, `bike-rival.png`), the pistol doesn't. The singer's bike is white with a purple strip, the rival's black with a green one. The bridge was heavy rain; the highway is after the rain, the road wet, no rain falling, so the weather says it's another night. The gantry is Vidu's own in 25e and in words in 25g and 25h: there is no gantry plate, since an action on a gantry already in the plate broke every roll.

| # | On screen | Shot | Camera | Gen |
| --- | --- | --- | --- | --- |
| 25a | 1:32:01–1:34:01 (2.0s) | Another night. 24d cuts straight to 25a on the downbeat, and a lower third types `3 NIGHTS LATER` over `NEO-EDO EXPRESSWAY · 02:14` across the whole of 25a, 1:32:01–1:34:01: shot 3's Typewriter title and settings, in the same place, but with a heavier Drop Shadow (Opacity 90%, Blur 10, Distance 0) since it sits on the wet road's reflections, the two lines as shot 3's two, typed by about 1:33:01 so a second is left to read. A black card between them was too short to read. `BONUS STAGE` comes in on the cut to 25b. The rival on a black motorbike, flat out down the empty highway after the rain, her blade across her back, leaning into a curve, the rear wheel throwing spray | Moving, from her side or ahead, never from behind | Q4, made: the camera left to Vidu, never from behind (from behind, the blade on her back broke), the singer's headlight behind her, all 5s usable. No side piece: 25b's gun cuts straight to 25d's parry, shot to reverse |
| 25b | 1:34:01–1:35:21 (1.8s), the shot at 1:35:15 | The singer on a bike behind her, in her white racing suit and helmet, leaning out of a curve, swinging the pistol up in her left hand and firing one purple tracer round, the camera closing in on the gun. 25c is folded into it | From the front, the rival's look back, round to her left side and in on the gun | Q4, made: the last part, under 3s, after the hands come right, ending on the shot |
| 25d | 1:35:21–1:37:01 (1.2s), the parry at 1:36:06 | The rival, her blade already drawn, glances back and swings it hard down to her lower right, toward the shot; as it stops a purple flash bursts on the steel. No bullet and no chaser in the frame. `PERFECT PARRY` on her side. No hit stop: on a moving bike a held frame reads as the video stalling | Low on her right, a little behind, tilted up against the sky | Q4, made: all 5s usable; holds a speed-up to about 200% too |
| 25e | 1:37:01–1:41:07 (4.3s) | 25e and 25f in one clip: the rival strikes the base of the gantry's right leg in one fast sweep as she passes, in an explosion of sparks, and rides on under it; the struck leg snaps and the beam falls from the right, pivoting on the left leg, its right end smashing into the road and catching fire. The gantry is Vidu's own, not a plate. A white flash on the strike, no hit stop; the white strobe, shake and extra sparks on the impact at 1:39:16 | Low on the road behind her, the chaser's view | Q4 8s, `highway.png`, made: `25e.mp4` |
| 25g | 1:41:07–1:42:21 (1.6s) | The fallen gantry stops the singer: she brakes too late, lays the bike down and slides in a shower of sparks, stopping just short of the burning beam, the road beyond it closed. Fire and smoke on the beam. The slide only: the torn sleeve and the pistol on the road are 26's panels | Low side view, sliding with her | Q4, made: `25g.mp4`, the second half (2.5s) usable at 100% |
| 25h | 1:42:21–1:44:07 (1.4s) | The rival's tail light shrinking into the distance beyond the burning gantry, into 26's last panel: the singer's view, stopped | Low on the road behind the fallen beam, still | Q4, made: `25h.mp4`, all 5s usable |

## Verse 3 · 1:44–2:06 · the master

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 26 | 1:44–1:49 | "Sleeves torn open, sandals gone": three manga panels. The singer's torn sleeve, her pistol on the wet road, a tail light vanishing | Q3C ×2 and a crop of 25a, highway | F10 |
| 27 | 1:49–1:54 | "Lanterns swinging, steel on stone": memory. The two as apprentices with wooden swords in the old dojo, laughing, the master watching. Their hair is the old hair: the singer's long and loose, the rival's in two low pigtails. 4:3, grain, film burn | Q3C, both in training clothes, master, training room | F8, F20 |
| 28 | 1:54–1:59 | "Every step we ever trained": the master shows a stance, the two copy her. Her eye flashes red for one frame | Q3C, the same | F2, F11 |
| 29 | 1:59–2:06 | "Every scar we never named": now. The singer alone in her apartment at night, tending her arm, the rival alone at the closed tea stall at night looking at a photo of the three of them. Cut faster and faster (`apartment.png`, `tea-stall-night.png`) | Q4 ×2 | F24, F1 |

## Chorus 2 · 2:06–2:30 · the raid

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 30 | 2:06.5 | `ROUND 2`, then "Draw!": the warehouse doors blow in, the singer in tactical gear comes through gun first, and her body wipes to the next shot | Q3C, singer tactical, warehouse | M8, F13, F4 |
| 31 | 2:09–2:11 | "Red against the rain": red alarm lights over stacks of glowing crates, muzzle flashes | Q3C, singer tactical, warehouse | F11, F20 |
| 32 | 2:11–2:16 | "Only one walks off": the two face to face between the crates, her gun at the rival, the rival's blade at her | Q3C, both, warehouse | F5, F2 |
| 33 | 2:16–2:21 | "Draw!", "Faster than the light": the rival swings at her and cuts down the thug behind her. Trails | Q3C, both, warehouse | F16, F7 |
| 34 | 2:21–2:24 | "Smile at me": the rival smiles and flips open a badge. The CRT switches back on to the pixel select screen of 4, `P2` on her card: `SMUGGLER` is struck out and `UNDERCOVER` slams in | Q4, rival raid, warehouse | F24, M8, M2 |
| 35 | 2:24–2:30 | "Then cut me down tonight": back to back, the two of them cut and shoot their way through the thugs, crash zoom on the last | Q3C, both, warehouse | F6, F7, F21 |

## Bridge · 2:30–2:42 · the boss

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 36 | 2:30–2:32 | The dip: `HERE COMES A NEW CHALLENGER!`, and the `LOCKED` card from 4 opens. On the rooftop the master steps out of the dark, the koi hologram behind her turns from cyan to red, and a boss health bar fills the top of the frame | Q3C, master, rooftop | G7, M8 |
| 36b | 2:30–2:32 | Her eyes glow red, a dark red aura rises off her | Q4, master, rooftop | F21 |
| 37 | 2:32–2:35 | "Left, right, low, high": four strikes, one a word, on twos. The two block. Arrow inputs on screen | Q3C ×2, all three, rooftop | F17, M4, M8 |
| 38 | 2:35–2:37 | "Blade on blade": the clash, sparks | Q3C, all three, rooftop | F7, F21 |
| 39 | 2:36.6 | "(Ha!)": she throws a wave of red energy and both are thrown back. White flash, negative frame | Q3C, master, rooftop | F4 |
| 40 | 2:37–2:39 | "Left, right, low, high" again, faster | From 37 | F17, M4 |
| 41 | 2:39.7–2:42 | "Draw it like you mean it": the two get up side by side, blade and gun raised. Crash zoom | Q3C, both, rooftop | F6 |

## Break · 2:42–3:01 · two against one

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 42 | 2:42.25–2:59 | The team-up at full speed: she shoots while the rival cuts in, a combo counter climbing, strobe on the hardest hits, one fake take through the joins. The finisher gets a double cut-in: both pairs of eyes in two bands | Q3C ×4, all three, rooftop | G8, F18, F20, M8 |
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
| 50 | 3:19–3:26.7 | "We'll draw again at night": both on the roof edge with tea and the confiscated case, eating the evidence. The singer's stat panel pops up and her empty `ZUNDA` fills, ☆☆☆☆☆ to ★★★★★ | Q3C, both, case, rooftop dawn | F23 |

## Outro · 3:26.7–3:38 · the last hit

| # | Time | Shot | Gen | Technique |
| --- | --- | --- | --- | --- |
| 51 | 3:26.7–3:36.25 | The dive of shot 3 in reverse, up from the two of them into the dawn sky. End card | Q3C, both, rooftop dawn | M7, G5 |
| 52 | 3:36.25 | The sound drops out: black | Edit | |
| 53 | 3:37.0 | The last hit: `CONFISCATED` stamps down on one mochi, then the title | Edit, a frame of 50 | F4, M2 |

## What gets generated

Outside 1 and 13–24, the shot list needs 35 Q3C clips and 13 Q4 clips, the made ones included. Made so far: 1b, 3, 5b, 6, 6-2, 8b, 9, 9b, 10, 11 and 12, and the chase, 25a, 25b, 25d, 25e, 25g and 25h.

## Order

Midjourney is done. Vidu: the chase is made. The last chorus 1 roll (23a and 24a in one clip) is out, then the second half in song order, 26–53. The queue is in [`prompts.md`](prompts.md#vidu-next).

Everywhere: F1 beat cuts, F23 one grade over the whole song, F24 on every close-up, F26 at each section change.
