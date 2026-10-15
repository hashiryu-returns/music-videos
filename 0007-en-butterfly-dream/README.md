# EN — working title "Butterfly Dream"

An alluring woman performs illusions for the viewer, and every door she opens is another world: a Japanese room in a kimono, a Chinese palace in a red qipao, a golden theatre, a European palace in a white gown. Places and costumes change all the time, and the change is the trick. The song is a slow wa-rock ballad, sung in English. The lyric is in [`lyrics.md`](lyrics.md#butterfly-dream), with the Suno settings.

- **Status:** lyric and Suno settings written. Next: the song in Suno, then the first test, then the plates.
- **Setting:** worlds behind doors, all lit by candles, lanterns and chandeliers: an old Japanese room, a Chinese palace, a golden theatre, a European palace. No modern city.
- **Sound:** a slow wa-rock ballad, about 96 BPM in D minor: the koto and the shakuhachi up front the whole song, the band and taiko under them in the choruses, a female vocal with a folk singer's vibrato

## The MV

She is a butterfly and a magician. Each section is a new world and a new costume, and the change happens on her: a spin, a sleeve across the lens, a fan closing, a door. The viewer never sees where one world ends. The chorus names the colours, red, jade, gold and white, one a world, and the last chorus runs them all together.

| Section | World | Costume | What she does |
| --- | --- | --- | --- |
| Intro | a dark empty stage, one candle | | a butterfly of light lands on the flame, and she is standing where it was |
| Verse 1 | a Japanese room of paper screens, lanterns | a red kimono | she dances with a fan; snow falls from her open hand |
| Pre-chorus | the same room | | she turns, counts three on her fingers, and is gone in smoke |
| Chorus 1 | doors opening one after another | a new costume on each line | red, jade, gold, white: one door a line, she steps through each |
| Verse 2 | a Chinese palace hall, dragon lanterns, incense | a red qipao, a jade hairpin | smoke from her sleeves unfolds into butterflies |
| Pre-chorus | a corridor of mirrors | | every reflection wears a different costume |
| Chorus 2 | a golden theatre, the stage and the empty seats | a gold gown | she bows, and the curtain falls through her; cards thrown in the air become butterflies |
| Interlude | behind paper screens | | shadow play under the shakuhachi: her silhouette becomes a butterfly, then a dancer in another costume |
| Bridge | a European palace, chandeliers, a hall of mirrors | a white lace gown | she waltzes alone; her reflections dance a beat behind her |
| Last chorus | every world in turn | every costume | quick cuts through all the doors, the wings opening in all their colours |
| Outro | the empty theatre | | the candle out, a little butterfly dust on the stage |

**How the magic is made.** The tricks are cuts, not generated sleight of hand: a small hand action comes out robotic in Vidu and a prop someone handles breaks ([DESIGN.md](../DESIGN.md#vidu)). Each clip has one move, a turn, a step, a fan opening. Vanishing, a costume change on a spin and a reflection that moves on its own are built in the edit with match cuts, masks and speed ramps. Butterflies, smoke and petals are overlays.

**The cast.** One woman, so one face plate, with a costume plate per section. The plates are neutral on purpose, as on 0006: the allure goes into each shot's prompt, not the plate. The picture is anime, flat cel shading, drawn in Midjourney Niji: Vidu holds a flat anime face better than a painted one, and nothing pulls it toward 3D. Hands, handled props, counts and full-body dance stay weak, so a shot shows the upper body, one move, and the props in words.

**First test, before the plates.** One face plate and one costume, then 2–3 Vidu rolls: a fan dance from the waist up, a spin, the sleeves swinging. If the sleeves and the spin hold, the rest of the costumes get made.

## Practice

What this one practises in Final Cut Pro is the opposite of [`0006`](../0006-en-steel-in-bloom/README.md#practice). 0006 is fast cutting, and the cut is the hit. Here the cut is hidden: a slow song, long takes, and the viewer never sees where one world ends.

- Match cuts on a movement: the cut lands inside a spin, a sleeve across the lens or a fan closing, so the move carries over into the next world
- Masks and compositing: Magnetic Mask to lift her out of a clip, duplicated and flipped layers for the mirrors, a copy a few frames late for a reflection that moves on its own
- Overlays in blend modes as the main effect, not an extra: butterflies, smoke, snow, butterfly dust
- A colour grade per world, red, jade, gold and white, with the Color Board and Curves, and the grade carried across the match cut
- Gentle speed ramps on the dance accents, slowing into a pose rather than stopping on a hit
- Dissolves and light leaks between worlds, where 0006 is almost all hard cuts

## Techniques to try

0006 uses none of these, or only in passing (a film burn, one fade to black). The shot each lands on gets fixed with the shot list.

| # | Technique | Where |
| --- | --- | --- |
| T1 | Match cut on a spin: she turns in one world and comes out of the turn in the next costume | Chorus 1, last chorus |
| T2 | Wipe on a sleeve or a fan that crosses the lens | Verse 1, chorus 1 |
| T3 | Vanish in smoke: the empty room under her, a smoke overlay, a dissolve under the smoke | Pre-chorus 1 |
| T4 | Appear where a butterfly of light was: a light overlay grows and fades as she dissolves in | Intro |
| T5 | Mirrors: one clip duplicated, flipped and masked into each frame, each in another costume | Pre-chorus 2 |
| T6 | A reflection a beat behind: the same clip copied, flipped and offset by a few frames | Bridge |
| T7 | Shadow play: her silhouette keyed onto a lit paper screen, a butterfly overlay crossing it | Interlude |
| T8 | The curtain falling through her: a curtain overlay with her masked in front of it | Chorus 2 |
| T9 | Butterflies, smoke and snow as blend-mode overlays, scaled and moved by keyframes | Everywhere |
| T10 | A grade per world: warm red, jade, gold, cold white | Every section |
| T11 | Slow speed ramps into a pose on the accents | The dance shots |
| T12 | Light leaks and cross dissolves between worlds | Section changes |