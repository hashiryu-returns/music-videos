# EN — Steel in Bloom

A spy story in a near-future city, with no message to it. The point is two cool characters and a video that never sits still. Excitement first, story second, the lyric only where it helps. The first ten seconds have to hold a viewer.

This one is a study piece in making a fight look fast. The edit alone can't: cutting still footage faster reads busy, not dynamic. Each clip has to move on its own, the camera or the body, and the cutting, the speed, the type and the effects build on that. A fight-game layer (a pixel select screen, a VS screen, rounds, a boss health bar, `K.O.`) ties the graphics together.

## Story

The two women trained under the same master and were friends. Now the singer is an agent who works international crime. The rival is mixed up in smuggling zunda mochi, banned by the Shogunate, and the singer tries to stop her: she sends her an old photo of the two of them with their master, then ambushes her on the bridge, chases her down the highway and raids the warehouse. In the warehouse the rival shows her badge: she is undercover on the same case. The one behind the smuggling is their old master. She wakes to the Surge of Murderous Intent: a red aura, red eyes, and she is strong, but the two of them beat her together. At dawn they drink tea on the roof and eat the evidence.

The select screen in the intro labels the rival `SMUGGLER`, and the reveal strikes it out for `UNDERCOVER`. In the memory of their training, the master's eye flashes red for one frame.

| Section | Story | Place | Fight |
| --- | --- | --- | --- |
| Intro | Flash-forwards, the title, the city, the select screen | the towers | |
| Verse 1 | The case at the agency, cut against the rival alone at the tea stall, still pouring two cups. The singer's message, an old photo, lands over her tea | HQ, the stall | |
| Verse 2 | The deal at the harbour, watched through a scope | harbour | |
| Pre-chorus, chorus 1 | The ambush and the duel | the bridge, the old clothes | swords |
| Instrumental | The chase | highway | gun against sword |
| Verse 3 | Memories of the master, then the two alone | old dojo, now | |
| Chorus 2 | The raid, the reveal, back to back | warehouse | guns and swords |
| Bridge, break | The master, two against one | rooftop | the boss |
| Last chorus, outro | `K.O.`, tea at dawn, the evidence | rooftop at dawn | the last blow |

