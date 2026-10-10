# 0006 prompts

Plan and techniques: [`README.md`](README.md). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

## The two women

Built to read apart at a glance in a fast fight: a black ponytail and buzzed sides against a green silhouette, white against black, red against green. Red belongs to the singer, so the colour-isolation shot (F11) lands on her.

The singer is my wife. The face is chosen by eye against the 0002 plate [`her-full.png`](../0002-fr-je-marrete-pas/characters/her-full.png), the drawing that caught her best. The plate goes into no slot: as Omni Reference it brings 0002's inked comic look and the kimono with it. Face anatomy in words (cheekbones, jaw, eyelids, skin tone) pulled the picture toward American comics and a different ethnicity, so the prompt names only the brows and leaves the rest to the roll. No photo of her is kept in this repo or goes into Midjourney.

The plates are neutral on purpose. Q4 copies a plate's expression and pose into every shot, so a sultry plate makes every shot sultry. Allure goes into the shots that want it, through the gaze, the mouth, the pose, the light and how close the camera is.

The rival's silhouette is the hair. Where the edamame pods sat, she has two thick tufts of her own yellow-green hair, tied and standing up, one above each temple. The rest of her hair is short. Nothing about Zundamon goes in the prompt.

| | The singer | The rival |
| --- | --- | --- |
| Hair | the kept plate: sides and nape buzzed, the crown in a high ponytail with a red cord | short yellow-green hair, two thick tufts tied upright above the temples, nothing past the shoulders |
| Face | thick straight dark brows, relaxed, no frown line, outer eye corners a little lower than the inner corners, a calm face, no earrings | amber eyes |
| Coat | short white jacket with wide sleeves, worn open | long black high-collared coat, open, green lining |
| Under it | black bodysuit, collar closed to the throat, wide black trousers, red sash | dark green bodysuit, collar closed to the throat, slim black trousers |
| Feet | black sandals over black split-toe socks | the same |
| Blade | katana, purple-wrapped hilt | katana, green-wrapped hilt, thin green line along the spine |

The lyric's "sleeves torn open, sandals gone" needs a damaged set of plates later. The test uses the intact set.

## Files

Plates go in [`characters/`](characters/):

| File | What | Made from |
| --- | --- | --- |
| `singer-front.png` | full body, front | text, V8.2 |
| `singer-back.png` | full body, back | `singer-front.png` via the Edit model |
| `singer-face.png` | head and shoulders | `singer-front.png` via the Edit model |
| `rival-front.png` | full body, front | text, V8.2, styled on `singer-front.png` |
| `rival-back.png` | full body, back | `rival-front.png` |
| `rival-face.png` | head and shoulders | `rival-front.png` |
| `blade-singer.png` | her katana alone | text |
| `blade-rival.png` | the rival's katana alone | text |
| `bridge.png` | the footbridge at night, empty | text |
| `tea-stall.png` | the tea stall under the highway at dawn, empty | text |
| `master-front.png` | the master, a woman, full body, front | text, V8.2, styled on `singer-front.png` |
| `master-face.png` | the master, head and shoulders | `master-front.png` via Quick Edit |
| `singer-suit.png` | the singer in a black suit and sunglasses: HQ, harbour, chase, verse 3 | `singer-front.png` via Quick Edit |
| `singer-tactical.png` | the singer in tactical gear: warehouse, rooftop | `singer-front.png` via Quick Edit |
| `rival-hood.png` | the rival in a black hoodie: harbour, chase, warehouse, rooftop | `rival-front.png` via Quick Edit |
| `singer-gi.png` | the singer as an apprentice, training clothes | `singer-front.png` via Quick Edit |
| `rival-gi.png` | the rival as an apprentice, training clothes | `rival-front.png` via Quick Edit |
| `case.png` | the open case of glowing zunda mochi | text |
| `hq.png` | the agency operations room at night, empty | text |
| `harbour.png` | a container harbour at night, empty | text |
| `warehouse.png` | inside the smugglers' warehouse, empty | text |
| `highway.png` | an empty elevated highway at night | text |
| `training-room.png` | a white virtual training room | text |
| `rooftop.png` | a tower rooftop at night, a hologram billboard, empty | text |
| `rooftop-dawn.png` | the same rooftop at dawn | `rooftop.png` via Quick Edit |

A Q3 shot takes seven: each person's costume front and face, then blades or the case, then one place. The face plates (`singer-face.png`, `rival-face.png`, `master-face.png`) go with every costume. The bridge and the stall use the original fronts.

## Midjourney

Done: `singer-face.png`, `singer-front.png` (middle row, second from the left), `singer-back.png` (bottom row, second from the left), `rival-front.png` (Quick Edit on the middle row, far right), `rival-face.png` (second from the left), `rival-back.png` (second from the left), `blade-rival.png` (second roll, top left), `blade-singer.png` (second roll, bottom left), `bridge.png` (first roll, bottom left), `street.png` (second roll without Style Reference, top left), `tea-stall.png` (top left). Next: the master, the costumes, the case and the places, 8 onward below.

Settings panel:

- Version **8.2**
- Aspect **2:3** for the body plates, **1:1** for the faces, **16:9** for the bridge, **3:1** for the blades
- Stylization 250, Weirdness 0, Variety 0
- Speed **Relax**

V8.2, not V7. On the same prompt V7 came back younger and flatter, the kid-anime look. V8.2 is closer to the target thumbnails: an adult face, finer eyes, cinematic light. Niji is out. It only does flat cel shading.

V8.2 has no Omni Reference. A second view of someone is the Edit model: drag the front plate onto the prompt, or on Discord add `--edit` and the image URL. It takes up to four images. Style Reference still works, so the rival, the blades and the bridge keep `--sw`. `shaved head` in `--no` wipes the undercut, so the hair is described in the positive.

Every plate is on plain light grey, so Q4 takes the woman and nothing else from it. Props stay off the plates; the blades are their own references.

### 1. `singer-front.png`

Done. Three prompts, in the order they were run. The kept full body is the middle row, second from the left of the rebuild. The kept back is the bottom row, second from the left.

First roll, no reference. This is the body the close-up was made from:

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, an adult woman with a sharp undercut, the sides of her head and the nape buzzed to the scalp, only the hair on the crown left long and tied into a high ponytail with a red cord, a calm neutral face, bold straight dark eyebrows, a short white jacket with wide sleeves worn open over a black bodysuit with the collar closed to the throat, wide black trousers, a red sash at the waist, black sandals over black split-toe socks, plain light grey background --no chibi, child, three-quarter view, profile, turned head, flat cel shading, mascot, american comic, western comic, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, earrings
```

Then Quick Edit on that image. This close-up is the approved face:

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her undercut, and her ponytail. Make her eyebrows very thick and straight, relaxed, with a smooth forehead and no crease between them. The outer corner of each eye sits slightly lower than the inner corner.
```

Then Quick Edit on that close-up. This rebuilt the full body:

```text
Full body from head to feet, straight-on, both shoulders square to the camera. Keep this exact face, these eyebrows, this undercut, and this ponytail. A short white jacket with wide sleeves worn open over a black bodysuit with the collar closed to the throat, wide black trousers, a red sash, black sandals, arms relaxed, plain light grey background.
```

### 2. `rival-front.png`

