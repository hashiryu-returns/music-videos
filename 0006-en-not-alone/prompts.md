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

One style sheet per scene, never both. Sheet A goes on every scene with a person or a monster in it, however small: front, back, silhouette, hands, a tiny figure. Sheet B is only for scenes with nobody in them. B has no character in it, so anything alive rolled on B comes out in Niji's default flat style. Drag only that sheet into Style Reference. Paste the prompt as is; it already ends in `--sw 250`. Check `sw 250` shows under the result.

Sheet A pulls toward a face close-up. Scenes meant to be wider leave out the face words, say what must fit in the frame (whole body, the whole harp, columns three times her height), and use `--sw 200`. If one still comes back too close, do the same.

Dark scene coming back sunny: swap `vivid saturated colours` for `muted dark colours` and add `blue sky, sun, sunlight` to `--no`. #1 and #2 already have it.

## Vidu

Image to Video, Q2, 1080p, Cinematic, Amount 1. Q3 only as a second try on a shot Q2 keeps getting wrong. Duration is on each scene's Vidu line. Trim to the scene's `use` length in the editor.

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

Midjourney · sheet A

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
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot, an old man with a long white beard and a deep green robe kneeling in a dimly lit stone chamber, lifting the lid of a small carved wooden chest, intense warm golden glow from inside the chest lighting his face from below, shelves of old books in shadow behind him, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, candles inside chest --sw 250
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

Midjourney · sheet A

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

Midjourney · sheet A

```text
low angle medium wide shot inside a dark cave, shot from behind over the shoulder of a woman paladin, three-quarter back view, turned away from camera, looking at a massive ancient stone tablet in sharp focus, holding up a burning torch, glowing carved runes on the tablet, torchlight on wet rock walls, modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, vivid saturated colours, inked backgrounds, fine ink detail of cracks, neutral grey shadows, crisp high resolution --no front view, facing viewer, facing camera, looking at viewer, chibi, crosshatching, painted background, letterbox, black bars, sepia, 3d render, text, watermark --sw 250
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

Midjourney · sheet A

```text
a magnificent serpentine emerald green dragon coiled tightly around ancient, moss-covered stone pillars deep inside a vast, shadowy cavern lair. wide angle shot, cinematic anime illustration style, thin precise black outlines on every edge, clean digital line art. flat cel shading with soft neutral grey shadows. fine inked details of cracks, chips, and speckled grime on the rock. dramatic, dim atmosphere: golden eyes glowing intensely in the dark, white smoke curling from its nostrils. the environment is defined by low-key, green and amber lighting filtering through the shadows. piles of detailed rubble and treasure on the floor. no chibi, no crosshatching, no painted background, no letterbox, no black bars, no sepia, no 3d render, no text, no watermark, realistic adult proportions, natural full color, vivid saturated colors. --sw 250
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

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, dynamic low angle shot, a young man swordsman with dark brown skin and short black hair in silver armour leaping toward camera through a dark cavern, sword raised over his head in both hands, his left knee forward and both feet off the ground, cape flaring behind him, rocks and embers in the air, realistic anime face, smooth clean skin, strong eyebrows, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
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

Midjourney · sheet A

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

Midjourney · sheet A

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

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle wide shot from a distance, a young man mage in a deep purple hooded robe walking through an ancient misty forest, his whole body from hood to boots and the full length of his tall staff in frame, a glowing lantern at the staff's tip, giant mossy roots arching three times his height around him, glowing blue mushrooms on the ground, shafts of light through the canopy --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 200
```

Accept: robed mage, whole body and staff in frame, small under giant roots.

Reject: face close-up; lantern not lit; black bars, painted background.

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
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium shot from the waist up, a young woman bard with short lavender hair and a ribbon headband playing a slender silver flute held sideways, both arms and the whole length of the flute in frame, eyes closed, flower petals in the wind, warm dusk light, a stretch of town wall and sky beside her, realistic anime face, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: bard from the waist up, the whole flute in frame, eyes closed, petals in the air.

Reject: face filling the frame; flute held like a recorder; black bars, painted background.

Vidu · 5s

```text
Her fingers move along the flute and the ribbons and petals drift in the breeze.
```

Accept: fingers move and petals drift.

Reject: flute bends or melts into her fingers; a cut to another shot, the style turning 3D.

**#15** · 1:12.0–1:19.0 · use 7.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, low angle, a colossal moss covered stone golem standing guard in front of a long unbroken stone town wall at dusk, rooftops, chimneys and towers of the town rising behind the wall, glowing amber eyes, arms hanging at its sides, vines across its shoulders, a tiny cloaked figure at its feet for scale, orange sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, gate, portcullis, door --sw 250
```