- **Status:** the first half, 0:00–1:44, is generated and cut, with its type, HUD and effects. One roll is out for 23a and 24a. Every plate is made. Next: the prompts and the Vidu clips for verse 3 on, 26–53. Prompts in [`prompts.md`](prompts.md), shots in [`shotlist.md`](shotlist.md)
- **Song:** Steel in Bloom, the same-school duel take ([Suno](https://suno.com/s/GAqifIu57ILXIPND)), 3:38. Lyric in [`lyrics.md`](lyrics.md#steel-in-bloom). Captions: [`captions/en.vtt`](captions/en.vtt) (lyrics), [`captions/ja.vtt`](captions/ja.vtt)
- **Song file:** `audio/song.wav` (not committed), 218.4s
- **Clips:** `clips/` (not committed), named by shot number (`13.mp4`, `13-2.mp4`).
- **Setting:** a near-future city like Ghost in the Shell, under a Shogunate: an agency HQ, a harbour, an elevated highway, a warehouse, a tower rooftop. The footbridge with its red lanterns and the tea stall are the only scenes in the old clothes, and with the dojo and the singer's tatami apartment the Japanese places. Everywhere else is modern clothes, a new costume each scene, and guns as well as swords. Every place is used once, except the tea stall, which comes back closed at night in 29. Anyone but the three leads is used once and thrown away.
- **Sound:** J-rock with Japanese instruments, a high-tone female vocal, a metal edge
- **Tools:** Midjourney V8.2 for reference plates only. Vidu Q4 for almost every shot, Q3 Cinematic only where Q4 is known to fail. Final Cut Pro for the edit and the type; the fight-game graphics are drawn by `_tools/image/fight_hud.py` and `pixel_select.py`. No Motion

## Why every shot is Reference to Video

Two fixed characters in a few fixed places is the case [DESIGN.md](../DESIGN.md#pick-the-tool-by-how-many-references-a-shot-needs) sends to multi-reference. Midjourney → Vidu image-to-video redraws her face and clothes in every still.

Q4 keeps the faces, and Q3 Cinematic changes them, so Q4 does almost every shot. Q4 loses a fight when several people do a complex move in one take, so the fight is cut one woman a shot, one move each, the way the reference MV cuts one; cut that way, Q4 carried the charges, the draw, the clash and the chase. Q3 Cinematic only for a run straight at the lens and the dojo, where Q4 goes flat 2D. Neither model keeps the Midjourney texture, and the grade makes the clips match. The lessons are in [DESIGN.md](../DESIGN.md#vidu).

Midjourney's job is the plates both models read: each woman front, back and face, the places, and the two blades.

## Order of work

1. Reference plates (Midjourney)
2. Vidu test. Done. Q4 first, one woman a cut
3. Final Cut Pro basics on 0005 (iMovie → File → Send Movie to Final Cut Pro)
4. Timing sheet. Done: [`captions/en.vtt`](captions/en.vtt)
5. Shot list. Done: [`shotlist.md`](shotlist.md)
6. Generate, in song order
7. Edit in layers: beat-cut rough edit, retiming, masks and type, grade, overlays

## Practice

What this one practises in Final Cut Pro is fast cutting: the edit makes the speed and the hits on clips that already move.

- Cutting on the beat, a bar in the verses and a beat or two in the fights, each cut checked by ear
- Retiming: slowing to a stop into a freeze, and running clips at 150–200% to fit more of each into the chase
- Hit effects on a frame: white flash, negative frames, a strobe, Position keyframes for the shake, a 2-frame hit stop (at 100% only: in sped-up footage it reads as the video stalling)
- Titles animated by keyframes: the slams, the intro cards, the Typewriter lower thirds, type behind her with a Magnetic Mask, video inside the letters
- Split screens and screens inside the picture, built from compound clips moved by Position alone
- Graphics drawn by a script and laid over the cut as ProRes with alpha: the select screen, the VS screen, the health bars, the bonus stage

[`0007`](../0007-en-butterfly-dream/README.md#practice) practises the other half: hiding the cut.

## Techniques

Every well-known one goes in, and every cut gets at least one. The verses cut a bar at a time, the choruses every beat or two, and each chorus goes one step further than the last. The shot and the time each one lands on are in [`shotlist.md`](shotlist.md). Status is for 0:00–1:44, the half that is cut.

Made in the generation, so they go in the Vidu prompt:

| # | Technique | Where | Status |
| --- | --- | --- | --- |
| G1 | Match cut: her pouring tea, then her drawing the blade, same hand, same framing | Verse 1 → chorus 1, reversed in the last chorus | 7 → 17 done; 49 to come |
| G2 | Whip pan between the two women | Break | To come |
| G3 | Orbit around the locked blades, bullet time | Break | To come |
| G4 | Dolly zoom, then the rain stopping in mid-air | | Dropped: Vidu did neither. 15 is slowed to a stop in the edit (F2) |
| G5 | FPV dive down the towers, and in reverse up into the sky | Intro, outro | 3 done; 51 to come |
| G6 | Rack focus from rain on the lens to her eye | Intro | Done, built in the edit as a blur on 1 |
| G7 | Silhouette against the hologram, backlit: the master's entrance | Bridge | To come |
| G8 | Fake one-take, cut in the edit from separate clips. A generated 16s multi-shot broke twice | Break | To come |
| G9 | Vanish and reappear behind the other | | Dropped: no roll did it |

Made in Final Cut Pro:

| # | Technique | Where | Status |
| --- | --- | --- | --- |
| F1 | Beat-cut editing: a bar a cut in the verses, a beat or two in the fights | Everywhere | Done to 1:44, by ear and the caption bars |
| F2 | Speed ramp and retiming | Everywhere | 15 slowed to a stop, 24c at 200%, the chase at 150–200% |
| F3 | Freeze frame held before the drop, and under each intro card | Verses 1 and 2, pre-chorus | Done: the two cards, 16 |
| F4 | White flash, and a 1–2 frame negative impact frame | Every "Draw!" and hit | Done: 17, 9b, 22, 24b, 25e |
| F5 | Crop punch-in on the beat, as a hard cut, and a Ken Burns push on a wide clip. A punch-in and back out on a clip that already pushes in reads as a bad cut | Chorus 1 | Done: 23, 24 |
| F6 | Crash zoom | Chorus 2, bridge | To come |
| F7 | Camera shake on impact: Position keyframes, Scale 104% | Every hit | Done: 4, 24b, 25e |
| F8 | Aspect change: a 2.39:1 letterbox closing in, and 4:3 for the memories | Pre-chorus, memories | Done: 15, 23b; 27 to come |
| F9 | Split screen | Verses 1 and 2 | Done: 8, the scope in 10 |
| F10 | Manga-panel layout: three or four panels of one moment | Verse 3 | To come |
| F11 | Colour isolation: everything grey except one colour | Chorus 1, verse 3, chorus 2 | Done: 19, the freezes under the cards |
| F12 | Big type behind the subject (Magnetic Mask) | "Draw! Steel in bloom" | Done: 18 |
| F13 | Subject-masked wipe: she crosses the lens and reveals the next shot | Chorus 2 | To come |
| F14 | Video inside the letters | Title card | Done: 2 |
| F15 | Double exposure: the rival's face over the harbour | | Not used: verse 2 has the scope split instead |
| F16 | Afterimage trails on a fast swing | Chorus 1 clash, chorus 2 | 22 done |
| F17 | Choppy frame rate, anime on twos, for a few beats | Bridge "Left, right, low, high" | To come |
| F18 | Strobe | Hits, the break | Done: 24b, 25e |
| F19 | RGB split and glitch | Intro, hits, break → last chorus | Done: 4, 24b |
| F20 | Overlays in blend modes: rain, sparks, petals, light leaks, film burn, grain | From chorus 1 | The photo in 8, the memories; the rest to come |
| F21 | Bloom and glow | Night shots, hits | Done: 8, 18, 24b |
| F22 | Blade glint: a light running along the edge, on the still blade plates only | The VS screen | Not used |
| F23 | One grade over everything | | Not used: a darkening grade made the night clips muddy, and one setting can't even out clips this different. The clips stay as generated |
| F24 | Vignette and lens blur to pull the eye | Close-ups | Done: i2-2 |
| F25 | Ink-brush wipe into the bridge | | Not used: verse 2 ends on a freeze and a hard cut |
| F26 | Transitions at section changes | Section changes | So far hard cuts, a flash, and a fade to black out of 24d. None of the built-in ones |
| F27 | Hit stop: the hit frame held 2 frames (Retime → Hold). Never in sped-up footage | Hits at 100% | Done: 20c, 24b |
| F28 | Hologram: Colorize, Distort into a trapezoid, Bad TV, opening from a line | Verse 1 | Done: the photo in 8 |
| F29 | CRT on and off: Scale Y from a line, then down to a point | Intro, chorus 2 | 4 done; 34 to come |

Type and graphics, made without Motion: Final Cut Pro titles with keyframes, or drawn by the scripts in `_tools/image/` and laid over the cut:

| # | Technique | Where | Made with | Status |
| --- | --- | --- | --- | --- |
| M1 | Text typed one character at a time | Lower thirds | Typewriter title | Done: 3, 25a |
| M2 | Kinetic type slam, landing a few frames before the beat so the hit is on it | Chorus hooks | a title, Scale and Opacity keyframes | Done: 18, `ONLY` / `ONE` in 20 |
| M3 | Character intro cards in an anime-opening style, with a freeze | Verses 1 and 2, one per woman | titles over a freeze | Done |
| M4 | HUD and AR overlay | Verses 1 and 2, bridge | titles and generators | Done: the altitude in 3, the file in 6, the scope in 10; the arrows in 37 to come |
| M5 | Glitch type that tears and re-forms | Last chorus | a title with the built-in glitch effects | To come |
| M6 | Glowing outline traced around the two | Last chorus | a mask and a glow, or dropped | To come |
| M7 | Song title card and end card | Intro, outro | titles | Title done (2); end card to come |
| M8 | The fight-game layer | Intro to the last chorus | `fight_hud.py`, `pixel_select.py`: PNGs and ProRes 4444 with alpha | Done: the select screen, the VS screen, `ROUND 1`, the health bars, the bonus stage. To come: `ROUND 2`, the boss bar, the inputs, `K.O.` |

The full lyric ships as YouTube caption tracks, `captions/en.vtt` and `captions/ja.vtt`, not burned in. On-screen type is design: the hooks and a few lines, not every line.