Version **8.2**. A new generation, not a Quick Edit. Put `singer-front.png` in **Style reference** only, so the rendering matches. Leave **Attach to prompt** empty. If she is attached there, the rival comes out as a copy of her.

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, an adult woman, a calm neutral face, short bright yellow-green hair, two thick tufts of that same hair tied with bands and standing upright above her temples, amber eyes, the rest of her hair cut short above the shoulders, a long black high-collared coat worn open with a green lining, a dark green bodysuit with the collar closed to the throat, slim black trousers, black sandals over black split-toe socks, plain light grey background --no chibi, child, three-quarter view, profile, turned head, antennae, horns, pods, long hair, ponytail, flat cel shading, mascot, overalls, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, animal tail --ar 2:3 --sw 200 --v 8.2
```

Reject: dark hair, a white coat, pods or antennae that are not hair, the two tied tufts missing, hair past her shoulders, an animal tail instead of hair, anything that makes her look like the singer.

"Long black coat" and "bodysuit" came back as shiny leather and latex, which reads as a 3D game render next to the singer's matte cloth. The kept roll is the middle row, far right. The kept plate is this Quick Edit on it, materials only:

```text
Keep this exact face, this hair, and these clothes. Make the coat matte black wool and the bodysuit matte dark green knit fabric, no shine, no leather, no latex.
```

If rolling again instead, write the materials into the prompt: `a long black matte wool coat`, `a dark green bodysuit of matte knit fabric`, and add `leather, latex, vinyl, shiny fabric` to `--no`.

### 3. Back and face plates

Open the chosen full-body image. Quick Edit. Paste only this:

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her undercut, and her ponytail. Plain light grey background.
```

Reject a plate where her face turns back toward the camera. From behind, the buzzed sides and the ponytail both show.

The rival, same steps, on `rival-front.png`. Back:

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her short hair, and the two tied tufts on top of her head. Plain light grey background.
```

Face:

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her short hair, and the two tied tufts.
```

The close-up draws the tufts longer than the front plate does. Pick the one closest to the front. On the back, reject green legs: the trousers are black.

The long form, if Quick Edit is not available. Version **8.2**, Edit model. Attach her front plate.

`singer-back.png` and `rival-back.png`:

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, crisp high resolution, character design, full body from head to feet in frame, back view, seen from directly behind, eye level, the woman standing straight, arms relaxed at her sides, plain light grey background --no chibi, child, front view, face, letterbox, black bars, text, watermark, signature, sword, weapon --ar 2:3 --v 8.2
```

`singer-face.png` and `rival-face.png`:

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, crisp high resolution, character design, head and shoulders portrait, front view, eye level, the woman looking straight at the camera, a calm neutral face, plain light grey background --no chibi, child, letterbox, black bars, text, watermark, signature --ar 1:1 --v 8.2
```

Reject a back plate with the face turned toward the camera. From behind, the singer's buzzed sides and ponytail both show. The rival's two tied tufts show above her head. Her hair does not pass her shoulders.

### 4. The blades

Version **8.2**, Style Reference `singer-front.png`.

`blade-singer.png`:

The first roll came back red and black, and the two blades did not read apart. Red belongs to the singer's sash, so the blades are purple and green.

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a purple-wrapped hilt, a round black guard, a long curved polished steel blade, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200 --v 8.2
```

`blade-rival.png`:

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a green-wrapped hilt, a square black guard, a long curved dark steel blade with a thin glowing green line along its spine, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200 --v 8.2
```

### 5. `bridge.png`

Version **8.2**, Style Reference `singer-front.png`. Empty, so Vidu places the women.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a narrow arched wooden footbridge over a dark canal, the whole bridge in frame from one bank to the other, red paper lanterns hung along both railings glowing warm, heavy rain, the wet planks shining, a near-future city at night behind it, elevated highways on concrete pillars, tall towers covered in neon signs and hologram billboards in cyan and magenta, their light reflected in the canal --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --sw 200 --v 8.2
```

Signs come out as fake script. Fine as long as no real word or logo is readable.

Pick a side view with the whole arch in frame and a clear deck: the fight runs along it. Reject lantern posts that block the deck, a watermark, or a dark shape that could be a person.

### 6. `tea-stall.png`

Version **8.2**, no Style Reference, for the same reason as `street.png` below. Aspect **16:9**. Empty, with two cups already on the counter, so shot 6 has them.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a small tea stall tucked between the concrete pillars of an elevated highway at dawn, a worn wooden counter under a short cloth awning, a steaming iron kettle, two empty ceramic tea cups side by side on the counter, a single paper lantern still glowing warm, light rain, wet pavement, pale blue morning light, a near-future city waking up behind it, hologram signs dimmed for the morning --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, ramen, noodles, menu --ar 16:9 --v 8.2
```

Pick one where the counter faces the camera with room in front of it for a woman to stand. Reject night, a bright sunny sky, food stall clutter, or more than two cups.

### 7. `street.png`

Deleted: the harbour took its scene. Its lesson stays: with `singer-front.png` as Style Reference the street came out in the singer's black, white and red, and the cyan and magenta neon was gone. A place is rolled without Style Reference.

### 8. `master-front.png` and `master-face.png`

The master, their old teacher and the one behind the smuggling. Silver hair worn loose with a blunt fringe, so her silhouette reads apart from the singer's ponytail and the rival's tufts. A grey haori, between the singer's white and the rival's black. Calm on the plate: the red eyes and the aura go into the shots that want them, because Q4 copies a plate's face into every shot.

Version **8.2**, aspect **2:3**, `singer-front.png` in **Style reference** only, the same as the rival. Kept: the fourth of the first roll.

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, a tall elegant woman who looks about forty-five, a sharp beautiful face, narrow cold grey eyes, a calm stern face, long straight silver hair worn loose down to her waist with a blunt straight fringe, a thin glowing blue circuit line running down from under her left eye, a long matte grey wool haori coat worn open over a fitted matte dark grey knit bodysuit with the collar closed to the throat, black hakama trousers, black boots, plain light grey background --no chibi, child, teenager, three-quarter view, profile, turned head, ponytail, bun, twin tails, red eyes, aura, flat cel shading, mascot, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, leather, latex, armour, green, red --ar 2:3 --sw 200 --v 8.2
```

A man first. Four rolls of an old or fifty-year-old swordmaster, from text at `--sw 200` and `--sw 400` and by Quick Edit on `rival-front.png`, all came back as a photorealistic face or a 3D game render, further from the women than any roll of a woman. On both kept plates the circuit line is under her right eye, whatever the prompt says.

Face: open the kept front, Quick Edit, paste only this. Kept: the fourth.

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her long straight silver hair with the blunt fringe, and the thin glowing blue line under her left eye.
```

### 9. The costumes

Quick Edit on the original front plate each time, so the face and hair stay. Aspect **2:3**. Reject any roll where the face changes, the singer loses the undercut or the red cord, or the rival loses the two tufts.

`singer-suit.png`, on `singer-front.png`. Kept: the third. The others hung a red strap at the hip, the old sash carried over.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, and this ponytail with its red cord. Dress her in a slim matte black suit, a white shirt with the collar open and no tie, black ankle boots, and narrow black sunglasses. Arms relaxed, plain light grey background.
```

`singer-tactical.png`, on `singer-front.png`. Kept: the third. Two rolls had UI-like marks in the corners.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, and this ponytail with its red cord. Dress her in fitted matte black tactical gear: a black combat suit, a black armoured vest, fingerless gloves, an empty holster on her thigh, black boots, a small earpiece. Arms relaxed, plain light grey background.
```

`rival-hood.png`, on `rival-front.png`. Kept: the first, the closest hair colour. Two rolls put lettering on the sleeve or in the frame.

