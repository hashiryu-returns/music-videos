# 0006 prompts

Plan and techniques: [`README.md`](README.md). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

## The two women

Built to read apart at a glance in a fast fight: opposite hair, opposite coat colour, one red and one cyan accent. Red belongs to the singer, so the colour-isolation shot (F11) lands on her.

| | The singer | The rival |
| --- | --- | --- |
| Hair | long straight black, high ponytail tied with a red cord | short silver-white bob, blunt bangs |
| Coat | short white jacket with wide sleeves | long black high-collared coat, open |
| Under it | fitted black high-neck bodysuit, wide black trousers, red sash | fitted dark navy bodysuit, slim black trousers |
| Mark | none | matte black cybernetic left arm with thin cyan seams |
| Feet | black sandals over black split-toe socks | the same |
| Blade | katana, red-wrapped hilt | katana, black hilt, thin cyan line along the spine |

The lyric's "sleeves torn open, sandals gone" needs a damaged set of plates later. The test uses the intact set.

## Files

Plates go in [`references/`](references/):

| File | What | Made from |
| --- | --- | --- |
| `singer-front.png` | full body, front | text, Niji 7 |
| `singer-back.png` | full body, back | `singer-front.png` |
| `singer-face.png` | head and shoulders | `singer-front.png` |
| `rival-front.png` | full body, front | text, Niji 7, styled on `singer-front.png` |
| `rival-back.png` | full body, back | `rival-front.png` |
| `rival-face.png` | head and shoulders | `rival-front.png` |
| `blade-singer.png` | her katana alone | text |
| `blade-rival.png` | the rival's katana alone | text |
| `bridge.png` | the footbridge at night, empty | text |

Ten Q4 slots out of fifteen, with room for the tea stall and the street later.

## Midjourney

Settings panel:

- Aspect **2:3** for the body plates, **1:1** for the faces, **16:9** for the bridge, **3:1** for the blades
- Stylization 250, Weirdness 0, Variety 0
- Speed **Relax**. Omni Reference is silently ignored in Fast and Draft

Every plate is on plain light grey, so Q4 takes the woman and nothing else from it. Props stay off the plates; the blades are their own references.

### 1. `singer-front.png`

Version **Niji 7**, no references. Roll until one is right, then keep that one: the same string won't give her back.

```text
modern anime illustration, anime key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, crisp high resolution, character design, full body from head to feet in frame, front view, facing camera, eye level, standing straight, arms relaxed at her sides, a young woman in her twenties, tall and lean, long straight black hair in a high ponytail tied with a red cord, sharp dark eyes, calm serious face, a short white jacket with wide sleeves over a fitted black high-neck bodysuit, wide black trousers, a red sash at the waist, black sandals over black split-toe socks, plain light grey background --no chibi, crosshatching, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon --ar 2:3
```

Reject: a sword or anything in her hands, shoes instead of sandals, a jacket that isn't white, the ponytail gone.

### 2. `rival-front.png`

Version **Niji 7**. Style Reference: `singer-front.png`, so both come from the same hand. No Omni Reference.

```text
modern anime illustration, anime key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, crisp high resolution, character design, full body from head to feet in frame, front view, facing camera, eye level, standing straight, arms relaxed at her sides, a young woman in her twenties, lean, short silver-white bob with blunt bangs, pale grey eyes, faint smile, a matte black cybernetic left arm with thin glowing cyan seams from shoulder to fingers, a long black high-collared coat worn open, a fitted dark navy bodysuit, slim black trousers, black sandals over black split-toe socks, plain light grey background --no chibi, crosshatching, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, ponytail --ar 2:3 --sw 200
```

Her left arm is on the viewer's right in a front view. Reject the cyber arm on the viewer's left, black hair, a white coat, anything that makes her look like the singer.

### 3. Back and face plates

Version **7**. For each woman, Omni Reference **and** Style Reference are her front plate. The prompt says only "the woman" and the view. Her face, hair and clothes come from the plate.

`singer-back.png` and `rival-back.png`:

```text
modern anime illustration, anime key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, crisp high resolution, character design, full body from head to feet in frame, back view, seen from directly behind, eye level, the woman standing straight, arms relaxed at her sides, plain light grey background --no chibi, crosshatching, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon --ar 2:3 --sw 200 --ow 350
```

`singer-face.png` and `rival-face.png`:

```text
modern anime illustration, anime key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, crisp high resolution, character design, head and shoulders portrait, front view, eye level, the woman looking straight at the camera, plain light grey background --no chibi, crosshatching, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature --ar 1:1 --sw 200 --ow 350
```

Check `ow` shows under the result. Missing means you're not in Relax. Reject a back plate with the face turned toward the camera, or the rival's arm switching sides. From behind, her cyber arm is on the viewer's left.

