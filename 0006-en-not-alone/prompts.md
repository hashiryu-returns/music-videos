# 0006 prompts

Shot list and timing: [`README.md`](README.md#shot-list). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

## Midjourney

Settings panel, for everything:

- Version Niji 7
- Aspect 16:9
- Stylization 150
- Weirdness 0
- Variety: 15 for the style sheets, 0 for the scenes
- Speed Fast

### Style sheets

No Style Reference. Roll each, pick one, save as `stills/style-sheet-a.png` and `stills/style-sheet-b.png`.

Reject crosshatching, sepia, painted backgrounds (no outlines on rocks and walls), blue shadows, black bars.

**A**

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium full shot, high angle looking down, her whole body visible from hood to boots, an adult woman adventurer in her late twenties in a deep red hooded cloak and leather bracers, reaching one gloved hand toward the camera, her body turned three quarters, sharp confident gaze up at the viewer, realistic anime face, strong eyebrows, sharp eyes with a heavy black upper lash line, glossy red lips, loose pale limestone rocks and tufts of grass around her feet, every rock outlined in black ink, bright midday sunlight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark
```

**B**

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle wide shot, a woman knight in plain steel armour with a red scarf walking between two towering ruined walls of pale cracked concrete and stacked stone blocks with mortar lines, rust streaks and chipped edges, green weeds and grass growing from the cracks, rubble at the base of the walls, warm grey stone, small in the frame, bright midday sunlight, flat clear blue sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark
```

### Scene stills

One style sheet per scene, never both: each scene says `sheet A` (faces) or `sheet B` (everything else). Drag only that sheet into Style Reference. Paste the prompt as is; it already ends in `--sw 250`. Check `sw 250` shows under the result.

Sheet A cropped too tight: change to `--sw 200`.

Dark scene coming back sunny: swap `vivid saturated colours` for `muted dark colours` and add `blue sky, sun, sunlight` to `--no`. #1 and #2 already have it.

## Vidu

Image to Video, Q2, 1080p, Cinematic, Amount 1. Duration is on each scene's Vidu line. Trim to the scene's `use` length in the editor.

Up to 5s is one price and 6–8s costs double, so every clip uses either 5.0s or less (generate 5s) or 6.0s or more (generate 6–8s). Nothing in between.

## Scenes

### Intro

**#1** · 0:00.0–0:08.0 · use 8.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from a ruined watchtower on a hillside, huge cracked stone blocks and rubble in the foreground with weeds in the cracks, below it a valley kingdom in the gloom before a storm, dark green fields in deep shadow, the whole sky covered by heavy black storm clouds down to the horizon, dim grey light, a small white castle on a hill in the far distance --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight --sw 250
```

Accept: dark storm sky over a dim valley, inked stone in front, castle visible.

Reject: blue sky or a sun; valley became a sea; black bars, painted background.

Vidu · 8s

```text
The black clouds roll slowly across the sky and the camera drifts forward over the valley.
```

Accept: clouds move and the camera drifts forward.

Reject: stone or castle melts; a cut to another shot, the style turning 3D.

**#2** · 0:08.0–0:14.0 · use 6.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from behind, eye level, a young woman in a dark blue travelling cloak standing alone on a castle battlement, small in the frame, her cloak and long silver hair blowing to the left, the whole sky covered by heavy black storm clouds, dim grey light, stone towers and a sleeping town below in deep shadow --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight --sw 250
```

Accept: small cloaked figure from behind on a battlement, grey storm clouds, town below.

Reject: black void sky with no clouds; she fills the frame; black bars, painted background.

Vidu · 6s

```text
Her cloak and hair whip in the strong wind as she steps up to the edge of the wall.
```

Accept: cloak and hair blow hard.

Reject: she turns to camera or falls off the wall; a cut to another shot, the style turning 3D.

**#3** · 0:14.0–0:18.7 · use 4.7s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium close-up, eye level, three quarter view, a woman soldier with short copper red hair in dented steel armour standing in a town square under a darkened sky, looking just past the camera with a sharp determined gaze, townspeople out of focus behind her, cold grey light, realistic anime face, smooth clean skin, strong eyebrows, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: sheet A face at eye level, armour, town and dark sky behind.

Reject: chin-up nostril view; face not like sheet A; black bars, painted background.

Vidu · 5s

```text
She slowly tilts her head back and looks up at the dark sky, her eyes narrowing, her hair stirring in the wind. Her hands stay down.
```

Accept: she looks up at the sky.

Reject: a hand comes up to her face or hair; a cut to another shot, the style turning 3D.

### Verse 1

**#4** · 0:18.7–0:23.7 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, an old man with a long white beard and a deep green robe kneeling in a candlelit stone chamber, lifting the lid of a small carved wooden chest, warm golden glow from inside the chest lighting his face from below, shelves of old books in shadow behind him, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: old bearded man lit gold from the chest, dark chamber.

Reject: young face; no glow from the chest; black bars, painted background.

Vidu · 5s

```text
He slowly raises the lid of the chest and his beard stirs as he leans in.
```

Accept: the lid rises.

Reject: chest or lid changes shape; a cut to another shot, the style turning 3D.

**#5** · 0:23.7–0:28.4 · use 4.7s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme close-up, two young open hands in fingerless leather gloves cupped together, holding a small glowing orb of white gold light, tiny sparks in the air, soft dark background --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: two cupped hands holding a glowing orb.

Reject: a mess of fingers; black bars, painted background.

Vidu · 5s

```text
Her fingers slowly close around the glowing orb and she draws it toward her chest.
```

Accept: the hands close around the orb.

Reject: orb vanishes or splits; a cut to another shot, the style turning 3D.

**#6** · 0:28.4–0:33.1 · use 4.7s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle medium wide shot inside a dark cave, a woman paladin with a long black braid in white and gold armour holding up a burning torch, facing a huge ancient stone tablet carved with glowing runes, torchlight on wet rock walls --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: paladin with a torch facing a carved glowing tablet in a dark cave.

Reject: no torch flame; black bars, painted background.

Vidu · 5s

```text
The torch flame flickers and she raises it higher toward the carved tablet.
```

Accept: the flame flickers and the torch rises.

Reject: a second torch appears; a cut to another shot, the style turning 3D.

### Verse 2

**#7** · 0:33.1–0:38.1 · use 5.0s · dragon 1 of 4, emerald

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot inside a vast cavern lair, an emerald green dragon with a long serpentine body coiled around stone pillars, golden eyes glowing in the dark, smoke curling from its nostrils, piles of rubble, green and amber light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: one green serpent dragon coiled in a dark lair.

Reject: extra heads; black bars, painted background.

Vidu · 5s

```text
The dragon lifts its head, opens its jaws in a snarl and smoke pours from its nostrils.
```

Accept: the head lifts and smoke comes out.

Reject: a second head appears or the jaw melts; a cut to another shot, the style turning 3D.

**#8** · 0:38.1–0:42.5 · use 4.4s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, dynamic low angle shot, a young man swordsman with dark brown skin and short black hair in silver armour leaping toward camera through a dark cavern, sword raised over his head in both hands, his left knee forward and both feet off the ground, cape flaring behind him, rocks and embers in the air --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: swordsman mid-leap toward camera, sword overhead.

Reject: standing still; two swords; black bars, painted background.

Vidu · 5s

```text
He brings the sword down hard in a sweeping strike toward the camera.
```

Accept: the sword swings down.

Reject: sword bends or doubles; a cut to another shot, the style turning 3D.

**#9** · 0:42.5–0:46.0 · use 3.5s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, a princess with long golden hair and a torn pale lilac gown kneeling on the stone floor of a dark cave cell, looking up toward a shaft of light from an opening above, hopeful wet eyes, an iron door standing open behind her, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: kneeling princess looking up into a shaft of light.

Reject: standing; face not like sheet A; black bars, painted background.

Vidu · 5s

```text
She rises slowly to her feet, her hair and gown drifting as she looks up into the light.
```

Accept: she gets to her feet.

Reject: she floats instead of standing; a cut to another shot, the style turning 3D.

**#10** · 0:46.0–0:49.4 · use 3.4s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from behind, a princess with long golden hair in a pale lilac gown walking down a red carpet through a grand castle hall, small in the frame, tall stained glass windows, warm lamplight, rows of banners, an empty throne at the far end --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: same princess from behind, small, walking down a red carpet.

Reject: face to camera; not the princess from #9; black bars, painted background.

Vidu · 5s

```text
The camera follows slowly behind her as her gown trails along the carpet.
```

Accept: she walks away and the camera follows.

Reject: she turns around; a cut to another shot, the style turning 3D.

### Chorus 1

**#11** · 0:49.4–0:56.5 · use 7.1s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide aerial view, three tiny adventurers walking along a high grassy ridge at sunrise, a sea of clouds below, a winding river valley and distant snow mountains, long shadows, golden light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: tiny figures on a ridge above a sea of clouds at sunrise.

Reject: not about three figures; bent fisheye horizon; black bars, painted background.

Vidu · 8s

```text
The sea of clouds drifts below and the camera glides slowly along the ridge.
```

Accept: clouds drift and the camera glides.

Reject: figures vanish; a cut to another shot, the style turning 3D.

**#12** · 0:56.5–1:01.5 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, side view, a woman archer with a long dark green ponytail in leather and green cloth standing on a windy cliff edge, drawing a longbow with the string at her cheek, wind pushing her ponytail and cloak, a deep canyon and sunlight behind her, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: side view archer at full draw on a cliff.

Reject: no bow, or a broken bow; black bars, painted background.

Vidu · 5s

```text
She draws the bowstring back to her cheek and releases the arrow.
```

Accept: she draws, and maybe releases.

Reject: bow bends. A clip that only draws is fine; a cut to another shot, the style turning 3D.

**#13** · 1:01.5–1:07.5 · use 6.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle wide shot, a young man mage in a deep purple hooded robe walking through an ancient misty forest, holding a tall staff with a glowing lantern at its tip, giant mossy roots, glowing blue mushrooms, shafts of light through the canopy --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: robed mage with a lantern staff in a misty forest.

Reject: lantern not lit; black bars, painted background.

Vidu · 6s

```text
The mist swirls around him as he walks forward, his robe swaying.
```

Accept: he walks and the mist moves.

Reject: staff bends; a cut to another shot, the style turning 3D.

### Interlude 1

**#14** · 1:07.5–1:12.0 · use 4.5s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, close-up, a young woman bard with short lavender hair and a ribbon headband playing a slender silver flute, eyes closed, flower petals in the wind, warm dusk light, town walls soft in the background, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: bard playing a flute, eyes closed, petals in the air.

Reject: flute held like a recorder; black bars, painted background.

Vidu · 5s

```text
Her fingers move along the flute and the ribbons and petals drift in the breeze.
```

Accept: fingers move and petals drift.

Reject: flute bends or melts into her fingers; a cut to another shot, the style turning 3D.

**#15** · 1:12.0–1:19.0 · use 7.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, low angle, a colossal moss covered stone golem standing guard in front of the gate of a walled town at dusk, glowing amber eyes, arms hanging at its sides, vines across its shoulders, a tiny cloaked figure at its feet for scale, orange sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: huge standing mossy golem at a town gate, tiny figure at its feet.

Reject: golem already kneeling; no small figure for scale; black bars, painted background.

Vidu · 7s

```text
The golem slowly sinks down onto one knee and lowers its head as the glow in its eyes fades.
```

Accept: the golem kneels.

Reject: golem stands up or walks; a cut to another shot, the style turning 3D.

**#16** · 1:19.0–1:26.0 · use 7.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide shot, a ruined desert town of broken towers half buried in sand, a lone woman warrior with a long spear and a hooded sand coloured cloak walking through the ruins, small in the frame, wind blowing sand across, hot hazy sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: small warrior with a spear walking through sand-buried ruins.

Reject: she fills the frame; black bars, painted background.

Vidu · 7s

```text
Sand blows across the ruins as she walks forward, her cloak streaming.
```

Accept: sand blows and she walks.

Reject: spear bends; a cut to another shot, the style turning 3D.

**#17** · 1:26.0–1:30.0 · use 4.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme close-up at the roots of a huge dead tree, two gauntleted hands pulling an ancient engraved silver breastplate up out of the dry earth, dust and soil falling away, a faint blue gleam on the metal --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: gauntleted hands pulling an engraved breastplate out of the earth.

Reject: a whole person visible; black bars, painted background.

Vidu · 5s

```text
The hands lift the breastplate free and soil pours off it.
```

Accept: the breastplate comes free.

Reject: breastplate changes shape; a cut to another shot, the style turning 3D.

**#18** · 1:30.0–1:33.7 · use 3.7s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, heroic low angle full body shot, a woman knight with a high black ponytail in ancient blue and silver armour with an engraved breastplate and a long blue cape, standing in desert ruins, one hand on her sword hilt, the sun behind her --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: full-body knight from a low angle, cape, sun behind.

Reject: not full body; black bars, painted background.

Vidu · 5s

```text
Her cape billows out behind her as she lifts her head.
```

Accept: the cape billows.

Reject: cape turns into wings; a cut to another shot, the style turning 3D.

### Verse 3

**#19** · 1:33.7–1:38.7 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, a young man elf bard with long platinum hair playing a silver harp inside a crystal shrine, glowing pale blue crystals around him, eyes half closed, soft light, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: elf man playing a harp among pale blue crystals.

Reject: harp has no strings; black bars, painted background.

Vidu · 5s

```text
His fingers sweep across the strings and his long hair stirs.
```

Accept: his hands move on the strings.

Reject: hands pass through the harp; a cut to another shot, the style turning 3D.

**#20** · 1:38.7–1:44.9 · use 6.2s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, an old woman sage with long grey hair and a weathered brown robe standing on a rocky mountain peak, raising a gnarled wooden staff to the sky, dark rain clouds gathering above her, wind tearing at her robe --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: old sage on a peak raising a staff under dark clouds.

Reject: staff not raised; black bars, painted background.

Vidu · 7s

```text
She thrusts the staff upward and heavy rain begins to pour from the clouds.
```

Accept: the staff goes up and rain falls.

Reject: staff bends; a cut to another shot, the style turning 3D.

**#21** · 1:44.9–1:49.9 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium full shot, a young woman cleric with short white hair in white and gold robes standing in a sunlit marble temple, raising a glowing amber stone above her head with both hands, beams of sunlight between high columns, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: cleric in a temple holding a glowing stone overhead.

Reject: stone not glowing; black bars, painted background.

Vidu · 5s

```text
She lifts the amber stone higher and her robes and hair rise as if in a strong wind.
```

Accept: robes and hair lift.

Reject: stone splits in two; a cut to another shot, the style turning 3D.

### Chorus 2

**#22** · 1:49.9–1:54.9 · use 5.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, three quarter back view, a woman hero with long auburn hair and a red cape standing on a sea cliff at a stormy shore, holding a teardrop shaped crystal up toward the sky, across a dark strait a black island castle under storm clouds, waves crashing below --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: caped hero from behind on a sea cliff, crystal raised, island castle across the water.

Reject: face to camera; no crystal; black bars, painted background.

Vidu · 5s

```text
Her cape whips in the wind as she thrusts the crystal toward the sky.
```

Accept: the cape whips.

Reject: crystal vanishes; a cut to another shot, the style turning 3D.

**#23** · 1:54.9–2:02.8 · use 7.9s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide landscape, a glowing rainbow bridge arching from a sea cliff across a dark stormy sea to a black island castle, storm clouds beginning to part, shafts of light on the water, waves crashing --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: rainbow bridge from cliff to island castle over a stormy sea.

Reject: no bridge across the sea; black bars, painted background.

Vidu · 8s

```text
The storm clouds part and the waves roll beneath the rainbow bridge.
```

Accept: clouds part and waves move.

Reject: bridge bends or wobbles; a cut to another shot, the style turning 3D.

**#24** · 2:02.8–2:08.8 · use 6.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, high angle wide shot from behind, two small figures, a woman knight in silver armour and a man monk in orange robes, walking across a glowing rainbow bridge toward a black castle on an island, dark sea far below, clouds drifting --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: two small figures from behind walking a glowing bridge to a castle.

Reject: not two figures; black bars, painted background.

Vidu · 6s

```text
The two walk forward along the bridge as the clouds drift past.
```

Accept: they walk forward.

Reject: a third figure appears; a cut to another shot, the style turning 3D.

### Interlude 2

**#25** · 2:08.8–2:14.8 · use 6.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, high angle shot looking down a vast spiral stone staircase descending into darkness inside a black castle, torches on the walls, a lone woman rogue with a short silver bob and a dark hood descending the stairs, small in the frame --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: top-down spiral staircase into darkness, small figure, torches.

Reject: not a spiral staircase; black bars, painted background.

Vidu · 6s

```text
The torch flames flicker as she hurries down the spiral stairs.
```

Accept: she goes down and the flames flicker.

Reject: stairs rotate; a cut to another shot, the style turning 3D.

**#26** · 2:14.8–2:19.3 · use 4.5s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, close-up, an armoured hand pushing open a giant black door carved with dragons, a thin line of violet light spilling through the gap, dust in the air --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: armoured hand on a huge carved black door, violet light in the gap.

Reject: a whole person visible; black bars, painted background.

Vidu · 5s

```text
The giant door swings slowly open and violet light floods through.
```

Accept: the door swings open.

Reject: door bends instead of swinging; a cut to another shot, the style turning 3D.

### Bridge

**#27** · 2:19.3–2:26.0 · use 6.7s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium wide shot, low angle, a tall pale sorcerer king with long black hair and a crown of curved horns seated on an obsidian throne, violet and black robes, extending one open hand toward camera in an offer, a faint smile, a vast dark throne room with violet flames, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: horned sorcerer king on a throne, hand held out to camera.

Reject: hand not reaching toward camera; black bars, painted background.

Vidu · 7s

```text
He leans forward and extends his open hand, his robes rippling.
```

Accept: he leans in with the hand out.

Reject: hand grows extra fingers; a cut to another shot, the style turning 3D.

**#28** · 2:26.0–2:33.2 · use 7.2s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, close-up, a woman hero with a short black bob and a thin scar across one cheek, defiant eyes, holding her sword upright in front of her face, the blade catching violet light, a dark throne room out of focus behind her, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: scarred hero holding her sword upright in front of her face.

Reject: sword not in front of her face; black bars, painted background.

Vidu · 8s

```text
She raises the sword up in front of her face and her eyes narrow.
```

Accept: the sword rises and her eyes narrow.

Reject: sword bends or doubles; a cut to another shot, the style turning 3D.

### Break

**#29** · 2:33.2–2:38.8 · use 5.6s · dragon 2 of 4, crimson

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide low angle shot, a colossal crimson and black dragon with four horns rising through the collapsing roof of a dark throne room, wings spreading, stone falling, violet fire below, night sky above --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: crimson dragon bursting up through a collapsing roof.

Reject: dragon not crimson; black bars, painted background.

Vidu · 6s

```text
The dragon spreads its wings and roars as stones crash down around it.
```

Accept: the wings spread and stone falls.

Reject: wings multiply; a cut to another shot, the style turning 3D.

### Final chorus

**#30** · 2:38.8–2:43.8 · use 5.0s · dragon 3 of 4, white and gold

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle wide shot, a woman knight with long white hair and a greatsword standing small in a ruined starlit hall, facing a towering white and gold dragon rearing up over her, broken columns --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: small knight facing a towering white and gold dragon.

Reject: dragon not white; black bars, painted background.

Vidu · 5s

```text
The white dragon rears higher and she braces, raising her greatsword.
```

Accept: the dragon rears and she braces.

Reject: dragon merges with the columns; a cut to another shot, the style turning 3D.

**#31** · 2:43.8–2:48.8 · use 5.0s · dragon 4 of 4, storm blue

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, dynamic shot, a man martial artist with a shaved head in an orange gi leaping through the air, right fist thrust forward, toward a storm blue serpent dragon, rain and dark clouds around them --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: bald martial artist leaping fist-first at a blue serpent dragon.

Reject: hair on his head; man and dragon merged; black bars, painted background.

Vidu · 5s

```text
He drives his fist forward into the dragon as lightning flashes around them.
```

Accept: the punch lands.

Reject: fist merges into the dragon; a cut to another shot, the style turning 3D.

**#32** · 2:48.8–2:56.0 · use 7.2s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, a young woman mage with long pink hair in a white coat thrusting a crystal staff forward, hair and coat blown back, a dark ruined hall behind her, determined face, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: pink-haired mage thrusting a crystal staff, sheet A face.

Reject: face not like sheet A; black bars, painted background.

Vidu · 8s

```text
She thrusts the staff forward and a blinding spear of light bursts from its tip.
```

Accept: the staff thrusts and light bursts.

Reject: white light covers most of the clip; a cut to another shot, the style turning 3D.

### Outro

**#33** · 2:56.0–3:02.0 · use 6.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, the silhouette of a young woman cleric on top of a castle tower raising both arms to the sky, a sphere of light floating above her hands, the first dawn breaking on the horizon, clouds opening --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: silhouette on a tower with arms up and a sphere of light, dawn breaking.

Reject: not a silhouette; black bars, painted background.

Vidu · 6s

```text
The sphere of light rises slowly into the sky as the clouds open.
```

Accept: the sphere rises.

Reject: sphere doesn't rise; a cut to another shot, the style turning 3D.

**#34** · 3:02.0–3:10.0 · use 8.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from a ruined watchtower on a hillside, huge cracked stone blocks and rubble in the foreground with weeds and small white flowers in the cracks, below it a green valley kingdom at sunrise, golden light across fields and rivers, the last clouds clearing, bright blue sky opening, a small white castle on a hill in the far distance, flocks of birds --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: sunlit green valley at sunrise past inked stone, castle visible.

Reject: dark or stormy; valley became a sea; black bars, painted background.

Vidu · 8s

```text
The last clouds roll away and flocks of birds fly across the valley.
```

Accept: clouds clear and birds fly.

Reject: stone or castle melts; a cut to another shot, the style turning 3D.

**#35** · 3:10.0–3:15.0 · use 5.0s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, close-up, a golden crown resting on a single white stone stair step in warm morning sunlight, petals scattered on the stone, a long empty staircase out of focus behind --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: golden crown on one sunlit stair step, petals.

Reject: crown worn or held; black bars, painted background.

Vidu · 5s

```text
Petals drift across the step and the camera pushes slowly toward the crown.
```

Accept: petals drift and the camera pushes in.

Reject: crown changes shape; a cut to another shot, the style turning 3D.

**#36** · 3:15.0–3:22.4 · use 7.4s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from behind, two travellers walking side by side out of an open castle gate onto a long road at sunrise, a woman knight with a sword at her hip and a young woman in a travelling cloak, long shadows stretching ahead of them, open green land to the horizon --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: two travellers from behind leaving a castle gate at sunrise.

Reject: not two figures; facing camera; black bars, painted background.

Vidu · 8s

```text
They walk away down the road, their cloaks moving in the morning breeze.
```

Accept: they walk away down the road.

Reject: they turn around; a cut to another shot, the style turning 3D.
