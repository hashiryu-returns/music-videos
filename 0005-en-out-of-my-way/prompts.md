# 0005 prompts

Shot list and timing: [`README.md`](README.md#shot-list). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

## Files

Characters, in [`characters/`](characters/) (copies of the 0002 plates). These go in Omni Reference:

- `hedgehog.png`: her, in every scene she's in
- `papa-panda.png`: #36 only
- `brother-fox.png`: #37 only
- `mama.png`: #38 only

Style sheets, in [`stills/`](stills/). These go in Style Reference:

- `style-character.png`: every scene with anything alive in it, however small. Her, the family, every robot and monster
- `style-landscape.png`: only the empty scenes, #1, #25, #29–#31, #43

## Midjourney

Settings panel, for everything:

- Version 7. Niji 7 has no Omni Reference
- Aspect 16:9
- Stylization 250
- Weirdness 0
- Variety 0 (15 for the style sheets)
- Speed **Relax**. Omni Reference is silently ignored in Fast and Draft

For each scene:

1. Drag the file named after **Style Reference** on the cut's Midjourney line into Style Reference.
2. Drag the file named after **Omni Reference** into Omni Reference. If it says **no Omni Reference**, leave that slot empty.
3. Paste the prompt as is. It already ends in `--sw` (and `--ow` when there's an Omni Reference).
4. Check `sw` and `ow` show under the result. If `ow` is missing, you're not in Relax.

Two references, two jobs. Omni Reference holds who she is: her face, spines, cape and the 0002 ink look all come from `hedgehog.png`. Style Reference holds the line weight and the colour feel. Never two style sheets on one scene.

### Sky and time

No take shares a background with another take. Each enemy is in one take, and its defeat is shown with beams or bubbles over empty ground, or in the second half of its own split take. Close-ups of her are against open sky. Two cuts may share a planet, but never a set: no ledge, house, hill or beach is drawn twice. So the only thing that has to carry over is the sky.

Every prompt ends its scene with one fixed sky line, word for word the same for every cut in that place. The style sheets were rolled at different times of day, so the prompt has to set it. Ground colour can drift a little between cuts; sky colour and time of day can't.

| Place | Cuts | Sky line |
| --- | --- | --- |
| Desert, day | #1–#18, #34 | `late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight` |
| Ice planet, evening | #19 | `evening on the ice planet, a deep violet twilight sky, cold blue light on the snow` |
| Ice planet, night | #25–#31 | `dark violet night sky, deep purple indigo sky, faint stars` |
| Swamp | #20 | `night on the swamp planet, a dark navy sky full of stars, the only light coming from the glowing plants` |
| Crystal canyon | #21–#24 | `midday on the crystal planet, a clear pale blue sky, bright white daylight` |
| Above the clouds | #32–#33 | `late afternoon high above the clouds, a warm golden sky, soft golden light` |
| Desert, night | #39 | `night on the desert planet, a dark navy sky full of stars` |
| Desert, sunset | #35–#38 | `sunset on the desert planet, an orange and pink sky, long warm shadows` |
| Pink sea | #40–#42 | `morning on the ocean planet, a clear pale turquoise sky, bright morning light` |
| Orbit | #43 | `deep space, a black sky full of stars` |

#41 swaps in a cloud-bank version of their place's line, because the beam needs clouds to come out of.

Planets, moons and suns change shape and colour from roll to roll, so they're only in the prompts that need them: the pale planet in #1 and #43, two moons in #19, two suns in #35. One that turns up uninvited is fine unless it takes over the picture.

Reject on sight: day turning to night, or night to day, between cuts in the same place; a sunset or pink-cloud look in the daytime desert (#1–#18) or at the pink sea; ground of a clearly different colour.

### Writing a prompt

- With an Omni Reference, the prompt says only "the hedgehog girl" (or "the panda", "the fox kit", "the woman") and what she's doing and holding. Describing her face or cape again fights the plate.
- Full-body shots of her say `with bare clawed feet`. The plate is barefoot and V7 likes to add shoes and trousers; once she wears them in one cut she'd need them in all. Shoes or clothes on her legs are a reject.
- Wide shots say what must fit in the frame and use `--sw 200`. If a still comes back too close, do the same.
- Night scenes use `muted dark colours` instead of `vivid saturated colours`, and add `blue sky, sun, sunlight` to `--no`.
- Only three things recur: her, the family plates, and the lightsaber (a red glow, so a different hilt doesn't show). Anything else she wears or rides is in one take only, because Omni Reference holds one thing, her. The hoverbike and the goggles are both in #3 and nowhere else.
- Her face never changes in motion: no putting goggles on, no waking from closed eyes. The still starts in the end state and Vidu moves the body.
- Props use the same words every time so they match: `a red lightsaber` (`an unlit lightsaber hilt with no blade` before it lights).
- `signature` is in every `--no`: the character sheet has a scrawl in its corner, and Style Reference passes it on.
- `modern anime` in the opening block doesn't take, because the look comes from the plate. It's left in so every prompt starts the same.

No Zoom Out, Pan or Vary Region on an Omni Reference result. Re-roll with the framing in the prompt.

### Style sheets

Already made. These are the strings they were rolled with.

**`style-character.png`**

- Style Reference: **none**
- Omni Reference: `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, eye level, her whole body from the tips of her spines to her feet in frame, the hedgehog girl standing on a rocky ledge on an alien desert planet, holding a short silver hilt with a glowing red energy blade in one paw, the other paw pointing forward, her red cape blowing, orange sand dunes and red rock spires behind her with every crack outlined in black ink, a huge ringed planet low in a clear sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark --ow 350
```

**`style-landscape.png`**

- Style Reference: `style-character.png`
- Omni Reference: **none**

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot, an alien desert planet, orange sand dunes, tall red rock spires with layered strata and cracks outlined in black ink, the rusty hull of an old crashed starship half buried in the sand with panel lines and rivets, a huge gas giant with wide bright rings low in a clear sky --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, person, figure, animal --sw 250
```

## Vidu

Image to Video, Q2, 1080p, Cinematic, Amount 1, Off-Peak Mode. Off-Peak makes any Q2 length free, so takes over 5s are generated at 8s and trimmed. Takes of 5.0s or less are generated at 5s. #3 runs past 8s: generate 8s, then Extend from its end with the next motion line. Q3 came out unusable on #3; don't use it for length.

An 8s take needs two actions, joined with `then`, and so does each part of #3. One action stretched over 8s goes slack: the lightsaber lighting up on its own couldn't hold #2. A 5s take gets one.

Say `lightsaber`, not `energy sword`. Vidu drew a proper one from that word on #2, so the Midjourney prompts use it too. It stays out of titles and descriptions.

**Split takes.** One clip can play twice, as two cuts with another cut between them: three cuts from two clips, and the halves match because they're the same clip. Cuts 3, 6, 7, 10, 16, 21 and 25 are clips that play twice. The later cut only says which part to use. In iMovie, drop the clip in twice and trim one copy to its first action and the other to its second.

- The clip needs two clearly separate actions joined with `then`, so the second cut starts on something readable.
- The insert is a different subject, never her in the same situation: the other side of a fight (her against the walker, the drones, the giant), or the world reacting (#4's winged reptiles, #13's critters). An insert that needs her goggles, bike or set to match defeats the point of splitting.

Beams and bursts are never in the still; Vidu adds them from the motion line. Bubbles that are already floating (#14, #17, #42–#43) are painted in.

## Scenes

Numbered by cut, in edit order. A cut that reuses an earlier cut's clip only says which part to use.

### Intro

#### Cut 1 · Gas giant over the desert

0:00.0–0:04.2 · use 4.2s

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot, an alien desert planet, orange sand dunes and tall red rock spires in the foreground with every crack outlined in black ink, a huge plain pale grey gas giant with faint stripes sitting low on the horizon, half hidden below it, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, sunset --sw 250
```

Keep: inked red spires and dunes in front, a big plain pale planet low on the horizon, teal sky, daylight.

Re-roll: pink or orange clouds; a sunset or dawn look; a planet with bold colours or patterns; a figure anywhere; black bars, painted background.

**Vidu** · 5s

```text
The small white clouds drift across the sky and the wind blows streams of sand off the dunes as the camera drifts forward.
```

Keep: the clouds drift, sand blows and the camera moves forward. The planet stays put.

Re-roll: the planet moves fast or melts; the spires melt; a cut to another shot, the style turning 3D.

#### Cut 2 · Lightsaber on the ledge

0:04.2–0:12.2 · use 8.0s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot from behind, low angle, the hedgehog girl with bare clawed feet standing on the edge of a high red rock ledge, small in the frame, seen from behind, her red cape blowing out to the side, the dunes far below, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, front view, facing camera, sunset --sw 200 --ow 330
```

Keep: her from behind, small on the edge of a high ledge, cape out to the side.

Re-roll: she faces the camera; she fills the frame; shoes or trousers; a human child; black bars, painted background.

**Vidu** · 8s

```text
A glowing red lightsaber shoots up out of the hilt in her paw and hums, then she swings it in a wide arc over her head and points it at the horizon. The wind moves her cape and the plants.
```

Keep: the lightsaber lights, then swings and points; the cape and plants move.

Re-roll: she turns to the camera or steps off the ledge; two lightsabers; the blade bends; a cut to another shot, the style turning 3D.

The first take with only the lightsaber lighting up was too slow for 8s; the swing and point fill the second half.

#### Cut 3 · Hoverbike ride

0:12.2–0:15.8 · use 3.6s. Cut 5 is 3.6s of this clip, flipped.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
Modern anime illustration, anime opening key visual style, clean digital line art with thin precise black outlines, flat cel shading, soft two-tone shadows. A wide-angle, slightly low shot of a full anthropomorphic hedgehog girl with bare, clawed feet, crouched low in a dynamic pose. She is riding a sleek, red and white futuristic hoverbike with large, circular anti-gravity repulsor pads underneath, glowing with blue light. The hoverbike is leaping or hovering in mid-air over a large, rolling sand dune. She is wearing round, brass-rimmed goggles over her eyes and has a big grin, her spines textured. Both paws are on the handlebars. The background is a vast desert planet with rolling orange dunes, under a clear, bright teal blue sky fading to pale cream at the horizon, with a few wispy clouds. Natural full color, vivid, saturated colors. Crisp, high resolution. Fine detailed ink outlines on every edge of the bike, the character, and the terrain detail. No text, no signature. --sw 250 --ow 330
```

Keep: her crouched on the red and white hoverbike in mid-air over a dune, goggles on, blue glow under the repulsor pads.

Re-roll: wheels; the bike on flat ground; shoes; black bars, painted background.

**Vidu** · 8s, then Extend by at least 2.8s

```text
The futuristic hoverbike accelerates forward off the crest of the dune and glides out into mid-air over the slope, hovering smoothly above the ground as it lands, then races left to right across the dunes as the camera tracks alongside, glowing thrusters blazing and a massive spray of sand blasting behind it from the repulsor pads.
```

**Vidu Extend** · from the end of the 8s clip

```text
The hoverbike suddenly launches over a sharp dune crest into mid-air, catching massive height. The camera dynamically orbits around the front of the vehicle in a dramatic low-angle shot as blue energy arcs from its bottom repulsors, before it slams back toward the sand in a high-speed glide.
```

Keep: the glide off the crest and the race in the 8s clip (cut 3); the second launch and the orbiting camera in the extension (cut 5), the hoverbike unchanged across the join.

Re-roll: the hoverbike changes shape across the join; wheels appear; a cut to another shot, the style turning 3D.

Made with these prompts, written in full sentences rather than the block above. The only take with the hoverbike and the goggles. Neither is on the plate, so they'd come out different in any other still. The goggles are on in the still: putting them on in Vidu changes her face and breaks the plate.

### Verse 1

#### Cut 4 · Winged reptiles scatter

0:15.8–0:19.3 · use 3.5s

Insert between the two halves of #3, on "Red cape on and spikes up high". The planet's wildlife, scattered by the bike's noise. Nothing in it has to match anything.

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot, low angle, a flock of a dozen small winged reptiles like pterosaurs with spiky red crests and leathery teal wings bursting off the top of a tall red rock spire and wheeling into the sky, every wing, claw and crack of the spire outlined in black ink, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset, person, figure, hedgehog, vehicle, hoverbike, dragon --sw 200
```

Keep: the winged reptiles in the air above a red spire, only sky and rock in frame.

Re-roll: a dragon instead of small reptiles; the bike, a rider or any figure; feathers or birds; black bars, painted background.

**Vidu** · 5s

```text
The flock of winged reptiles bursts off the top of the rock spire all at once, screeching, and wheels across the sky in a wide arc, wings beating hard, as sand blows off the spire in a gust.
```

Keep: they all take off and wheel across the sky.

Re-roll: they merge into one creature; the spire moves; a cut to another shot, the style turning 3D.

#### Cut 5 · Hoverbike ride, second half

0:19.3–0:22.9 · use 3.6s of cut 3's clip, flipped.

#### Cut 6 · Walker robot

0:22.9–0:25.7 · use 2.8s. Cut 8 is 2.2s of this clip, flipped.

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle wide shot, a giant four-legged walker robot stepping over the ridge of an orange sand dune, a boxy armoured head with two round red lights, long jointed metal legs, panel lines, rivets and dents outlined in black ink, sand pouring off its feet, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, sunset --sw 200
```

Keep: one huge four-legged walker on a dune ridge, inked panels.

Re-roll: a person or animal in frame; more than one walker; black bars, painted background.

**Vidu** · 8s

```text
The colossal walker marches forward across the desert, planting each huge foot heavily onto the dune as sand bursts up around it, the entire body moving steadily across the frame as the camera tracks its motion, then it stops dead and swivels its boxy head toward the camera, its two red lights flaring.
```

Keep: it strides across the frame (cut 6), then stops and turns its lights on her (cut 8).

Re-roll: the legs slide or multiply; the head turns before it stops; a cut to another shot, the style turning 3D.

The 5s take had only the stride. Re-take at 8s for the stop and turn.

#### Cut 7 · Point, then spin

0:25.7–0:27.7 · use 2.0s. Cut 9 is 3.5s of this clip.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle full shot, the hedgehog girl with bare clawed feet standing with a red lightsaber held down at her side in one paw, her other paw pointing straight up out of the frame, her mouth open shouting, her red cape blowing, nothing behind her but open sky, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 200 --ow 330
```

Keep: her from below pointing up and shouting, lightsaber down at her side, only sky behind.

Re-roll: a robot or anything else in the sky; two lightsabers; shoes; black bars, painted background.

**Vidu** · 8s

```text
She jabs her paw up and shouts, then spins the red lightsaber in fast circles around her and ends pointing it straight ahead. Her cape whips in the wind.
```

Keep: the point and shout (cut 7), then the spin, ending on a point (cut 9).

Re-roll: she walks or slides; the blade bends or doubles; a cut to another shot, the style turning 3D.

#### Cut 8 · Walker robot, second half

0:27.7–0:29.9 · use 2.2s of cut 6's clip, flipped.

### Pre-chorus 1

#### Cut 9 · Point, then spin, second half

0:29.9–0:33.4 · use 3.5s of cut 7's clip.

#### Cut 10 · Laser charge

0:33.4–0:35.4 · use 2.0s. Made, `clips/10.mp4` (8.0s). The first "Out of my way!" lands at 0:35.4, where this cut ends and Chorus 1 starts. Cut 12 is the last 1.9s of this same clip.

The base's laser cannon, white with a red rim, charges until the lens glows solid red. The walker isn't in the shot, so nothing has to match cuts 6 and 8.

A satellite seen from orbit never came out: Midjourney drew it skimming low over the ground every time. A cannon close-up with the planet behind it works.

### Chorus 1

#### Cut 11 · Laser fire

0:35.4–0:36.9 · use 1.5s. Made, `clips/11.mp4` (8.0s). The laser fires from the station's structure.

#### Cut 12 · The beam hits

0:36.9–0:38.8 · use the last 1.9s of cut 10's clip. The beam comes down and hits the desert.

#### Cut 13 · Critters pop up

0:38.8–0:40.6 · use 1.8s. Made, `clips/13.mp4` (2.1s). After the blast, big-eared desert critters pop their heads out of round burrows and sit up, looking out. They don't bow. The boss isn't in the shot.

#### Cut 14 · Bubble hop

0:40.6–0:42.4 · use 1.8s. Made, `clips/14.mp4` (8.0s). No still. She bounces from bubble to bubble over the dunes, between the critters and the wide shot of the dust.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium wide shot, the hedgehog girl with bare clawed feet in mid-air bouncing off the top of a big shiny soap bubble, hundreds of bubbles of every size floating around her over the dunes, her red cape streaming, laughing, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 200 --ow 330
```

Keep: her in the air over a big bubble, bubbles everywhere, dunes below.

Re-roll: standing on the ground; shoes; black bars, painted background.

**Vidu** · 8s

```text
She bounces off the big bubble and it pops, then she lands on the next bubble and bounces off it again, laughing. Each bounce carries her further left to right across the frame as the camera tracks alongside and the bubbles and dunes scroll past behind her.
```

Keep: a bounce and a pop, then a second bounce.

Re-roll: her feet sink into the bubble or slide; the bubbles turn solid; a cut to another shot, the style turning 3D.

#### Cut 15 · Bubbles from the blast

0:42.4–0:47.0 · use 4.6s. Made, `clips/15.mp4` (8.0s), still [`stills/15.png`](stills/15.png). The blast on the dunes throws up a cloud of orange dust and hundreds of soap bubbles drift out of it into the sky. No robot in frame. The still is the empty desert; Vidu adds the dust and the bubbles.

#### Cut 16 · Drone swarm

0:47.0–0:49.6 · use the first 2.6s. The rest of this clip is cut 18.

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot, a swarm of dozens of small round flying drone robots, each a metal sphere with one red eye and short stubby fins, pouring over the ridge of a sand dune toward the camera, dust in the air, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, sunset --sw 250
```

Keep: many small round drones coming over a dune.

Re-roll: one big robot instead of many small ones; black bars, painted background.

**Vidu** · 8s

```text
The swarm of drones pours over the dune and rushes at the camera, growing bigger in the frame as the camera pulls back fast in front of it, then the drones pop one after another into shiny soap bubbles that float up into the sky.
```

Keep: the swarm rushes in (cut 16), then pops into bubbles (cut 18). Her spin in #17 sits between, so the pop reads as her doing.

Re-roll: the drones merge into a blob; a cut to another shot, the style turning 3D.

#### Cut 17 · Mid-air spin

0:49.6–0:52.9 · use 3.3s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium wide shot, the hedgehog girl with bare clawed feet in mid-leap spinning sideways in the air, a red lightsaber held out at arm's length, her red cape whirling around her, shiny soap bubbles all around her, nothing behind her but open sky, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 200 --ow 330
```

Keep: her airborne and spinning, lightsaber out, bubbles around her, sky behind.

Re-roll: standing on the ground; robots in frame; shoes; black bars, painted background.

`stills/17.png` shows the ground and she isn't spinning. The clip is the one that counts: she's in the air, seen from behind, lightsaber out, bubbles around her.

**Vidu** · 5s

```text
She spins in the air slashing the red lightsaber and the bubbles around her burst.
```

Keep: she spins and slashes.

Re-roll: the blade doubles; a cut to another shot, the style turning 3D.

#### Cut 18 · Drone swarm, second half

0:52.9–0:56.3 · use 3.4s of cut 16's clip.

### Verse 2

#### Cut 19 · Space dragon

0:56.3–0:59.8 · use 3.5s

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, low angle wide shot, a long-necked space dragon with pale blue crystal scales, a round goofy face, glowing cyan eyes, head thrown back roaring at the sky, wings spread wide, standing on top of a snowy ice hill, blue ice rocks, deep violet twilight sky, two small pale moons in the sky, evening on the ice planet, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, neutral grey shadows --no red skin, red dragon, chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure --sw 100
```

Keep: one crystal-blue dragon roaring on an ice hill, violet sky.

Re-roll: extra heads; too scary for a five-year-old (gore, dripping fangs); a daytime blue sky; black bars, painted background.

**Vidu** · 5s

```text
The dragon throws back its head and roars, frost puffing from its mouth.
```

Keep: the head goes back and frost comes out.

Re-roll: a second head appears or the jaw melts; a cut to another shot, the style turning 3D.

#### Cut 20 · Blob alien

0:59.8–1:03.1 · use 3.3s

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium shot, a big round wobbly translucent green jelly alien with two big googly eyes on stalks sitting in a swamp, bright cyan glowing plants and mushrooms around it, dark water, night on the swamp planet, a dark navy sky full of stars, the only light coming from the glowing plants --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, blue sky, sun, sunlight --sw 250
```

Keep: one round green jelly with eye stalks, glowing swamp at night.

Re-roll: a daytime sky; teeth or a gaping mouth; black bars, painted background.

**Vidu** · 5s

```text
The jelly alien wobbles and jiggles from side to side, its eye stalks bouncing.
```

Keep: the jelly wobbles.

Re-roll: it melts into the water; a cut to another shot, the style turning 3D.

#### Cut 21 · Stone giant

1:03.1–1:06.3 · use the first 3.2s. Cut 23 uses another 3.0s of this clip.

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle medium wide shot, a huge grumpy stone giant made of grey boulders with a frowning face and crossed arms, standing in the middle of a narrow canyon of giant purple crystals and blocking the way, every crystal edge outlined in black ink, midday on the crystal planet, a clear pale blue sky, bright white daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure --sw 200
```

Keep: one boulder giant with crossed arms filling a purple crystal canyon.

Re-roll: a human-looking giant; more than one giant; black bars, painted background.

**Vidu** · 8s

```text
The stone giant uncrosses its arms and leans down, scowling at the camera, then it turns around and runs away down the canyon, getting smaller as it goes.
```

Keep: the scowl (cut 21), then it turns and runs (cut 23). Her stamp in #22 sits between: "I stamp my foot, he runs away".

Re-roll: the boulders fall apart; it runs toward the camera; a cut to another shot, the style turning 3D.

#### Cut 22 · Stamp

1:06.3–1:07.4 · use 1.1s. Cut 24 is a second Vidu clip from this same still.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, low angle, the hedgehog girl with bare clawed feet standing on smooth purple crystal ground, one foot raised to stamp, a red lightsaber in one paw drawn back behind her shoulder ready to throw, giant purple crystals far off at the sides, midday on the crystal planet, a clear pale blue sky, bright white daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 330
```

Keep: her whole body on crystal ground, one foot up, lightsaber drawn back.

Re-roll: a giant or other creature in frame; shoes; two lightsabers; black bars, painted background.

**Vidu** · 5s

```text
Fast action. The hedgehog girl slams her foot down hard onto the crystal ground. Strong camera shake on impact as bright light cracks spread across the floor. 2D anime animation.
```

Keep: the stamp, the shake, and light cracks across the floor.

Re-roll: she slides forward; the lightsaber leaves her paw; a cut to another shot, the style turning 3D.

#### Cut 23 · Stone giant, second half

1:07.4–1:10.4 · use 3.0s of cut 21's clip.

### Pre-chorus 2

#### Cut 24 · Throw

1:10.4–1:13.8 · use 3.4s. Same Midjourney still as cut 22.

**Vidu** · 5s

```text
Fast dynamic anime action. The hedgehog girl swings her arm and throws the weapon. The glowing red lightsaber transforms into a rapidly spinning red energy disc flying fast across the frame, leaving a glowing light streak behind. Smooth 2D anime effect.
```

Keep: she throws, and the lightsaber becomes a spinning disc with a light streak.

Re-roll: it stays a sword in her paw; it doubles or bends; she stamps; a cut to another shot, the style turning 3D.

#### Cut 25 · The lightsaber cuts through the ice

1:13.8–1:15.6 · use 1.8s. Cut 28 uses another 1.8s of this clip. The chorus line lands at 1:15.8, just into the next cut.

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, wide shot, dynamic camera angle, empty snow field, pure white snow, tall blue crystal ice spikes stretching to the horizon, cold blue light on the ice, clean digital line art, thin precise black outlines, flat cel shading, dark violet night sky, deep purple indigo sky, faint stars, neutral grey shadows --no red sky, pink sky, red glow, sunset, orange, dragon, creature, monster, person, figure, bubbles, chibi, crosshatching, painted background, letterbox, 3d render, photorealistic --sw 150
```

Keep: empty white snow, tall blue ice spikes to the horizon, dark violet night sky.

Re-roll: a dragon, creature or figure; a red, pink or orange sky; bubbles in the still; black bars, painted background.

**Vidu** · 8s

```text
Fast intense anime action. A spinning red lightsaber glowing disc zips from the camera toward the background, slicing low through the tall blue ice spikes. The ice spikes dynamically shatter into glowing blue ice shards and spark particles. Shockwaves ripple across the snow field. Smooth 2D anime animation, high frame rate.
```

Keep: the disc flies away from the camera, the spikes shatter into blue shards, shockwaves cross the snow.

Re-roll: it flies toward the camera; a hand holds it; the ice melts into mush; a cut to another shot, the style turning 3D.

### Chorus 2

1:15.6–1:29.3, cuts 26 to 31, all on the ice planet at night.

#### Cut 26 · Catch

1:15.6–1:18.4 · use 2.8s. Made. Generated as her throwing the lightsaber up, then reversed in the edit, so it reads as a clean catch.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png` · [`stills/26.png`](stills/26.png)

**Vidu** · 5s, played backwards

```text
Fast anime action. The hedgehog girl throws the glowing red lightsaber upward into the sky. It spins rapidly into a red glowing energy disc as it flies high. Smooth 2D anime animation.
```

Keep: the lightsaber leaves her paw cleanly and spins into a disc. Reversed, that is the catch.

Re-roll: it bends or doubles; her paw deforms; a cut to another shot, the style turning 3D.

#### Cut 27 · Spin

1:18.4–1:20.9 · use 2.5s. Made. Same still as cut 26.

**Vidu** · 5s

```text
Fast dynamic 2D anime animation. The hedgehog girl fiercely twirls the glowing red lightsaber over her head in fast glowing circles, then points it straight at the camera with a confident grin.
```

Keep: the twirl, then the point at the camera.

Re-roll: the blade doubles or bends; she walks; a cut to another shot, the style turning 3D.

#### Cut 28 · The ice, second half

1:20.9–1:22.7 · use 1.8s of cut 25's clip. The spikes still shattering.

#### Cuts 29–31 · Ice mountain pops

Made. Three Vidu clips, one from each still. Cut 29 is 1:22.7–1:24.4 (1.7s), cut 30 is 1:24.4–1:26.1 (1.7s), cut 31 is 1:26.1–1:29.3 (3.2s). Stills: [`stills/29.png`](stills/29.png), [`30.png`](stills/30.png), [`31.png`](stills/31.png). One huge ice mountain bursting per cut, so the chorus hits on each beat.

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, dynamic low angle close-up shot, a massive blue crystal ice mountain collapsing and shattering into glowing ice shards, bright blue energy shockwaves bursting out, dark violet night sky background, deep purple indigo sky, faint stars, pure white snow, clean digital line art, thin precise black outlines, flat cel shading with neutral grey shadows --no red sky, pink sky, sunset, orange, person, figure, creature, monster, bubbles, chibi, crosshatching, painted background, letterbox, 3d render, photorealistic --sw 150
```

Keep: one huge ice mountain breaking open, blue glow, violet night sky.

Re-roll: a red or pink sky; a figure or creature; black bars, painted background.

**Vidu** · 5s

```text
Extreme dynamic 2D anime effect. The huge blue ice mountain violently shatters from the impact, exploding into thousands of bright glowing ice shards and snow dust that fly directly toward the camera. Smooth 2D anime animation, high frame rate.
```

Keep: the mountain bursts and the shards come at the camera.

Re-roll: it melts instead of shattering; a cut to another shot, the style turning 3D.

### Bridge

Nothing in the bridge is split. Cut 33 is its own still: the wide back view can't turn into a fist pump.

#### Cut 32 · The fleet

1:29.3–1:36.1 · use 6.8s. "Who's the boss? (Me!)" twice, then "Little spikes and a big red cape".

Made, [`stills/32.png`](stills/32.png). From behind, she stands on a rock above the clouds and the silver grey fleet flies past. A window shot was tried first; the style sheet turned the hull into a crash site, and Omni Reference turned her to face the camera.

**Vidu** · 8s

```text
Fast dynamic anime camera move. The fleet flies straight ahead, no turning. The camera starts behind her, then swings out to a low side angle as the huge silver battleship rushes past close to the lens, then rises to look down over the whole fleet stretching to the horizon. Her red cape whips in the wind and she stands still on the rock. Clouds rush past. Smooth 2D anime animation, high frame rate.
```

Keep: the ships fly straight while the camera swings from behind her, to a low side angle, to above the fleet. She stays on the rock.

Re-roll: the ships turn or bank; the ships merge or bend like rubber; she jumps or falls off; a cut to another shot, the style turning 3D.

#### Cut 33 · Fist pumps

1:36.1–1:38.8 · use 2.7s. "Who's the boss? (Me! Me! Me!)". Her own still. She's still on the rock, still facing the fleet, close enough that the fist reads. She does not turn around.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, neutral grey shadows, crisp high resolution, back view, medium shot from behind, the hedgehog girl with bare clawed feet seen from the back, her back to the camera, her face not visible, standing on a rocky outcrop high above a sea of golden clouds, one fist punched straight up, her other paw at her side, her red cape blowing, ahead of her a fleet of weathered silver grey starships with rounded hulls and glowing pink portholes, late afternoon high above the clouds, a warm golden sky, soft golden light --no front view, facing camera, face, eyes, lightsaber, sword, weapon, hilt, window, cockpit, shoes, trousers, pants, chibi, crosshatching, painted background, letterbox, black bars, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 150
```

`--ow 150`. At 330 she turns to face the camera, because `hedgehog.png` does.

Keep: her back, one fist up, the rock, silver grey ships over golden clouds.

Re-roll: her face showing; no fist; a window or a cockpit; white and red ships; shoes; black bars, painted background.

**Vidu** · 5s

```text
Seen from behind, she punches her fist up and shouts, then punches it up again and again. She does not turn around. The silver fleet keeps flying straight ahead over the golden clouds. Dynamic 2D anime animation.
```

Keep: the fist goes up again and again on "Me! Me! Me!", and we never see her face.

Re-roll: she turns toward the camera; she jumps off the rock; the ships bank; a cut to another shot, the style turning 3D.

#### Cut 34 · The blast, again

1:38.8–1:42.6 · use 3.8s, then a 1s circle close. The same explosion as cut 12, the beam hitting the desert, from its own image. Not the tail of `clips/10.mp4`.

### Verse 3

#### Cut 35 · Two suns setting

1:42.6–1:46.1 · use 3.5s, then a 0.3s cross dissolve.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

`--ow 180`. At 330 she turns around, because `hedgehog.png` faces the camera.

```text
modern anime illustration, anime opening key visual, epic wide shot from behind, cute hedgehog girl seen strictly from behind, rear view of her back and head spikes, wearing her red cape, sitting alone on the crest of a high sand dune, small in frame, looking towards two suns setting on the desert horizon, a lightsaber hilt lying unlit on the sand beside her, orange and pink sunset sky, long warm shadows, clean digital line art, thin black outlines, flat cel shading --no front view, facing camera, face, eyes, snout, mouth, active laser blade, holding weapon, glowing sword, standing, house, vehicle, shoes, chibi, 3d render --sw 250 --ow 350
```

Keep: her small, strictly from behind, sitting, two suns low, the handle dark on the sand.

Re-roll: her face, even in profile; she stands; the blade is lit; black bars, painted background.

**Vidu** · 5s

```text
The two suns sink slowly toward the horizon as the wind lifts the edge of her cape.
```

Keep: the suns sink and the cape lifts.

Re-roll: she stands up or turns around; a cut to another shot, the style turning 3D.

#### Cut 36 · Papa

1:46.1–1:48.2 · use 2.1s, then a 1s cross dissolve.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `papa-panda.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, eye level, the panda standing on a low sand dune, one paw raised and waving, a warm smile, sunset on the desert planet, an orange and pink sky, long warm shadows --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 330
```

Keep: the panda from the plate on a dune at sunset, waving.

Re-roll: a house or building; spines or a red cape (the style sheet leaking into him); a real bear; black bars, painted background.

**Vidu** · 5s

```text
The panda waves his paw slowly side to side and smiles.
```

Keep: the paw waves.

Re-roll: he walks; his face changes; a cut to another shot, the style turning 3D.

#### Cut 37 · Brother

1:48.2–1:50.2 · use 2.0s, then a 1s cross dissolve.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `brother-fox.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, the fox kit standing on top of a small sand dune, holding a small toy robot up over his head in both paws, mouth wide open cheering, sunset on the desert planet, an orange and pink sky, long warm shadows --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 330
```

Keep: the fox kit from the plate on a dune, toy robot overhead, cheering.

Re-roll: spines or a red cape; a grown fox; black bars, painted background.

**Vidu** · 5s

```text
The fox kit bounces on the spot, waving the toy robot over his head.
```

Keep: he bounces and waves the toy.

Re-roll: he runs; the toy changes; a cut to another shot, the style turning 3D.

#### Cut 38 · Mama

1:50.2–1:52.8 · use 2.6s, then a 1s cross dissolve.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `mama.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium shot, the woman holding a folded blanket in both arms, a soft smile, the evening wind in her hair, nothing behind her but the sunset sky, sunset on the desert planet, an orange and pink sky, long warm shadows --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 250 --ow 330
```

Keep: Mama from the plate with a blanket against the sunset sky.

Re-roll: a house or doorway; animal ears or spines (the style sheet leaking into her); a different woman; black bars, painted background.

**Vidu** · 5s

```text
She unfolds the blanket and holds it open with a smile.
```

Keep: the blanket opens.

Re-roll: she walks; her face changes; a cut to another shot, the style turning 3D.

#### Cut 39 · Hammock

1:52.8–1:55.8 · use 3.0s, then a 1s wipe up.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

`--ow 120`. At 330 she sits up and faces the camera, because `hedgehog.png` does. The hammock and the cape have to be two different cloths or they merge into one red wrap.

```text
modern anime illustration, anime opening key visual, epic wide shot from the side, the hedgehog girl lying flat on her back in a pale tan cloth hammock slung by ropes between two wooden posts, her red cape laid over her like a separate blanket, eyes open looking straight up at the stars, not at the camera, nothing behind the hammock but the sky, night on the desert planet, a dark navy sky full of stars, clean digital line art, thin black outlines, flat cel shading --no sitting up, upright, standing, front view, facing camera, eyes closed, bed, house, shoes, chibi, 3d render --sw 200 --ow 120
```

Keep: her flat on her back, a pale hammock between two posts, the red cape on top of her, stars behind.

Re-roll: she sits up; she faces the camera; the hammock is just the cape; eyes closed; a house or a bed.

**Vidu** · 5s

```text
She sits bolt upright in the swaying hammock and throws off the cape.
```

Keep: the sudden sit-up on the "Hey! Hey!".

Re-roll: she falls out of the hammock; her eyes close; a cut to another shot, the style turning 3D.

Eyes open in the still. Asleep-then-waking changes her face and breaks the plate, as the goggles did.

### Final chorus

#### Cut 40 · Rise and light up

1:55.8–1:58.6 · use 2.8s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

Not the hammock and not the dune. She is in the air, morning, turquoise sky. `--ow 200`: at 330 she stands on the ground facing the camera, which is the plate.

```text
modern anime illustration, anime opening key visual, extreme low angle, the hedgehog girl launched high in mid air, feet off the ground, knees tucked, small against a huge clear pale turquoise sky, holding an unlit lightsaber hilt with no blade, red cape snapping above her, a thin strip of pink sea at the very bottom of the frame, morning on the ocean planet, bright morning light, clean digital line art, thin black outlines, flat cel shading --no hammock, blanket, lying, sitting, standing on ground, desert, dune, sand, night, stars, sunset, orange sky, lit blade, glowing sword, chibi, 3d render --sw 200 --ow 200
```

Keep: her in the air, unlit hilt, turquoise sky, a little pink sea at the bottom.

Re-roll: she is on the ground; a hammock or a dune; night or a sunset; the blade is already lit.

**Vidu** · 5s

```text
She rises from the bottom of the frame up into the middle as the camera holds still, and a glowing red lightsaber shoots out of the hilt and hums.
```

Keep: she rises and the blade comes out.

Re-roll: the blade comes out bent or doubled; a cut to another shot, the style turning 3D.

#### Cut 41 · Robot squid

1:58.6–2:06.0 · use 7.4s

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle wide shot, a colossal robot squid with a domed metal head, two big round glowing yellow eyes and long segmented metal tentacles rising out of a shining pink sea, water pouring off it, panel lines and rivets outlined in black ink, morning on the ocean planet, a thick bank of white clouds across the top of the sky with pale turquoise showing through the gaps, bright morning light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, sunset --sw 200
```

Keep: one huge metal squid rising out of a pink sea, clouds above.

Re-roll: a real squid; a blue sea; no clouds; black bars, painted background.

**Vidu** · 8s

```text
The robot squid climbs higher and higher out of the sea, its whole body towering up the frame as water pours off it and its tentacles curl, then a thick red beam blasts down from the clouds onto it and it bursts into a huge cloud of shiny bubbles.
```

Keep: the squid rises, then the beam hits and it turns to bubbles.

Re-roll: tentacles tangle into mush; a fiery explosion; the squid stays whole; a cut to another shot, the style turning 3D.

The satellite base's second and last shot, from the clouds. The first was cuts 10 and 11.

### Outro

#### Cut 42 · Wave goodbye

2:06.0–2:11.2 · use 5.2s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium full shot, eye level, the hedgehog girl with bare clawed feet standing on a pink sand beach facing the camera, waving one paw, an unlit lightsaber hilt hanging at her side, hundreds of shiny soap bubbles drifting in the air around her, the pink sea behind her, morning on the ocean planet, a clear pale turquoise sky, bright morning light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 250 --ow 330
```

Keep: her facing camera and waving, bubbles all around, pink sea.

Re-roll: a human child; no bubbles; shoes; black bars, painted background.

**Vidu** · 8s

```text
She waves her paw at the camera with a big grin, then hops up and spins around as the bubbles swirl around her.
```

Keep: the wave, then the hop and spin.

Re-roll: she walks toward camera; her feet slide; a cut to another shot, the style turning 3D.

#### Cut 43 · Planet at night

2:11.2–2:20.0 · use 8.8s, then a 1s fade. The fade ends at 2:21.0.

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot from space, the same huge plain pale grey gas giant with faint stripes seen from orbit, its night side lit by starlight, shiny soap bubbles drifting in front of the planet, deep space, a black sky full of stars --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, blue sky, sun, sunlight --sw 250
```

Keep: the pale planet from orbit with bubbles in front.

Re-roll: a figure or a ship; a planet with bold colours or patterns; black bars, painted background.

**Vidu** · 8s, to reach the end of the song (covers up to 2:25.2)

```text
The bubbles drift slowly past as the camera pulls back from the planet.
```

Keep: the bubbles drift and the camera pulls back.

Re-roll: the planet melts; a cut to another shot, the style turning 3D.