```text
Full body from head to feet, straight-on. Keep this exact face, this short yellow-green hair and the two tied tufts. Dress her in an oversized matte black hoodie with the hood down and green drawstrings, slim black cargo trousers, and black sneakers. Arms relaxed, plain light grey background.
```

`singer-gi.png` and `rival-gi.png` are the past, so the hair is different too: the switch to the memories reads in one frame. The colour stays, so each is still recognisable. Both wore the same uniform as apprentices.

`singer-gi.png`, on `singer-front.png`:

```text
Full body from head to feet, straight-on. Keep this exact face. Change her hair: no undercut, her black hair grown out long and loose past her shoulders, a thin red cord tied around her left wrist. Dress her in a plain indigo training jacket and indigo hakama trousers, barefoot. Arms relaxed, plain light grey background.
```

`rival-gi.png`, on `rival-front.png`:

```text
Full body from head to feet, straight-on. Keep this exact face and this yellow-green hair colour. Change her hair: no upright tufts, the hair longer, down to her shoulders, tied into two low loose pigtails. Dress her in a plain indigo training jacket and indigo hakama trousers, barefoot. Arms relaxed, plain light grey background.
```

Reject a roll where the face changes. Everywhere else the hair stays as on the plates: in fast cuts and changing costumes, the hair is how the viewer tells the two apart.

### 10. `case.png`

Version **8.2**, `singer-front.png` in Style reference, aspect **16:9**. The contraband: the deal, the raid's crates and the last frame.

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a hard silver case lying open, seen from slightly above, neat rows of Japanese sweets inside on black foam like jewels, each one a soft round white rice cake covered in a thick smooth coat of bright pale green mashed edamame paste, the paste glossy with a faint green glow, a red circular crest stamped on the inside of the lid, plain light grey background --no brussels sprouts, cabbage, vegetable, leaves, lettuce, balls, person, hand, text, watermark, signature, 3d render, photorealistic, letters --ar 16:9 --sw 200 --v 8.2
```

`zunda mochi` alone means nothing to Midjourney: it drew Brussels sprouts, four out of four. Describe the thing: a white rice cake under green edamame paste.

Reject a crest with readable letters, or mochi that look like green balls of plastic. Kept: the fourth of the second roll, where the white mochi shows under the paste.

### 11. The places

Version **8.2**, no Style Reference (it drained the neon on `street.png`), aspect **16:9**. Empty, so Vidu places the people. Reject any person or a dark shape that could be one, readable real words or logos, a 3D-render look, and a photograph. Night water and city lights pull V8.2 toward a photo, so every place prompt opens with `anime background art, hand-painted`. `hq.png` was rolled before that line was added. Kept: the fourth.

`hq.png`, verse 1 and verse 3:

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a dark high-tech agency operations room at night in a near-future city, a huge curved wall of hologram screens glowing cyan, a long glass table lit from within, floor-to-ceiling windows streaked with rain, neon towers outside --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature --ar 16:9 --v 8.2
```

`harbour.png`, verse 2. Kept: the second, of the roll with `anime background art`. Three rolls put a lone figure on the quay despite `--no person`.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a container harbour at night in a near-future city, stacks of shipping containers, huge cranes against the sky, a wet concrete quay, orange sodium lights and cyan neon, the city's towers glowing across the black water, light rain --no person, figure, crowd, ship crew, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, sun, sunlight --ar 16:9 --v 8.2
```

`warehouse.png`, chorus 2. Kept: the first, the widest aisle.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, inside a huge dark warehouse at night, tall stacks of wooden crates and shipping containers with an aisle between them, red alarm lights, beams of cold light through high windows, a metal catwalk overhead, a wet concrete floor --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature --ar 16:9 --v 8.2
```

`highway.png`, the chase and verse 3. Kept: the second.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, an empty elevated highway at night in a near-future city, the road closed and empty, wet asphalt reflecting neon, white lane lines running away from the camera, tall streetlights, towers with hologram billboards in cyan and magenta on both sides, heavy rain, a red and white glow of traffic far below --no person, figure, crowd, car, truck, vehicle, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --v 8.2
```

`training-room.png`, the memories in verse 3. Kept: the first. The one place where a clean, game-like render is the point, so `3d render` stays out of `--no`:

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, crisp high resolution, wide shot, eye level, a vast empty white virtual training room, a thin glowing cyan grid on the white floor, walls and ceiling, soft even light with no shadows, a few translucent holographic interface panels floating in the air, clean and minimal, a digital simulation --no person, figure, crowd, letterbox, black bars, sepia, text, watermark, signature, furniture --ar 16:9 --v 8.2
```