### 4. The blades

Version **7**, Style Reference `singer-front.png`, no Omni Reference.

`blade-singer.png`:

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a red-wrapped hilt, a round black guard, a long curved polished steel blade, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200
```

`blade-rival.png`:

```text
modern anime illustration, clean digital line art, thin precise black outlines, flat cel shading, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a black-wrapped hilt, a square black guard, a long curved dark steel blade with a thin glowing cyan line along its spine, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200
```

### 5. `bridge.png`

Version **7**, Style Reference `singer-front.png`, no Omni Reference. Empty, so Q4 places the women.

```text
modern anime illustration, anime key visual, clean digital line art, thin precise black outlines, flat cel shading, muted dark colours, inked backgrounds with black outlines on every edge, crisp high resolution, wide shot, eye level, a narrow arched wooden footbridge over a dark canal, the whole bridge in frame from one bank to the other, red paper lanterns hung along both railings glowing warm, heavy rain, the wet planks shining, a near-future city at night behind it, elevated highways on concrete pillars, tall towers covered in neon signs and hologram billboards in cyan and magenta, their light reflected in the canal --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --sw 200
```

Signs come out as fake script. Fine as long as no real word or logo is readable.

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

The prompts use the API's `[@reference_image_N]` tags. In the web app, swap each one for whatever tag the image gets when you upload it. Each image has one role, stated once at the top. Every prompt closes with the same stability paragraph.

Pass: both faces still match their face plates at the last frame, one blade each, the rival's cyber arm on the left. A fail tells us which of the three is the problem: the close contact, the travel, or the multi-shot.

### Test 1 · Locked blades, close (5s)

Close contact, two faces in one frame. The hardest frame for keeping two identities apart.

```text
[@reference_image_1], [@reference_image_2] and [@reference_image_3] are the singer: front, back and face. [@reference_image_4], [@reference_image_5] and [@reference_image_6] are the rival: front, back and face. [@reference_image_7] is the singer's katana. [@reference_image_8] is the rival's katana. [@reference_image_9] is the place.

Night, heavy rain, the middle of the footbridge in [@reference_image_9]. Close-up from the side at eye level: the singer on the left, the rival on the right, their katanas crossed and locked between their faces. They push against each other, blades grinding, sparks spraying from the contact point, rain bouncing off the steel. The camera holds steady.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana in both hands. The rival's cybernetic arm is her left arm. Flat anime cel shading and black outlines as in the references.
```

### Test 2 · Leap and parry, wide (8s)

Travel across the bridge, two actions. Feet slide in Vidu, so both actions start and end in the air or on a landing.

```text
[@reference_image_1], [@reference_image_2] and [@reference_image_3] are the singer: front, back and face. [@reference_image_4], [@reference_image_5] and [@reference_image_6] are the rival: front, back and face. [@reference_image_7] is the singer's katana. [@reference_image_8] is the rival's katana. [@reference_image_9] is the place.

Night, heavy rain, the footbridge in [@reference_image_9], seen from the side, wide, the whole bridge in frame, the two women small against the city. The singer leaps from the left end of the bridge high into the air and brings her katana down at the rival, who raises her katana and blocks it in a burst of sparks. Then the rival throws her off, and the singer flips backward through the air and lands crouched on the railing. The camera tracks sideways with the leap.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana. The rival's cybernetic arm is her left arm. Flat anime cel shading and black outlines as in the references.
```

### Test 3 · Four shots in one take (16s)

The plan's assumption: one 16s take cut into pieces keeps the faces from shot to shot. Four shots of about 4s, each with one action.

```text
[@reference_image_1], [@reference_image_2] and [@reference_image_3] are the singer: front, back and face. [@reference_image_4], [@reference_image_5] and [@reference_image_6] are the rival: front, back and face. [@reference_image_7] is the singer's katana. [@reference_image_8] is the rival's katana. [@reference_image_9] is the place.

Night, heavy rain, the footbridge in [@reference_image_9]. Four shots.

Shot 1: close-up of the rival's face, rain running down it, her eyes narrowing as she looks at the camera.
Shot 2: from behind the singer, the rival at the far end of the bridge sprinting straight at her, katana low, coat flying.
Shot 3: side view, medium wide, the two women dash past each other and slash once, a flash of sparks between them, and both stop back to back with their blades out to the side.
Shot 4: slow push-in on the singer's face, calm, rain falling, a red lantern swinging behind her.

Both women keep the faces, hair and outfits of their references in every shot. Each holds only her own katana. The rival's cybernetic arm is her left arm. Flat anime cel shading and black outlines as in the references.
```

Note what each take got right and wrong here, so the lesson goes into DESIGN.md.
