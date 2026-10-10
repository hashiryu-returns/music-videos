# EN — working title "Two Blades"

A spy story in a near-future city, with no message to it. The point is two cool characters and a video that never sits still. Excitement first, story second, the lyric only where it helps. The first ten seconds have to hold a viewer.

This one is a study piece: can the edit make simple footage exciting? The shots stay simple, and the cutting, the speed, the type and the effects make it busy. A fight-game layer (a VS screen, rounds, a boss health bar, `K.O.`) ties the graphics together.

## Story

The two women trained under the same master and were friends. Now the singer is an agent who works international crime. The rival is mixed up in smuggling zunda mochi, banned by the Shogunate, and the singer tries to stop her: she sends her an old photo of the two of them with their master, then ambushes her on the bridge, chases her down the highway and raids the warehouse. In the warehouse the rival shows her badge: she is undercover on the same case. The one behind the smuggling is their old master. She wakes to the Surge of Murderous Intent: a red aura, red eyes, and she is strong, but the two of them beat her together. At dawn they drink tea on the roof and eat the evidence.

The VS screen in the intro labels the rival `SMUGGLER`, and the reveal strikes it out for `UNDERCOVER`. In the memory of their training, the master's eye flashes red for one frame.

| Section | Story | Place | Fight |
| --- | --- | --- | --- |
| Intro | Flash-forwards, the title, the city, the VS screen | the towers | |
| Verse 1 | The case at the agency, cut against the rival alone at the tea stall, still pouring two cups. The singer's message, an old photo, lands over her tea | HQ, the stall | |
| Verse 2 | The deal at the harbour, watched through a scope | harbour | |
| Pre-chorus, chorus 1 | The ambush and the duel | the bridge, the old clothes | swords |
| Instrumental | The chase | highway | gun against sword |
| Verse 3 | Memories of the master, then the two alone | training room, now | |
| Chorus 2 | The raid, the reveal, back to back | warehouse | guns and swords |
| Bridge, break | The master, two against one | rooftop | the boss |
| Last chorus, outro | `K.O.`, tea at dawn, the evidence | rooftop at dawn | the last blow |