`rooftop.png`, the boss fight, and the start of shot 3's dive:

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, the flat rooftop of a skyscraper at night in a near-future city, heavy rain, wet concrete shining with reflected neon, a painted helipad circle, air vents and a low parapet at the edge, a giant hologram billboard of a koi fish glowing cyan and magenta on the tower next to it, more towers covered in neon signs all around and far below, low clouds lit from beneath --no person, figure, crowd, helicopter, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --v 8.2
```

Pick one with open floor in the middle for three people to fight on, and the koi big behind it. Kept: the fourth, the koi centred over the floor.

`rooftop-dawn.png`, the last chorus and the outro. Open the kept `rooftop.png` and run Quick Edit, so the roof stays the same roof:

```text
Keep this exact rooftop and these towers. Make it dawn: the rain has stopped, the sky pale pink and gold, the hologram billboard faded and almost transparent, the neon signs switched off, puddles on the roof reflecting the sky.
```

## What the Vidu tests showed

Off-Peak, 1080p, 16:9. Q4 takes the nine plates. Q3 reference takes seven, so the two back plates stay out. The web app tags them `@image1`, `@image2`, in upload order. Q3 Pro takes two images, so it cannot run a shot with both women, both blades and the bridge. Q3's modes are Cinematic, Flash and Advertisement.

**Q4, 5s, blades locked.** Identities hold the whole way. The singer keeps the undercut, the ponytail, the white jacket and the red sash. The rival keeps the short yellow-green hair, the two tufts and the black coat. One blade each, purple hilt and green hilt, and the two bodies do not melt together. The blades come out short and thick, not the katana plates. The clip is the finished pose from the first frame: blades already crossed, both women breathing hard, sparks already flying, rain behind them. Breath, sparks and rain move. The pose does not, so there is no approach and no strike. Usable as a held struggle. It does not show that the faces survive a fight.

**Q4, 8s, the leap.** The leap and the clash happen. Both women stay readable, one blade each, the tufts still there. The jump's physics are a little off. The bridge design holds: the red arch, the lanterns, the wet deck, the highways. The rendering does not. It looks like an older 3D game. Seen by someone else, the women look composited onto the bridge, and the frame has a lot of other problems besides. Their edges, their light and their material do not belong to the wet background.

**Q4, 16s, four shots in one take.** The two close-ups hold: the rival's face in the rain, and the singer's face against the red lantern. The running wide shot and the blade clash fail on the motion and on the picture, the same composited game render as the 8s.

**What the edit can do with that.** A short piece of a weak clip can still be cut in: half a second of the leap sped up, a few frames of the hit slowed, a white flash, camera shake, added sparks, grain, and one grade over the whole song. That is most of what the technique list is for. It cannot put a pasted figure back into the rain, turn the game render back into the Midjourney plate, or carry a long wide shot. Q4 close-ups and Q4 hits of a second or two are material. A Q4 fight is not.

**Q3 Cinematic, the same leap.** Motion is clearly better, and the women sit in the same rain and the same lantern light as the bridge. The Midjourney texture is gone here too. This is the model for the fight and the wide shots. A second roll of the same prompt still does the leap and the clash, and it is the worse of the two. It adds its own slow motion on the hit, the rival briefly holds two blades, and the throw breaks her body for a moment. Keep the first. Two or three rolls per shot is the normal way to get one.

**Q3 Cinematic, 16s, four shots.** Both rolls failed. The first arrived in order with extra swords, a blade through the rival, and her close-up replaced by another face. The second was worse: four arms, the two women appearing back to back out of nothing, then a blade lock from a senseless angle. Multi-shot is out. The fight is 8s, one action at a time.

**Q3 Flash, the same leap.** Rejected. Flat cel shading, a mobile-game render, and the singer standing on the railing instead of the deck.

Q3 Cinematic for the fight and the wides. Q4 for face close-ups. The grade in Final Cut Pro is what makes a close-up sit next to a wide. Neither video model keeps the plate texture.

**Q4 and Q3 Cinematic, one woman with a sword, and the two of them unarmed.** Both on an empty stage, no bridge. Identities hold. Both models render a 3D game body. The plates are already glossy and semi-real, and a full body gives the model cloth, limbs and a floor to rebuild. The Q4 face close-ups stayed closer to the plates because the face fills the frame. Q4 stays on faces. Full-body shots stay on Q3 Cinematic, in the rain and the lantern light, where that render is less bare.

**Q4, 5s, the same sword dance from flat anime plates.** Quick Edit on singer-front and singer-face: "Redraw this same woman as a 2D anime illustration: clean ink line art, cel shading with two tones, flat colours. Keep her face, her undercut, her ponytail, and her clothes exactly." Uploads: the two edits and `blade-singer.png`. The body stays 2D at front and at three-quarter, no 3D game render. One blade the whole way, feet planted, a shadow on the floor, so she stands on the stage instead of on top of it. Identity holds. The blade comes out too long and thin. The picture looks cheap because the plate is flat. The CG look comes from the plate, not the model. 

**Q4, 5s, the same sword dance from fuller anime plates.** Quick Edit on singer-front: "Redraw this same woman as a high-quality modern TV anime key visual: detailed clean line art, cel shading with soft gradients and highlights, rich colour, detailed cloth folds. Keep her face, her undercut, her ponytail, and her clothes exactly." The face plate is a head-and-shoulders Quick Edit of that result, since the same edit on singer-face drew other women. The blade holds and the feet stay planted. The ink line is gone and the cloth takes soft rounded shading, so the body reads as a toon-shaded 3D model again. It is cleaner than the original glossy plates, but it is not 2D. The more painted shading the plate has, the more 3D the full body comes back.

## Vidu Q4 test

Reference to Video, **Q4**, 1080p, 16:9, Off-Peak Mode. Turn audio off if there's a switch; the song replaces it.

Upload the plates in this order every time, so the numbers in the prompts match:

1. `singer-front.png`
2. `singer-back.png`
3. `singer-face.png`
4. `rival-front.png`
5. `rival-back.png`
6. `rival-face.png`
7. `blade-singer.png`
8. `blade-rival.png`
9. `bridge.png`

The web app tags uploads `@image1`, `@image2`, and so on, in the order above. Each image has one role, stated once at the top. Every prompt closes with the same stability paragraph. What came back is in the section above.

### Test 1 · Locked blades, close (5s)

Close contact, two faces in one frame. The hardest frame for keeping two identities apart.

Result: identities held for the whole 5s. Both women, the tufts, the coats and one blade each stayed. The blades came out short and thick, not the katana plates. The clip is one held moment from the first frame: blades already crossed, both breathing hard, sparks already flying, rain behind them. Breath, sparks and rain move. The pose does not change, so this take does not show a fight progressing.

```text
@image1, @image2 and @image3 are the singer: front, back and face. @image4, @image5 and @image6 are the rival: front, back and face. @image7 is the singer's katana. @image8 is the rival's katana. @image9 is the place.

Night, heavy rain, the middle of the footbridge in @image9. Close-up from the side at eye level: the singer on the left, the rival on the right, their katanas crossed and locked between their faces. They push against each other, blades grinding, sparks spraying from the contact point, rain bouncing off the steel. The camera holds steady.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana in both hands. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

### Test 2 · Leap and parry, wide (8s)

Travel across the bridge, two actions. Feet slide in Vidu, so both actions start and end in the air or on a landing.

Result: the leap and the clash happen, and both women stay readable, one blade each, tufts still there. The jump's physics are a little off. The bridge design holds: the red arch, the lanterns, the wet deck, the highways. What drops is the rendering. It looks like an older 3D game instead of the plate. The women also look composited onto the bridge: their sharp edges, light and material do not belong to the wet background.

```text
@image1, @image2 and @image3 are the singer: front, back and face. @image4, @image5 and @image6 are the rival: front, back and face. @image7 is the singer's katana. @image8 is the rival's katana. @image9 is the place.

Night, heavy rain, the footbridge in @image9, seen from the side, wide, the whole bridge in frame, the two women small against the city. The singer leaps from the left end of the bridge high into the air and brings her katana down at the rival, who raises her katana and blocks it in a burst of sparks. Then the rival throws her off, and the singer flips backward through the air and lands crouched on the railing. The camera tracks sideways with the leap.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

### Test 3 · Four shots in one take (16s)

The plan's assumption: one 16s take cut into pieces keeps the faces from shot to shot. Four shots of about 4s, each with one action.

Result: the two close-ups hold. The rival's face in the rain and the singer's face against the lantern both read as the plates. The running wide shot and the blade clash do not. The motion is wrong and the picture drops to the same composited game render as the 8s take. Q4 is for close-ups, not the fight.

```text
@image1, @image2 and @image3 are the singer: front, back and face. @image4, @image5 and @image6 are the rival: front, back and face. @image7 is the singer's katana. @image8 is the rival's katana. @image9 is the place.

Night, heavy rain, the footbridge in @image9. Four shots.

Shot 1: close-up of the rival's face, rain running down it, her eyes narrowing as she looks at the camera.
Shot 2: from behind the singer, the rival at the far end of the bridge sprinting straight at her, katana low, coat flying.
Shot 3: side view, medium wide, the two women dash past each other and slash once, a flash of sparks between them, and both stop back to back with their blades out to the side.
Shot 4: slow push-in on the singer's face, calm, rain falling, a red lantern swinging behind her.

Both women keep the faces, hair and outfits of their references in every shot. Each holds only her own katana. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

## Q3 Cinematic, same leap (8s)

Q3 reference takes 7 images, so the two back plates stay out. Order: singer front, singer face, rival front, rival face, singer blade, rival blade, bridge. Mode **Cinematic**, 8s, 1080p, 16:9, Off-Peak.

Result: the first roll is the keeper. The motion is good, and the women belong in the rain and the bridge light. The plate texture is gone, same as Q4. The second roll still does the leap and the clash, then adds its own slow motion, a second blade in the rival's hand, and a broken tumble. Two or three rolls per shot. This is the fight model. Q4 stays on face close-ups.

Q3 Flash, same leap: rejected. Flat cel shading, a game render, and the women standing on the railing. Faster, and worse.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the footbridge in @image7, seen from the side, wide, the whole bridge in frame, the two women small against the city. The singer leaps from the left end of the bridge high into the air and brings her katana down at the rival, who raises her katana and blocks it in a burst of sparks. Then the rival throws her off, and the singer flips backward through the air and lands crouched on the railing. The camera tracks sideways with the leap.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