Accept: huge standing mossy golem in front of the town wall, rooftops behind, tiny figure at its feet.

Reject: a gate or door behind it; golem already kneeling; no small figure for scale; black bars, painted background.

Vidu · 7s

```text
The golem slowly sinks down onto one knee and lowers its head as the glow in its eyes fades.
```

Accept: the golem kneels.

Reject: golem stands up or walks; a cut to another shot, the style turning 3D.

**#16** · 1:19.0–1:26.0 · use 7.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, eye level, side view, a young woman ranger with a short auburn ponytail, a green hooded cloak and a short sword at her hip walking from left to right along a cracked stone street through the overgrown ruins of a fallen town, her whole body from head to boots in frame, mid stride, broken houses with collapsed roofs on both sides, vines and tall grass growing over the walls, a shallow violet swamp pooling across one side of the street, pale grey afternoon sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: ranger in side view walking left to right, whole body in frame, ruins and violet swamp around her.

Reject: facing the camera; she fills the frame; more than one figure; the street turned into a river; black bars, painted background.

Vidu · 7s

```text
She walks to the right along the ruined street as the camera tracks beside her, her cloak swaying, the broken houses sliding past behind her.
```

Accept: she walks right and the ruins slide past.

Reject: she turns to the camera or walks backward; legs tangle; a cut to another shot, the style turning 3D.

**#17** · 1:26.0–1:30.0 · use 4.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle medium wide shot, a hulking knight in black spiked armour with a glowing red eye slit in its helmet raising a huge double bladed battle axe over its head with both hands, its whole body from helmet to boots in frame, standing in front of a stone altar in the overgrown ruins of a fallen town, an ancient engraved blue and silver suit of armour resting on the altar behind it, broken walls and vines, pale grey afternoon sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: black axe knight raising its axe, the blue armour on the altar behind it.

Reject: the blue armour worn by someone; two axes or two knights; black bars, painted background.

Vidu · 5s

```text
The black knight swings the huge axe down toward the camera and dust bursts up from the ground.
```

Accept: the axe comes down and dust bursts up.

Reject: the axe bends or splits; the knight walks away; a cut to another shot, the style turning 3D.

**#18** · 1:30.0–1:33.7 · use 3.7s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, high angle full body shot looking down, a woman knight with a high black ponytail in ancient blue and silver armour with an engraved breastplate and a long torn blue cape, standing alone on a scorched cracked wasteland after a battle, her sword point resting on the ground, breathing hard, clouds of dust drifting low across the ground around her, deep gouges and scattered rubble in the earth, a scratch on her cheek, hazy pale sunlight, realistic anime face, smooth clean skin, strong eyebrows, sharp eyes with a heavy black upper lash line --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: full-body knight seen from above, blue armour, torn cape, dust drifting across a battered wasteland.

Reject: low angle; not full body; an enemy or a body in the frame; black bars, painted background.

Vidu · 5s

```text
Dust drifts across the ground and her torn cape stirs as she slowly lifts her head and looks up toward the camera.
```

Accept: the cape billows.

Reject: cape turns into wings; a cut to another shot, the style turning 3D.

### Verse 3

**#19** · 1:33.7–1:38.7 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, eye level, a young man elf bard with long platinum hair seated on a stone step inside a crystal shrine, playing a tall silver harp, his whole body from head to feet and the whole harp in frame, glowing pale blue crystals twice his height rising around him, eyes half closed, soft light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 200
```

Accept: elf man seated, whole body and whole harp in frame, tall crystals around him.

Reject: face close-up; harp has no strings; black bars, painted background.

Vidu · 5s

```text
His fingers sweep across the strings and his long hair stirs.
```

Accept: his hands move on the strings.

Reject: hands pass through the harp; a cut to another shot, the style turning 3D.

**#20** · 1:38.7–1:44.9 · use 6.2s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, an old woman sage with long grey hair and a weathered brown robe standing on a rocky mountain peak, her whole body from head to feet in frame, small against the sky, raising a gnarled wooden staff high above her head, the whole sky covered by heavy black storm clouds down to the horizon, dim grey light, wind tearing at her robe --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight --sw 200
```

Accept: small old sage on a peak raising a staff, the whole sky black with storm cloud.

