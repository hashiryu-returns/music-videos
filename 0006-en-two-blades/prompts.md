# 0006 prompts

Plan and techniques: [`README.md`](README.md). Shots and cutting: [`shotlist.md`](shotlist.md). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

In order: what to generate next, the rules every Vidu prompt follows, the cast and their plates, then every shot in timeline order with its uploads and prompt. The Midjourney recipes for the plates and the first Vidu tests are at the end.

## Vidu next

1. [24a · The spin cut](#24a--the-spin-cut): Q4 5s, one roll for 23a and 24a, the bind breaking into the spin. Rolled; to judge.
2. Verse 3 on, 26–53, in song order: [not written yet](#verse-3-on).

The chase (25a–25h) is made and cut. In chorus 1, 21b, 23b and 24d are kept; 23a and 24a stay on their placeholders until the roll above is judged.

## How every Vidu shot is run

Reference to Video, Off-Peak, 1080p, 16:9, audio off. Q4 at 5s, Q3 Cinematic at 8s. Upload exactly the images listed under the shot, in that order: the web app tags them `@image1`, `@image2` in upload order, and each prompt opens by saying what each one is. Q4 takes up to nine images, Q3 seven. Two or three rolls is normal. A shot that gets two runs of four with no keeper takes its best usable roll and goes to the back of the queue. A roll is judged only on the stretch that goes on screen: two good beats out of a broken clip is a keeper.

**Which model.** Q4 by default: it keeps the faces, and it carried the charges, the clash and the bind where Q3 failed. Q3 Cinematic for the wides of verses 1–2, a run straight at the lens (20c, 20d) and the dojo, where Q4 draws flat 2D anime at any size. A frame with no face in it, only hands or a blade, comes back flat cel on both models (20g, 21b's first swing), so a face, a profile or a helmet stays in the frame.

**The camera.** Every prompt names a camera move: tracking, circling, tilting, pulling back, whipping after the action. The reference fights change about 0.06 of the picture a frame; prompts with "the camera holds" gave 0.025, and cutting faster doesn't close the gap. A still camera is chosen for one cut (24d). On the bridge, a roll that falls back to the eye-level view down the deck with the lanterns running away on both sides is rejected whatever else it gets right. Vidu doesn't move the lens: focus pulls, dolly zooms and lens effects are built in the edit, and so are screens, scopes and the HUD.

**The bridge plates.** Any camera on the deck takes `bridge-deck.png`. Given `bridge.png`, Vidu copies its view, the arch from the bank, behind women standing on the deck. `bridge.png` is only for a camera high above the whole bridge (24d) or across the canal (14).

**The singer's face plate.** `singer-face.png` goes in only where her face is the whole shot (1, 14, 22c). Its long loose locks come back as broken hair over her face whatever the prompt says, and `singer-front.png` carries her face everywhere else. The hair is then said in words: one high ponytail with a red cord, the shaved side showing, her face clear of hair. Seen from the side running right, her right side is toward the camera, the long-haired side on the plate, and the prompt says so.

**The rival's hair.** The lantern light and the dojo's dusk turn yellow-green gold. Every rival prompt says her hair is clearly green, a vivid leaf green, not blonde, and closes on "a drawn anime character, not live action": rolls that drifted blonde drifted toward live action too.

**Blades.** Say which hand holds it and that the other hand is empty: Q3 swaps the hand, and a flip mirrors the hair. Run the blade past the frame edge so the tip is never seen: with the tip in the frame Q4 draws it short and thick. A draw names the scabbard and says the scabbard is empty after it, and still leaves a second hilt now and then (21). Two blades crossed in an X in one frame change colour where they cross: Vidu colours the picture by halves, purple on the singer's side and green on the rival's, so the blades meet at the tips or the guards, each in its own half.

**Faces and bodies.** Never "rain running down her face": it reads as tears and puts a wet sheen on the skin. The face is matte, a few drops at most. A hand raised to the face lands in the hair, so hands stay down. Walking feet slide, so walks are framed above the feet. Any shot that shows their feet says `flat black sandals, no high heels`. Two women apart in one frame broke every time; they share a frame only when they touch.

**Light.** From "Draw!" on, every bridge prompt carries this paragraph, with `purple` for the singer and `green` for the rival:

```text
Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. Her blade leaves a glowing purple trail of light that hangs in the air for a moment behind every move.
```

The dojo is its opposite, warm and shaped, never flat even light, which was one of the two things that turned 20e flat:

```text
Dusk in the old dojo in @image3: the paper screens glow deep orange from the low sun outside, red paper lanterns hang lit from the beams, warm light and deep warm shadows that give her face and clothes their shape. Wooden practice swords, no steel: each is one plain piece of pale wood, no wrapped grip, no metal.
```

Neither model goes as dark as the prompt asks, and a darkening grade made the night muddy, so rolls are picked for the light they have.

**Screen direction.** On the bridge the singer moves left to right and the rival right to left, the way they stand at the two ends. In the chase both ride to the right, the rival ahead.

**The closing line.** Every prompt ends on what to keep from the references and on the look: "Glossy semi-realistic anime with soft airbrushed shading, as in the references", plus "not flat cel shading" or "not live action", whichever that model drifts toward.

## The cast

Built to read apart at a glance in a fast fight: a black ponytail and buzzed sides against a green silhouette, white against black, red and purple against green. The costumes change every scene; the hair never does outside the memories, so the hair is how the viewer tells the two apart.

The singer is my wife. The face is chosen by eye against the 0002 plate [`her-full.png`](../0002-fr-je-marrete-pas/characters/her-full.png), the drawing that caught her best. That plate goes into no slot: as a reference it brings 0002's inked comic look and its kimono with it. Face anatomy in words (cheekbones, jaw, eyelids, skin tone) pulled the picture toward American comics and a different ethnicity, so the prompt names only the brows and leaves the rest to the roll. No photo of her is kept in this repo or goes into Midjourney.

The rival's silhouette is the hair: two thick tufts of her own yellow-green hair, tied and standing up above the temples, the rest short. Nothing about Zundamon goes in a prompt.

The master, their old teacher and the one behind the smuggling: long straight silver hair, so her silhouette reads apart from the ponytail and the tufts.

The plates are neutral on purpose. Q4 copies a plate's expression and pose into every shot, so a sultry plate makes every shot sultry. Allure, anger and the master's red eyes go into the shots that want them.

| | The singer | The rival |
| --- | --- | --- |
| Hair | sides and nape buzzed, the crown in a high ponytail with a red cord | short yellow-green hair, two thick tufts tied upright above the temples, nothing past the shoulders |
| Face | thick straight dark brows, relaxed, no frown line, outer eye corners a little lower than the inner corners, a calm face, no earrings | yellow-green eyes, the green of her hair |
| Blade | katana, purple-wrapped hilt, glows purple | katana, green-wrapped hilt, thin green line along the spine, glows green |

A costume per scene, dressed for what she does in it. The second half wears nothing from the first, except the memories.

| Scene | The singer | The rival | The master |
| --- | --- | --- | --- |
| The bridge, the tea stall | `singer-front.png`: short white jacket with wide sleeves over a black bodysuit, wide black trousers, red sash, black sandals | `rival-front.png`: long black high-collared coat with a green lining over a dark green bodysuit, slim black trousers, black sandals | |
| The agency, the harbour | `singer-suit.png`: black suit, white shirt, sunglasses | `rival-hood.png`: black hoodie | |
| The memories | `singer-gi.png`: indigo training clothes, long loose hair | `rival-gi.png`: indigo training clothes, two low pigtails | `master-front.png`: grey haori |
| The chase | `singer-ride-helmet.png`: white racing suit, white helmet | `rival-ride.png`: black riding jacket, katana on her back, no helmet | |
| Verse 3 | `singer-ride-torn.png`: the racing suit after the crash | `rival-raid.png`: cropped bomber jacket | |
| The warehouse, the rooftop | `singer-tactical.png`: black tactical gear | `rival-raid.png` | `master-boss.png`: black and crimson coat |

## Plates

All made. They are in [`characters/`](characters/), each on plain light grey so Vidu takes the subject and nothing else from it. How each was made is in [Midjourney](#midjourney) below.

| File | What | Used in |
| --- | --- | --- |
| `singer-front.png`, `singer-back.png`, `singer-face.png` | the singer in the bridge clothes: front, back, head and shoulders | the bridge |
| `rival-front.png`, `rival-back.png`, `rival-face.png` | the rival in the bridge clothes: front, back, head and shoulders | the bridge, the stall; the face with every costume |
| `master-front.png`, `master-face.png` | the master in the grey haori: front, head and shoulders | the photo in 8, the memories; the face with every costume |
| `singer-suit.png` | black suit and sunglasses | the agency, the harbour |
| `rival-hood.png` | black hoodie | the harbour |
| `singer-gi.png`, `singer-gi-face.png` | the singer as an apprentice, long loose hair: full body, face | the memories |
| `rival-gi.png`, `rival-gi-face.png` | the rival as an apprentice, two low pigtails: full body, face | the memories |
| `singer-ride-helmet.png` | the racing suit with the helmet on | the chase |
| `singer-ride-torn.png` | the racing suit after the crash, the right sleeve torn, the holster empty | 26, 29 |
| `rival-ride.png`, `rival-ride-back.png` | black riding gear, katana across her back: front, back | the chase |
| `rival-ride-drawn.png`, `rival-ride-drawn-back.png` | the same, the scabbard empty: front, back | 25d, 25e, with the blade drawn |
| `rival-raid.png`, `rival-raid-back.png` | cropped bomber jacket, katana across her back: front, back | 29, the warehouse, the rooftop |
| `singer-tactical.png` | black tactical gear | the warehouse, the rooftop |
| `master-boss.png` | black coat with a crimson lining | the rooftop |
| `blade-singer.png`, `blade-rival.png` | each katana alone | every shot with a blade |
| `bike-singer.png`, `bike-rival.png` | each motorbike alone, side on, facing right | the chase |
| `case.png` | the open case of glowing zunda mochi | the deal, the raid, the end |
| `bridge.png` | the footbridge at night from the bank | a camera high above or across the canal |
| `bridge-deck.png` | close on the railing and the deck | every camera on the deck |
| `tea-stall.png` | the tea stall under the highway at dawn | verse 1 |
| `tea-stall-night.png` | the same stall at night, closed | 29 |
| `hq.png` | the agency operations room at night | verse 1, verse 3 |
| `apartment.png` | the singer's small apartment at night, empty | 29 |
| `harbour.png` | the container harbour at night | verse 2 |
| `highway.png` | the empty elevated highway at night, after the rain | the chase, the gantry included, verse 3 |
| `dojo.png` | the old wooden dojo at dusk | the memories |
| `warehouse.png`, `warehouse-aisle.png` | the warehouse: wide, and close on the crates | chorus 2 |
| `rooftop.png`, `rooftop-floor.png` | the rooftop at night: wide, and close on the parapet with the koi behind | shot 3, the bridge, the break |
| `rooftop-dawn.png`, `rooftop-floor-dawn.png` | the same at dawn | the last chorus, the outro |

`rival-raid.png` and `rival-raid-back.png` have small marks at the bottom edge: crop them before uploading.

## Intro and verses 1–2

Shots 2, 4 and 8 are made in the edit, 8 from 5, 8b and the plates.

### 1 · Rain on the lens

Q4, 5s. On screen 0:00–0:05:23, retimed to fit, with 1b cut against it. The clip only has to be her eye, sharp and still, in the rain. The focus pull is in the edit: Gaussian Blur 50 to 0 over the first 16 frames, sharp on the beat. Kept `1.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge-deck.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred far behind her. Extreme close-up of the singer's eyes and brows, filling the frame. Her eyes are open and look straight into the camera the whole time. Rain falls between her and the camera. She breathes slowly. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. Her eyes are dry and calm, not crying. Glossy semi-realistic anime, as in the references.
```

### 1b · The rival's eye

Q4, 5s. Cut against 1 on the beat. Kept `1b.mp4`.

1. `rival-hood.png`
2. `rival-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the place.

Night, light rain, on the quay of the harbour in @image3, orange and cyan lights blurred far behind her. Extreme close-up of the rival's eyes and brows under the edge of her black hood, filling the frame, a strand of yellow-green hair across her forehead. Her amber eyes look straight into the camera the whole time. Rain falls between her and the camera. She breathes slowly. The camera holds still.

She keeps the face of her references for the whole clip. Her eyes are dry and calm. Glossy semi-realistic anime, as in the references.
```

### 1c, 1d · Blades, a glimpse ahead

Not generated. 1d is `22e-4.mp4` from 2:00 to 2:16 at 400%, 4 frames: the hit the opening flashes forward to. `1c.mp4`, four frames from a failed roll of the old bridge batch, holds 5:08 until the master's red eye (36b) is made.

### 3 · The dive

Q3 Cinematic, 8s. On screen 0:08:11–0:13:16, speed-ramped. Kept `3.mp4`: in it the koi comes off the billboard and swims through the air, which is fine to keep. The line pinning the hologram to its screen is for a reroll.

1. `rooftop.png`

```text
@image1 is the city.

Night, heavy rain, the near-future city of @image1. The hologram on the tower is a flat picture on a billboard screen fixed to the wall. FPV drone shot: the camera starts above the wet rooftop, tips over its edge and dives straight down the face of the tower, neon signs rushing past, then levels out just above the wet street far below and races forward. One continuous fast camera move.

Glossy semi-realistic anime, as in the reference.
```

### 5 · The agency

Q3 Cinematic, 8s. On screen 0:26–0:31. The rival's file and the turning mochi go onto the screens in the edit, from `rival-face.png` and `case.png`. Kept `5.mp4`.

1. `singer-suit.png`
2. `singer-face.png`
3. `hq.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, the agency operations room in @image3, rain on the windows. Medium shot, the singer from the waist up in her black suit and sunglasses, standing with her back to the camera, facing the huge wall of cyan hologram screens. Then she turns around to face the camera. Her hands stay down. The camera slowly pushes in.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail with its red cord. Glossy semi-realistic anime, as in the references.
```

### 5b · The sunglasses

Q4, 5s. Kept `5b.mp4`; `5b-2.mp4` has bigger glasses than the plate.

1. `singer-suit.png`
2. `singer-face.png`
3. `hq.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, the agency operations room in @image3. Extreme close-up of the singer's face in her dark sunglasses, the cyan hologram screens reflected in the lenses, lines of data scrolling across the reflection. Her lips stay closed. She is still. The camera holds still.

She keeps the face of her references. Glossy semi-realistic anime, as in the references.
```

### 6-2 · The stall, alone

Q3 Cinematic, 8s. On screen 26:11–28:16, "Morning steam above the stall". From the street; 8b is the reverse from behind the counter. Kept `6-2.mp4`.

1. `rival-front.png`
2. `rival-back.png`
3. `tea-stall.png`

```text
@image1 and @image2 are the rival: her outfit from the front and from the back. @image3 is the place.

Dawn, light rain, the tea stall in @image3, pale blue morning light. Wide shot from the street, eye level, the whole stall in frame. The rival sits alone on one of two wooden stools at the counter, her back to the camera, in her black coat. The stool beside her is empty. Steam rises from the iron kettle on the counter into the cold air. She doesn't move. The camera slowly pushes in.

She keeps her short yellow-green hair and the two tied tufts. Only one person in the whole frame. Glossy semi-realistic anime, as in the references.
```

Reject a second person, both stools taken, or full cups on the counter: the cups are empty until 7 pours.

### 6 · Two cups

Q3 Cinematic, 8s. On screen 31:08–33:16, "Two cups waiting by the wall". From straight above: any eye-level angle shows the customers' seats, and she is sitting in one of them. Kept `6.mp4`, used from 0:06; its first six frames are the plate.

1. `tea-stall.png`

```text
@image1 is the place: use its counter and its bowls.

Dawn, the tea stall in @image1. Top-down shot, the camera looking straight down at the worn wooden counter under the stall's roof. The counter is dry: the roof keeps the rain off it. Two small empty tea bowls in dark brown glaze sit side by side on the counter, a little apart, in the middle of the frame. Nothing in them, completely dry inside, no steam. Only the wood of the counter fills the frame around them: no floor, no street, no stools. Warm lantern light falls across the counter and flickers very slightly. The camera slowly rotates, still looking straight down. No rain, no water. No people, no hands.

Glossy semi-realistic anime, as in the reference.
```

The counter is under the roof, so no rain on it, and rain would leave water in the bowls. The motion is the slow rotation and the lantern.

Reject rain on the counter, water in the bowls, tea, steam, white or celadon glaze, more than two bowls, any angle that is not straight down, or stools and floor at the edges.

### 7 · The pouring hand

Q3 Cinematic, 8s. On screen 35:19–38:16. The first half of the match cut into 17, so it copies the flipped 17's frame: the black sleeve from the top, centre right; the hand gripping from above; the handle from lower left to upper right; red lanterns on the right. The hilt becomes the straight side handle of a kyusu teapot. Kept `7.mp4`.

1. `rival-front.png`
2. `tea-stall.png`

```text
@image1 is the rival's outfit. @image2 is the place.

Dawn, light rain, at the counter of the tea stall in @image2, pale blue morning light, a red paper lantern glowing on the right behind. Extreme close-up. The rival's right hand in the sleeve of her black coat comes in from the top of the frame and grips the long straight side handle of a small black kyusu teapot from above, the handle pointing up and to the right, the teapot at the lower left. She tilts it and pours hot green tea into a ceramic cup at the bottom left of the frame, steam rising. The camera holds still.

Only her hand, her sleeve, the teapot and the cup are in frame. Glossy semi-realistic anime, as in the references.
```

### 8b · Her eyes on her tea

Kept `8b.mp4`, the rival's eyes on her tea. The message, an old photo, lands over her cup as a hologram in the edit, so the two are never in one frame here: every two-person roll at the counter was stiff.

### 9 · The deal

Q3 Cinematic, 8s. On screen 0:46–0:49. Kept `9.mp4` from 3s, after the case stops warping, and `9-2.mp4`, her hood down so the tufts show who it is. The handover itself is cut, not generated: Vidu drew the closed case wrong, having only the open one to go on. An extra keeps his hood up or his face in shadow: men with faces showing came out photorealistic.

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

Q3 Cinematic, 8s. Kept `9b.mp4`, its last three seconds, after the lid stops and the edges hold. A lid opening on a hinge bent the case on every roll, so the prompt starts with it open; the reveal is the flash on the cut and the push-in.

1. `case.png`
2. `harbour.png`

```text
@image1 is the case. @image2 is the place.

Night, light rain, on the wet concrete of the quay in @image2. Close-up from above of the silver case from @image1, already lying wide open, the lid standing still. Inside, rows of soft white rice cakes under glossy green paste glow faintly, the glow slowly pulsing. Raindrops land on the lid and run down it. The camera slowly pushes in.

Glossy semi-realistic anime, as in the references.
```

### 10 · The scope

Q3 Cinematic, 8s. On screen 48:22–51:14, full frame, with the scope's view opening over it in the edit. Kept `10-3.mp4`, side-on along the girder. A black costume in rain shines like rubber unless it is written as matte wool or cotton with `no shine`.

1. `singer-suit.png`
2. `singer-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, light rain, high on a crane above the harbour in @image3, the lit quay far below. The singer in her matte black wool suit, no shine, lies flat along the crane's steel arm and looks through the scope of a long rifle, aiming down at the quay. She stays still, only her breath moving. The camera slowly moves along her side toward her face.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail with its red cord. Glossy semi-realistic anime, as in the references.
```

### 11 · The eye at the scope

Q4, 5s. On screen 52:14–53:19. The close-up of 10-3: the same girder, pose and dusk light. Kept the roll where the girder hides her hand: every roll put the finger on the trigger. A real scope sits a few centimetres from the eye, so an eye a little back from the eyepiece is right.

1. `singer-suit.png`
2. `singer-face.png`
3. a tight crop of `10-3.mp4` at 5.5s around her head and the scope, scaled to 1920×1080, kept outside the repo (the full frame made Q4 copy the wide framing)

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the framing, the place and the light: keep them.

Dusk, light rain, on the steel girder of @image3, grey-blue sky and steel beams behind. Tight side close-up: her face and the rear of the rifle scope fill the frame, as in @image3. Not a wide shot. She lies flat in her matte black wool suit, no shine, cheek resting on the rifle stock. Her right eye is level with the scope's eyepiece, a few centimetres behind it, aiming to the right of frame. Her right index finger lies straight along the side of the rifle above the trigger guard, off the trigger, as a trained sniper holds it until the moment of the shot. She is completely still for the whole clip, like a held breath: her head, eye and hands do not move. No visible breath, no mist. Only the rain moves, and her hair stirs a little in the wind. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. The singer keeps her undercut and her high black ponytail with its red cord. Glossy semi-realistic anime, as in the references.
```

Reject her facing left, her finger inside the trigger guard, her eye above or below the eyepiece, her head lifting, a breath out, a shiny suit, or night.

### 12 · The rival looks up

Q4, 5s. On screen 53:19–54:12, then a freeze for her intro card. Kept `12.mp4` and `12-2.mp4`, eyes down.

1. `rival-hood.png`
2. `rival-face.png`
3. `harbour.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the place.

Night, light rain, on the quay of the harbour in @image3, lights blurred behind her. The camera looks down at her from above. Close-up from the shoulders up, the rival in her black hood, her eyes lowered. She lifts her eyes and looks straight up into the camera, and holds the look. The camera holds still.

She keeps the face of her references for the whole clip, yellow-green hair showing under the hood. Her eyes are dry and calm. Glossy semi-realistic anime, as in the references.
```

## Pre-chorus

### 13 · The lantern

Q3 Cinematic, 8s. On screen 0:55:23–0:58:12. Kept `13.mp4`, the one where the front lantern swings most and the lights behind it move a little, as one wind.

1. `bridge.png`

```text
@image1 is the place.

Night, heavy rain, the empty footbridge in @image1. Close-up of one red paper lantern hanging from the railing. The wind swings it back and forth, rain streaking past it, its warm light sweeping across the wet planks. Shallow depth of field: everything behind the lantern is soft blurred bokeh. The camera holds still.

Glossy semi-realistic anime, as in the reference.
```

### 14 · The singer, before the VS screen

Q4, 5s. On screen 0:58:12–1:01:02. In profile facing right, against the city across the canal; the camera arcs round her in a gust. Kept `14.mp4`.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the singer: outfit and face. @image3 is the place.

Night, heavy rain, at the end of the footbridge in @image3, on the canal bank. Behind her, out of focus across the canal, the neon high-rises of the city, pink and blue signs smeared by the rain and doubled in the black water; no bridge and no lanterns in the frame. The camera starts close behind her left shoulder, her ponytail and the city in the frame, and arcs smoothly around her to a close-up of her face in profile, facing the right of the frame, from the shoulders up; the neon lights behind her slide across the frame as it turns. A gust of wind drives the rain sideways across the frame, whips her ponytail and a few strands of her hair, and snaps the collar of her white jacket. Cold purple-white light from the right of the frame rims her face. She looks ahead to the right, still and calm, and breathes out slowly once through parted lips; the wind tears the white mist of her breath away to the left.

Her skin is matte and soft as in @image2, no shine, no wet sheen: only a few small raindrops in her hair, nothing running down her face, no tears. She keeps the face, hair and outfit of her references for the whole clip. Glossy semi-realistic anime, as in the references.
```

Reject the arc ending with her facing the camera or the left, the shaved side toward the camera at the end, a bridge or lanterns behind her, shine or water running down her face, or the mist on the inhale.

### 15 · The rival, before the VS screen

Q4, 5s. On screen 1:01:02 to the VS screen. Three-quarter from her left, facing left, the focus pulling from the railing to her face. Kept `15.mp4`.

1. `rival-front.png`
2. `rival-face.png`
3. `bridge.png`

```text
@image1 and @image2 are the rival: outfit and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3. In the foreground, out of focus, rain drips off the red railing; behind it, the rival in a three-quarter view from her left, from the shoulders up, facing the left of the frame. The focus pulls from the railing to her face. Her eyes slide to the left and fix on something far off. The camera holds still.

Her skin is matte and soft as in @image2, no shine, no wet sheen: only a few small raindrops in her hair, nothing running down her face, no tears. She keeps the face, hair and outfit of her references for the whole clip. Glossy semi-realistic anime, as in the references.
```

Reject a face square to the camera, one facing the wrong side, shine or water running down the face, or tears.

### 16 · The VS screen

Q4, 5s, one each, no place: a fighting game's VS screen, each in her own colour. In a slanted split in the edit, the singer top left facing right, the rival bottom right facing left. Blades stay sheathed: the draws are 17 and 21a. Kept `16a.mp4` and `16b.mp4`.

16a, the singer:

1. `singer-front.png`
2. `singer-face.png`

```text
@image1 and @image2 are the singer: outfit and face.

No place behind her: a dark purple void, purple fire rising from below, embers and streaks of purple light rushing past, a storm wind. Extreme low angle, the camera tilted, below her chin, a three-quarter view from her left, the singer from the chest up on the left of the frame, her body turned toward the right of the frame. Her left hand rests on the hilt of her sheathed katana at her hip. The wind whips her long black hair and her sleeves. She lifts her chin and looks down her nose at the camera with cold contempt, her eyes catching the purple light, and holds the look. The camera pushes in fast, then holds.

She keeps the face and the clothes of her references for the whole clip. No rain, no drawn blade. Glossy semi-realistic anime, as in the references.
```

16b, the rival:

1. `rival-front.png`
2. `rival-face.png`

```text
@image1 and @image2 are the rival: outfit and face.

No place behind her: a dark poison-green void, green lightning cracking behind her, streaks of green light rushing past, a storm wind. High angle, the camera tilted the other way, above her, a three-quarter view from her right, the rival from the chest up on the right of the frame, her body turned toward the left of the frame. Her right hand rests on the hilt of her sheathed katana at her hip. The wind whips her yellow-green hair. She tilts her head and looks sideways up into the camera, and her smirk widens into a wild grin, and holds it. The camera pushes in fast, then holds.

She keeps the face and the clothes of her references for the whole clip. No rain, no drawn blade. Glossy semi-realistic anime, as in the references.
```

Reject a drawn blade, a face square to the camera, or a body facing the wrong side: the two face each other across the seam.

## Chorus 1

One woman a cut until the hit (22e); from the hit on, the two share the frame while they are locked or trading blows. Every cut changes the camera and every camera moves but 24d's. The past comes once, out of the lock, in the dojo at dusk. The full cut and its times are in [`shotlist.md`](shotlist.md#chorus-1--1088132--the-duel).

### 17 · Draw

Q3 Cinematic, 8s. From 1:07.7 under `ROUND 1`, to "Draw!", about a second. Flipped in the edit so she faces left. Kept `17.mp4`, roll 6 of 7: she grips the hilt and pulls the blade a little way out, then stops; 2–3s of usable motion.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Extreme close-up at the rival's left hip: her katana sits in a black lacquered scabbard tied at her left hip, the green-wrapped hilt pointing forward. Her right hand rests on the hilt, the black sleeve of her coat at the edge of the frame. Her left thumb pushes the guard forward, and a short strip of bright steel slides out of the mouth of the scabbard, catching the lantern light. The sword stays in the scabbard. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, as in @image3. Glossy semi-realistic anime, as in the references.
```

A draw is the hardest motion there is for Vidu. With no scabbard named she pulled the sword out of her pocket; with one, she gripped it the wrong way round, the sword drew itself, or Q4 showed the blade bare from the first frame with the hilt bent at a right angle.

### 18 · Steel in bloom, the title

Q4, 5s. 5 beats out of 17's flash, with `STEEL`, `IN` and `BLOOM` coming in one at a time around her head in the edit. Kept `18.mp4`, the coolest and a little dark. Her eyes glow purple, which fits "Steel in bloom".

1. `singer-front.png`
2. `bridge-deck.png`

```text
@image1 is the singer. @image2 is the place.

Night, heavy rain, on the footbridge in @image2. Close shot from the chest up, straight on, the singer in the middle of the frame, only the dark sky and the lanterns far behind her head. She stands still with her head lowered, then lifts her face and looks straight into the camera. The light is behind her: a bright rim of light along her hair, her shoulders and her ponytail, her face mostly in shadow. The rain between her and the camera is lit from behind. Her hands and the sword stay out of the frame. The camera pushes in slowly.

She keeps the face, hair and outfit of her reference for the whole clip. Her long black hair is tied up in one high ponytail at the back of her head with a red cord, the shaved side of her head showing, her face clear of hair. Glossy semi-realistic anime with soft airbrushed shading on her face and clothes, as in the references, not flat cel shading.
```

Reject a sword or a hand in the frame, the railing right behind her head (the type goes there), or a face lit bright from the front.

### 21a · The rival draws

Q4, 5s. 4 beats from 1:11.28: she finishes the draw her hand started in 17, and the green arc goes into the white flash. Kept `21a.mp4`, facing left, the scabbard in her left hand; the tufts are above the frame, and the green hair says who it is.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Medium shot from the side, a low camera, the rival from the waist up, facing the left of the frame. Her left hand holds the black lacquered scabbard at her left hip. Her right hand draws the katana out in one fast motion and swings it out wide, the blade sweeping out past the edge of the frame so its tip is never seen. The blade lights up green as it leaves the scabbard and leaves a glowing green arc in the air where it swung. After the draw the scabbard is empty and she holds the one katana ready in her right hand. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, lit green from the blade. Fast, full real-time speed.

She keeps the face, hair and outfit of her references for the whole clip. There is only one sword. Her hair is clearly green, a vivid leaf green as in @image2, closer to green than to yellow, and stays green in the lantern light: not blonde, not gold. It is short, above her shoulders, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

Reject a second hilt left in the scabbard, the draw in her left hand, a blade already out on the first frame, or the tip in the frame.

### 21b · Steel in bloom

Q4, 5s. 4 beats after 21a, to 1:13.70, where the purple `ONLY` comes in over 20a: the first time her blade is seen. Her face only as a soft profile at the top, so it doesn't repeat 18's face from the front. Kept `21b.mp4`, about 2s usable.

1. `singer-front.png`
2. `blade-singer.png`
3. `bridge-deck.png`

```text
@image1 is the singer. @image2 is her katana. @image3 is the place.

Night, heavy rain, on the footbridge in @image3. Close shot from the side and a little below, at the height of her hands: the singer in profile facing the right of the frame, from her waist up to her eyes, her face soft and out of focus at the top left of the frame, the blade sharp. It is the slender katana of @image2: a long, narrow, slightly curved blade, no wider than two fingers, never thick or broad like a sabre, its tip always beyond the right edge of the frame. She sweeps the blade up fast from below the frame in her right hand and snaps it level in front of her, stopping it dead; it cuts through the falling rain and the drops burst off the steel in a spray. The blade is plain dark steel with no glow until it stops. As it stops, the whole blade ignites from inside the steel, evenly along its whole length at the same time, from dark steel to a deep, bright purple in a flash, like metal turning hot, and a pulse of purple light turns the rain around it into sparks of light and lights her face from below. The camera whips up with the swing, jolts when the blade stops, then pushes in along the blade toward her hand gripping the purple hilt, her fingers tightening. Dark: the only light is the glow of the blade and the lanterns far behind. Fast, full real-time speed, no slow motion.

Only one sword, her own, with its purple hilt. She keeps the face, hair and outfit of her reference. Glossy semi-realistic anime with soft airbrushed shading on her face and clothes, as in the reference, not flat cel shading.
```

Reject a short blade with the tip in the frame, a thick or broad blade, a green glow, a second blade, the glow already full on the first frame, her face sharp in the frame, or a spot or line of light travelling along the blade. The glow comes up in the whole blade at once.

What the runs taught. Seen along its length the blade foreshortens and fattens like a sabre, so it is shown from the side, its width given, the tip out past the edge so the length can't be judged. Anything that names a line or a glint moving along the blade comes out as a laser dot. A slow track along a still blade barely moves, so she swings it up and snaps it level, and the glow lands on the stop. With her face out of the frame the swing came back flat cel and lost the blade, so her profile is back in, soft.

### 20a · The singer's step

Q4, 5s. 2 beats from 1:13.70, on "Only": the charge starts here. Kept `20a.mp4`, her body turned into the bridge toward the rival.

1. `singer-front.png`
2. `bridge-deck.png`

```text
@image1 is the singer. @image2 is the place.

Night, heavy rain, on the footbridge in @image2. Extreme close-up at the height of the deck: a shallow puddle on the wet planks, the red lanterns far behind reflected in it. A foot in a flat black sandal over a black split-toe sock slams down into the puddle from the left, the hem of wide black trousers above it, and the water bursts up toward the lens in a crown of drops. Dark: the only light is the lanterns far behind, shining in the water. The camera holds still.

Flat black sandals, no high heels. Glossy semi-realistic anime, as in the reference.
```

Keep a roll where the foot lands in the first two seconds. Reject walking, a shoe, or a heel.

### 20b · The rival's step

Q4, 5s. 2 beats after 20a. Kept `20b.mp4`: the foot points left, toward the singer.

1. `rival-front.png`
2. `bridge-deck.png`

```text
@image1 is the rival. @image2 is the place.

Night, heavy rain, on the footbridge in @image2. Extreme close-up at the height of the deck: a shallow puddle on the wet planks, the red lanterns far behind reflected in it. A foot in a flat black sandal over a black sock slams down into the puddle from the right, the hem of slim black trousers and of a long black coat above it, and the water bursts up toward the lens in a crown of drops. Dark: the only light is the lanterns far behind, shining in the water. The camera holds still.

Flat black sandals, no high heels. Glossy semi-realistic anime, as in the reference.
```

Keep a roll where the foot lands in the first two seconds and her body is turned left, toward the singer. Reject walking, a shoe, or a heel.

### 20c · The singer runs at the camera

Q3 Cinematic, 8s. 2 beats after 20b, cut before she veers past the lens. Kept `20c.mp4`, from straight in front: the camera starts on the planks and tilts up as she runs in, and a smooth ribbon of purple light runs off the blade in her right hand the whole way. Used from about 7.0s.

1. `singer-front.png`
2. `singer-face.png`
3. `blade-singer.png`
4. `bridge.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. The camera sits low on the wet wooden deck right beside the left railing, a wide lens, tilted slightly, looking diagonally across the deck toward the far right corner of the bridge, so the railing runs past close on the left of the frame and the deck crosses the frame at an angle. The singer sprints on a diagonal from the far right of the deck toward the camera, growing from small to filling the frame. Her katana is in her right hand, which is on the left of the frame as she runs toward us, held low and out to her side, away from her body, the blade pointing back. Her left hand, on the right of the frame, is empty and swings as she runs. Just before she reaches the lens she swerves past it out of the left of the frame. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. The blade glows purple, and a long ribbon of purple light streams from its tip through the air beside her and behind her, tracing her path down the deck, always on the open side of her body where the camera sees it. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, by its purple hilt, in her right hand. Flat black sandals, no high heels. She keeps her undercut and her high black ponytail with the red cord. Glossy semi-realistic anime, as in the references.
```

Reject the blade in her left hand, a blade that glows with no trail, a second woman, high heels, or slow motion.

A trail behind a woman running at the lens sits behind her body, so the ribbon is asked for beside her, on the side the camera sees. Asked for as a swing, Vidu drew the arc as a solid crescent hanging in the air. The keeper is the view down the deck, but no other cut of the chorus is, so it doesn't repeat.

### 20d · The rival runs at the camera

Q3 Cinematic, 8s. 2 beats after 20c, its mirror. Kept `20d.mp4`, about 7.1s to 7.75s: her face, her body crossing the lens, then the frame full of green light, cut straight into 22a. The hair came out olive: a Color Mask on the hair in the edit, Hue toward green. The tufts came out wide and furry; a scale to 110% pushes them out of the frame.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. The camera sits on the wet wooden deck, low, a wide lens, tilted slightly. The rival sprints straight at the camera from the far end of the deck, growing from small to filling the frame. Her katana is in her right hand, which is on the left of the frame as she runs toward us, held low and out to her side, away from her body, the blade pointing back. Her left hand, on the right of the frame, is empty and swings as she runs. Just before she reaches the lens she swerves past it out of the right of the frame. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. The blade glows green, and a long ribbon of green light streams from its tip through the air beside her and behind her, tracing her path down the deck, always on the open side of her body where the camera sees it. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, by its green hilt, in her right hand. Flat black sandals, no high heels. Her hair is clearly green, a vivid leaf green as in @image2, closer to green than to yellow, and stays green in the lantern light: not blonde, not gold. It is short, above her shoulders, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

Reject blonde or golden hair, live action, the blade in her left hand, a blade that glows with no trail, a second woman, or high heels.

Both leave the frame on the same side, and that is right: the two shots are reverse angles down the deck, so they pass right shoulder to right shoulder.

### 22a · The singer's charge

Q4, 5s. 2 beats from 1:16.16. Kept `22a.mp4`, from an earlier version of the prompt below: the near side of her hair came out right on about one roll in five, and a wrong haircut reads in a few frames where nobody checks a blade. The prompt below fixes the rest of that version (the flat cel render, the blade leading forward) for a reroll.

1. `singer-front.png`
2. `blade-singer.png`
3. `bridge-deck.png`

```text
@image1 is the singer. @image2 is her katana. @image3 is the place.

Night, heavy rain, on the deck of the footbridge in @image3. Medium shot from the side at waist height, the camera tracking alongside her at her speed: the red railing with its glowing red lanterns runs right behind her the whole time, smearing past in streaks of motion blur. The singer sprints from the left of the frame toward the right, facing the right edge of the frame the whole time, her feet splashing through the puddles on the planks. Her katana is in her right hand, the hand nearest the camera, held low at her side with the tip trailing behind her, the way a swordsman carries a drawn blade at a run. Her left hand, on the far side of her body, is empty. The frame holds her from the waist to above her head. Her long black hair is tied up in one high ponytail with a red cord, streaming back in the wind; on the side of her head toward the camera, long black hair is swept down over her temple and ear, with no shaved skin showing. Her wide white sleeves stream back. Dark, low-key light: the only light comes from the red lanterns behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. The whole blade glows bright purple from the guard to the tip. The purple light streaks back off the tip of the blade, behind her, like a comet's tail, and hangs in the air for a moment. Nothing glows at the hilt or anywhere else on her. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her reference for the whole clip. She holds only her own katana, by its purple hilt. Glossy semi-realistic anime with soft airbrushed shading on her face and clothes, as in the reference, not flat cel shading.
```

Reject the shaved side of her head toward the camera, the blade pointing forward, light off the hilt, flat cel shading, the arch of the bridge behind her, or slow motion.

### 22b · The rival's charge

Q4, 5s. 2 beats after 22a, its mirror. Kept `22b.mp4`, the blade pointing back behind her as 22a's, so the two charges match; in its second half the whole blade flares neon green, and the two beats are cut before the flare. `22b-2.mp4` is the fallback. Q3 broke every way on this shot: two blades, a reverse grip, the blade in both hands.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Medium shot from the side at waist height, the camera tracking alongside her at her speed, on the deck of the bridge: its red railing with hanging red lanterns runs right behind her the whole time, the canal and the city beyond it. The rival sprints from the right of the frame toward the left, facing the left edge of the frame the whole time. Her katana is in her right hand, on the far side of her body, held low with the tip trailing behind her, so the blade shows behind her back, the way a swordsman carries a drawn blade at a run. Her left hand, nearest the camera, is empty. The frame holds her from the waist to above her head, her long black coat streaming back in the wind. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. The whole blade glows bright green from the guard to the tip. The green light streaks back off the tip of the blade, behind her, like a comet's tail, and hangs in the air for a moment. Nothing glows at the hilt or anywhere else on her. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, by its green hilt. Her hair is clearly green, a vivid leaf green as in @image2, closer to green than to yellow, and stays green in the lantern light: not blonde, not gold. It is short, above her shoulders, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

Reject her running left to right, two blades, a reverse grip, the blade in both hands, the bridge gone, or a purple glow.

### 22c · The singer's eyes

Q4, 5s. 1 beat, just before the hit. Kept `22c.mp4`, the angriest, the clearest contrast as her eyes narrow.

1. `singer-front.png`
2. `singer-face.png`
3. `bridge-deck.png`

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3. Extreme close-up of the singer's eyes, from her brows to the bridge of her nose, nothing else in frame. Purple light from her blade, out of the frame below, lights her face from beneath. Her eyes narrow and fix on something just ahead of her. Rain falls in front of her face. Dark all around. The camera holds still.

She keeps the face of her references for the whole clip. Her eyes stay dry, no tears. Glossy semi-realistic anime, as in the references.
```

### 22d · The rival's eyes

Q4, 5s. 1 beat after 22c. Kept `22d.mp4`: the green light from below and the hard brows mirror 22c. The irises are named yellow-green: "amber" gave amber on every roll.

1. `rival-front.png`
2. `rival-face.png`
3. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3. Extreme close-up of the rival's eyes, from her brows to the bridge of her nose, nothing else in frame. Her irises are a bright yellow-green, the green of her hair, exactly as in @image2. Green light from her blade, out of the frame below, lights her face from beneath. Her eyes narrow and fix on something just ahead of her. Rain falls in front of her face. Dark all around. The camera holds still.

She keeps the face of her references for the whole clip. Her eyes stay dry, no tears. Her fringe is green, a vivid leaf green as in @image2, not blonde. Glossy semi-realistic anime, as in the references.
```

### 22e · The hit

Q4, 5s. 1:18:01–1:19:07, the flash on the downbeat of the second "Draw!". Kept `22e-4.mp4`, from 1:09 to 2:15: the run-in from the two sides, the contact, a sphere of light split purple and green where the two stand, then the lock held. It is also the glimpse 1d. Q3 never gave a keeper here; Q4 put them on a plaza in front of the arch until the prompt put the railing right behind them.

1. `singer-front.png`
2. `rival-front.png`
3. `rival-face.png`
4. `blade-singer.png`
5. `blade-rival.png`
6. `bridge-deck.png`

```text
@image1 is the singer. @image2 and @image3 are the rival: front and face. @image4 is the singer's katana. @image5 is the rival's katana. @image6 is the place.

Night, heavy rain, in the middle of the footbridge in @image6, on its wooden deck: the red railing with its hanging red lanterns runs right behind them across the whole frame, the canal below and the city beyond. Wide shot from the side at deck level, a low camera. The singer sprints in from the left of the frame and the rival from the right, each with her katana in her right hand, the singer's glowing purple and the rival's glowing green. They meet in the middle of the frame and their blades strike, and a huge burst of purple and green light explodes from the point where they meet, throwing the rain away in a ring. The two stay where they met, blades locked, pushing against each other. Dark, low-key light: the only light comes from the lanterns far behind them and from their blades. The wet deck reflects every light. Full real-time speed, no slow motion.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer's long black hair is tied up in one high ponytail at the back of her head with a red cord, the shaved side of her head showing, her face clear of hair. The rival's hair is clearly green, a vivid leaf green as in @image3, not blonde, short, with the two tied tufts standing up. Glossy semi-realistic anime with soft airbrushed shading on their faces and clothes, as in the references: not flat cel shading, not live action.
```

Reject the two passing each other and swapping sides, a camera at eye level looking down the deck, or slow motion.

### 23a · The lock

Q4. 4 beats at 1:19:07, out of 22e's burst, once. The two chest to chest, the blades crossed at the guards, shoving. Cut from the start of the 24a roll: one clip that starts in the bind and breaks into the spin, so the lock and the spin are the same take, and the memory between them (20e, 23b) cuts out of the bind and back into it. The prompt is under [24a](#24a--the-spin-cut). Placeholder `23a.mp4`, from an over-the-shoulder version that kept the singer's head out of the frame; its blades cross in an X and change colour in the middle.

What the runs taught. Blades crossed in an X change colour at the middle of the frame. A circling camera flips which half each blade is in. With `singer-face.png` her hair broke on all eight rolls; without it, on two of four. With `bridge-deck.png` the deck and the colours held on all four, but the two stood apart with the blades crossed loosely: the prompt above makes it a real bind, both hands on the hilt, the blades at the guards, the two shoving.

### 20e · The apprentice runs in

Q3 Cinematic, 8s. 2 beats out of the white flash: the past. Kept `20e.mp4`, the nearest to the plates' style. Its wooden sword has a plain guard; a kendo bokuto often has one, so it stays.

1. `singer-gi.png`
2. `singer-gi-face.png`
3. `dojo.png`

```text
@image1 and @image2 are the singer as a young apprentice: training clothes and face. @image3 is the place.

Dusk in the old dojo in @image3: the paper screens glow deep orange from the low sun outside, red paper lanterns hang lit from the beams, warm light and deep warm shadows that give her face and clothes their shape. Wooden practice swords, no steel: each is one plain piece of pale wood, no wrapped grip, no metal. Side view, full body, the camera tracking with her. The singer at about twenty, a serious apprentice in the middle of hard training, drives in from the left of the frame toward the right, barefoot, and strikes down at her opponent just out of the frame on the right: one fast, precise, trained cut with the wooden practice sword in both hands, right hand above the left, elbows in, her front foot stamping on the floor as the cut lands, the sword stopping dead at head height. Her long loose black hair flies behind her. Her face is focused and hard, mouth closed, eyes fixed ahead, no smile. Full real-time speed, no slow motion.

She keeps the face of her references and the indigo training jacket and hakama of @image1 for the whole clip. No undercut, no ponytail: her black hair is long and loose past her shoulders. A thin red cord around her left wrist. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action, not a real person, not a photograph.
```

Reject a smile or a playful swing (she is a grown apprentice training hard), the undercut or the ponytail, a real sword, a wrapped grip, shoes, or a second person in the frame.

What the runs taught. With `singer-face.png` (undercut, ponytail) against the training plate's long hair, Q4 matched neither face: hence the past's own face plates. Q4 drew the dojo flat 2D at any size. Every bright daylit room turned her live action, so the dojo is at dusk and the closing line says she is drawn.

### 23b · The old smile

Q3 Cinematic, 8s. 6 beats from 1:20:13, straight after 20e's cut: the young rival takes the blow, sits down hard on the floor and laughs up at her friend. Ten years before the singer throws her in 24a–24c. Kept `23b.mp4` for now: falls back, a moment's pause, then the laugh, but wide, a small full figure, scaled up in the edit, and it holds up in the cut. The prompt below names one size for the whole clip, for a reroll if one is wanted.

1. `rival-gi.png`
2. `rival-gi-face.png`
3. `dojo.png`

```text
@image1 and @image2 are the rival as an apprentice: training clothes and face. @image3 is the place.

Dusk in the old dojo in @image3: the paper screens glow deep orange from the low sun outside, red paper lanterns hang lit from the beams, warm light and deep warm shadows that give her face and clothes their shape. The rival in her indigo training jacket, her hair in two low loose pigtails, clearly green, a vivid leaf green closer to green than to yellow, not blonde even in the orange light. Medium close shot, from her chest up, the same size for the whole clip. A blow from someone out of the frame on the left knocks her backward and she sits down hard on the polished wooden floor; the camera drops with her, keeping her from the chest up, ending low at the height of her face. She props herself up on one hand, stunned for a moment, looks up to the left at her friend, and bursts out laughing, a warm, open laugh, shaking her head as if saying "you're too strong!".

She keeps the face of her references for the whole clip. Two low loose pigtails, no upright tufts. No sword in her hands. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action, not a real person, not a photograph.
```

Reject tufts, a real sword, a second sword, a second person in the frame, or a smirk: it is the laugh of a friend who has just lost, not the smuggler's smile of `23.mp4`.

### 24a · The spin cut

Q4, 5s. One roll for 23a and 24a: the bind, then the break and the spin. Its first 1.3s is 23a (4 beats at 1:19:07); the rest is 24a, 9 beats, 2.8s, 1:23:02–1:25:19, out of the memory. That is 4.1s of the 5s, so the bind can't run long: if the spin part comes out short, 24a starts a shove earlier rather than slowing down. 24a starts on the last shove of the bind, where she breaks it, not on more shoving: a second look at the lock after the memory came back to the same picture and stopped the fight. The camera has pushed in by then, so 24a also opens closer than 23a. The cut ends before the blades meet: the contact is 24b's. Q3 Cinematic if the spin breaks on Q4. Placeholder `24a.mp4`, which starts with the two apart, about 0.7s of standing before the spin.

1. `singer-front.png`
2. `rival-front.png`
3. `rival-face.png`
4. `blade-singer.png`
5. `blade-rival.png`
6. `bridge-deck.png`

```text
@image1 is the singer. @image2 and @image3 are the rival: front and face. @image4 is the singer's katana. @image5 is the rival's katana. @image6 is the place.

Night, heavy rain, on the wooden deck of the red footbridge in @image6, the bridge's own red railing with its glowing paper lanterns close behind them, out of focus, the dark overpass and the city lights far behind. Close two-shot from the side at the height of their chests: the singer on the left of the frame and the rival on the right, locked in a sword bind, chest to chest. Each grips her hilt in both hands, and the two katanas are crossed right at the guards, between their chests, guard against guard, the blades rising steeply past their faces. For the first half of the clip they hold the bind, leaning into each other with all their weight, arms shaking, feet sliding on the wet planks: the singer shoves, the rival is forced back half a step and shoves back. Steel grinds on steel, and a fountain of orange sparks sprays up from the crossed guards with every shove. Their faces are a hand's width apart over the crossed blades, eyes locked, the singer's jaw set, the rival's teeth bared, the rain running between them. The camera pushes in to their two faces over the crossed guards and shakes with every shove; it never goes around them. Then the singer explodes out of the bind: she shoves the rival's blade up and away with a burst of sparks, spins all the way around once on one foot, and slashes flat across at the rival's chest. A long ribbon of purple light streams from the tip of her blade and traces the whole circle of the spin around her, mirrored in the wet deck. The rival gets her green blade in the way just in time, and the blow throws her backward out of the right of the frame. As the bind breaks, the camera pulls back fast and drops low to the deck, so the spin and the ribbon of light fill the frame, motion blur on the swing. The singer's whole blade glows purple from the guard to the tip; the rival's whole blade glows green from the guard to the tip; purple light on the singer's face and green light on the rival's. The singer stays on the left and the rival on the right the whole time. Dark, low-key light: the only light comes from the lanterns behind them and from their blades. The wet deck reflects every light. Fast, full real-time speed, no slow motion.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. The singer's long black hair is tied up in one high ponytail at the back of her head with a red cord, the shaved side of her head showing, her face clear of hair. The rival's hair is clearly green, a vivid leaf green as in @image3, not blonde, short, with the two tied tufts standing up. Glossy semi-realistic anime with soft airbrushed shading on their faces and clothes, as in the references: not flat cel shading, not live action.
```

Reject the two swapping sides, the two starting apart, the bind breaking in the first second, blades crossed in an X, a blade passing through the other or bending, a blade in a left hand, one colour on both blades, a blade that changes colour along its length, a solid shape of light hanging in the air or bent into the blade, a camera that goes around them during the bind or holds still, a camera at eye level through the spin, the rival thrown out of the left, or slow motion.

What the runs taught, in the lock. Blades crossed in an X change colour at the middle of the frame. A circling camera flips which half each blade is in. With `singer-face.png` the singer's hair broke on all eight rolls; without it, on two of four. With `bridge-deck.png` the deck and the colours held on all four, but the two stood apart with the blades crossed loosely: the prompt makes it a real bind, both hands on the hilt, the blades at the guards, the two shoving.

### 24b · She takes it

Q4, 5s. 2 beats from 1:25:19: the hit only, built up in the edit (hit stop, strobe, RGB split, shake, the health bar). Kept `24b.mp4`: the singer's purple blade comes in from the left at 1:06 clip time, the burst at 1:09, and she is thrown back by 2:06. `24b-2.mp4`, the fallback, has the light but no blade.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Close shot from the chest up, straight on. The rival holds her katana by its long hilt in both hands, one hand right above the other on the hilt, raised in a slanting guard across in front of her against a blow from the left, the green-glowing blade crossing the frame and running out past its top left edge, so the tip is never seen. Her hands stay on the hilt and never touch the blade. A blow from out of the frame on the left slams into her blade in a burst of purple light. The shock throws her arms back, her head snaps back, her hair whips, and she is thrown backward to the right. The camera jolts with the impact and whips to the right after her, keeping her in the frame as she flies back, the rain and the lanterns smearing past in motion blur. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, by its green hilt. Her hair is clearly green, a vivid leaf green as in @image2, closer to green than to yellow, and stays green in the lantern light: not blonde, not gold. It is short, above her shoulders, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

Reject a second woman in the frame, a blade in one hand, a hand on the blade (a real block, but it reads as grabbing the steel), a camera that holds still, or slow motion.

### 24c · She slides back

Q4, 5s. 1:26:04–1:29:09. Kept `24c.mp4`, run to its end at 200%: she is already down on one knee and dragged backward, then the camera pushes in on her face. Her hard face here is the payoff of the laugh in 23b.

1. `rival-front.png`
2. `rival-face.png`
3. `blade-rival.png`
4. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4. Side view, the camera low on the planks of the deck, the red railing with its lanterns behind her. The rival is thrown in from the left of the frame by a blow, still facing the left, toward the blow. She lands hard on the deck on her feet and one knee and skids backward to the right, braking hard: her boots and her knee scrape on the planks, her body jolts, and she jams the tip of her green-glowing katana down into the planks in front of her to stop herself, gouging a line through the wood with sparks, splinters and a spray of water. She slows fast and stops within a second, crouched low, one hand on the deck. The camera whips in from the left with her, low over the planks, the railing and the lanterns smearing past behind her, and jolts to a stop when she stops. Her head is down; she lifts her eyes toward the left and the camera pushes in on her face. Dark, low-key light: the only light comes from the red lanterns far behind her and from her blade. Her face is half in shadow, with a thin rim of light on her hair and shoulders. The wet deck reflects every light. Fast, full real-time speed, no slow motion.

She keeps the face, hair and outfit of her references for the whole clip. She holds only her own katana, by its green hilt. Her hair is clearly green, a vivid leaf green as in @image2, closer to green than to yellow, and stays green in the lantern light: not blonde, not gold. It is short, above her shoulders, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

Reject her facing the way she slides, the camera at eye level or left behind as she slides, a second woman, or a smooth even glide: that reads as skating, not as being thrown. Nothing drove the slide or stopped it in the first rolls, so the prompt starts with the throw and makes the stop the action.

### 24d · Apart

Q4, 5s. 1:29:09–1:32:01, 64 frames, the end of chorus 1. She follows 24c, down on one knee with her blade in the planks: she pulls it out, gets up and runs off the right, the way she rides in the chase. The one still camera after "Draw!": after twenty moving cuts the stillness is the change. Once she is gone the camera tilts up off the bridge into the rain and the dark sky, and the chase opens on the dry highway: the turn away from the bridge and the rain stopping say the scene has changed, with 25a's `3 NIGHTS LATER`. The run is quick so the tilt fits the 64 frames. The edit fades the sky to black over the last 12 frames, and 25a cuts in hard on the downbeat. Kept `24d.mp4`, the roll that tilts up into the rain.

1. `singer-front.png`
2. `rival-front.png`
3. `rival-face.png`
4. `blade-singer.png`
5. `blade-rival.png`
6. `bridge.png`

```text
@image1 is the singer. @image2 and @image3 are the rival: front and face. @image4 is the singer's katana. @image5 is the rival's katana. @image6 is the place.

Night, heavy rain, the footbridge in @image6 seen from high above at a steep angle, close enough that the wooden deck fills the frame and both ends of the bridge are outside it, the railings with their glowing red paper lanterns along the top and the bottom of the frame. The camera holds still until the rival is gone. The singer stands at the left end of the deck and the rival at the right end, far apart, both small in the frame, their drawn blades glowing faintly, purple and green, the glow fading. The singer is standing. The rival is crouched low on one knee, the tip of her green katana jammed into the planks in front of her, as if she has just stopped herself after being thrown back. Quickly, she pulls the blade out of the deck, rises to her feet, turns her back on the singer and runs away from her, to the right, off the right edge of the frame. The singer stays where she is. As soon as the rival is gone, the camera tilts slowly up, away from the bridge, past the lanterns and the city lights, up into the dark rainy night sky, until only low clouds and the rain streaking down toward the lens fill the frame.

Both women keep the faces, hair and outfits of their references for the whole clip. Each holds only her own katana, by the hilt, the singer's with a purple hilt and the rival's with a green hilt. Flat black sandals, no high heels. The singer's long black hair is tied up in one high ponytail at the back of her head with a red cord, the shaved side of her head showing, her face clear of hair. The rival's hair is clearly green, a vivid leaf green as in @image3, not blonde, short, with the two tied tufts standing up. Glossy semi-realistic anime, as in the references: drawn anime characters, not live action.
```

Reject a camera that moves before the rival is gone, a camera that pans or flies instead of tilting up, no sky at the end, figures bigger than a lantern, the singer moving, a third person, the rival walking off down the deck, or the rival already standing at the start. The glow fading off both blades is right: it reads as the fight ending.

## The chase

The instrumental, 1:32–1:44, the rival's bonus stage, another night. One woman a cut, on Q4. The bridge was heavy rain; the chase is after the rain, the road still wet and mirroring the neon, no rain falling, so the weather says it is another night along with the costumes and the edit. 24d's run off the right into 25a's ride to the right reads as one continuous move, so 24d tilts up into the rain and fades to black, and 25a cuts in hard on the downbeat under `3 NIGHTS LATER`. Both ride to the right, the rival ahead, the way she ran off in 24d; the singer chases from the left. Every prompt names the camera and its move, at full speed. The singer is in a helmet the whole chase: the purple on her helmet, her bike and her bullets says who she is, and with no face in the shot Vidu can't break it. The rival rides bare-headed, her green hair saying who she is.

### 25a · The rival on the highway

Q4, 5s. On screen 1:32:01–1:34:01, under the `3 NIGHTS LATER` lower third, never slowed down. The camera move is left to Vidu, anywhere from her side round to her front, never from straight behind: a camera starting behind her and swinging round broke the blade on her back as it passed behind her, roll after roll. From the front side the singer's headlight shows behind her; once it closes in, the cut ends. No blade plate: the sword stays sheathed and the hilt is on the riding plates, and a bare blade given as a reference invites a drawn one. There is no side piece: 25b's gun cuts straight to 25d's parry. Kept `25a.mp4`, from the prompt below: all 5s usable, a little flat; the type, the `BONUS STAGE` HUD and the cut on the beat carry it.

1. `rival-ride.png`
2. `rival-ride-back.png`
3. `rival-face.png`
4. `bike-rival.png`
5. `highway.png`

```text
@image1 and @image2 are the rival from the front and from behind, @image3 is her face. @image4 is her motorbike. @image5 is the place.

Night, after the rain, on the empty elevated highway in @image5, the asphalt still wet. The rival rides the black motorbike of @image4 flat out toward the right of the frame, low over the tank, her green hair and its two tied tufts whipping in the wind, her katana in its black scabbard strapped across her back, the green hilt above her right shoulder, as in @image2. The thin green light strip along the side of the bike glows, and its headlights sweep the wet road. She leans the bike hard into a curve, the rear wheel throwing a fan of spray, the neon of the city streaking past behind her in long lines of light. The camera races with her at her speed, from her side or ahead of her, moving the whole time, never from behind her. She is being chased: a single round white headlight follows close behind her on the road, a few car lengths back, glaring on the wet asphalt, the rider behind it lost in its glare. Dark: the only light comes from the neon, the bike's lights and the wet road reflecting them. Fast, full real-time speed, no slow motion.

She keeps the face, hair and riding gear of her references for the whole clip. Her hair is clearly green, a vivid leaf green as in @image3, not blonde, short, with the two tied tufts standing up. No helmet. One rider in clear view, one katana, in its scabbard on her back; behind her only the chaser's headlight. Glossy semi-realistic anime with soft airbrushed shading, as in the references: a drawn anime character, not live action.
```

Reject riding to the left, a helmet or a hood, a second rider seen clearly, no headlight behind her, a headlight far down the road, two headlights behind her, the blade in her hand, the scabbard at her hip, a broken or bent blade on her back, a bike that changes shape, a camera behind her, a camera that holds still or looks down from above, falling rain, or slow motion.

### 25b · The singer gives chase

Q4, 5s. On screen 1:34:01–1:35:21, the shot at 1:35:15: the rival's look back, the singer coming at the camera, the gun swinging up, and one shot, in one clip, so the camera closes in on the gun instead of cutting to it. No face plate: the helmet hides her face. Kept `25b.mp4`, from the prompt below: it ends on the first shot, a purple flash. Her hands break early in the clip, so the cut is the last part, a little under 3s, from where the hands are right to the shot, ending on the flash. One shot, one parry in 25d: Vidu doesn't keep a count of shots or strokes (five or six shots for three asked), and three strokes made the parry weak. The pistol is in her left hand from the first frame and only swings up: with a draw from the holster, three of four moved the gun to her right hand or held it in both, off the handlebars.

1. `singer-ride-helmet.png`
2. `bike-singer.png`
3. `highway.png`

```text
@image1 is the singer. @image2 is her motorbike. @image3 is the place.

Night, after the rain, on the empty elevated highway in @image3, the asphalt still wet. The singer rides the white motorbike of @image2 flat out straight at the camera, low over the tank, in her white racing suit with the purple stripes and her white helmet with the purple stripe, the dark visor closed, the thin purple light strip along the side of the bike glowing, its headlight glaring off the wet road. Her right hand stays on the right handlebar grip the whole time, on the throttle. A black pistol is already in her left hand from the first frame, held low at her side. She leans the bike hard into a curve, her left knee almost on the asphalt, the tyres hissing through a sheet of spray, and as she comes out of the lean she swings the pistol up in her left hand alone and aims it past the camera, her left arm straight out. The camera starts low and close in front of her front wheel, racing backward ahead of her, then swings round to her left side as she leans, ending close beside the gun at the height of her arm, her helmet just behind it; it shakes with the road, the neon of the city streaking past behind her in long lines of light. Her whole upper body and the front of the bike stay in the frame. Dark: the only light comes from the neon, the bike's lights and the wet road reflecting them. Fast, full real-time speed, no slow motion.

She keeps the helmet and outfit of her reference for the whole clip, the visor closed, no hair showing. One motorbike, one rider, one pistol, always in her left hand; her right hand never leaves the handlebar. Glossy semi-realistic anime with soft airbrushed shading, as in the reference, not flat cel shading.
```

Reject the gun in her right hand or in both hands, her right hand off the handlebar, a draw from the holster, the helmet off or the visor open, hair out of the helmet, a sword, a second rider, her small in the distance, a camera that holds still or stays in front of her, falling rain, or slow motion.

### 25d · Perfect parry

Q4, 5s. On screen 1:35:21–1:37:01, the parry at 1:36:06, straight from the gun to the rival, shot to reverse: she cuts the bullet out of the air. `PERFECT PARRY` on her side of the HUD, and no hit stop: a held frame on a moving bike reads as the video stalling. One blade in the frame, so the colour can't split. The blade is drawn from the first frame, on the plates with the empty scabbard: with a draw, the blade came from somewhere other than her back and the parry was weak. Neither the chaser nor the bullet is in the frame: with `bike-singer.png` the bullet came out of odd parts of the bike, without it the headlight came out as a car, and a bullet asked for in the frame gave a wrong, cheap parry every time. The singer fires from behind her, low on her right, so the rival swings her blade down and back to her lower right, and the hit is a purple flash on the steel where it stops. Kept `25d.mp4`, all 5s usable, which swings hard enough at 100% and holds up to about 200%.

1. `rival-ride-drawn.png`
2. `rival-ride-drawn-back.png`
3. `rival-face.png`
4. `blade-rival.png`
5. `bike-rival.png`
6. `highway.png`

```text
@image1 and @image2 are the rival from the front and from behind, @image3 is her face. @image4 is her katana. @image5 is her motorbike. @image6 is the place.

Night, after the rain, on the empty elevated highway in @image6, the asphalt still wet. The rival rides the black motorbike of @image5 flat out toward the right of the frame, its thin green light strip glowing, the empty black scabbard on her back. Her green-glowing katana is already drawn in her right hand from the first frame; her left hand steers. Close shot from low on her right side, a little behind her, the camera tilted up, from her waist to above her head, the night sky and the neon towers behind her. She glances back over her right shoulder and swings the blade hard down and back to her lower right in one fast stroke, and it snaps to a dead stop: at that instant a bright purple flash bursts on the green steel with a spray of purple and green sparks, and the shock jolts her arm. She looks ahead again, calm. The camera races beside her, close, and shakes with the hit. Dark: the only light comes from the neon, her blade and the flash. Fast, full real-time speed, no slow motion.

She keeps the face, hair and riding gear of her references for the whole clip. Her hair is clearly green, a vivid leaf green as in @image3, not blonde, short, with the two tied tufts standing up. No helmet. One rider, one katana, in her right hand; the scabbard on her back is empty, no hilt in it. No bullet, no tracer, no gun, no other vehicle anywhere in the frame. Glossy semi-realistic anime with soft airbrushed shading, as in the references: a drawn anime character, not live action.
```

Reject a bullet or tracer in the frame, a vehicle or a headlight behind her, the flash before the blade stops, more than one stroke, a slow, floating stroke, riding to the left, the blade in her left hand, a draw from the scabbard, a hilt on her back, falling rain, or slow motion.

### 25e · The gantry falls

Q4, 8s. On screen 1:37:01–1:41:07: 25e and 25f in one clip, the cut and the fall. A rider can't reach the beam, so she cuts a leg and the beam comes down. The gantry is drawn by Vidu, not given as a plate: an action on something already in the plate (a gantry plate, since deleted) broke every time, a stroke at nothing, a gantry falling flat from both legs. In one clip the leg she cuts is the one that gives way. The strike is one fast sweep that hits the leg in an explosion of sparks: worded as slicing through the leg, she drew the blade through it like a kitchen knife. The beam has to come down hard and catch fire, because 25g's gantry is burning. Kept `25e.mp4`, from the prompt below. The edit adds a white flash on the strike, with no hit stop since she is riding, then the three-frame white strobe, a shake and extra sparks on the impact at 1:39:16.

1. `rival-ride-drawn.png`
2. `rival-ride-drawn-back.png`
3. `rival-face.png`
4. `blade-rival.png`
5. `bike-rival.png`
6. `highway.png`

```text
@image1 and @image2 are the rival from the front and from behind, @image3 is her face. @image4 is her katana. @image5 is her motorbike. @image6 is the place.

Night, after the rain, on the empty elevated highway in @image6, the asphalt still wet. A short way ahead, a big steel sign gantry spans the whole road: two thick steel legs at the two edges of the road and a steel beam across the top, three large glowing blue and white direction signs hanging from it, with nothing written on them. The camera is low on the road behind the rival, the chaser's view. She rides away from the camera toward the gantry flat out on the black motorbike of @image5, seen from behind as in @image2, the empty black scabbard on her back, her green-glowing katana already drawn in her right hand. She swerves to the right edge of the road, and as she passes the right leg she whips the blade across in one wide, lightning-fast sweep without slowing down, her arm already through the swing in an instant: the blade's edge strikes the base of the steel leg with a violent explosion of white and orange sparks spraying across the road and a sharp flash of green light, a glowing green gash left in the steel. She rides on under the beam and away down the road. Behind her the struck right leg buckles and snaps with a burst of sparks. The beam tips: its right end crashes down toward the road in a long, heavy arc, pivoting on the left leg, which stays standing, and smashes into the asphalt in a massive explosion of sparks, the signs shattering into flying glass and burning debris, flames bursting up along the twisted steel and thick black smoke rolling up into the night. The left end stays up on the left leg, so the beam lies slanting across the road, burning. The camera races after her low on the road, then slows as the beam comes down in front of it, and shakes hard with the impact. Dark: the only light comes from the neon, the signs, her blade, the sparks and the fire. Fast, full real-time speed, no slow motion.

She keeps the hair and riding gear of her references. Her hair is clearly green, a vivid leaf green as in @image3, not blonde, with the two tied tufts standing up. No helmet. One rider, one katana, in her right hand; the scabbard on her back is empty, no hilt in it. The motorbike only ever moves forward, away from the camera. No other vehicle. Glossy semi-realistic anime with soft airbrushed shading, as in the references: a drawn anime character, not live action.
```

Reject a slow sawing or slicing motion, the blade held against the steel, a stroke that hits nothing, no sparks on the strike, the left leg cut or falling, a beam that lands without fire or smoke, both legs falling, the beam falling flat and even, the gantry falling before the stroke, her riding toward the camera or across the frame, the bike stopping, slowing or moving backward, the blade in her left hand, a hilt on her back, a car or any other vehicle, lettering on the signs, falling rain, or slow motion.

### 25g · Stopped

Q4, 5s. On screen 1:41:07–1:42:21: the fallen gantry stops her. She brakes too late, lays the bike down and slides, and stops just short of the burning beam, the road beyond it closed. One size for the whole clip, her whole body and the bike. The slide only: with the pistol flying from her hand and the sleeve tearing in the prompt, the first four made the pistol the subject, and what the crash cost, the torn sleeve and the pistol on the road, is in 26's panels. A prompt where she slid under the beam had her through it and stopping on the far side on every roll, still in the chase, which 26 contradicts. The fallen gantry is in words, with `highway.png`: 25e's gantry is Vidu's own. It burns and smokes, so it reads as a wall. Kept `25g.mp4`: she slides and stops against the burning beam, on this side, the bike on its side, the helmet on. Only the second half, about 2.5s, is usable: she is braking, so the slower slide is right, and a speed-up makes it look like she never braked.

1. `singer-ride-helmet.png`
2. `bike-singer.png`
3. `highway.png`

```text
@image1 is the singer. @image2 is her motorbike. @image3 is the place.

Night, after the rain, on the empty elevated highway in @image3, the asphalt still wet. A big steel sign gantry has just fallen across the whole road, slanting from one edge to the other, a wall of twisted steel and smashed blue and white signs on the asphalt, small fires burning along it, thick dark smoke rolling up from it into the night, sparks and embers drifting. Low side view from the road, the fallen beam on the right of the frame. Both hands on the handlebars, the singer rides in from the left of the frame flat out on the white motorbike of @image2 with its purple strip, toward the beam, in her white racing suit and white helmet. She brakes hard, too late: she throws the bike down on its side and slides with it on her right hip along the wet asphalt toward the beam, in a long shower of orange sparks where the bike scrapes the road, and comes to a stop just short of the burning beam, on this side of it, the bike on its side beside her. The camera slides with her, low over the road, and jolts when she stops. Dark: the only light comes from the fires, the sparks, the headlight and the neon on the wet road. Fast, full real-time speed, no slow motion.

She keeps the helmet and outfit of her reference, the visor closed, no hair showing. One motorbike, one rider, nothing in her hands but the handlebars. She never passes the beam. Glossy semi-realistic anime with soft airbrushed shading, as in the references, not flat cel shading.
```

Reject her passing under or through the beam, her stopping on the far side, a road open past the beam, the bike hitting the beam, her tumbling off the bike, the helmet coming off, a pistol anywhere in the frame, no fire or smoke, falling rain, or slow motion.

### 25h · The tail light

Q4, 5s. On screen 1:42:21–1:44:07, into 26's last panel. The singer's view from where 25g stopped her: the camera is still from the first frame, because she can't follow, and the burning gantry is between the camera and the rival, so the cut from 25g keeps the wall. Kept `25h.mp4`, the second of four, all 5s usable: the green light of her bike on the road and the wall says it's her even as a dot. A roll with the camera still and no gantry in it is the fallback, `25h-2.mp4`.

1. `rival-ride-back.png`
2. `bike-rival.png`
3. `highway.png`

```text
@image1 is the rival from behind. @image2 is her motorbike. @image3 is the place.

Night, after the rain, on the empty elevated highway in @image3, the asphalt still wet. The camera is low on the road and completely still for the whole clip. Across the bottom of the frame, close in front of the camera, lies a fallen steel sign gantry, twisted steel and smashed signs, small fires burning along it, dark smoke drifting up past the camera. Beyond it, already well down the road, the rival rides away flat out on the black motorbike of @image2, seen from behind, down the middle of the road, her red tail light and the green light strip shrinking into the neon until they are one point of red light. Dark: the only light comes from the fires, the neon and her tail light on the wet road. Full real-time speed, no slow motion.

One motorbike, one rider, no helmet. Glossy semi-realistic anime, as in the references: not live action.
```

Reject a camera that moves, the gantry standing or missing, her riding toward the camera, a second rider, a car, falling rain, or the light vanishing behind anything.

## Verse 3 on

Not written yet: 26–53. The plates are all made, 29's two places included: the singer tending her arm in her apartment (`apartment.png`) and the rival alone at the closed tea stall at night (`tea-stall-night.png`), instead of the agency and the rooftop again.

## Made, out of the cut

Kept for later use, with the prompt that made them.

### 23 · The smuggler's smile

Q4, 5s. Kept `23.mp4` for the reveal in 34: at this point in the song she is still the smuggler. A small sure smile, the yellow eyes and the green bob, no sword.

1. `rival-front.png`
2. `rival-face.png`
3. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred behind her. Extreme close-up of the rival's face, from her chin to the top of her head, nothing below her chin in frame. Rain falls on her hair, and a few drops sit on her cheeks. Her eyes are dry and calm, not crying. The corner of her mouth slowly lifts into a small, confident smile. Her eyes stay on the camera. No sword in frame. The camera holds still.

She keeps the face, hair and outfit of her references for the whole clip. She keeps the two tied tufts of short yellow-green hair. Glossy semi-realistic anime, as in the references.
```

### 20f · The apprentice takes the blow

Q3 Cinematic, 8s. Kept `20f.mp4`, for the memories in 27: 23b holds the blow in chorus 1, and the same woman twice in a row broke the cut. Green hair on every roll once `rival-gi.png` was corrected; before that the dusk turned it blonde on all four.

1. `rival-gi.png`
2. `rival-gi-face.png`
3. `dojo.png`

```text
@image1 and @image2 are the rival as a young apprentice: training clothes and face. @image3 is the place.

Dusk in the old dojo in @image3: the paper screens glow deep orange from the low sun outside, red paper lanterns hang lit from the beams, warm light and deep warm shadows that give her face and clothes their shape. Wooden practice swords, no steel: each is one plain piece of pale wood, no wrapped grip, no metal. Side view, full body, the camera tracking with her. The rival at about twenty, a serious apprentice in the middle of hard training, steps in from the right of the frame toward the left, barefoot, and meets a downward cut from an opponent just out of the frame on the left. She stands upright, her back straight, her weight centred between her feet, not leaning forward. She raises her wooden practice sword in both hands and holds it level above her head to catch the cut, the shock running down her arms, her back foot sliding a little on the floor, then she pushes the blow away. Her hair in two low loose pigtails swings with the impact. Her hair is vivid leaf green as in @image2, closer to green than to yellow, and stays green even in the orange light: not blonde, not gold. Her face is focused and hard, mouth closed, eyes fixed ahead, no smile. Full real-time speed, no slow motion.

She keeps the face of her references and the indigo training jacket and hakama of @image1 for the whole clip. Two low loose pigtails, no upright tufts, her hair down to her shoulders. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action, not a real person, not a photograph.
```

### 23c · Her face now

Q4, 5s. Kept `23c.mp4`; out because her hard face now is the end of 24c.

1. `rival-front.png`
2. `rival-face.png`
3. `bridge-deck.png`

```text
@image1 and @image2 are the rival: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3. The camera starts low on her green-glowing katana, held level just under her chin, the steel filling the bottom of the frame, and tilts up fast to her face, pushing in until it fills the frame from her chin to just above her brows. Her face is hard and cold, no smile, her mouth set, her eyes fixed on someone very close just ahead of her. The green light of her blade lights her face from beneath. Rain falls in front of her face. Dark all around.

She keeps the face of her references for the whole clip. Her eyes stay dry, no tears. Her hair is clearly green, a vivid leaf green as in @image2, not blonde. Glossy semi-realistic anime, as in the references: a drawn anime character, not live action.
```

### 15b · The stage from above

Q3 Cinematic, 8s. Kept `15b.mp4`, the long straight deck from high above, the two small, walking toward each other. Out: a shot from high above can't hold both a long bridge and two readable women, and the chorus needs the whole bridge between them.

```text
@image1 and @image2 are the singer: front and face. @image3 and @image4 are the rival: front and face. @image5 is the singer's katana. @image6 is the rival's katana. @image7 is the place.

Night, heavy rain, the footbridge in @image7 in an extreme wide shot from very high above, looking steeply down at the whole bridge. The deck is long and runs straight across the whole frame from the left edge to the right edge, many times longer than it is wide, about twenty glowing red paper lanterns along each railing, black canal water all around it and the lights of the city on the far bank. The people on it are tiny: each woman is no taller than one of the lanterns. The singer at the left end and the rival at the right end walk slowly toward each other, a calm, steady, smooth walk, and stop far apart, facing each other. Both are small in the frame. Both katanas stay in black scabbards at their left hips. The camera holds still.

Both women keep the faces, hair and outfits of their references for the whole clip. The singer's white jacket and the rival's long black coat stand out against the dark deck. Flat black sandals, no high heels. Glossy semi-realistic anime, as in the references: drawn anime characters, not live action.
```

### i1, i2, i3 · Inserts

Q4, 5s. Kept `i1.mp4`, `i2.mp4`, `i2-2.mp4`, `i3.mp4`, `i3-2.mp4`, made for an earlier cut of chorus 1. i1 and i2 the singer's and the rival's eyes narrowing (i1 with the singer's front, face and `bridge.png`; i2 the same for the rival, `the singer` changed to `the rival`); i3 her hand on the hilt of the drawn blade, a standoff pose the bridge has no place for.

```text
@image1 and @image2 are the singer: front and face. @image3 is the place.

Night, heavy rain, on the footbridge in @image3, red lanterns blurred behind. Extreme close-up of the singer's eyes and brows. She narrows her eyes and stares hard into the camera. The camera holds still.

She keeps the face of her references for the whole clip. Glossy semi-realistic anime, as in the references.
```

i3: `rival-front.png`, `rival-face.png`, `blade-rival.png`, `bridge-deck.png`.

```text
@image1 and @image2 are the rival: front and face. @image3 is her katana. @image4 is the place.

Night, heavy rain, on the footbridge in @image4, red lanterns blurred behind. Extreme close-up of the rival's right hand on the green-wrapped hilt of her katana at her hip, the black coat sleeve at the edge of the frame, rain running off the hilt. Her hand tightens its grip. The camera holds still.

She holds only her own katana, as in @image3. Glossy semi-realistic anime, as in the references.
```

Also on disk and out of the cut: `18-old.mp4`, `19-1.mp4`, `19-2.mp4` (the singer from behind), `20-1.mp4`, `20-2.mp4`, `21.mp4`, `22.mp4`, `24.mp4`, `22c-2.mp4`, `22d-2.mp4`, all from the first bridge batch, before the rebuild to one woman a cut.

## Midjourney

All plates are made. These are the recipes, for a remake.

Settings: Version **8.2**, Stylization 250, Weirdness 0, Variety 0, Speed Relax. Aspect **2:3** for bodies, **1:1** for faces, **16:9** for places and bikes, **3:1** for blades.

V8.2, not V7: on the same prompt V7 came back younger and flatter. Niji only does flat cel shading. V8.2 has no Omni Reference, so a second view of someone is Quick Edit on the front plate (or the Edit model with the plate attached). Style Reference still works. `shaved head` in `--no` wipes the undercut, so hair is described in the positive. Props stay off the plates, except where the shots draw from them: the rival's katana on her back, the singer's holster, the master's sheath at her hip.

What every Quick Edit needs said, or it goes wrong:

- **The side of the picture.** "Her left thigh" alone put the holster on the wrong side on every roll; "her left thigh, on the right side of the picture as she faces the camera" fixed it. Same for the hilt over a shoulder and a torn sleeve.
- **Nothing printed.** Clothes come back with brand-like marks on the chest and shoulder. Name the chest plain and add `--no logo, emblem, badge, patch, lettering, text, watermark`. A few still get through: pick the clean one, and crop marks at the image edges.
- **The figure, not the fabric.** "Tight across her chest" drew every chest flat; name the shape itself.
- **"Bare" means no sleeve.** "A graze on her bare forearm" tore the sleeve off. Keep both sleeves on and put the graze inside the tear.
- **Matte.** "Coat" and "bodysuit" came back as shiny leather and latex, which reads as a 3D game render. Write `matte wool`, `matte knit`.

### The singer

Three steps. First roll, no reference: the body the close-up was made from.

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, an adult woman with a sharp undercut, the sides of her head and the nape buzzed to the scalp, only the hair on the crown left long and tied into a high ponytail with a red cord, a calm neutral face, bold straight dark eyebrows, a short white jacket with wide sleeves worn open over a black bodysuit with the collar closed to the throat, wide black trousers, a red sash at the waist, black sandals over black split-toe socks, plain light grey background --no chibi, child, three-quarter view, profile, turned head, flat cel shading, mascot, american comic, western comic, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, earrings
```

Quick Edit on that image: the approved face.

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her undercut, and her ponytail. Make her eyebrows very thick and straight, relaxed, with a smooth forehead and no crease between them. The outer corner of each eye sits slightly lower than the inner corner.
```

Quick Edit on that close-up: the full body, rebuilt. Kept the middle row, second from the left.

```text
Full body from head to feet, straight-on, both shoulders square to the camera. Keep this exact face, these eyebrows, this undercut, and this ponytail. A short white jacket with wide sleeves worn open over a black bodysuit with the collar closed to the throat, wide black trousers, a red sash, black sandals, arms relaxed, plain light grey background.
```

### The rival

A new generation, not a Quick Edit: `singer-front.png` in **Style reference** only, so the rendering matches, and nothing attached to the prompt, or she comes out a copy of the singer.

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, an adult woman, a calm neutral face, short bright yellow-green hair, two thick tufts of that same hair tied with bands and standing upright above her temples, amber eyes, the rest of her hair cut short above the shoulders, a long black high-collared coat worn open with a green lining, a dark green bodysuit with the collar closed to the throat, slim black trousers, black sandals over black split-toe socks, plain light grey background --no chibi, child, three-quarter view, profile, turned head, antennae, horns, pods, long hair, ponytail, flat cel shading, mascot, overalls, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, animal tail --ar 2:3 --sw 200 --v 8.2
```

Reject dark hair, a white coat, pods or antennae that are not hair, the tufts missing, hair past her shoulders, an animal tail, anything that makes her look like the singer. The kept roll (middle row, far right) came back in leather and latex; the kept plate is this Quick Edit on it:

```text
Keep this exact face, this hair, and these clothes. Make the coat matte black wool and the bodysuit matte dark green knit fabric, no shine, no leather, no latex.
```

### Backs and faces

Quick Edit on the front plate. The singer's back:

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her undercut, and her ponytail. Plain light grey background.
```

The rival's back:

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her short hair, and the two tied tufts on top of her head. Plain light grey background.
```

The rival's face:

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her short hair, and the two tied tufts.
```

Reject a back with the face turned toward the camera, or green legs on the rival (the trousers are black). The close-up draws the tufts longer than the front plate; pick the one closest.

The long form, if Quick Edit is not available: Version 8.2, the Edit model, the front plate attached. Back, then face:

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, crisp high resolution, character design, full body from head to feet in frame, back view, seen from directly behind, eye level, the woman standing straight, arms relaxed at her sides, plain light grey background --no chibi, child, front view, face, letterbox, black bars, text, watermark, signature, sword, weapon --ar 2:3 --v 8.2
```

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, crisp high resolution, character design, head and shoulders portrait, front view, eye level, the woman looking straight at the camera, a calm neutral face, plain light grey background --no chibi, child, letterbox, black bars, text, watermark, signature --ar 1:1 --v 8.2
```

The first `singer-back.png` had the jacket ending at the waist with the sash showing, which the front rules out. Fixed by Quick Edit: "The back of her white jacket is longer and hangs straight down to her hips, plain white fabric across her whole back and waist, with only black trousers below it. Keep everything else exactly the same." Naming the sash in an edit, even to hide it, puts it back.

### The master

`master-front.png`: Version 8.2, 2:3, `singer-front.png` as Style reference only. Kept the fourth of the first roll. A man first: four rolls of an old swordmaster all came back photorealistic or as a 3D game render. On both kept plates the circuit line is under her right eye, whatever the prompt says.

```text
straight-on front view, the camera directly in front of her face, both shoulders square to the camera, both ears equally visible, symmetrical, eye level, full body from head to feet in frame, adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, luminous skin, finely detailed eyes, soft airbrushed shading, vivid saturated colour, crisp high resolution, standing straight, arms relaxed at her sides, a tall elegant woman who looks about forty-five, a sharp beautiful face, narrow cold grey eyes, a calm stern face, long straight silver hair worn loose down to her waist with a blunt straight fringe, a thin glowing blue circuit line running down from under her left eye, a long matte grey wool haori coat worn open over a fitted matte dark grey knit bodysuit with the collar closed to the throat, black hakama trousers, black boots, plain light grey background --no chibi, child, teenager, three-quarter view, profile, turned head, ponytail, bun, twin tails, red eyes, aura, flat cel shading, mascot, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, sword, weapon, leather, latex, armour, green, red --ar 2:3 --sw 200 --v 8.2
```

`master-face.png`: Quick Edit on the front. Kept the fourth.

```text
Head and shoulders close-up of this same woman, straight-on. Keep her face, her long straight silver hair with the blunt fringe, and the thin glowing blue line under her left eye.
```

### Costumes

Quick Edit on the front plate each time, 2:3, so the face and hair stay. Reject any roll where the face changes, the singer loses the undercut or the red cord, or the rival loses the tufts.

`singer-suit.png`, on `singer-front.png`. Kept the third; the others carried the red sash over as a strap.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, and this ponytail with its red cord. Dress her in a slim matte black suit, a white shirt with the collar open and no tie, black ankle boots, and narrow black sunglasses. Arms relaxed, plain light grey background.
```

`rival-hood.png`, on `rival-front.png`. Kept the first, the closest hair colour.

```text
Full body from head to feet, straight-on. Keep this exact face, this short yellow-green hair and the two tied tufts. Dress her in an oversized matte black hoodie with the hood down and green drawstrings, slim black cargo trousers, and black sneakers. Arms relaxed, plain light grey background.
```

`singer-ride.png`, on `singer-front.png`: the base for the helmet and the crash, deleted once the two were made. A racer's one-piece zipped to the throat: the fit shows her shape, where an open zip read as fan service. White and purple, her bridge colours. The holster on her left thigh: she is right-handed, but the throttle is the right grip, so the left hand draws. Kept the bottom row's third of the last two rolls.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, and this ponytail with its red cord, all her hair pulled back into the ponytail, no loose locks over her face, the shaved side of her head showing. Dress her in a form-fitting matte white one-piece motorcycle racing suit, skin-tight from the shoulders to the ankles, a full, rounded bust clearly shaped by the tight fabric, an hourglass figure with a narrow waist, rounded hips and long legs, a thin purple stripe down each sleeve and curving down the side of her waist, hip and leg, zipped all the way up to a short high collar at her throat, the chest plain white on both sides with nothing printed or sewn on it, black riding gloves, black knee-high riding boots over the suit, and a black pistol holster strapped high on her left thigh, on the right side of the picture as she faces the camera. No helmet, no glasses. Arms relaxed, plain light grey background. --no logo, emblem, badge, patch, chest mark, lettering, text, watermark
```

Reject a flat chest, an open zip, sunglasses or goggles, shine, patches or logos, the holster on the left of the picture, locks of hair over her face, or a changed face.

`singer-ride-helmet.png`, on `singer-ride.png`. Kept the first, the visor dark all over. All her hair inside the helmet: a ponytail streaming out would break in Vidu.

```text
Full body from head to feet, straight-on. Keep this exact racing suit, these boots and this holster. Put a matte white full-face motorcycle helmet on her head, a purple stripe running over the crown from front to back, a dark smoked visor closed over her face, a faint purple glow along the lower edge of the visor. All her hair is inside the helmet: no hair shows. Arms relaxed, plain light grey background.
```

Reject a face visible through the visor, hair out of the helmet, a gloss helmet, lettering, or a changed suit.

`singer-ride-torn.png`, on `singer-ride.png`: after the crash in 25g, for 26 and 29. Kept the fourth of the second roll, the only empty holster. Its scuffed knee is her left, not her right; at the size of 26's panels it doesn't read.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, this ponytail with its red cord, and this riding gear. Damage the clothes only. Both sleeves stay on her arms, down to her gloves. Her left sleeve, on the right side of the picture, is whole and clean. Her right sleeve, on the left side of the picture, has one long ragged tear from the shoulder to the elbow, the sleeve still on the arm, a red graze on her skin showing through the tear. Grey road grit down her right side, her right hip and right knee scuffed through. The holster on her left thigh is empty, its open top showing, no pistol in it. Arms relaxed, plain light grey background.
```

Reject a changed face, blood, a bare arm or a sleeve torn off, both sleeves torn, the tear on the right of the picture, or the pistol still in the holster.

`rival-ride.png`, on `rival-front.png`. Black and green against the singer's white and purple; no helmet. Kept the third, the strap clear across her chest.

```text
Full body from head to feet, straight-on. Keep this exact face, this short yellow-green hair and the two tied tufts. Dress her in a fitted matte black motorcycle riding jacket zipped all the way up to a short high collar at her throat, a thin green stripe down each sleeve, fitted matte black riding trousers, black knee-high riding boots and black riding gloves. Her katana in a black lacquered scabbard is strapped across her back: a black strap runs across her chest from her right shoulder down to her left hip, and the green-wrapped hilt rises above her right shoulder, on the left side of the picture as she faces the camera. No helmet, no hood. Arms relaxed, plain light grey background. --no logo, emblem, badge, patch, lettering, text, watermark
```

Reject a helmet or a hood, shine, lettering, the hilt on the right of the picture, a sword in her hand, the tufts lost, or a changed face.

`rival-ride-back.png`, on `rival-ride.png`. Kept the third, the green stripes down both sleeves as on the front.

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her short hair, the two tied tufts on top of her head, and the katana in its black scabbard strapped diagonally across her back, from her right shoulder down to her left hip, the green-wrapped hilt above her right shoulder, on the right side of the picture. Plain light grey background.
```

Reject her face turned toward the camera, the scabbard missing, the hilt on the left of the picture, or green legs.

`rival-ride-drawn.png` and `rival-ride-drawn-back.png`: 25d and 25e start with the blade drawn, and a plate with the hilt in the scabbard makes Vidu draw a second hilt on her back. The scabbard stays, empty. Not Midjourney: Quick Edit asked to empty the scabbard repainted the whole figure, a near-photo face and a short thick tube for a scabbard, on all eight. Made from the kept plates by `_tools/image/erase_hilt.py`, which paints the hilt and guard out with the background and caps the scabbard with the oval of its open mouth:

```sh
python _tools/image/erase_hilt.py 0006-en-two-blades/characters/rival-ride.png 0006-en-two-blades/characters/rival-ride-drawn.png --top 180 56 --guard 297 230 --side left --cut 16 --half-width 15 --radius 23 --guard-half 13 40
python _tools/image/erase_hilt.py 0006-en-two-blades/characters/rival-ride-back.png 0006-en-two-blades/characters/rival-ride-drawn-back.png --top 657 52 --guard 547 234 --side right --cut 22 --half-width 16 --radius 23 --guard-half 13 40
```

`rival-raid.png`, on `rival-front.png`: 29, the raid and the roof, one night. Not the hood: the hoodie was her cover at the harbour, and in the raid she is in charge. Kept the first, the green lining at the collar and both cuffs.

```text
Full body from head to feet, straight-on. Keep this exact face, this short yellow-green hair and the two tied tufts. Dress her in a cropped matte black bomber jacket with a short high collar, its dark green lining showing at the collar and the cuffs, a fitted matte dark green top under it, slim black cargo trousers tucked into black combat boots, black fingerless gloves, and the black sheath of her katana strapped across her back. No hood. Arms relaxed, plain light grey background.
```

`rival-raid-back.png`, on `rival-raid.png`. Kept the first, one small green tab at the collar.

```text
Show this same woman from directly behind, full body, standing straight, arms relaxed. Keep her clothes, her short hair, the two tied tufts on top of her head, and the katana in its black sheath strapped diagonally across her back, from her right shoulder down to her left hip, the hilt above her right shoulder, on the right side of the picture. Plain light grey background.
```

`singer-tactical.png`, on `singer-front.png`. Kept the third.

```text
Full body from head to feet, straight-on. Keep this exact face, this undercut, and this ponytail with its red cord. Dress her in fitted matte black tactical gear: a black combat suit, a black armoured vest, fingerless gloves, an empty holster on her thigh, black boots, a small earpiece. Arms relaxed, plain light grey background.
```

`master-boss.png`, on `master-front.png`: the rooftop. The grey haori is the teacher of the memories; on the roof she is the one behind the smuggling, so black, the red of her eyes in the seams. Calm on the plate: the red eyes and the aura go into the shots. Kept the fourth, the crimson lining framing her face.

```text
Full body from head to feet, straight-on. Keep this exact face, this long straight silver hair with the blunt fringe, and the thin glowing line under her eye. Dress her in a long matte black high-collared coat worn open, its crimson lining showing, over a fitted matte charcoal armoured bodysuit, thin crimson seams glowing faintly along the edges of the coat and the bodysuit, black gloves, black boots, and a katana with a red-wrapped hilt in a black sheath at her left hip. Calm face, her eyes their own colour. Arms relaxed, plain light grey background.
```

Reject red eyes, the haori, shine, armour plates like a robot, or a changed face.

The apprentices. The past has different hair, so the switch to the memories reads in one frame; the colour stays, so each is still recognisable. `singer-gi.png`, on `singer-front.png`:

```text
Full body from head to feet, straight-on. Keep this exact face. Change her hair: no undercut, her black hair grown out long and loose past her shoulders, a thin red cord tied around her left wrist. Dress her in a plain indigo training jacket and indigo hakama trousers, barefoot. Arms relaxed, plain light grey background.
```

`rival-gi.png`, on `rival-front.png`:

```text
Full body from head to feet, straight-on. Keep this exact face and this yellow-green hair colour. Change her hair: no upright tufts, the hair longer, down to her shoulders, tied into two low loose pigtails. Dress her in a plain indigo training jacket and indigo hakama trousers, barefoot. Arms relaxed, plain light grey background.
```

The kept `rival-gi.png` came back pale yellow-green and went blonde in the dojo's light. Quick Edit toward the green of `rival-gi-face.png` gave dark forest green or yellow-green again, so the kept plate's hair was shifted by `_tools/image/match_hair_hue.py` to the face plate's median hue (+25°). The prompt that was tried:

```text
Keep this exact woman, her face, pose, clothes, framing and the white background unchanged. Change only her hair colour: a bright, light, fresh leaf green, like a young spring leaf in sunlight, with light green highlights. Not dark green, not forest green, not yellow, not blonde. Keep the two low loose pigtails.
```

The face plates of the past, so Q4 doesn't get two hairstyles to choose from. Quick Edit on the present face plate, so the face is the one already chosen. `singer-gi-face.png`, on `singer-face.png` (kept the second, the wrap-front jacket):

```text
Keep this exact face, expression, framing and lighting. Change only her hair and clothes: no undercut, no ponytail, her black hair grown out long and loose past her shoulders. A plain indigo training jacket. Plain white background.
```

`rival-gi-face.png`, on `rival-face.png` (kept the second). "Training jacket" alone came back as a zipped sports jacket, one with a Nike logo, so it names the keikogi.

```text
Keep this exact face, expression, framing, lighting and this yellow-green hair colour. Change only her hair and clothes: no upright tufts, the hair down to her shoulders, tied into two low loose pigtails. A plain indigo keikogi, the Japanese martial arts training jacket with a crossed wrap-front collar, no zip, no logo, no text. Plain white background.
```

For the old photo in shot 8 the three backgrounds have to match. Quick Edit on `singer-gi.png`, `master-front.png` and `rival-gi.png`:

```text
Keep this exact woman, her face, hair, clothes, pose and framing unchanged. Replace only the background with pure white, no gradient, no floor line, no shadow, no vignette.
```

### Blades and bikes

Version 8.2, Style Reference `singer-front.png`, 3:1. Purple and green: the first roll came back red and black, and red is the singer's cord. `blade-singer.png`, kept the second roll's bottom left:

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a purple-wrapped hilt, a round black guard, a long curved polished steel blade, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200 --v 8.2
```

`blade-rival.png`, kept the second roll's top left:

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a single katana lying horizontally, the whole sword from the pommel to the tip in frame, a green-wrapped hilt, a square black guard, a long curved dark steel blade with a thin glowing green line along its spine, plain light grey background --no person, hand, sheath, text, watermark, signature, 3d render, photorealistic --ar 3:1 --sw 200 --v 8.2
```

The bikes, 16:9, no Style Reference. In words alone Vidu draws a different bike every cut. No make or model in the prompt: a brand name brings its badges. Different shapes as well as colours, so the two read apart in silhouette. Side on, facing right, the way both ride. `bike-rival.png`, kept the top left:

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, crisp high resolution, a sleek matte black full-fairing sport motorcycle, aggressive sharp angular bodywork, twin narrow LED headlights, a thin glowing green light strip running along the side of the fairing, black wheels, side view from the right, the whole motorcycle in frame, facing the right of the frame, no rider, plain light grey background --no logo, brand, lettering, text, number, decal, rider, person, watermark --ar 16:9 --v 8.2
```

`bike-singer.png`, kept the middle left:

```text
adult anime illustration, anime key visual, cinematic lighting, glossy detailed rendering, crisp high resolution, a sleek matte white full-fairing sport motorcycle, smooth rounded bodywork, a single round headlight, a thin glowing purple light strip running along the side of the fairing, black wheels, side view from the right, the whole motorcycle in frame, facing the right of the frame, no rider, plain light grey background --no logo, brand, lettering, text, number, decal, rider, person, watermark --ar 16:9 --v 8.2
```

Reject lettering anywhere on the bike, a light strip wider than a thin line (a glowing bike glows whole in Vidu), wheels of different sizes, a three-quarter view, or a bike facing left.

### The case

Version 8.2, `singer-front.png` as Style reference, 16:9. `zunda mochi` alone drew Brussels sprouts, four of four: the prompt describes the thing. Kept the fourth of the second roll, the white mochi showing under the paste.

```text
glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, a hard silver case lying open, seen from slightly above, neat rows of Japanese sweets inside on black foam like jewels, each one a soft round white rice cake covered in a thick smooth coat of bright pale green mashed edamame paste, the paste glossy with a faint green glow, a red circular crest stamped on the inside of the lid, plain light grey background --no brussels sprouts, cabbage, vegetable, leaves, lettuce, balls, person, hand, text, watermark, signature, 3d render, photorealistic, letters --ar 16:9 --sw 200 --v 8.2
```

### Places

Version 8.2, 16:9, empty so Vidu places the people. No Style Reference from a character plate, except `bridge.png`, made first: on a street plate it drained the neon. Every place prompt opens with `anime background art, hand-painted`: night water and city light pull V8.2 toward a photo. Reject any person or a shape that could be one, readable real words or logos, a 3D render, or a photograph. Signs come out as fake script, which is fine.

Every place that has held the anime look in Vidu is dim with a strong light in it. Every bright daylit room turned the apprentice live action.

`bridge.png`, Style Reference `singer-front.png`. Kept the first roll's bottom left: a side view, the whole arch, the deck clear.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a narrow arched wooden footbridge over a dark canal, the whole bridge in frame from one bank to the other, red paper lanterns hung along both railings glowing warm, heavy rain, the wet planks shining, a near-future city at night behind it, elevated highways on concrete pillars, tall towers covered in neon signs and hologram billboards in cyan and magenta, their light reflected in the canal --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --sw 200 --v 8.2
```

`tea-stall.png`, no Style Reference, two empty cups already on the counter. Kept the top left.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a small tea stall tucked between the concrete pillars of an elevated highway at dawn, a worn wooden counter under a short cloth awning, a steaming iron kettle, two empty ceramic tea cups side by side on the counter, a single paper lantern still glowing warm, light rain, wet pavement, pale blue morning light, a near-future city waking up behind it, hologram signs dimmed for the morning --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature, ramen, noodles, menu --ar 16:9 --v 8.2
```

`hq.png`. Kept the fourth.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a dark high-tech agency operations room at night in a near-future city, a huge curved wall of hologram screens glowing cyan, a long glass table lit from within, floor-to-ceiling windows streaked with rain, neon towers outside --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature --ar 16:9 --v 8.2
```

`apartment.png`, for 29: the singer tending her arm after the crash. Empty of props she handles: given in the plate, the bandages and the first-aid kit would break the moment she reaches for them, so they go in the Vidu prompt in words. Dry: it is the night of the chase, after the rain. Neo-Edo inside as well as out, tatami and shoji with light built into them: a plain room with only the neon outside read as today, and a plain cyberpunk room as any sci-fi film. Kept the second roll's bottom left: the table near and large, the shoji's warm light on one side and the window's neon on the other.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a small dark one-room apartment at night in a near-future neo-Edo city, Japanese tradition and future tech together, a tatami mat floor, sliding shoji screens with thin glowing light strips set into their dark wooden frames, a low wooden table on the tatami with a flat cushion beside it, a futon rolled up against the wall, a thin glowing lamp bar on the table casting warm light, a faint hologram panel floating blank on one wall, a curved smart-glass window filling the far wall with neon towers, elevated highways and a hologram billboard outside throwing cyan and magenta light across the room, deep shadows in the corners, lonely and quiet --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, rain, sun, sunlight, daylight --ar 16:9 --v 8.2
```

`tea-stall-night.png`, for 29: the rival alone at the stall, closed. Quick Edit on `tea-stall.png`, so it is the same stall as verse 1. The cups go: on the counter they would be a prop she can't touch. Kept the top left, the counter bare.

```text
Keep this exact tea stall, the pillars and the city. Make it late at night: the stall closed, the cloth awning rolled up, the counter bare, no cups and no kettle, the paper lantern unlit. The only light is a cold streetlight from the highway above and the neon of the city behind. No rain, the pavement dry.
```

`harbour.png`. Kept the second. Three rolls put a figure on the quay despite `--no person`.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, a container harbour at night in a near-future city, stacks of shipping containers, huge cranes against the sky, a wet concrete quay, orange sodium lights and cyan neon, the city's towers glowing across the black water, light rain --no person, figure, crowd, ship crew, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, sun, sunlight --ar 16:9 --v 8.2
```

`warehouse.png`. Kept the first, the widest aisle.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, inside a huge dark warehouse at night, tall stacks of wooden crates and shipping containers with an aisle between them, red alarm lights, beams of cold light through high windows, a metal catwalk overhead, a wet concrete floor --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature --ar 16:9 --v 8.2
```

`highway.png`. Kept the second.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, an empty elevated highway at night in a near-future city, the road closed and empty, wet asphalt reflecting neon, white lane lines running away from the camera, tall streetlights, towers with hologram billboards in cyan and magenta on both sides, heavy rain, a red and white glow of traffic far below --no person, figure, crowd, car, truck, vehicle, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --v 8.2
```

`highway.png` was then made dry by Quick Edit, so the chase reads as another night than the bridge. All four came back nearly the same; kept the top left. A gantry plate made the same way is deleted: an action on a gantry already in a plate broke every roll, so Vidu draws it.

```text
Keep this exact highway, these towers and this light. The rain has stopped: no falling rain, no drops in the air. The asphalt is still wet, mirroring the neon in puddles.
```

`dojo.png`. At dusk, because daylit rooms turned the apprentice live action and a Style Reference drained the gold to grey. Warm amber against the bridge's blue rain, with 4:3 and grain, tells the past from the present.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, inside an old wooden Japanese dojo at dusk, dark polished wooden floorboards, dark wooden pillars and beams, paper shoji screens along one wall glowing deep orange from the low setting sun outside, red paper lanterns hanging from the beams, lit and glowing warm, deep warm shadows in the corners, a wooden rack of practice swords on the far wall --no person, figure, crowd, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, calligraphy, scroll, watermark, signature, daylight, blue sky --ar 16:9 --v 8.2
```

`rooftop.png`. Kept the fourth, the koi centred over the floor.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, wide shot, eye level, the flat rooftop of a skyscraper at night in a near-future city, heavy rain, wet concrete shining with reflected neon, a painted helipad circle, air vents and a low parapet at the edge, a giant hologram billboard of a koi fish glowing cyan and magenta on the tower next to it, more towers covered in neon signs all around and far below, low clouds lit from beneath --no person, figure, crowd, helicopter, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --v 8.2
```

`rooftop-dawn.png`, Quick Edit on `rooftop.png` so the roof stays the same roof:

```text
Keep this exact rooftop and these towers. Make it dawn: the rain has stopped, the sky pale pink and gold, the hologram billboard faded and almost transparent, the neon signs switched off, puddles on the roof reflecting the sky.
```

The close views: the wide plate as Style Reference at `--sw 200`, no image prompt, and the prompt names only what fills the frame, never the whole place. Given the wide plate as an image, every roll came back as the wide plate again, and Vidu sees the place from outside.

`bridge-deck.png`, Style Reference `bridge.png`. Kept: the railing straight and level across, no post in the middle, the deck in the bottom third.

```text
glossy semi-realistic anime, anime key visual, soft airbrushed shading, vivid saturated colour, crisp high resolution, close view of a red wooden railing with glowing red paper lanterns hanging from it, the railing running straight and level across the whole frame at chest height a few steps away, wet wooden planks shining in the foreground along the bottom of the frame, night, heavy rain, behind the railing a black canal and far away elevated highways and neon towers of a near-future city, blurred into bokeh, shallow depth of field --no person, figure, crowd, arch, whole bridge, river bank, letterbox, black bars, sepia, 3d render, photorealistic, text, watermark, signature --ar 16:9 --sw 200 --v 8.2
```

`warehouse-aisle.png`, Style Reference `warehouse.png`. Kept the first roll's bottom left, the only one in two rolls with the crates straight across the frame.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, close view at chest height of a wall of stacked wooden crates a few steps away, running straight and level across the whole frame, a faint green glow leaking through the slats of some crates, a red alarm light throwing red light across them, a wet concrete floor shining in the foreground along the bottom of the frame, a metal catwalk high above, blurred, shallow depth of field, night --no person, figure, crowd, aisle, whole warehouse, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature --ar 16:9 --sw 200 --v 8.2
```

`rooftop-floor.png`, Style Reference `rooftop.png`. Kept the first roll's top right, the koi big over the parapet, no lettering.

```text
anime background art, hand-painted anime key visual, glossy semi-realistic anime, soft airbrushed shading, vivid saturated colour, crisp high resolution, close view at chest height of a low concrete parapet at the edge of a skyscraper roof a few steps away, running straight and level across the whole frame, wet concrete floor shining with reflected neon in the foreground along the bottom of the frame, behind the parapet a giant hologram koi fish glowing cyan and magenta on the next tower and neon towers far below, blurred into bokeh, shallow depth of field, night, heavy rain --no person, figure, crowd, helicopter, helipad, whole roof, letterbox, black bars, sepia, 3d render, photorealistic, photograph, photo, text, watermark, signature, blue sky, sun, sunlight --ar 16:9 --sw 200 --v 8.2
```

`rooftop-floor-dawn.png`, Quick Edit on `rooftop-floor.png`. Kept the second roll's bottom left, the tail almost gone. The night koi is solid, so Quick Edit can't fade it to an outline; it reads as the same hologram still running at dawn. The first roll, with `rooftop-dawn.png`'s text, drew a real red carp.

```text
Keep this exact rooftop, this parapet and these towers. Make it dawn: the rain has stopped, the sky pale pink and gold, the neon signs on the towers switched off and dark, puddles on the roof reflecting the sky. The hologram koi is fading out: only a faint glowing cyan and magenta outline of the fish is left, so thin and transparent that the tower behind it shows clearly through its whole body. Not a real fish. Painted anime background art, not a photograph.
```

## The first Vidu tests

Run before the shots, on the bridge plates.

**Q4, blades locked, 5s.** Identities held the whole way: one blade each, the bodies apart. The blades came out short and thick. The clip was the finished pose from the first frame, with only breath, sparks and rain moving.

**Q4, the leap, 8s.** The leap and the clash happen and the bridge holds, but the render is an older 3D game, and the women look composited onto the bridge.

**Q4, four shots in one take, 16s.** The two face close-ups held; the running wide and the clash failed on motion and picture.

**Q3 Cinematic, the same leap, 8s.** Better motion, and the women sit in the rain and the light. A second roll added its own slow motion, a second blade and a broken tumble. Two or three rolls per shot is normal. **Q3 Flash:** flat cel and a mobile-game render. **Q3, four shots in 16s:** extra swords, four arms, women appearing from nothing. Multi-shot is out: one action a clip.

**One woman with a sword on an empty stage, Q4 and Q3.** Both render a 3D game body: a full body gives the model cloth, limbs and a floor to rebuild. Full bodies stay in rain and city light, never on a bare stage.

**Flat anime plates, Q4.** Plates redrawn as 2D anime stayed 2D but looked cheap; fuller TV-anime plates came back toon-shaded 3D. The CG look comes from the plate, not the model, so the glossy semi-real plates stayed.

What the edit can do with a weak clip: a short piece sped up, a few frames of the hit slowed, a white flash, a shake, sparks, grain, one grade over the song. It can't put a pasted figure back into the rain or carry a long wide shot.