## Q3 Cinematic, four shots (16s)

Same seven images, same order. Both rolls failed, the second worse than the first: four arms, the women appearing back to back out of nothing, then a blade lock from a senseless angle. Dropped. The fight is 8s, one action at a time.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the footbridge in @image7. Four shots.

Shot 1: close-up of the rival's face, rain running down it, her eyes narrowing as she looks at the camera.
Shot 2: from behind the singer, the rival at the far end of the bridge sprinting straight at her, katana low, coat flying.
Shot 3: side view, medium wide, the two women dash past each other and slash once, a flash of sparks between them, and both stop back to back with their blades out to the side.
Shot 4: slow push-in on the singer's face, calm, rain falling, a red lantern swinging behind her.

Both women keep the faces, hair and outfits of their references in every shot. Each holds only her own katana. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

## Shots 1–12 · intro and verses

Shots 2, 4 and 11 are made in the edit. Settings as in 13–24: Q3 Cinematic **8s**, Q4 **5s**, 1080p, 16:9, Off-Peak. Two or three rolls each.

What 13–24 taught, applied here: Vidu does not move the lens, so the focus pull in 1 is built in the edit. Walking feet slide, so walks are framed above the feet. A face change in motion is kept to the eyes. A hand raised to the face lands in the hair, so hands stay down. Screens, scopes and files are added in the edit, not asked of Vidu.

### 1 · Rain on the lens

Made: `1.mp4`.

Q4, 5s. On screen 0:00–0:06, slowed to 6s. The black, the rain on the lens and the focus pull are in the edit: a Gaussian Blur from full to zero over her eye, with a rain overlay on top. The clip only has to be her eye, sharp and still, in the rain.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred far behind her. Extreme close-up of the singer's eyes and brows, filling the frame. Her eyes are open and look straight into the camera the whole time. Rain falls between her and the camera. She breathes slowly. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. Her eyes are dry and calm, not crying. Glossy semi-realistic anime, as in the references.
```

### 1b · The rival's eye

Q4, 5s. Cut against 1 on the beat.

1. `rival-hood.png`
2. `rival-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the place.

Night, light rain, on the quay of the harbour in @image3, orange and cyan lights blurred far behind her. Extreme close-up of the rival's eyes and brows under the edge of her black hood, filling the frame, a strand of yellow-green hair across her forehead. Her amber eyes look straight into the camera the whole time. Rain falls between her and the camera. She breathes slowly. The camera holds still.

She keeps the face of her references for the whole clip. Her eyes are dry and calm. Glossy semi-realistic anime, as in the references.
```

### 3 · The dive

Q3 Cinematic, 8s. On screen 0:08–0:17, speed-ramped. Named in the motion, the koi on the billboard came off it and swam through the air. A swimming koi is fine to keep here; the line pinning it to the screen is for a roll without it.

1. `rooftop.png`

```text
@image1 is the city.

Night, heavy rain, the near-future city of @image1. The hologram on the tower is a flat picture on a billboard screen fixed to the wall. FPV drone shot: the camera starts above the wet rooftop, tips over its edge and dives straight down the face of the tower, neon signs rushing past, then levels out just above the wet street far below and races forward. One continuous fast camera move.

Glossy semi-realistic anime, as in the reference.
```

### 5 · The agency

Q3 Cinematic, 8s. On screen 0:26–0:31. The rival's file and the turning mochi go onto the screens in the edit (M4), from `rival-face.png` and `case.png`.

1. `singer-suit.png`
2. `singer-face.png`
3. `hq.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, the agency operations room in @image3, rain on the windows. Medium shot, the singer from the waist up in her black suit and sunglasses, standing with her back to the camera, facing the huge wall of cyan hologram screens. Then she turns around to face the camera. Her hands stay down. The camera slowly pushes in.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail with its red cord. Glossy semi-realistic anime, as in the references.
```

### 5b · The sunglasses

Q4, 5s.

1. `singer-suit.png`
2. `singer-face.png`
3. `hq.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, the agency operations room in @image3. Extreme close-up of the singer's face in her dark sunglasses, the cyan hologram screens reflected in the lenses, lines of data scrolling across the reflection. Her lips stay closed. She is still. The camera holds still.

She keeps the face of her references. Glossy semi-realistic anime, as in the references.
```

### 6 · Two cups

Q3 Cinematic, 8s. On screen 0:31–0:36, 5s.

1. `tea-stall.png`

```text
@image1 is the place.

Dawn, the tea stall in @image1. Close-up of the two ceramic tea cups side by side on the worn wooden counter, full of hot green tea, steam curling up from both into the cold morning air. Light rain drips from the edge of the awning behind them, soft and blurred. The camera holds still.

Glossy semi-realistic anime, as in the reference.
```

### 7 · The pouring hand

Q3 Cinematic, 8s. On screen 0:36–0:41. The first half of the match cut into 17, so it copies the flipped 17's frame: the black sleeve, buckled at the cuff, comes in from the top, centre right; the hand grips from above, right of centre; the hilt runs from lower left to upper right; the guard and the scabbard go off to the lower left; red lanterns glow on the right. The hilt becomes the straight side handle of a kyusu teapot, gripped the same way. If the roll comes out mirrored, flip it in the edit.

1. `rival-front.png`
2. `tea-stall.png`

```text
@image1 is the rival's outfit. @image2 is the place.

Dawn, light rain, at the counter of the tea stall in @image2, pale blue morning light, a red paper lantern glowing on the right behind. Extreme close-up. The rival's right hand in the sleeve of her black coat comes in from the top of the frame and grips the long straight side handle of a small black kyusu teapot from above, the handle pointing up and to the right, the teapot at the lower left. She tilts it and pours hot green tea into a ceramic cup at the bottom left of the frame, steam rising. The camera holds still.

Only her hand, her sleeve, the teapot and the cup are in frame. Glossy semi-realistic anime, as in the references.
```

### 8 · The message

No generation. The singer and the rival are never in one frame here: the singer is at the agency (5, 5b), the rival alone at the stall (6, 6-2, 7, 8b), and the message, an old photo, lands as a hologram over her cup in the edit. Kept: `8b.mp4`, the rival's eyes on her tea, the first roll with the two tufts in frame.

Dropped: the two of them at the counter, the photo slid across (8, 8a), and the singer turning to camera at the stall (8c). Every two-person roll was stiff, sat them face to face in some and side by side in others, and kept left and right in no fixed order.

### 9 · The deal

Q3 Cinematic, 8s. On screen 0:46–0:49. The two men are used once. Kept, from the roll with the men hooded: `9.mp4`, the rival with her hood up, from 3s on, after the case stops warping, and `9-2.mp4`, her hood down so the tufts show who it is. The handover itself is cut, not generated: every roll was stiff, and Vidu drew the closed case with a wrong shape and the handle in the wrong place, having only the open case to go on. Men with their faces showing came out photorealistic, the same as the master in Midjourney, so an extra keeps his hood up or his face in shadow.

1. `rival-hood.png`
2. `rival-face.png`
3. `case.png`
4. `harbour.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the case. @image4 is the place.

Night, light rain, on the wet quay of the harbour in @image4, containers and cranes behind. Wide shot. The rival in her black hoodie, hood up, stands facing two men in dark hooded jackets, hoods up, their faces in shadow, and hands them the silver case from @image3. One of the men takes it. The camera slowly circles the three of them.