Reject: blue sky or sunlight; face close-up; staff not raised; black bars, painted background.

Vidu · 7s

```text
She thrusts the staff upward and heavy rain begins to pour from the clouds.
```

Accept: the staff goes up and rain falls.

Reject: staff bends; a cut to another shot, the style turning 3D.

**#21** · 1:44.9–1:49.9 · use 5.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, eye level, a young woman cleric with short white hair in white and gold robes standing in the middle of a sunlit marble temple, her whole body from head to sandals in frame with the floor in front of her, raising a glowing amber stone above her head with both hands, marble columns three times her height on both sides, beams of sunlight between the columns --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 200
```

Accept: cleric whole body in frame between tall columns, glowing stone overhead.

Reject: face close-up; stone not glowing; black bars, painted background.

Vidu · 5s

```text
She lifts the amber stone higher and her robes and hair rise as if in a strong wind.
```

Accept: robes and hair lift.

Reject: stone splits in two; a cut to another shot, the style turning 3D.

### Chorus 2

**#22** · 1:49.9–1:54.9 · use 5.0s

Midjourney · sheet A

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

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme low angle wide shot, a young woman witch in a long violet coat and a wide brimmed pointed hat, holding a tall crooked staff, standing on wet black rocks at the foot of a colossal black castle on an island, her whole body small in the lower part of the frame, looking up at the castle, sheer black walls and jagged towers rising above her into heavy storm clouds, her coat and hat brim blown by the wind, sea spray around the rocks --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight, door, gate, bridge --sw 200
```

Accept: small witch on wet rocks, looking up at a towering black castle under storm clouds.

Reject: face close-up; a door or gate in view; more than one figure; black bars, painted background.

Vidu · 6s

```text
Her long coat and hat brim whip in the storm wind as sea spray bursts over the rocks behind her.
```

Accept: coat whips and spray bursts.

Reject: the hat flies off; the castle warps; a cut to another shot, the style turning 3D.

### Interlude 2

**#25** · 2:08.8–2:14.8 · use 6.0s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, side view, slightly low angle, inside a dark hall of a black castle where the stone floor has collapsed into a deep black chasm, a lone woman rogue with a short silver bob and a dark hood leaping across the chasm from one broken ledge to the other, her whole body in mid air in the middle of the frame, front knee drawn up and back leg trailing, arms out for balance, cloak streaming behind her, both broken ledges in frame, torches in iron brackets on the black walls, a faint violet glow rising from the depths --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight, window --sw 200
```

Accept: rogue in mid air over the chasm, side view, both ledges in frame, torches on the walls.

Reject: standing on a ledge; stairs; more than one figure; the chasm too narrow to need a jump; black bars, painted background.

Vidu · 6s

```text
She lands in a crouch on the far ledge, one hand touching the stone, as her cloak swings down around her and loose stones fall into the chasm.
```

Accept: she lands on the far ledge and her cloak settles.

Reject: she falls into the chasm or floats; legs tangle; a cut to another shot, the style turning 3D.

**#26** · 2:14.8–2:19.3 · use 4.5s

Midjourney · sheet B

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide shot, eye level, a vast empty throne hall inside a black castle, the floor as wide as a town square, a vaulted ceiling so high it disappears into darkness, slender black pillars set far back against the distant side walls, a bare floor of large black stone slabs with inked cracks between them, a pair of colossal black doors standing wide open at the far end, violet light pouring out through the open doors, low violet mist lying across the floor --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight, window, statue, carpet, rug --sw 250
```

Accept: huge bare stone floor with the pillars far off at the sides, open doors with violet light at the far end, mist on the floor.

Reject: a person in the hall; a carpet or rug on the floor; pillars or statues crowding the middle; the hall reads as a narrow corridor; doors closed; black bars, painted background.

Vidu · 5s

```text
The violet mist rolls slowly along the floor toward the camera as the camera glides forward down the hall.
```

Accept: the mist rolls and the camera moves toward the doors.

