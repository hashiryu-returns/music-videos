# FR prompts

The Midjourney and Vidu record for « Je m'arrête pas ». The plates and stills on disk are canonical. These strings are how they were made, and rerunning them won't reproduce the same image. Settings and the reasons behind them are in [`../DESIGN.md`](../DESIGN.md). The Seedance prompts are in [`README.md`](README.md#seedance-25-prompts).

## Midjourney settings

V7, Standard (not Draft), Raw off, Landscape 16:9 for scenes (9:16 for plates), Stylization 230, Weirdness 0, Variety 0, **Speed Relax**: Omni Reference is silently ignored in Fast. Style Reference `characters/style-sheet.png` on every still except #11. Omni Reference is the character plate at the strength listed with each scene, and empty when no plated character is in frame.

Style block, at the start of every prompt:

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail
```

## Vidu settings

Image to Video (not References to Video), Q2, 1080p, Cinematic, Amount 1, 4s unless the scene says otherwise. Frame 1 is the still. Multi-image scenes load the stills in order. The prompt is the single English motion line. #14 was redone on Q3.

## Plates


### her-full.png

Niji 7, 9:16, `--s 230`. Later stills use `characters/style-sheet.png` as Style Reference.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of an adult woman, standing upright, eye level camera at her chest height, straight on level view, her whole body from the top of her head to the soles of her feet inside the frame, empty margin above her head and below her feet, arms relaxed at her sides, empty hands, sharply drawn face, detailed eyes with a defined upper lash line and a bright highlight, defined eyelids, shaped dark eyebrows, defined nose bridge, clearly drawn lips, defined jaw, high cheekbones, light olive skin, confident level expression, side-shave undercut hairstyle, both temples and the nape shaved down to the skin, ears fully exposed, the rest swept back and tied high into one thick glossy black ponytail hanging down behind her, one small pearl stud in the exposed ear, a matte black japanese kimono tailored for fighting, cut close to the body, the left front panel crossed over the right in a deep diagonal V from the throat down to the sash, that overlap plainly visible, a thin crimson under-collar line along the overlap, narrow straight tube sleeves to the wrist, plain unpatterned black cloth, a wide gold obi tied with a knot at the front, a short kimono hem over close-fitting black hakama, black leather tekkou on the backs of both hands, plain black tabi boots, black shin wraps, plain light grey backdrop, even flat lighting
```

### her-back.jpeg

V7, `--oref her-full.png --ow 350`, `--sref style-sheet.png`.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of the same woman seen from directly behind, back view, the back of her head toward camera, standing upright, eye level camera at her chest height, her whole body from the top of her head to the soles of her feet inside the frame, empty margin above her head and below her feet, arms relaxed at her sides, empty hands, wearing exactly the same black kimono and gold sash as the reference, plain light grey backdrop, even flat lighting --s 250 --ow 350 --no her face visible, turning her head, looking over her shoulder, front view, three quarter view, profile, high angle, bird's eye view, feet out of frame, cropped at the ankles, background scenery, watermark
```

### panda.png

V7, `--sref style-sheet.png`.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of an anthropomorphic giant panda, adult male, soft rounded body, round belly, gentle appealing face, round black eye patches, warm dark eyes, small black ears, a soft sheepish half smile, a plain dark kimono and hakama, standing on two feet, arms relaxed, empty hands, eye level camera, straight on level view, his whole body from the top of his head to the soles of his feet inside the frame, empty margin above his head and below his feet, plain light grey backdrop, even flat lighting --s 250 --no grumpy, scowling, frowning, angry, grizzled, scarred, weathered, fierce, shaggy matted fur, bear man, warrior, muscular, high angle, bird's eye view, feet out of frame, cropped at the knees, close up, bust shot, human face, human skin, suit and tie, office, monitors, desk, glasses, hat, armor, chibi, mascot, plush toy, children's picture book, disney, pixar, dreamworks, thin uniform outlines, soft airbrush gradient, flat simple shading, dot eyes, 3d render, photorealistic, background scenery, watercolour wash, watermark
```

### hedgehog.png

V7, `--sref style-sheet.png`.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of a small anthropomorphic hedgehog girl, five years old, unmistakably a hedgehog, a dense cape of short stiff brown and cream spines covering her crown, her back and her shoulders, all the spines swept straight back off her face, short soft cream fur on her face and belly, a small rounded snout with a tiny black nose, small round ears, large warm dark eyes, soft cheeks, small clawed paws, large head, small thin body, a red cape, bare feet, one paw raised as if giving an order, bossy but sweet, standing on two feet, eye level camera, straight on level view, her whole body from the top of her head to the soles of her feet inside the frame, empty margin above her head and below her feet, plain light grey backdrop, even flat lighting --s 250 --no human girl, human child, human face, human skin, human hair, hair tie, elastic, ponytail, ferret, meerkat, otter, mouse, rat, squirrel, porcupine, long quills, grumpy, scowling, fierce, adult, teen, tall, sword, armor, four legs, feral, baby, crying, high angle, bird's eye view, feet out of frame, cropped at the knees, close up, bust shot, chibi, mascot, plush toy, children's picture book, disney, pixar, dreamworks, thin uniform outlines, soft airbrush gradient, flat simple shading, dot eyes, 3d render, photorealistic, background scenery, watercolour wash, watermark
```

### fox.png

V7, `--sref style-sheet.png`.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of a chubby two-year-old anthropomorphic fox kit, appealing round face, large warm eyes, large head, short soft muzzle, bright orange fur, white chest, round belly, a small kimono with a diaper visible at the hem, bare feet, mouth wide open mid-demand, unmistakably a fox, standing on two feet, eye level camera, straight on level view, his whole body from the top of his head to the soles of his feet inside the frame, empty margin above his head and below his feet, plain light grey backdrop, even flat lighting --s 250 --no human child, human face, human skin, human hair, grumpy, scowling, fierce, grizzled, scarred, sharp fangs, teen fox, slim, adult, four legs, feral, on someone's back, baby sling, carrier, sword, armor, high angle, bird's eye view, feet out of frame, cropped at the knees, close up, bust shot, chibi, mascot, plush toy, children's picture book, disney, pixar, dreamworks, thin uniform outlines, soft airbrush gradient, flat simple shading, dot eyes, 3d render, photorealistic, background scenery, watercolour wash, watermark
```

### aramis.png

V7, `--sref style-sheet.png`. No `--no`: the moderator blocked every dog prompt that had one.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of a long-furred black show Pekingese in full show grooming, the whole dog in frame seen from the side, standing square on all four paws, all four paws inside the frame, eye level camera, a silky well groomed show coat brushed out and sweeping down to the ground, clean glossy fur, a thick mane framing a bare neck with nothing worn on it, heavily feathered ears hanging past the jaw, a full plumed tail carried up over the back, flat pushed-in face, large warm dark eyes, appealing, plain light grey backdrop, even flat lighting --s 250
```

### daru.png

V7, `--sref style-sheet.png`. No `--no`. The text says silver grey; the plate came out cream-gold sable with a full black mask, and the plate is canonical.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, full length character sheet of a long-furred grey sable show Pekingese in full show grooming, silver grey coat with darker sable shading through the tips, a dark black mask across the muzzle and around the eyes, the whole dog in frame seen from the side, sitting, all four paws inside the frame, eye level camera, a silky well groomed show coat brushed out and sweeping down to the ground, clean glossy fur, a thick mane framing a bare neck with nothing worn on it, heavily feathered ears hanging past the jaw, a full plumed tail carried up over the back, flat pushed-in face, large warm dark eyes, appealing, calm and content, plain light grey backdrop, even flat lighting --s 250
```

## Scenes

Scenes 1–26 and 28–30. 27, 31, 32 and 35 are Seedance. 33, 34 and 36 have stills but no recorded prompt string.

### 1 · the sword on the stand

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, interior of a clean traditional Japanese washitsu at dawn, a single sheathed sword resting horizontally on a low black lacquered katana stand, black lacquer scabbard, gold braided hilt, round iron guard, the sword shut inside the scabbard, low camera close to the stand, dark polished wooden floorboards, behind it an intact white paper shoji screen with a fine dark wood lattice, the paper opaque and softly glowing with warm dawn light from outside, a long soft shadow across the boards, tidy and undamaged, calm --ar 16:9 --no hand, hands, fingers, arm, person, figure, face, drawn sword, unsheathed, exposed steel, blood, red splatter, red paint, red stain, ruin, ruined, abandoned, derelict, rubble, debris, broken glass, broken window, factory, warehouse, industrial, peeling paint, sky, sunset, clouds, outdoors, dirt, battlefield, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

### 2 · the village outside

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, wide establishing shot from inside a dark doorway looking out at dawn, a medieval French hill village below, steep slate roofs and half-timbered houses, a narrow stone street winding down, thick mist lying in the valley, pale orange sunrise behind the rooftops, the black doorframe framing the edges of the picture, empty street, still and quiet before the day starts --ar 16:9 --no person, figure, crowd, cars, modern buildings, power lines, pagoda, temple, cherry blossom, castle, dragon, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `Thick mist rolls slowly through the valley from right to left, drifting between the rooftops and thinning as it goes. The street stays empty.`

### 3 · her back

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-back.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, full length from behind, standing alone in the interior of a clean traditional Japanese washitsu at dawn, dark polished wooden floorboards, an intact white paper shoji screen with a fine dark wood lattice ahead of her filled with pale morning light, a sheathed sword in a black lacquer scabbard with a gold-braided grip at her left hip, empty floor around her boots, tidy and undamaged, seen entirely from behind, the whole figure from head to boots inside the frame --ar 16:9 --no front view, three quarter view, turning around, looking back, cropped, drawn sword, unsheathed, blood, red splatter, red stain, ruin, ruined, derelict, rubble, debris, broken window, factory, industrial, dirt, sand, battlefield, outdoors, sky, sunset, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `Her hanging sash and hair sway once and settle.`

### 4 · drawn blade

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, extreme close on a spotless mirror-polished sword blade crossing the frame diagonally, freshly cleaned steel, the temper line visible along the cutting edge, pale 6am light running the length of the edge, the hilt continuing out of the frame, behind it slightly out of focus an empty black lacquer scabbard lying on a low black lacquered katana stand, interior of a clean traditional Japanese washitsu, dark polished wooden floorboards, an intact white paper shoji screen softly lit from outside, tidy and undamaged, quiet early morning --ar 16:9 --no hand, hands, fingers, arm, person, figure, face, blood, red splatter, red stain, stains, rust, notches, chips, ruin, ruined, derelict, rubble, debris, broken window, factory, industrial, battlefield, dirt, outdoors, sky, sunset, wide shot, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `She lowers the blade once to a downward ready angle.`

### 5 · fox alone

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `fox.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, a small orange fox kit standing in a kitchen doorway, head tilted back, eyes squeezed shut, brows pushed up in the middle, mouth wide open in a loud wail, both small arms raised up toward the viewer wanting to be picked up, white chest, red jacket, blue wrap, dawn interior behind, alone, seen from the waist up --ar 16:9
```

Vidu: `The fox kit yells, arms reaching higher, ears twitching.`

### 6 · Aramis alone

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `aramis.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, a long-furred black Pekingese sitting on a wooden kitchen floor in front of a closed door, seen from the side, the neck bent right back so the muzzle points straight up at the ceiling, jaws wide open in a long howl, eyes shut, a thick ruff of fur covering the whole throat, alone, dawn, the whole dog from ears to paws inside the frame --ar 16:9
```

Vidu: the prompt asked for a howl and the take came back as a bark. It was kept, because at 1.4s `Le chien pleure` only needs noise.

### 7 · tea

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, close on a ceramic tea bowl on a plain wooden kitchen table, thin steam rising, dawn, an empty French farmhouse kitchen with plaster walls and a panelled door behind, quiet, nobody home --ar 16:9 --no person, figure, man, woman, face, portrait, hat, sharp background, second bowl, tatami, shoji, low table, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The steam above the tea bowl rises and curls upward, thinning and fading away.`

### 8 · hedgehog alone

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `hedgehog.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, a small hedgehog standing on two feet in an empty French farmhouse kitchen with plaster walls and a panelled door behind, red cape, one arm thrown straight up above her head, cream face and belly, alone, giving an order, the whole hedgehog inside the frame --ar 16:9
```

Vidu: `She swings the raised arm down and points straight ahead. The red cape lifts.`

### 9 · he landed

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `fox.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, low camera down at floor level, a small orange fox cub lying flat on his front on a French farmhouse kitchen floor, both arms still stretched out ahead of him along the boards, cheek resting on the floor, ears flattened back, red jacket, blue wrap, white chest, dawn light across the floorboards, alone --ar 16:9
```

Vidu: `The fox cub slowly lifts his head up off the floor, his ears twitching.`

### 10 · her face

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-face.png`, strength **330** — **not `her-full.png`**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, close up of her face, flat expression, mouth closed, looking slightly off camera, dawn light --ar 16:9 --no red kimono, red robe, red garment, red clothing, smile, laughing, crying, wide shot, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `She blinks once.`

### 11 · the wall goes

- **Style Reference:** **empty**
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, low angle inside a French farmhouse kitchen, a man-sized ant stands upright on two legs on the floorboards in the middle of the room, glossy black chitin skin, a segmented insect abdomen, a huge ant head with curved mandibles bent antennae and compound eyes, extra insect arms raised, it stands as tall as the doorway, behind it a ragged hole blown through the plaster wall with broken lath and dust still hanging in the air, an overturned wooden chair, hard daylight cutting through the dust, dim interior --ar 16:9 --no red, flowers, blossom, blood, gore, corpse, knight, helmet, visor, cape, sword, metal armour, steel, human face, person, fur, dog, crawling on the wall, clinging to the wall, four legged, tiny insect, macro, cockroach, beetle, landscape, horizon, open sky, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The dust and plaster blow toward the camera as the ant pushes forward through the wall.`

### 12 · the hedgehog runs

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `hedgehog.png`, strength **200**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, full length side view, a small anthropomorphic hedgehog girl sprinting hard from right to left across a wrecked French farmhouse kitchen, both feet off the ground mid stride, spines on her back, the whole body inside the frame, plaster dust and an overturned wooden chair on the floorboards, dim interior, empty doorway ahead of her --ar 16:9
 --ar 16:9
```

Vidu: `The hedgehog sprints left across the room.`

### 13 · the fox runs

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `fox.png`, strength **200**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, low wide angle down at floor height inside a wrecked farmhouse hallway, on the left a small anthropomorphic fox cub in a short child's kimono running toward the camera with both feet off the ground, on the right two man-sized black ants standing upright on two legs striding after him, glossy black chitin, huge ant heads with curved mandibles and bent antennae, extra insect arms, they are twice his height and fill the right half of the frame, splinters and plaster across the floorboards, hard daylight through a broken wall --ar 16:9
 --ar 16:9
```

Vidu: `The fox cub runs toward the camera as the dust rolls forward behind him.`

### 14 · up the stairs

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-back.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, seen from behind and slightly below, she climbs a narrow wooden staircase inside a French farmhouse, a katana with a black lacquer scabbard and a gold-wrapped hilt resting sheathed over her right shoulder, her other hand on a worn wooden banister, plaster walls close on both sides, the stairs turning out of sight above her, the whole figure from head to hem inside the frame, dim midday light from a small window --ar 16:9 --no front view, three quarter view, turning around, looking back, drawn sword, unsheathed, bare blade, red kimono, red robe, red garment, red clothing, tatami, shoji, Japanese house, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `Her hem and hair swing as she climbs up and away from the camera.`

### 15 · run into the demon

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-full.png`, strength **280** on both frames
- **Multi-image.** Locked stills: `stills/15a.jpeg` → `stills/15b.png`

Prompt not recorded; the still on disk is the record.

Vidu: `She runs forward along the ridge and encounters a flying monster ahead.`

### 16 · Aramis casts

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `aramis.png` **only**, strength **280**

Prompt not recorded; the still on disk is the record.

Vidu: `He casts a spell. A magic circle flares under him and an energy ball shoots straight out along the ridge at lightspeed.`

### 17 · the orb lands

- **Still:** reuse `15b.png` (identical to `17.png`). No new Midjourney render.

Vidu: `An energy ball smashes the monster. It flashes and bursts apart into ash.`

### 18 · switch to Daru

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `daru.png`, strength **200**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, a cream and gold sable long-furred Pekingese with a full solid black face mask sitting upright on a grey slate roof ridge, seen from the side, full body from ears to paws, looking away along the ridge the way someone just ran, the long coat brushed and well groomed, a thick ruff of fur covering the whole throat, bright daylight, medieval French rooftops below, alone --ar 16:9
```

Vidu: `His long fur lifts and settles in the wind.`

### 19 · walk into a hero stop

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-full.png`, strength **330** on both frames
- **Multi-image.** Start `19a.png` / end `19b.png`. One Vidu clip. Trim to 4.1s — take the useful middle of the morph, not the settled end if it wobbles.

**Start (A)**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, full length three-quarter view, she walks along a grey slate roof ridge toward the camera, mid-stride with the trailing foot pushing off the tiles, wearing a black kimono whose long wrapped skirt falls to her ankles, plain black tabi boots, a crimson sash wrapped at her waist with its end trailing and a gold sash knotted over it, drawn sword low at her side, her hair and the black hem streaming back behind her, the ridge line running across the frame under her feet, medieval French rooftops and chimneys spread out below, pale afternoon sky, clean air, no debris --ar 16:9 --no red skirt, red hem, red dress, standing still, feet together, beast, monster, ash, smoke, red sun, red disc, bare legs, trousers, pants, hakama, white socks, red kimono, red robe, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

**End (B)**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, low camera looking up at her standing planted on a slate roof ridge against open sky, facing the camera, feet together, wearing a black kimono whose long wrapped skirt falls to her ankles, plain black tabi boots, a crimson sash wrapped at her waist and a gold sash knotted over it, drawn sword held down at her side, hair and hem still, pale blue and gold afternoon sky with scattered cloud behind her, the edge of the slate ridge in the bottom of the frame, clean air, no debris --ar 16:9 --no red skirt, red hem, red sun, red disc, rising sun flag, sunset, beast, monster, ash, smoke, walking, running, bare legs, trousers, pants, hakama, white socks, red kimono, red robe, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: load A then B. Prompt: `She walks forward along the roof ridge, turns to face the camera and comes to a stop, her hair and black hem swinging and settling.` Generate 5s if the UI offers it, then trim to 4.1s — keep the walk and the plant, cut before a broken end.

### 20 · the whole village below

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, sweeping wide panorama from the top of a slate roof out over a whole medieval French hill village, the grey slate tiles and ridge of that roof across the bottom of the frame in the foreground, beyond it hundreds of mostly grey slate rooftops with a few red tiled roofs mixed in among them, half-timbered houses with pale grey stone walls spreading away down the hillside, chimneys with thin trails of smoke rising, lines of washing strung between the upper storeys, a stone church tower rising out of the middle of the town, green valley and low hills on the horizon, birds circling over the roofs, bright daylight with the sun high overhead, clear pale blue sky --ar 16:9 --no all red roofs, terracotta town, orange rooftops everywhere, mediterranean village, tuscan village, gate, gatehouse, archway, stone arch, town wall, city wall, fortress, castle, rampart, narrow alley, narrow street, close walls, night, nighttime, dusk, twilight, evening, sunset, late afternoon, dark sky, moon, lamp, lantern, street lamp, person, figure, human, crowd, face, beast, monster, pagoda, temple, torii, Japanese buildings, red banner, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The chimney smoke drifts upward, the hanging washing sways, and the birds glide across over the rooftops.`

### 21 · the dog leads

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `aramis.png`, strength **200** — lower than usual, because the plate is a portrait and this shot needs the whole animal

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, low camera set at ground level in a narrow cobbled village alley that slopes gently downhill in one smooth unbroken surface and bends out of sight behind the houses further up, a long-furred black Pekingese seen almost in profile and turned only slightly toward the camera so the entire length of his body is visible from chest to tail, standing off to one side of the frame in the lower third with the alley curving away behind him, an extremely low long-bodied dwarf dog whose body is far longer than it is tall, a heavy broad chest carried low and forward, the back long and level, all four feet flat on the cobbles and the weight leaning onto the near side, very short thick bowed legs completely hidden because the long show coat hangs all the way down to the stones with no daylight under the body and only the front toes showing, the coat skirt pooling and trailing on the cobbles behind him, the plumed tail curled up over the back, a thick ruff of fur covering the whole throat, a solid black coat with only a pale blonde fringe on the ear feathering, the long ear feathering hanging past his chest, his shoulder no higher than the stone doorstep beside him, a small wooden crate against the wall taller than he is, half-timbered French houses leaning tight on both sides, washing lines strung overhead, slate rooftops of the lower village beyond the bend, bright midday light, alone --ar 16:9 --no sitting, seated, sitting up, on his haunches, front view, head on, symmetrical, facing the camera directly, centred, round body, ball of fur, long legs, leggy, tall legs, high stance, visible thigh, visible upper leg, daylight under the body, gap under the body, lifted paw, raised paw, terrier, pomeranian, spitz, shiba, borzoi, tall dog, large dog, giant dog, oversized, leaping, running, stairs, steps, staircase, treads, kerb, ledge, collar, lead, leash, harness, second dog, cream coat, gold coat, parti colour, white patches, person, figure, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The dog comes slowly toward the camera with a heavy side-to-side rolling waddle, his body swaying, his long coat skirt sweeping the cobbles and his ear feathering bouncing, the washing swaying overhead. His legs stay hidden under the coat.` Trim to 1.4s. Do not extend; the lyric slot is intentionally fast. **Reject any take with a long reaching stride** — once the legs extend the breed reads wrong, and no trim saves it.

### 22 · the neighbours turning

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty.** No plated character in this shot.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, medium wide symmetrical shot, camera at eye level, four turned villagers standing close together across a narrow cobbled French village street and facing the camera straight on, full length, filling the width of the frame, nobody else anywhere in the picture, all four of them fully grown adults, gaunt with ashen grey skin, blank pale eyes with no pupils, mouths cut a little too wide, long thin arms hanging at their sides, all four of them dressed only in the soft cotton sleepwear they went to bed in, loose baggy one-piece cotton sleepsuits and buttoned pyjama jackets with elasticated cuffs at the wrist and ankle, two of them in an all-over repeating nursery print of small brown cartoon teddy bears on pale yellow cotton and two of them in an all-over repeating nursery print of small red cartoon rabbits on pale blue cotton, the kind of pattern printed on children's bedding, the print dense and clearly visible across the whole garment, bare grey feet on the cobbles, nothing on their heads, one of them tall and heavy, one of them stooped and elderly, two of them women, all four dead still and staring blankly straight into the camera, leaning half-timbered houses close on both sides behind them, bright flat midday light --ar 16:9 --no plain fabric, unprinted, solid colour clothing, boiler suit, overalls, prison uniform, western, cowboy, cowboy hat, wide brimmed hat, stetson, hat, cap, bandana, neckerchief, scarf, denim, jeans, boots, shoes, slippers, waistcoat, coat, jacket over the top, gunslinger, high noon, frontier town, dusty street, desert, child, children, kid, boy, girl, toddler, family, crowd, mob, many people, background figures, parade, procession, foreground figure, hero shot, cape, superhero, seen from behind, facing away, backs to the camera, group photo, katana, sword, samurai, armour, identical faces, repeated character, clones, mask, costume, clown, harlequin, jester, carnival, fancy dress, robe, cloak, kimono, monk, uniform, werewolf, four legs, fur, walking, running, chasing, comic pose, funny face, smiling, waving, blood, gore, wounds, severed, corpse, red on the ground, red splatter, ash, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, lettering, watermark
```

Vidu: `The four turned villagers stare into the camera without moving, only their loose pyjamas and hair stirring in the air.` Trim to 1.4s. Ken Burns the push in the editor, not in Vidu. **Reject any take where someone walks, waves or reacts.**

### 23 · the third carriage of the year

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty** on both frames. No plated character.
- **Multi-image.** Two stills, one Vidu clip. Add a middle frame only if A→B stutters.

**Start (A)**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, a narrow cobbled French village street, an ornate gilded French carriage with gold scrollwork and red lacquered wheels small in the distance far up the lane coming toward the camera, completely whole and undamaged, no driver and no horses, dark empty doorways along both sides, half-timbered houses tight on both sides, bright midday light --ar 16:9 --no woman, sword, katana, warrior, heroine, driver, coachman, horse, person, figure, drawn sword, damage, split, broken, debris, smoke, flash, light beam, boar, beast, blood, red splatter, pagoda, Japanese buildings, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

**End (B)**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, the identical camera on the same narrow cobbled village street, the same ornate gilded French carriage with gold scrollwork and red lacquered wheels now large and rushing toward the camera filling the lane, completely whole and undamaged, no driver and no horses, the same dark empty doorways, the same half-timbered houses tight on both sides, bright midday light --ar 16:9 --no woman, sword, katana, warrior, heroine, driver, coachman, horse, person, figure, drawn sword, damage, split, broken, debris, flash, light beam, boar, beast, blood, red splatter, pagoda, Japanese buildings, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: A into Frame 1, B into Frame 2, prompt `The gilded carriage rushes up the empty lane toward the camera and sweeps through.` Trim the 4s take to 2.6s. If it stutters, generate a middle still with the carriage at half distance — same camera, same empty doorways — and load A, middle, B.

### 24 · the empty corner house

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty.** No plated character.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, an abandoned corner house on a cobbled French street with a dark wide open doorway and nothing inside it, boarded shutters hanging loose, one glassless upstairs window with a torn grey curtain spilling out over the sill, weeds in the gutter, the house in cold flat shade while the street beyond it stays in bright midday sun, half-timbered houses further down the lane, no people --ar 16:9 --no figure in the doorway, person in the doorway, woman, sword, katana, monster, creature, silhouette, shadow figure, face, eyes, drawn sword, blood, gore, corpse, red on the ground, ash, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The torn curtain drifts out of the upstairs window and dust turns slowly in the dark empty doorway.` Trim to 2.9s.

### 25 · she looks up

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `her-full.png`, strength **200**. Low on purpose — see the framing note. 280 and 330 both reproduce the plate's own full-body crop.

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, wide establishing shot of a narrow cobbled French village street with the entire two-storey half-timbered house in frame from the cobbles right up to its roofline and the sky above it, and small down on the street below she is walking left to right in profile, no taller than a third of the frame, her near foot lifted off the cobbles in mid-stride, her head thrown back so the underside of her chin is visible, her face turned up toward a dark open first floor window high on the wall above her, a sheathed katana at her hip, the window a black opening with no lamp, the house whole and undamaged, wide empty cobbles around her, bright flat midday sunlight, alone --ar 16:9 --no looking at the camera, eye contact, head-on, facing the camera, front view, close-up, close up, portrait, filling the frame, large in frame, cropped roof, second figure, monster, crowd, pot, flowerpot, planter, objects in the air, lamplight, lit window, warm glow, interior light, candle, lantern, ruin, ruins, rubble, broken wall, collapsed, derelict, standing still, planted square, drawn sword, unsheathed blade, bare blade, wolf, dog, four legs, fur, animal, blood, gore, ash, splinters, bare legs, red kimono, red robe, red garment, red clothing, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `She walks slowly, slowing further, looking up, as scraps of torn cloth and bits of rubbish fall past in front of her from above. Her hem and hair swing. Nothing hits her.` Trim to 2.8s. **Reject any take that stops her dead or that has the rubbish strike her.**

### 26 · the question

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, inside the apse of a vast gothic cathedral, a single tall priest-like sorcerer standing alone behind a carved stone altar and facing the camera, wrapped from shoulders to floor in a heavy black ritual robe with a deep hood, the hood casting absolute black shadow over both eyes while only a pale mouth and chin are visible below it, holding a large open ancient scripture-like leather book at chest height with both hands beneath it, pointed arches, candles, crosses and stained glass rising behind the altar, cold coloured light, ominous and still --ar 16:9 --no visible eyes, eye glow, uncovered head, detailed face, ordinary modern priest, cassock, suit, dog, animal, woman, warrior, katana, second person, crowd, readable text, letters on pages, blood, gore, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, watermark
```

Vidu: `The hooded figure's visible mouth moves as he asks the question; the robe hem and candle flames stir. His eyes stay hidden. The camera does not move.` Trim to 2.3s. Keep the hold; do not invent a second action.

### 28 · the robe comes off

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty** on both frames
- **Multi-image. Two stills, one clip, 4.1s.** Generate 5s if the UI offers it, then trim. Generate A first, then edit only the body for B.

**Still A**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, fixed camera inside the apse of a vast gothic cathedral, a single tall priest-like sorcerer standing behind a carved stone altar and facing the camera, both arms raised as the heavy black ritual robe begins to spread open and slip from the shoulders, deep hood still casting absolute shadow over both eyes with only the pale mouth and chin visible, the large open ancient leather book falling through the air in front of the altar, the same pointed arches, candles, crosses and stained glass behind him --ar 16:9 --no visible eyes, demon body, monster skin, wings, horns, claws, dog, animal, second figure, crowd, woman, katana, blood, gore, readable text, letters on pages, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, watermark
```

**Still B**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, the identical fixed camera in the same cathedral apse, the same carved stone altar still in frame below, a single huge charcoal grey winged demon airborne above that altar facing the camera, long curved horns, blank burning eyes, heavy leathery wings spread wide across the vault, the torn black ritual robe falling away beneath him as cloth, the same pointed arches, candles, crosses and stained glass unchanged --ar 16:9 --no priest, human face, hood, dog, animal, second figure, crowd, woman, katana, blood, gore, severed, corpse, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The heavy robe tears away and a winged demon rises from it, climbing into the air above the altar with wings opening. The book and robe fall. The room and camera stay fixed.` Trim to 4.1s.

### 29 · Daru casts

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** `daru.png`, strength **330**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, tight low close up of a single long-furred Pekingese filling the frame against a plain black background, cream and gold sable coat with a full black face mask, head tilted up, long ear feathering and coat lifting, many small blue-white points of light gathering in the air around him and caught in his fur, cold blue rim light along his back, nothing else in the picture --ar 16:9 --no architecture, cathedral, pillars, window, room, second dog, black dog, person, woman, demon, orange, fire, flame, beam, blast, explosion, ball of light, thin uniform outlines, soft airbrush gradient, flat simple shading, dot eyes, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The blue-white points of light rush inward and bloom into a sphere of cold holy light around the dog, his fur blown back by it. No beam leaves the frame.` Trim to 3.2s.

### 30 · the cathedral goes

- **Style Reference:** `style-sheet.png`
- **Omni Reference:** **empty**

```text
seinen manga illustration, dramatic anime key visual, bold heavy black ink outlines with varying line weight, hard edged cel shading, strong dark cast shadow shapes, rich deeply saturated colour, high level of detail, cinematic 16:9, very wide distant view across an empty stone square of an entire vast gothic cathedral standing completely whole and undamaged, both square west towers and the tall central spire fully in frame with generous open sky above and empty paving below, great rose window, carved saints, flying buttresses and tall crosses, doors shut, flat overcast afternoon light --ar 16:9 --no fire, flames, smoke, explosion, blue light, glow, damage, cracks, rubble, ruin, collapsed, debris, cropped towers, cropped spire, close up, person, figure, woman, dog, crowd, thin uniform outlines, soft airbrush gradient, flat simple shading, disney, 3d render, photorealistic, readable text, watermark
```

Vidu: `The cathedral explodes violently from inside, blue-white fire bursting through the rose window, doors and roof, the central roof lifting as stone debris and smoke drive outward. Both towers remain visible and the camera does not move.` Trim to 4.5s.