The rival keeps her face and her yellow-green hair, showing under the hood. Glossy semi-realistic anime, as in the references.
```

### 9b · The case

Q3 Cinematic, 8s. Two or three cuts out of it. The case is already open: in every roll where a gloved hand lifted the lid, the case's edges bent as it opened. A rigid box on a hinge is a motion Vidu cannot hold. The reveal comes from the edit, a flash on the cut and the push-in. Kept from the roll with the hand: `9b.mp4`, its last three seconds, after the lid stops and the edges hold still. The prompt below is for a reroll.

1. `case.png`
2. `harbour.png`

```text
@image1 is the case. @image2 is the place.

Night, light rain, on the wet concrete of the quay in @image2. Close-up from above of the silver case from @image1, already lying wide open, the lid standing still. Inside, rows of soft white rice cakes under glossy green paste glow faintly, the glow slowly pulsing. Raindrops land on the lid and run down it. The camera slowly pushes in.

Glossy semi-realistic anime, as in the references.
```

### 10 · The scope

Q3 Cinematic, 8s. On screen 0:49–0:52, one side of the split screen. The other side is a crop of 9 behind a scope overlay, made in the edit. Kept: `10.mp4`, the close one, and `10-2.mp4`, the wide on the crane. All four rolls made the black suit shine like rubber. From here on, a dark costume in rain is written as matte wool or matte cotton, `no shine`.

1. `singer-suit.png`
2. `singer-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, light rain, high on a crane above the harbour in @image3, the lit quay far below. The singer in her matte black wool suit, no shine, lies flat along the crane's steel arm and looks through the scope of a long rifle, aiming down at the quay. She stays still, only her breath moving. The camera slowly moves along her side toward her face.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail with its red cord. Glossy semi-realistic anime, as in the references.
```

### 12 · The rival looks up

Q4, 5s. On screen 0:54–0:56. She has seen the scope. The last frame freezes and her intro card builds.

1. `rival-hood.png`
2. `rival-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the place.

Night, light rain, on the quay of the harbour in @image3, lights blurred behind her. The camera looks down at her from above. Close-up from the shoulders up, the rival in her black hood, her eyes lowered. She lifts her eyes and looks straight up into the camera, and holds the look. The camera holds still.

She keeps the face of her references for the whole clip, yellow-green hair showing under the hood. Her eyes are dry and calm. Glossy semi-realistic anime, as in the references.
```

## Inserts i1–i3 · for the chorus 1 re-edit

The old clothes, on the bridge. i1 and i2 cut into 20, i3 into the end of 21. Kept: `i1.mp4` (lanterns caught in her eyes), `i2.mp4` (the matching extreme close-up; big drops now and then, so two 15-frame stretches between them) and `i2-2.mp4` (the whole face), `i3.mp4` (crop in on the guard; the veins on the back of the hand stand out) and `i3-2.mp4`.

### i1 and i2 · Eyes narrowing

Q4, 5s, one each. i1 the singer: `singer-front.png`, `singer-face.png`, `bridge.png`. i2 the rival: `rival-front.png`, `rival-face.png`, `bridge.png`. Change `the singer` to `the rival` for i2.

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred behind. Extreme close-up of the singer's eyes and brows. She narrows her eyes and stares hard into the camera. The camera holds still.

She keeps the face of her references for the whole clip. Glossy semi-realistic anime, as in the references.
```

### i3 · The grip

Q4, 5s.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4, red lanterns blurred behind. Extreme close-up of the rival's right hand on the green-wrapped hilt of her katana at her hip, the black coat sleeve at the edge of the frame, rain running off the hilt. Her hand tightens its grip. The camera holds still.

She holds only her own katana, as in @image3. Glossy semi-realistic anime, as in the references.
```

### i4 · Feet on the planks

Dropped. None of four rolls was a charge: an empty bridge, feet walking seen from the side, a full figure walking slowly. 22 is full without it.

## Shots 13–24 · pre-chorus to chorus 1

The first batch. Shot numbers match [`shotlist.md`](shotlist.md). Shot 16 is a freeze made in the edit, so it is not generated here.

Settings: Q3 Cinematic shots are **8s**. Q4 shots are **5s**. Both 1080p, 16:9, Off-Peak, audio off if there's a switch. Two or three rolls each, keep one.

Each shot lists its upload order. Upload only those images, in that order, so `@image1` onward matches. The last line of each prompt is the same stability line every time.

Shot 17 is one half of a match cut. Shot 7, the pouring hand at the stall, gets generated later to match its framing, so keep the roll whose hand sits most clearly in the frame.

### 13 · The lantern

Q3 Cinematic, 8s. On screen 0:56.01–0:58.56, 2.5s. Kept `13.mp4`.

1. `bridge.png`

```text
@image1 is the place.

Night, heavy rain, the empty footbridge in @image1. Close-up of one red paper lantern hanging from the railing. The wind swings it back and forth, rain streaking past it, its warm light sweeping across the wet planks. Shallow depth of field: everything behind the lantern is soft blurred bokeh. The camera holds still.

Glossy semi-realistic anime, as in the reference.
```

Three rolls, kept the first. Rolls 1 and 2 ran without the depth-of-field line. Roll 1: the front lantern swings most, the three behind it swing less, and even the blurred lights far back move a little, so it reads as one wind. Roll 2: the near blurred lights do not move at all. Roll 3, with the line: fine, but the water dripping off the railing slides along it.

### 14 · One more breath

Q4, 5s. On screen 0:58.56–1:01.14, 2.6s. Kept `14.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred behind her. Extreme close-up of the singer's face, rain running down it. She breathes out slowly through parted lips, a faint mist of breath in the cold air. Her eyes stay on the camera. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. Glossy semi-realistic anime, as in the references.
```

Q3 Cinematic first, by mistake, three rolls. Roll 1: the shot as asked, head to shoulders, a slight push in. The face and the shaved sides shine, which reads CG. Roll 2: a different face, and the breath mist comes out on the inhale. Roll 3: locked off and tighter, chin to just above the brow.

Then Q4, three rolls. No shine on any of them, and closer to the plates than Q3. Roll 1: very faithful to the plate, but the face is lit too bright for night. Roll 2: the tightest and the best, but Vidu adds tears running from her eyes. Roll 3: light from behind at an angle, good for night. The drops running off her face are a little heavy. Kept Q4 roll 3, `14.mp4`.

### 15 · The street goes still

Q3 Cinematic, 8s. On screen 1:01.14–1:06.86, 5.7s. Kept `15.mp4`: of four rolls, the only one with rain. She finishes lifting her eyes at about 4–5s, so the start is trimmed. Two others lift their eyes at about 4s or at the very end, with no rain. The world stops, made in the edit: the clip slows down step by step (100%, 50%, 25%) and shot 16 freezes its last frame. The slow-down starts on the first frame after her eyes have come fully up to the camera, never while they are still rising.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, the middle of the footbridge in @image3, medium shot from the front, the singer from the waist up, standing still in the centre of the deck, red paper lanterns along both railings behind her, swinging in the wind. Thin streaks of rain fall steadily the whole time, no large drops, no drops on the lens. Her eyes are lowered at first. Early in the clip she slowly lifts them to the camera and holds the look. Her hands stay empty at her sides. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail. No sword in frame. Glossy semi-realistic anime, as in the references.
```

Asking Vidu to stop the rain in mid-air did not work. Four rolls: large, unnaturally big drops pour onto the screen at 2s or 4s, before she lifts her eyes, and the lanterns keep swinging. Not kept.