Reject: a pillar moves; the doors close; a cut to another shot, the style turning 3D.

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
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, medium wide shot, eye level, a woman hero with a short black bob in steel armour standing in a vast dark throne room, her body from head to knees in frame with the whole length of her sword, holding the sword upright before her in both hands with the blade rising past her face, the blade catching violet light, violet flames and black pillars far behind her --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, scar --sw 200
```

Accept: hero from head to knees, the whole sword upright in front of her, throne room behind.

Reject: face filling the frame; a scar on her face; sword cut off by the frame; black bars, painted background.

Vidu · 8s

```text
She raises the sword up in front of her face and her eyes narrow.
```

Accept: the sword rises and her eyes narrow.

Reject: sword bends or doubles; a cut to another shot, the style turning 3D.

### Break

**#29** · 2:33.2–2:38.8 · use 5.6s · dragon 2 of 4, crimson

Midjourney · sheet A

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

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, low angle wide shot, a towering white and gold dragon looming over a small woman knight in a ruined starlit hall, its head lowered toward her, jaws wide open with bared fangs, a white glow in its throat, claws gripping the cracked stone floor, wings spread wide behind it, the knight with long white hair and a torn cape in a fighting stance below it, feet planted wide, knees bent, greatsword held up across her body in both hands, broken columns and scattered rubble around them --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 250
```

Accept: dragon looming with jaws open and fangs bared, the small knight braced below it with her sword up.

Reject: the dragon looking calm or playful; the knight standing relaxed or touching the dragon; dragon not white; black bars, painted background.

Vidu · 5s

```text
The dragon roars and a torrent of white fire bursts from its jaws toward her.
```

Accept: the dragon roars and the fire comes at her.

Reject: the knight vanishes in the fire or fuses with the dragon; dragon merges with the columns; a cut to another shot, the style turning 3D.

**#31** · 2:43.8–2:48.8 · use 5.0s · dragon 4 of 4, storm blue

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, extreme wide shot, side view, eye level, a colossal storm blue serpent dragon coiling through heavy rain above a jagged rocky mountain peak, its head on the right of the frame many times larger than a man, jaws open toward the left, a tall adult woman martial artist with a long black braid in a white sleeveless top, a red sash and loose white trousers on the left of the frame, her whole body in mid air between the peak and the dragon's head and about a third of the frame height, a flying kick toward its jaw, her right leg fully extended straight ahead, her left leg folded under her, her arms out for balance, her braid streaming behind her, the whole sky covered by heavy black storm clouds, rain streaking across the frame --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, blue sky, sun, sunlight --sw 200
```

Accept: side view, the woman in a straight-leg flying kick on the left, a third of the frame tall, the huge dragon head on the right, the rocky peak and storm sky around them.

Reject: she reads as a monkey or a child (hunched, knees tucked, tiny); a fist or face filling the frame; the dragon smaller than her or pasted behind her; a blank white background; woman and dragon merged; black bars, painted background.

Vidu · 5s

```text
She flies across the gap and her extended foot slams into the dragon's jaw as the rain whips around them.
```

Accept: she crosses the gap and the kick lands on the jaw.

Reject: her leg merges into the dragon; she turns toward the camera; a cut to another shot, the style turning 3D.

**#32** · 2:48.8–2:56.0 · use 7.2s

Midjourney · sheet A

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot, side view, eye level, a young woman mage with long pink hair in a white coat standing in a dark ruined hall, her whole body from head to boots and the whole length of her crystal staff in frame, thrusting the staff forward with both arms toward the right of the frame, feet apart, hair and coat blown back, broken columns twice her height behind her --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark --sw 200
```

Accept: pink-haired mage in side view, whole body and whole staff in frame, thrusting it forward, ruined hall behind.

Reject: face or upper body filling the frame; staff cut off by the frame; black bars, painted background.

Vidu · 8s

```text
She thrusts the staff forward and a blinding spear of light bursts from its tip.
```

Accept: the staff thrusts and light bursts.

Reject: white light covers most of the clip; a cut to another shot, the style turning 3D.

### Outro

**#33** · 2:56.0–3:02.0 · use 6.0s

Midjourney · sheet A

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
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, realistic adult proportions, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime, neutral grey shadows, crisp high resolution, wide shot from the edge of a high mountain ridge, huge cracked grey rocks with tufts of grass in the foreground, beyond them a vast sea of white clouds lit gold by the rising sun, distant snow-capped peaks rising out of the clouds, a clear pale blue morning sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, text, watermark, person, figure --sw 250
```

Accept: inked rocks in front, a gold-lit sea of clouds and distant peaks beyond.

Reject: a person anywhere in the frame; no rocks in front; the clouds turned into a sea of water; black bars, painted background.

Vidu · 8s

```text
The sea of clouds drifts slowly below and the camera glides forward past the rocks out over the clouds.
```

Accept: the clouds drift and the camera moves out over them.

Reject: the rocks melt; a figure appears; a cut to another shot, the style turning 3D.
