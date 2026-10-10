# EN — working title "Two Blades"

A sword fight between two women, with no message to it. The point is two cool characters and a fight worth watching. The first half shows their everyday lives; the second half is all fight.

This one is a study piece. The effects come first and the story makes room for them: if a shot wants the world to stop, the story gets a moment where it stops.

- **Status:** plates, captions and shot list done. Shots 13–24 (0:56–1:32) generated and edited, all but the grade. Next: shots 1–12. Prompts in [`prompts.md`](prompts.md), shots in [`shotlist.md`](shotlist.md)
- **Song:** Steel in Bloom, the same-school duel take ([Suno](https://suno.com/s/GAqifIu57ILXIPND)), 3:38. Lyric in [`lyrics.md`](lyrics.md#steel-in-bloom). Captions: [`captions/en.vtt`](captions/en.vtt) (lyrics), [`captions/ja.vtt`](captions/ja.vtt)
- **Song file:** `audio/song.wav` (not committed), 218.4s
- **Clips:** `clips/` (not committed), named by shot number (`13.mp4`, `13-2.mp4`). The model tests are in `clips/tests/`, named model, length, scene, roll (`q3c-08s-leap-2.mp4`)
- **Setting:** a near-future city like Ghost in the Shell: tea stalls under elevated highways, hologram lanterns, a footbridge over a canal in neon rain. The bakumatsu source gives texture only: no names, eras, places or Japanese terms in the lyric, the same rule as [0004](../0004-en-not-alone/README.md)
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

Every well-known one goes in. Each gets a home in the song instead of being stacked everywhere: the verses stay quiet, the first line of each chorus gets the strongest hit, and each chorus goes one step further than the last. The shot and the time each one lands on are in [`shotlist.md`](shotlist.md). The Where column here is the first pass.

Made in the generation, so they go in the Vidu prompt:

| # | Technique | Where |
| --- | --- | --- |
| G1 | Match cut: her pouring tea, then her drawing the blade, same hand, same framing | Verse 1 → Chorus 1 |
| G2 | Whip pan between the two women | Verse 3 |
| G3 | Orbit around the locked blades, bullet time | Chorus 2 |
| G4 | Dropped. A dolly zoom, then the rain stopping in mid-air: Vidu did neither. Shot 15 is slowed to a stop in the edit (F2) | Pre-chorus |
| G5 | FPV dive down from the towers onto the bridge | Chorus 1 opening |
| G6 | Rack focus from rain on the lens to her face | Verse 2 |
| G7 | Silhouette against a neon sign, backlit | Bridge |
| G8 | Fake one-take, cut in the edit from separate 8s clips. A generated 16s multi-shot broke twice | Interlude (shakuhachi) |
| G9 | Dropped. Vanish and reappear behind the other: no roll did it | |

Made in Final Cut Pro:

| # | Technique | Where |
| --- | --- | --- |
| F1 | Beat-cut editing: verses 3–5s per cut, choruses 1–2s (Beat Detection) | Everywhere |
| F2 | Speed ramp: fast into the swing, slow on the hit (Retime, Smooth Slo-Mo) | Verse 3 on |
| F3 | Freeze frame held before the drop | "Then the street goes still" |
| F4 | White flash, and a 1–2 frame negative impact frame | Every "Draw!" |
| F5 | Zoom punch on the downbeat | Chorus first beats |
| F6 | Crash zoom | Bridge |
| F7 | Camera shake on impact | Every blade contact |
| F8 | Aspect change: 16:9 closes to a 2.39:1 letterbox, and opens again on the cut to the chorus | Pre-chorus 1 |
| F9 | Split screen: both mornings side by side | Verse 1 |
| F10 | Manga-panel layout: three or four panels of one exchange | Verse 3 |
| F11 | Colour isolation: everything grey except red | "Red against the rain" |
| F12 | Big type behind the subject (Magnetic Mask) | "Draw! Steel in bloom" |
| F13 | Subject-masked wipe: she crosses the lens and reveals the next shot | Chorus 2 |
| F14 | Video inside the letters | Title card |
| F15 | Double exposure: one face over the other's city | Verse 2 |
| F16 | Afterimage trails on a fast swing | Chorus 1 clash, bridge |
| F17 | Choppy frame rate, anime on twos, for a few beats | Bridge "Left, right, low, high" |
| F18 | Strobe | Taiko breakdown |
| F19 | RGB split and glitch | Bridge → last chorus |
| F20 | Overlays in blend modes: rain, sparks, petals, light leaks, film burn, grain | Second half |
| F21 | Bloom and glow on lanterns and blade contact | Night shots |
| F22 | Blade glint: a light running along the edge. Only on the still blade plates. Vidu's blades already catch the lantern light, and a glint on top of a clip is too much | Shots 4 and 53 |
| F23 | One grade over everything: LUT plus Match Color | Everywhere |
| F24 | Vignette and lens blur to pull the eye | Close-ups |
| F25 | Ink-brush wipe, the one wa-style transition | Verse 2 → pre-chorus |
| F26 | Glitch, zoom-blur and light-leak transitions, built-in and Modular | Section changes |

Made in Motion and sent to Final Cut Pro as templates:

| # | Technique | Where |
| --- | --- | --- |
| M1 | Lyrics revealed one character at a time (Sequence Text) | Verses |
| M2 | Kinetic type slam, landing a few frames before the beat so the hit is on it | Chorus hooks |
| M3 | Character intro cards in an anime-opening style, with a freeze | Verse 1, one per woman |
| M4 | HUD and AR overlay calling the moves | Bridge "Left, right, low, high" |
| M5 | Glitch type that tears and re-forms | Last chorus |
| M6 | Glowing outline traced around her | Last chorus |
| M7 | Song title card and end card | Intro, outro |

The full lyric still ships as CC tracks. On-screen type is design: the hooks and a few lines, not every line.