Waist up, so it does not repeat 14's face close-up. No sword, because her draw is in 18.

Dropped: a dolly zoom on her face in the neon street. Neither Q3 Cinematic nor Q4 does a dolly zoom (six rolls, all plain zooms, tilts or a breaking street). Built in the edit instead, from a still face on green (Q4) keyed over `street.png`, it reads as a still image pasted on a background, and it was a second face close-up straight after 14. `15-1` to `15-3.mp4` are those green-screen rolls. Colour light asked for on her face spills onto the green and keys out as fog, so a green-screen prompt asks for neutral light.

### 17 · Draw

Q3 Cinematic, 8s. On screen from 1:08.78, up to about 1s. Kept `17.mp4`.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Extreme close-up at the rival's left hip: her katana sits in a black lacquered scabbard tied at her left hip, the green-wrapped hilt pointing forward. Her right hand rests on the hilt, the black sleeve of her coat at the edge of the frame. Her left thumb pushes the guard forward, and a short strip of bright steel slides out of the mouth of the scabbard, catching the lantern light. The sword stays in the scabbard. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, as in @image3. Glossy semi-realistic anime, as in the references.
```

Seven rolls, kept roll 6. The blade plates have no scabbard and neither outfit has one, so every draw has to name it.

1. Q3 Cinematic, no scabbard in the prompt. She pulls the sword out of her trouser pocket, and the blade is short, like a big knife.
2. Q3 Cinematic, with the scabbard. Her hand grips the wrong way round, and the blade jumps forward after the draw.
3. Q3 Cinematic. The sword draws itself.
4. Q3 Cinematic. Breaks in a way that is hard to describe.
5. Q4, a held grip ("her fingers tighten slowly on the hilt; the sword and the scabbard do not move at all"). Nothing is drawn: the blade is bare from the first frame, and the hilt bends at a right angle.
6. Q3 Cinematic, the prompt above. Kept. No thumb on the guard. She grips the hilt and pulls the blade a little way out, the ordinary way, then stops. 2–3s of usable motion. The shot is half a second on screen, so cut it from there.
7. Q4, the held grip. Two swords. The framing is not bad, but nothing is drawn.

A draw is the hardest motion in the batch. Roll it on Q3 Cinematic only, and expect to roll it many times. The full draw on screen is shot 21.

### 18 · Steel in bloom

Q3 Cinematic, 8s. On screen to 1:11.28, about 2s. Kept `18.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `blade-singer.png`
4. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, the middle of the footbridge in @image4. Close shot from the chest up, the singer centred with open sky and lanterns behind her. Her hands and the hilt stay below the bottom of the frame. The blade of her katana rises slowly up into the frame until it stands upright beside her face, the flat of the steel toward the camera, the lanterns reflected in it, rain running down it. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, as in @image3. Glossy semi-realistic anime, as in the references.
```

Two rolls of the waist-up version both turned the edge sideways and gave the hilt a long extra length below her hands, with or without a line asking for the edge forward and a short hilt. The fix is the framing. From the chest up, the hands and hilt are out of the frame. The flat of the blade faces the camera on purpose, which is the usual key-visual way to show a blade.

The chest-up roll still showed the hands and the hilt. The hilt bends only while the blade swings from diagonal to upright, and it is normal once the blade stands. The lanterns reflect in the blade. Kept. The upright part runs about 6s, and the shot is 2s on screen, so cut it from there.

The big type goes behind her in the edit, so keep a roll with sky or lanterns behind her head, not the railing.

### 19 · Red against the rain

Q3 Cinematic, 8s. On screen 1:11.28–1:13.70, 2.4s. Kept `19-1.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `singer-back.png`
4. `blade-singer.png`
5. `bridge.png`

```text
@image1, @image2 and @image3 are the singer: front, face and back. @image4 is her katana. @image5 is the place.

Night, heavy rain, wide shot from behind the singer as she stands alone at the top of the short arched footbridge in @image5, her katana held low at her side. The bridge is short: its deck curves down just ahead of her, and the far bank is close behind it. Seen from behind she looks exactly as in @image3, the white jacket covering her back down to the hips. The short red cord tied at the base of her ponytail, its ends only a hand long, and her wide sleeves blow in the wind, red lanterns glowing along both railings. The camera rises slowly above her.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana. Glossy semi-realistic anime, as in the references.
```

The first roll, without the back plate, put the sash in the wrong place on her back. The second, with the fixed back plate, was well lit and sat in the rain, but the bridge ran a long way into the distance, much longer than `bridge.png`, and the hair cord became a long red streamer. The camera rises until she is only a head at the bottom of the frame, and at the start the sash hangs below the jacket. The prompt above now says how short the bridge and the cord are. Of the two rolls with it, one failed and the other is the cleanest: whole figure, the jacket right, no sash. But the bridge is still long, the hilt is long, and the cord barely shows, so there is no red on her for the colour isolation.

Kept `19-1.mp4`. Use 2.4s from the middle, where her whole back shows, no sash hangs below the jacket, and the streamer moves without taking over. `19-2.mp4` is the clean one, kept for any later shot that needs her from behind.

The original `singer-back.png` had the jacket ending at the waist with the red sash showing, which the front plate rules out: the jacket hangs to the sash and covers it from behind. Fixed with Quick Edit: "The back of her white jacket is longer and hangs straight down to her hips, plain white fabric across her whole back and waist, with only black trousers below it. Keep everything else exactly the same." Naming the sash in an edit, even to hide it, puts it back, so the prompt does not mention it. The jacket comes out a little long, and Quick Edit will not shorten it. That does not show in a wide shot from behind. To fix it, erase the extra length in the Editor and fill it with "black wide trousers, the straight edge of a white jacket hem at the top".

### 20 · Only one walks off this bridge