- **Status:** captions and shot list done. Shots 1 and 13–24 generated, 13–24 rough-cut with their effects. 13–24 get re-cut faster, with inserts. Next: the master, the costumes, the case and the places in Midjourney, then shots 1–12. Prompts in [`prompts.md`](prompts.md), shots in [`shotlist.md`](shotlist.md)
- **Song:** Steel in Bloom, the same-school duel take ([Suno](https://suno.com/s/GAqifIu57ILXIPND)), 3:38. Lyric in [`lyrics.md`](lyrics.md#steel-in-bloom). Captions: [`captions/en.vtt`](captions/en.vtt) (lyrics), [`captions/ja.vtt`](captions/ja.vtt)
- **Song file:** `audio/song.wav` (not committed), 218.4s
- **Clips:** `clips/` (not committed), named by shot number (`13.mp4`, `13-2.mp4`).
- **Setting:** a near-future city like Ghost in the Shell, under a Shogunate: an agency HQ, a harbour, an elevated highway, a warehouse, a tower rooftop. The footbridge with its red lanterns and the tea stall are the only Japanese places, and the only scenes in the old clothes. Everywhere else is modern clothes, a new costume each scene, and guns as well as swords. Every place is used once. Anyone but the three leads is used once and thrown away.
- **Sound:** J-rock with Japanese instruments, a high-tone female vocal, a metal edge
- **Tools:** Midjourney V8.2 for reference plates only. Vidu Q3 Cinematic for the fight and wide shots. Vidu Q4 for face close-ups. Final Cut Pro and Motion for the edit

## Why every shot is Reference to Video

Two fixed characters in a few fixed places is the case [DESIGN.md](../DESIGN.md#pick-the-tool-by-how-many-references-a-shot-needs) sends to multi-reference. Midjourney → Vidu image-to-video redraws her face and clothes in every still.

Q4 holds a face and loses a fight: the wide shots look composited, and the motion is wrong. Q3 Cinematic, at 8s and one action, moves well and puts the women in the same light as the bridge. A 16s multi-shot broke twice, so the fight is separate 8s clips. Neither video model keeps the Midjourney texture. The grade in Final Cut Pro is what makes a Q4 close-up sit next to a Q3 wide.

Midjourney's job is the plates both models read: each woman front, back and face, the places, and the two blades.

## Order of work

1. Reference plates (Midjourney)
2. Vidu test. Done. Q3 Cinematic for the fight and wides, Q4 for face close-ups
3. Final Cut Pro basics on 0005 (iMovie → File → Send Movie to Final Cut Pro)
4. Timing sheet. Done: [`captions/en.vtt`](captions/en.vtt)
5. Shot list. Done: [`shotlist.md`](shotlist.md)
6. Generate, in song order
7. Edit in layers: beat-cut rough edit, retiming, masks and type, grade, overlays

## Techniques

Every well-known one goes in, and every cut gets at least one. The verses cut a bar at a time, the choruses every beat or two, and each chorus goes one step further than the last. The shot and the time each one lands on are in [`shotlist.md`](shotlist.md). The Where column here is the first pass.

Made in the generation, so they go in the Vidu prompt:

| # | Technique | Where |
| --- | --- | --- |
| G1 | Match cut: her pouring tea, then her drawing the blade, same hand, same framing | Verse 1 → chorus 1, reversed in the last chorus |
| G2 | Whip pan between the two women | Break |
| G3 | Orbit around the locked blades, bullet time | Break |
| G4 | Dropped. A dolly zoom, then the rain stopping in mid-air: Vidu did neither. Shot 15 is slowed to a stop in the edit (F2) | Pre-chorus |
| G5 | FPV dive down the towers, and in reverse up into the sky | Intro, outro |
| G6 | Rack focus from rain on the lens to her eye, built in the edit | Intro |
| G7 | Silhouette against the hologram, backlit: the master's entrance | Bridge |
| G8 | Fake one-take, cut in the edit from separate 8s clips. A generated 16s multi-shot broke twice | Break |
| G9 | Dropped. Vanish and reappear behind the other: no roll did it | |

Made in Final Cut Pro:

| # | Technique | Where |
| --- | --- | --- |
| F1 | Beat-cut editing: verses 3–5s per cut, choruses 1–2s (Beat Detection) | Everywhere |
| F2 | Speed ramp: fast into the swing, slow on the hit (Retime, Optical Flow) | Everywhere |
| F3 | Freeze frame held before the drop, and under each intro card | Verses 1 and 2, pre-chorus |
| F4 | White flash, and a 1–2 frame negative impact frame | Every "Draw!" |
| F5 | Crop punch-in on the beat, as a hard cut. A punch-in and back out on a clip that already pushes in reads as a bad cut | Chorus 1 re-edit |
| F6 | Crash zoom | Chorus 2, bridge |
| F7 | Camera shake on impact | Every blade contact |
| F8 | Aspect change: 16:9 closes to a 2.39:1 letterbox for the pre-chorus, and 4:3 for the memories | Pre-chorus 1, verse 3 |
| F9 | Split screen: the singer at the scope, and what the scope sees | Verse 2 |
| F10 | Manga-panel layout: three or four panels of one moment | Verse 3 |
| F11 | Colour isolation: everything grey except red. Also the master's one red frame | Chorus 1, verse 3, chorus 2 |
| F12 | Big type behind the subject (Magnetic Mask) | "Draw! Steel in bloom" |
| F13 | Subject-masked wipe: she crosses the lens and reveals the next shot | Chorus 2 |
| F14 | Video inside the letters | Title card |
| F15 | Double exposure: the rival's face over the harbour | Verse 2 |
| F16 | Afterimage trails on a fast swing | Chorus 1 clash, chorus 2 |
| F17 | Choppy frame rate, anime on twos, for a few beats | Bridge "Left, right, low, high" |
| F18 | Strobe | Chorus 1 hit, the chase, the break |
| F19 | RGB split and glitch | Intro, break → last chorus |
| F20 | Overlays in blend modes: rain, sparks, petals, light leaks, film burn, grain | From chorus 1 |
| F21 | Bloom and glow on lanterns, blade contact and the master's aura | Night shots |
| F22 | Blade glint: a light running along the edge. Only on the still blade plates. Vidu's blades already catch the lantern light, and a glint on top of a clip is too much | The VS screen |
| F23 | One grade over everything: LUT plus Match Color | Everywhere |
| F24 | Vignette and lens blur to pull the eye | Close-ups |
| F25 | Ink-brush wipe, the one wa-style transition, into the bridge | Verse 2 → pre-chorus |
| F26 | Glitch, zoom-blur and light-leak transitions, built-in and Modular | Section changes |

Made in Motion and sent to Final Cut Pro as templates:

| # | Technique | Where |
| --- | --- | --- |
| M1 | Lyrics revealed one character at a time (Sequence Text) | Verses |
| M2 | Kinetic type slam, landing a few frames before the beat so the hit is on it | Chorus hooks |
| M3 | Character intro cards in an anime-opening style, with a freeze | Verses 1 and 2, one per woman |
| M4 | HUD and AR overlay: the agency's hologram, the scope, the moves | Verses 1 and 2, bridge |
| M5 | Glitch type that tears and re-forms | Last chorus |
| M6 | Glowing outline traced around the two | Last chorus |
| M7 | Song title card and end card | Intro, outro |
| M8 | The fight-game layer: VS screen, health bars, `ROUND 1` and `ROUND 2`, a boss health bar, arrow inputs and a combo counter, `K.O.` | Intro, pre-chorus, chorus 2, bridge, last chorus |

The full lyric still ships as CC tracks. On-screen type is design: the hooks and a few lines, not every line.
