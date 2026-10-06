# 0005 prompts

Shot list and timing: [`README.md`](README.md#shot-list). Tool lessons: [`../DESIGN.md`](../DESIGN.md).

## Files

Characters, in [`characters/`](characters/) (copies of the 0002 plates). These go in Omni Reference:

- `hedgehog.png`: her, in every scene she's in
- `papa-panda.png`: #34 only
- `brother-fox.png`: #35 only
- `mama.png`: #36 only

Style sheets, in [`stills/`](stills/). These go in Style Reference:

- `style-character.png`: every scene with anything alive in it, however small. Her, the family, every robot and monster
- `style-landscape.png`: only the empty scenes, #1, #23, #32, #41

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
| Desert, day | #1–#16 | `late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight` |
| Ice planet | #17, #23–#27 | `evening on the ice planet, a deep violet twilight sky, cold blue light on the snow` |
| Swamp | #18 | `night on the swamp planet, a dark navy sky full of stars, the only light coming from the glowing plants` |
| Crystal canyon | #19–#22 | `midday on the crystal planet, a clear pale blue sky, bright white daylight` |
| Above the clouds | #28–#31 | `late afternoon high above the clouds, a warm golden sky, soft golden light` |
| Desert, night | #32, #37 | `night on the desert planet, a dark navy sky full of stars` |
| Desert, sunset | #33–#36 | `sunset on the desert planet, an orange and pink sky, long warm shadows` |
| Pink sea | #38–#40 | `morning on the ocean planet, a clear pale turquoise sky, bright morning light` |
| Orbit | #41 | `deep space, a black sky full of stars` |

#39 swaps in a cloud-bank version of their place's line, because the beam needs clouds to come out of.

Planets, moons and suns change shape and colour from roll to roll, so they're only in the prompts that need them: the pale planet in #1 and #41, two moons in #17, two suns in #33. One that turns up uninvited is fine unless it takes over the picture.

Reject on sight: day turning to night, or night to day, between cuts in the same place; a sunset or pink-cloud look in the daytime desert (#1–#16) or at the pink sea; ground of a clearly different colour.

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

**Split takes.** One clip can play twice, as two cuts with another cut between them: three cuts from two clips, and the halves match because they're the same clip. Cuts 3, 6, 7, 14, 19, 20, 23, 24, 28 and 29 are clips that play twice. The later cut only says which part to use. In iMovie, drop the clip in twice and trim one copy to its first action and the other to its second.

- The clip needs two clearly separate actions joined with `then`, so the second cut starts on something readable.
- The insert is a different subject, never her in the same situation: the other side of a fight (her against the walker, the drones, the giant), or the world reacting (#4's winged reptiles, #11's critters). An insert that needs her goggles, bike or set to match defeats the point of splitting.

Beams and bursts are never in the still; Vidu adds them from the motion line. Bubbles that are already floating (#13, #15, #40–#41) are painted in.

## Scenes

Numbered by cut, in edit order. A cut that reuses an earlier cut's clip only says which part to use.

### Intro

#### Cut 1 · Gas giant over the desert

0:00.0–0:04.0 · use 4.0s

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

0:04.0–0:12.0 · use 8.0s

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

0:12.0–0:15.8 · use the first 3.8s. The rest of this clip is cut 5.

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

0:19.3–0:22.8 · use the last 3.5s of cut 3's clip.

#### Cut 6 · Walker robot

0:22.8–0:25.9 · use the first 3.1s. The rest of this clip is cut 8.

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

0:25.9–0:28.4 · use the first 2.5s. The rest of this clip is cut 9.

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

0:28.4–0:30.0 · use the last 1.6s of cut 6's clip.

### Pre-chorus 1

#### Cut 9 · Point, then spin, second half

0:30.0–0:33.5 · use the last 3.5s of cut 7's clip.

#### Cut 10 · Laser strike

0:33.5–0:38.9 · use 5.4s. Two clips, `clips/09a.mp4` then `clips/09b.mp4`, both 8.0s. Trim so the laser leaves the barrel on the first "Out of my way!" at 0:35.4; the chorus starts there.

Made. The base's laser cannon, white with a red rim, charges until the lens glows solid red (`09a`), then fires from the station's structure (`09b`). The walker isn't in the shot, so nothing has to match cuts 6 and 8.

A satellite seen from orbit never came out: Midjourney drew it skimming low over the ground every time. A cannon close-up with the planet behind it works.

### Chorus 1

#### Cut 11 · Critters pop up

0:38.9–0:40.9 · use 2.0s

Made, `clips/11.mp4` (2.1s). On "I'm the little boss today": after the blast, big-eared desert critters pop their heads out of round burrows and sit up, looking out. They don't bow. The boss isn't in the shot.

#### Cut 12 · Bubbles from the blast

0:40.9–0:42.4 · use 1.5s

Made, `clips/12.mp4` (8.0s). On "Pop, pop, pop, they float away": the blast on the dunes throws up a cloud of orange dust and hundreds of soap bubbles drift out of it into the sky. No robot in frame.

#### Cut 13 · Bubble hopping

0:42.4–0:47.0 · use 4.6s

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

#### Cut 14 · Drone swarm

0:47.0–0:49.6 · use the first 2.6s. The rest of this clip is cut 16.

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

Keep: the swarm rushes in (cut 14), then pops into bubbles (cut 16). Her spin in #15 sits between, so the pop reads as her doing.

Re-roll: the drones merge into a blob; a cut to another shot, the style turning 3D.

#### Cut 15 · Mid-air spin

0:49.6–0:52.8 · use 3.2s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium wide shot, the hedgehog girl with bare clawed feet in mid-leap spinning sideways in the air, a red lightsaber held out at arm's length, her red cape whirling around her, shiny soap bubbles all around her, nothing behind her but open sky, late morning on the desert planet, a clear sky deep teal blue at the top fading to pale cream at the horizon, a few small white clouds, bright neutral daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 200 --ow 330
```

Keep: her airborne and spinning, lightsaber out, bubbles around her, sky behind.

Re-roll: standing on the ground; robots in frame; shoes; black bars, painted background.

`stills/15.png` shows the ground and she isn't spinning. The clip is the one that counts: she's in the air, seen from behind, lightsaber out, bubbles around her.

**Vidu** · 5s

```text
She spins in the air slashing the red lightsaber and the bubbles around her burst.
```

Keep: she spins and slashes.

Re-roll: the blade doubles; a cut to another shot, the style turning 3D.

#### Cut 16 · Drone swarm, second half

0:52.8–0:56.3 · use the last 3.5s of cut 14's clip.

### Verse 2

#### Cut 17 · Space dragon

0:56.3–0:59.9 · use 3.6s

**Midjourney** · Style Reference `style-character.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle wide shot, a long-necked space dragon with pale blue crystal scales, a round goofy face and glowing cyan eyes roaring on top of a snowy ice hill, wings spread, blue ice rocks outlined in black ink, two small pale moons in the sky, evening on the ice planet, a deep violet twilight sky, cold blue light on the snow --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure --sw 200
```

Keep: one crystal-blue dragon roaring on an ice hill, violet sky.

Re-roll: extra heads; too scary for a five-year-old (gore, dripping fangs); a daytime blue sky; black bars, painted background.

**Vidu** · 5s

```text
The dragon throws back its head and roars, frost puffing from its mouth.
```

Keep: the head goes back and frost comes out.

Re-roll: a second head appears or the jaw melts; a cut to another shot, the style turning 3D.

#### Cut 18 · Blob alien

0:59.9–1:03.2 · use 3.3s

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

#### Cut 19 · Stone giant

1:03.2–1:06.4 · use the first 3.2s. The rest of this clip is cut 21.

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

Keep: the scowl (cut 19), then it turns and runs (cut 21). Her stamp in #20 sits between: "I stamp my foot, he runs away".

Re-roll: the boulders fall apart; it runs toward the camera; a cut to another shot, the style turning 3D.

#### Cut 20 · Stamp, then throw

1:06.4–1:08.5 · use the first 2.1s. The rest of this clip is cut 22.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, low angle, the hedgehog girl with bare clawed feet standing on smooth purple crystal ground, one foot raised to stamp, a red lightsaber in one paw drawn back behind her shoulder ready to throw, giant purple crystals far off at the sides, midday on the crystal planet, a clear pale blue sky, bright white daylight --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 330
```

Keep: her whole body on crystal ground, one foot up, lightsaber drawn back.

Re-roll: a giant or other creature in frame; shoes; two lightsabers; black bars, painted background.

**Vidu** · 8s

```text
She stamps her foot down and cracks shoot across the crystal ground, then she hurls the spinning red lightsaber like a boomerang out of the frame.
```

Keep: the stamp and the cracks (cut 20), then the throw (cut 22).

Re-roll: she slides forward; the lightsaber doubles or bends; a cut to another shot, the style turning 3D.

#### Cut 21 · Stone giant, second half

1:08.5–1:10.6 · use the last 2.1s of cut 19's clip.

### Pre-chorus 2

#### Cut 22 · Stamp, then throw, second half

1:10.6–1:14.0 · use the last 3.4s of cut 20's clip.

#### Cut 23 · The lightsaber flies back

1:14.0–1:19.4 · use the first 5.4s. Trim so the lightsaber comes into frame on "Out of my way!" at 1:15.8; the chorus starts there. The rest of this clip is cut 25.

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot, an empty field of snow and tall blue ice spikes stretching to the horizon, every ice edge outlined in black ink, evening on the ice planet, a deep violet twilight sky, cold blue light on the snow --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure --sw 200
```

Keep: an empty ice field with tall ice spikes, twilight sky.

Re-roll: a creature or figure; a daytime blue sky; black bars, painted background.

**Vidu** · 8s

```text
A spinning red lightsaber whirls in low across the ice field like a glowing disc, slicing through the ice spikes one after another so they shatter and snow bursts up, then thousands of shiny bubbles float up out of the snow.
```

Keep: the spinning lightsaber shatters the spikes (cut 23), then rising bubbles (cut 25).

Re-roll: a hand or a figure holds the lightsaber; it flies straight like a spear; the ice melts into mush; a cut to another shot, the style turning 3D.

The lightsaber she threw in cut 22, on its way back to her paw in cut 24. The dragon, the jelly and the giant are beaten by her, not from orbit.

### Chorus 2

#### Cut 24 · Catch, then twirl

1:19.4–1:21.1 · use the first 1.7s. The rest of this clip is cut 26.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle medium shot, the hedgehog girl with one open paw raised high, a red lightsaber spinning in the air just above her paw, nothing behind her but the sky, evening on the ice planet, a deep violet twilight sky, cold blue light on the snow --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 250 --ow 330
```

Keep: her open paw up, the lightsaber spinning just above it, violet sky.

Re-roll: the lightsaber already in her paw; two lightsabers; ground or hills behind; black bars, painted background.

**Vidu** · 8s

```text
The spinning red lightsaber drops into her raised paw and she catches it, then she grins and twirls it in fast circles over her head.
```

Keep: the catch (cut 24), then the twirl (cut 26).

Re-roll: it passes through her paw; a second one appears; a cut to another shot, the style turning 3D.

#### Cut 25 · The lightsaber flies back, second half

1:21.1–1:22.8 · use the last 1.7s of cut 23's clip.

#### Cut 26 · Catch, then twirl, second half

1:22.8–1:26.1 · use the last 3.3s of cut 24's clip.

#### Cut 27 · Leap off the snow

1:26.1–1:29.4 · use 3.3s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, full shot, low angle, the hedgehog girl with bare clawed feet crouched low on flat snow about to jump, knees bent, a red lightsaber in one paw, looking straight up, plenty of empty sky above her, evening on the ice planet, a deep violet twilight sky, cold blue light on the snow --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 200 --ow 330
```

Keep: her crouched on snow, looking up, open sky above.

Re-roll: already in the air; standing straight; shoes; black bars, painted background.

**Vidu** · 5s

```text
She springs straight up and shoots out of the top of the frame.
```

Keep: she jumps up and leaves the frame.

Re-roll: she jumps and floats back down in the same spot; a cut to another shot, the style turning 3D.

### Bridge

#### Cut 28 · The fleet

1:29.4–1:31.2 · use the first 1.8s. The rest of this clip is cut 30.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot above a sea of white clouds, a fleet of dozens of sleek white and red starships flying in rows into the distance, the nearest flagship huge in the foreground with panel lines and rivets outlined in black ink, the hedgehog girl standing tiny on the nose of the flagship with a red lightsaber held down at her side, late afternoon high above the clouds, a warm golden sky, soft golden light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, cockpit, interior --sw 200 --ow 330
```

Keep: rows of ships over the clouds, her small but readable on the flagship's nose.

Re-roll: inside a ship; she's missing or as big as the ship; a ship that copies a famous film design; black bars, painted background.

**Vidu** · 8s

```text
The whole fleet surges forward into the distance as the clouds stream fast underneath and the camera flies alongside the flagship, then she raises the red lightsaber high over her head on the nose of the flagship, her cape flapping.
```

Keep: the fleet moves (cut 28), then she raises the lightsaber (cut 30).

Re-roll: ships merge or warp; she falls off; a cut to another shot, the style turning 3D.

#### Cut 29 · Fist pumps

1:31.2–1:32.9 · use the first 1.7s. The rest of this clip is cut 31.

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium close-up, low angle, the hedgehog girl shouting with her mouth wide open and one fist punched up, nothing behind her but golden clouds and sky, late afternoon high above the clouds, a warm golden sky, soft golden light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature --sw 250 --ow 330
```

Keep: her from below, fist up, shouting, golden sky behind.

Re-roll: a ship or hull in frame; a human child; black bars, painted background.

**Vidu** · 8s

```text
She punches her fist up once and shouts, then she punches it up three more times, shouting each time.
```

Keep: one punch (cut 29, "Me!"), then three (cut 31, "Me! Me! Me!").

Re-roll: her face melts; a cut to another shot, the style turning 3D.

#### Cut 30 · The fleet, second half

1:32.9–1:36.4 · use the last 3.5s of cut 28's clip.

#### Cut 31 · Fist pumps, second half

1:36.4–1:40.0 · use the last 3.6s of cut 29's clip.

#### Cut 32 · Beam fireworks

1:40.0–1:43.6 · use 3.6s

**Midjourney** · Style Reference `style-landscape.png` · no Omni Reference

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle wide shot from the ground, dark desert dunes, red rock spires as black silhouettes against the stars, night on the desert planet, a dark navy sky full of stars --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, person, figure, blue sky, sun, sunlight --sw 250
```

Keep: a starry night sky over dark dunes and spires.

Re-roll: a figure; a daytime sky; ships in the sky; black bars, painted background.

**Vidu** · 5s

```text
Dozens of red beams fan across the night sky like fireworks, the fleet celebrating.
```

Keep: beams streak across the sky.

Re-roll: no beams; the spires melt; a cut to another shot, the style turning 3D.

### Verse 3

#### Cut 33 · Two suns setting

1:43.6–1:47.3 · use 3.7s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, wide shot from behind, the hedgehog girl sitting alone on the crest of a sand dune, small in the frame, her red cape spread on the sand around her, a red lightsaber hilt lying beside her, watching two suns set on the horizon, sunset on the desert planet, an orange and pink sky, long warm shadows --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, front view, facing camera --sw 200 --ow 330
```

Keep: her small from behind, sitting on a dune, two suns low.

Re-roll: she faces the camera; a house or a vehicle; shoes; black bars, painted background.

**Vidu** · 5s

```text
The two suns sink slowly toward the horizon as the wind lifts the edge of her cape.
```

Keep: the suns sink and the cape lifts.

Re-roll: she stands up or turns around; a cut to another shot, the style turning 3D.

#### Cut 34 · Papa

1:47.3–1:50.8 · use 3.5s

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

#### Cut 35 · Brother

1:50.8–1:54.2 · use 3.4s

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

#### Cut 36 · Mama

1:54.2–1:57.6 · use 3.4s

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

#### Cut 37 · Hammock

1:57.6–2:01.2 · use 3.6s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, muted dark colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, medium shot, the hedgehog girl lying in a small hammock under her red cape like a blanket, wide awake, eyes open, gazing up at the stars, nothing behind the hammock but the starry sky, night on the desert planet, a dark navy sky full of stars --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, blue sky, sun, sunlight --sw 250 --ow 330
```

Keep: her lying in a hammock under the cape, eyes open, stars behind.

Re-roll: eyes closed; a house or a bed; black bars, painted background.

**Vidu** · 5s

```text
She sits bolt upright in the swaying hammock and throws off the cape.
```

Keep: the sudden sit-up on the "Hey! Hey!".

Re-roll: she falls out of the hammock; her eyes close; a cut to another shot, the style turning 3D.

Eyes open in the still. Asleep-then-waking changes her face and breaks the plate, as the goggles did.

### Final chorus

#### Cut 38 · Rise and light up

2:01.2–2:04.6 · use 3.4s

**Midjourney** · Style Reference `style-character.png` · Omni Reference `hedgehog.png`

```text
modern anime illustration, anime opening key visual, clean digital line art, thin precise black outlines, flat cel shading with soft two tone shadows, natural full colour, vivid saturated colours, inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and grime, neutral grey shadows, crisp high resolution, low angle medium shot, the hedgehog girl rising up into the frame holding an unlit lightsaber hilt with no blade in one paw, her red cape flaring, nothing behind her but the sky, morning on the ocean planet, a clear pale turquoise sky, bright morning light --no chibi, crosshatching, painted background, letterbox, black bars, sepia, painterly, 3d render, photorealistic, text, watermark, signature, sunset --sw 250 --ow 330
```

Keep: her from below with an unlit hilt, turquoise sky behind.

Re-roll: a blade already lit; beach or sea in frame; black bars, painted background.

**Vidu** · 5s

```text
She rises from the bottom of the frame up into the middle as the camera holds still, and a glowing red lightsaber shoots out of the hilt and hums.
```

Keep: she rises and the blade comes out.

Re-roll: the blade comes out bent or doubled; a cut to another shot, the style turning 3D.

#### Cut 39 · Robot squid

2:04.6–2:11.5 · use 6.9s

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

The satellite base's second and last shot, from the clouds. The first was cut 10.

### Outro

#### Cut 40 · Wave goodbye

2:11.5–2:17.2 · use 5.7s

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

#### Cut 41 · Planet at night

2:17.2–end of song · use 4.6s or more, to the end of the song

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