Q3 Cinematic, 8s. On screen 1:13.70–1:18.75, 5s. Kept `20-2.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `rival-front.png`
4. `rival-face.png`
5. `blade-singer.png`
6. `blade-rival.png`
7. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the footbridge in @image7, seen from the side from the canal bank, extreme wide shot, the whole low arch of the bridge in frame exactly as in @image7, open night sky above the deck. The singer stands at the far left end of the bridge and the rival at the far right end, the whole length of the empty wet deck between them, both small in the frame. They face each other. The singer holds her drawn katana by its hilt, the blade pointing down at her side. The rival's katana is still in the black scabbard at her left hip, her right hand resting on its hilt. They stand still while the wind pulls at the singer's sleeves and the rival's coat and the rain pours between them. The camera pushes in slowly.

Both women keep the faces, hair and outfits of their references for the whole clip. Each has only her own katana. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

The rival's blade stays sheathed here because she draws it in shot 21, right after. The singer's is already out from shot 18.

The first roll put them a step apart in the middle of the bridge instead of at the two ends. It added a round arch frame over the deck that `bridge.png` does not have. The rival held her blade by the steel. The look was flat and off. The prompt above asks for the camera on the bank, the two of them small at the far ends, open sky over the deck, and both holding by the hilt.

Kept a later roll, about 5s usable. Side view, the low arch, the two at the ends facing each other, rain. The rival's blade is already drawn, against the note above, and the lanterns and the neon city are gone: a dark cloudy sky instead. The figures are not small, so the drawn blade shows. Accepted: shot 21 cuts in on her close and fast, and nobody tracks one blade across a cut at this speed. That roll is `20-1.mp4`, the fallback.

The keeper, `20-2.mp4`, came from a roll of a back-to-back prompt written for shot 22 and since dropped. Instead of back to back, they stand facing each other at the two ends of the deck, seen from the middle of the bridge. The lanterns line both railings and the neon city is behind them, matching shots 13, 18, 19 and 21. The rival's katana is still in its scabbard, her right hand away from it, which is what the shot needs before she draws in 21. Neither woman moves at all. For this shot that is the brief. The camera pushes in slowly by itself, and the edit adds nothing.

A two-woman wide that keeps failing can be cut as shot and reverse shot instead: each woman alone at her end, half the time each. Single-woman shots hold up better than two-woman ones.

### 21 · The rival draws

Q3 Cinematic, 8s. On screen 1:18.75–1:21.16, 2.4s. Kept `21.mp4`.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, medium shot of the rival at the right end of the footbridge in @image4. Her left hand holds the black lacquered scabbard at her left hip, her right hand grips the hilt. She draws her katana out of the scabbard and swings it out to her side in one fast motion, then holds it ready in her right hand, the long curved blade as long as her arm, the thin green line along its spine glowing in the rain. After the draw the scabbard at her hip is empty. There is only one sword.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana. She keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

The first roll looks good overall, `21.mp4`. Two faults: her supporting hand is in the wrong place during the draw, and a second sword is left in the scabbard after it. The prompt above now places her left hand on the scabbard and says the scabbard is empty after the draw. Scaling in does not hide the second sword: at 0:04 she holds it in her left hand in the middle of the frame. The second roll, with the fixed prompt, not saved, has the right yellow-green hair and her left hand on the scabbard. But a short hilt sticks out of the scabbard after the draw, so it has two swords as well. The whole flat of the blade also glows green. Kept `21.mp4` with the second sword in. It is harder to see than in any other failed draw, and after the draw she swings the blade around in big, fast moves. The motion carries the shot and hides the extra sword. Her right hand goes to the hilt and draws, so the shot starts before the draw.

### 22 · Faster than the light

Q3 Cinematic, 8s. On screen 1:21.16–1:23.67, 2.5s. Kept `22.mp4`: the charge, the clash and the lock in one clip. Same seven images, same order as shot 20.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the middle of the footbridge in @image7, medium wide, side view, low camera, the camera fixed on the centre of the deck. The singer rushes into the frame from the left edge, running to the right. The rival rushes into the frame from the right edge, running to the left. They run toward each other, not in the same direction. In the centre they swing at the same moment and their two katanas clash hard in a burst of sparks, then stay locked, blades crossed, pressing against each other. Everything happens at full real-time speed, no slow motion.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer keeps her undercut and her high black ponytail. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

Four rolls of the first version failed. It had them run in down the length of an empty bridge. In three, both ran the same way and only crossed blades partway, too slow for the 1s the shot has. In one they came in from off frame and clashed, which is the shape needed, but the singer's hair was wrong and Vidu slowed the clash down by itself. The prompt above starts on the centre of the deck, brings them in from the two edges, and spells out the directions, the hair and the speed.

The clip holds the lock after the clash, so no separate lock clip is needed. Its first second is an empty bridge and is cut. The blades hit about a second before "light," and the hit stays there: moving it would need the empty second back or a slowed run. In the edit: an afterimage on the 8 frames before the hit (the clip duplicated, two frames later, Add blend, 40%), and the white flash from the hit frame.

An earlier plan had a vanish and a back-to-back. No roll did the vanish, and a back-to-back after a flash broke the left-right order and did not lead into a smile. Both are dropped. From 21 to 24 the shots are now one exchange: she draws, they charge, the blades meet, they hold the lock, and the singer breaks it in 24. The rival's smile (`23.mp4`) is out of the cut: she is still the smuggler here.

Full-body rolls turn the sandals into heels. Add `flat black sandals, no high heels` to the outfit line of any shot that shows their feet.

### 23 · Smile at me

Q4, 5s. On screen 1:23.67–1:26.13, 2.5s. Kept `23.mp4`.

1. `rival-front.png`
2. `rival-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred behind her. Extreme close-up of the rival's face, from her chin to the top of her head, nothing below her chin in frame. Rain falls on her hair, and a few drops sit on her cheeks. Her eyes are dry and calm, not crying. The corner of her mouth slowly lifts into a small, confident smile. Her eyes stay on the camera. No sword in frame. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. She keeps the two tied tufts of short yellow-green hair. Glossy semi-realistic anime, as in the references.
```

The first roll, with "rain running down it", read as crying, and it hung a sword on her back. The prompt above crops at the chin, keeps her eyes dry, and asks for no sword in frame. "Rain running down her face" reads as tears on any close-up. Shot 14 got tears from the same line.

The second roll, with the prompt above, is the keeper, `23.mp4`. A small, sure smile, the yellow eyes and the green bob, no sword. Drops sit on her cheeks, but with the smile they read as rain. The frame cuts at the brow, so the two tufts are out of shot. Fine for a 2s face.

### 24 · Then cut me down tonight

Q3 Cinematic, 8s. On screen 1:26.13–1:32.1, 6s. Kept `24.mp4`, from 24a, the backflip: usable from start to end. Same seven images, same order as shot 20. Four versions were written, each one big move that ends on a hit; 24a worked on the first roll, so the other three were not needed. Vidu slows the clip down by itself after the blades cross. In the edit the hit goes on "tonight," with the run-up at 160% and the rest at 68% with Optical Flow, to fill the slot.

#### 24a · Backflip

The keeper, `24.mp4`, first roll. It does not do the downward cut the prompt asks for. A short lock, the backflip, then she attacks with a rising cut from below, and the rival blocks it from above. The two swap sides during the attack.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the middle of the footbridge in @image7, wide, side view, low camera. The singer on the left and the rival on the right start with their katanas locked. The singer kicks off the rival's blade and backflips away through the rain, lands crouched on the wet deck, and in the same motion springs forward and brings her katana down on the rival, who blocks it above her head. Sparks burst where the blades meet. Full real-time speed.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer keeps her undercut and her high black ponytail. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

#### 24b · Spin cut

Not rolled: 24a was kept.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the middle of the footbridge in @image7, medium wide, side view. The singer on the left and the rival on the right start with their katanas locked. The singer slips out of the lock, spins all the way around, and slashes flat across at head height. The rival bends back and the blade passes a hand's width from her face, cutting through the falling rain in a bright arc. Full real-time speed.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer keeps her undercut and her high black ponytail. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

#### 24c · Leap from the railing

Not rolled: 24a was kept.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the footbridge in @image7, wide, low camera looking up. The singer runs up onto the red railing on the left, leaps high into the air above the rival, and comes down out of the rain with her katana raised over her head, cutting straight down. The rival on the right raises her blade flat above her head and catches the blow. Sparks burst and the water on the deck explodes outward around them. Full real-time speed.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer keeps her undercut and her high black ponytail. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```

#### 24d · Shove and re-clash

Not rolled: 24a was kept.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the middle of the footbridge in @image7, wide, side view, low camera. The singer on the left and the rival on the right start with their katanas locked. They shove each other apart and both slide backward along the wet deck, water spraying. Then they both lunge back in at once and their katanas clash in the centre so hard that the rain bursts away from them in a ring. Full real-time speed.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer keeps her undercut and her high black ponytail. The rival keeps the two tied tufts of short yellow-green hair. Her hair stays above her shoulders. Glossy semi-realistic anime, as in the references.
```
