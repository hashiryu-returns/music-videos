# Lessons

What the three videos taught about each tool. Everything here was hit in production; nothing is from a tutorial.

## Pick the tool by how many references a shot needs

This is the one decision that shaped all three videos.

| References in one frame | Tool | Why |
| --- | --- | --- |
| One character, or none | Midjourney V7 still → Vidu Q2 image-to-video | Midjourney holds one reference well, and Vidu animates a correct still faithfully |
| Two characters, or a character inside a fixed room | Seedance (2.0 on OiiOii for JP, 2.5 for the FR finale) | Takes several reference images at once and keeps them apart |
| Nothing, by design | OiiOii full-auto | Song in, finished MV out. EN was this |

JP and FR both started as Midjourney → Vidu and both hit the same wall: the husband inside his own room, the husband with his daughter, the wife in her kitchen. FR got around it by writing the story as a journey, so the same characters keep coming back but never share a frame or a location. JP couldn't do that because the whole song is set in one room, so it moved to Seedance.

## Midjourney

**Character lock**

- **Niji 7 has no character reference.** `--cref` is unsupported on it and `--oref` isn't available either. A prompt plus `--sref` locks the style, not the person. The FR plate `her-full.png` was a Niji 7 outlier roll, and rerunning the same string returned someone else.
- **V7 with Omni Reference (`--oref`, `--ow`) is the character lock.** 350 is the working weight for plates. Scene stills ran at 330. Go above 380 and results get unpredictable.
- **`--oref` is silently ignored in Fast, Draft and Conversational modes.** No error. You get a grid of a stranger at 2× GPU cost. Use Relax.
- **No Zoom Out, Pan or Vary Region on an `--oref` result.** Framing has to come from the prompt.
- **Pair `--oref` with `--sref`.** Omni Reference holds the character and the style reference holds the ink. V7 alone came out softer than the Niji plate.
- **Don't describe what the reference already supplies.** With `--oref` attached, writing her face, hair or clothes competes with the plate. Even writing face detail on a back-view plate turned her around.
- **Below about 330, the wardrobe goes.** Lowering the weight frees the pose but costs the clothes, and not linearly. At 200 a sprint came back in invented trousers. At 280 the clothes held. Below 330, write the wardrobe into the prompt.
- **The plate leaks onto every human shape in the frame.** Her plate at 330 next to four villagers gave four copies of her. Count the human shapes before setting the weight: one shape gets 330, two get 250–280, three or more get an empty slot.

**Framing**

- **A reference reproduces its own crop.** A head-and-shoulders plate pulls every still to head-and-shoulders. A full-body plate keeps the subject at full frame height no matter what the text says. Match the plate's framing to the shot: FR has separate full, back and face plates for this reason.
- **Geometry beats framing words.** `medium wide` and `a third of frame height` lose to the plate. `the entire two-storey house in frame from the cobbles to the roofline` wins, because the building has to fit.
- **Midjourney frames to fit every object you name.** Five nouns make a wide shot whatever else the prompt says. To get a tight shot, name one subject and let everything else go out of focus.
- **Two style references average into neither.** In 0006 a face sheet and a landscape sheet together gave a flat, generic Niji face; the face sheet alone gave its lashes, lips and gaze back. Use one sheet per shot, chosen by what the shot is. Anything alive in the shot uses the character sheet, however small, even a hand, a silhouette or a monster. Only a scene with nobody in it uses the landscape sheet: people and monsters rolled on it came out in Niji's default flat style, because the sheet had no character to copy.
- **A style reference imports its camera along with its ink.** A close-cropped `--sref` crops close. Lowering `--sw` to fix that drains the ink too. Face words make it worse: on the 0006 face sheet, every scene with `realistic anime face, sharp eyes` came back as a face close-up whatever the shot size said. Wide scenes drop the face words and name what has to fit (whole body, the whole harp, columns three times her height), at `--sw 200`.
- **A face looking up is a face seen from below.** `low angle, looking up at the sky` gave the 0006 soldier a jaw-and-nostrils view in every roll, and `eyes raised` still tilted the head back. `eye level, looking just past the camera` gave the face back. Let Vidu do the looking up.
- **`dynamic shot` plus a thrust fist puts the fist in the lens.** 0006 #31 came back as a face and fist filling the frame, the dragon pasted small behind him, on blank white. The shot had no place and no size relation, and the face words pulled sheet A in close. The rework drops the face words and gives side view, extreme wide, a named location, and the dragon's head "many times larger than a man" on the other side of the frame.
- **A small, tucked, shaved-head figure in an orange gi reads as a monkey.** The 0006 #31 martial artist came back as one in every roll, probably because the set (orange gi, leap, dragon, clouds) sits next to the Monkey King. The rework changes the costume and hair, makes the figure an adult a third of the frame tall, and gives a straight-leg flying kick that reads as a human body.
- **Check the camera can stand where the prompt puts it.** 0006 #36 asked for the camera outside the gate looking down the road and the gate's arch in the foreground. Both can't be true, and every roll broke. Put the camera on one side of the thing and say which way it faces.
- **A distant landscape has no surface for the ink.** An aerial valley came back as flat clip-art green whatever the sheet. Huge cracked stone blocks in the foreground, with the valley behind, carried sheet B's ink.

**What it can't do**

- **It can't stage two people from two references.** Two character references produce two portraits composited together. It can't do a body in contact with another body (a lap, a carry, a hug) either. Cut the contact, or give each character a separate frame.
- **It won't give one member of a group a property the others lack.** It applies an attribute to the whole set or drops it. Make the odd one out a different kind of thing at a different scale.
- **It won't distribute figures into architecture.** `six villagers in the doorways` comes back as six people in the middle of the road.

**Writing the prompt**

- **Midjourney reads nouns, not negations.** `no face` puts a face in the picture. An absence phrase like `nobody in the street` deletes every figure. Say where things are, never where they aren't.
- **A shared style block must name no subject.** Every noun in it gets drawn. `detailed eyes, defined lips` in the 0006 block put giant eyes and faces into the rock of every landscape, and `hatching on rock, walls` turned every scene into white cliffs. Subject detail goes into the shots that have that subject.
- **Colour words in the shared block beat the scene's light.** `vivid saturated colours` in the 0006 block plus a bright sheet B turned `dim grey light` under storm clouds into sunlit lime fields. Dark scenes swap the phrase for `muted dark colours` and add `blue sky, sun, sunlight` to `--no`. Don't name the sun at all: `the sun a faint pale disc` drew a blazing one.
- **Keep `--no` short.** About eighty exclusions flattened the image and wiped out variety. A long `--no` also suppresses the whole category, not just one instance.
- **Niji paints backgrounds unless told to ink them.** The 0006 sheets came back with inked figures on soft, outline-free painted rock. Naming the technique in the block (`inked backgrounds with black outlines on every edge, fine ink detail of cracks, chips and speckled grime`) together with `painted background` in `--no` gave inked backgrounds. `pen hatching` in `--no` had been banning the ink texture the targets have; ban `crosshatching` instead. Walls and stacked blocks hold the ink better than a cliff face, which Niji draws as painted background art.
- **Wide 16:9 rolls letterbox.** Most Niji 7 wide shots of the 0006 B sheet came back with black bars top and bottom. `letterbox, black bars` in `--no` cleared them. A sheet with bars passes them on through `--sref`.
- **The moderator reads `--no` word by word.** `head only` and `paws out of frame` on a dog read as dismemberment and got the prompt blocked. The dog plates carry no `--no` at all.
- **Never put a body part in `--no`.** `--no shaved head` killed the undercut. Ban the wrong silhouette instead.
- **A verb is not a pose.** `running` comes back standing. Name which foot is off the ground. On short-legged animals, though, a lifted paw buys a longer leg. Ask for the silhouette and let Vidu add the motion.
- **Name the shot, not the arrangement.** Composition prose drifts toward the nearest famous picture. Shot vocabulary like `medium wide, four figures, facing camera, eye level` doesn't.
- **Describe a garment's construction when the composition fights it.** A lineup of four adults pulled Western clothes over `pyjamas`. `one-piece cotton sleepsuit, elasticated cuffs` held.
- **Props stay out of plates.** JP's cigarette on the plate survived `--no cigarette` in every scene. A sword on her plate plus a sword in her hand gives two swords. Write props into each shot.
- **A real photo of a person is never an image prompt, and this repo does not keep one.** At `--iw 1` a photo came back as a shaved head in a photoreal style. Object photos are fine. A photo of a person is not.
- **Image prompts transfer palette and elements, not layout.** `--iw 2` is the ceiling on Niji 7. A plain-background reference brings its plain background with it.
- **Stop rolling at about ten.** Past that the shot is wrong, not the wording. Every fix that worked changed what was in the frame, not the sentence.

## Vidu

- **Image to Video, not Reference to Video.** References to Video redraws the frame from the plates.
- **One positive motion per clip, in English.** Vidu drops negations and keeps the noun. `camera fixed` produced a push-in, and `the sword stays on the stand` launched it off the stand.
- **It moves painted mass, not light.** Mist, cloth, hair, steam and smoke work. Dust in a beam, a shadow crossing a shoji or a highlight running along a blade all failed, three times out of three.
- **A still with nothing soft in it turns into an invented camera move.** Use Ken Burns in the editor for camera-only shots (FR #1).
- **Leave FX out of the still.** Paint the demon whole and the cathedral intact. Vidu does the burst, the orb and the explosion from the prompt.
- **Multi-image is for state changes on the same camera.** A→B for a robe tearing into a demon, or a carriage arriving. Two views of one room are two clips and a hard cut. Never morph across two identities.
- **A still can hide an anatomy error that motion exposes.** A Pekingese that looked right standing walked like a terrier. Check proportions before animating, and hide the hard part (a coat down to the ground).
- **Let it improvise where nothing specific has to land.** Asked to move a sash, it moved the sash, the arm and the blade, and the take was better for it.
- **Feet on the ground slide.** Walking and running on 0006's stairs drifted within a second, and Midjourney couldn't draw the stairs either. A jump starts with both feet in the air and ends in a landing, so there's no stride for Vidu to slide. Give a moving figure a leap, a landing or a stand-still action.
- **A hand raised near the face lands in the hair.** 0006 #3's `shields her eyes with one gauntleted hand` came back touching her hair. Give the action to the head and eyes, and add `Her hands stay down`.
- **Settings:** Q2, 1080p, Cinematic, one take at a time. Up to 5s is one price and 6–8s costs double, so generate 5s for anything that uses 5.0s or less, and never pay for 6s to use 5.2s. Move the cut instead.
- **Q2 over Q3.** Q3 allows longer clips but came out worse in testing. Use it only as a second try on a shot Q2 keeps getting wrong.

## Seedance and OiiOii

- **OiiOii always appends a ~2s platform credit to a merge,** on every plan. Support confirmed there's no setting for it. Trim it in the editor.
- **One shot, one camera, one subject.** A wide that names a desk, a sofa and stairs turns into a split-screen collage. Keep one establishing wide and frame everything else tight.
- **Never show game UI.** Mahjong on a monitor comes back as an FPS or abstract junk. Light the face with the screen instead.
- **The storyboard card text must match the video prompt.** If you only update the generation box, the old card text still drives the shot.
- **Don't write `0–4s / 4–7s` segments on a still scene.** Empty holds get filled with extra angles. On a scene that really moves, timed segments work: FR #35 used three.
- **What worked on the FR finale (Seedance 2.5):**
  - Assign each reference image one role, for example `@image4` as the room, `@image2` and `@image1` as her front and back, `@image3` as the panda.
  - State size relations explicitly.
  - Pin the style to the references and say which style not to drift into ("retro comic, not anime").
  - Close with a stability paragraph: faces, outfits and prop positions consistent, no extra particles, no marks on the floor.
- **Correct the reference in the prompt if it's off.** Daru's plate reads lighter than he was, so the FR prompts open with "the Pekingese is sable with a full black mask".
- **Resolutions differ by tool.** Vidu returns 1924×1078 or 1926×1076, OiiOii/Seedance 1280×720, and some Seedance takes 854×480. All of it sits in a 1920×1080 timeline.

## Suno

- **Custom Mode only.** Simple Mode chooses the lyrics and genre for you.
- **Exclude is the real negative control.** "No strings" in Style gets ignored. Each song carries its own decade guard in Exclude (`city pop, 80s retro` on JP, `60s retro, 80s retro, yé-yé` on FR), because Suno reaches for period sounds as soon as a genre tag allows it.
- **Bare section tags.** `[Bridge: stripped down]` gets sung aloud or swallows the section break. Arrangement directions go in Style.
- **Duration: Auto.** A custom 4:30 padded a ~3:00 song with garbage.
- **Name the language in Style as well as in the lyrics.** J-pop tags drift toward English vocals otherwise. A J-rock tag on a French song needs `Japanese lyrics` in Exclude.
- **Respell in the Lyrics field only.** Only the audio ships, so `とんいっきょく` can go to Suno while the subtitles keep `東一局`.
- **Keep line lengths even.** Wildly uneven lines are where Suno crams or drops words. Hard stops (`Fenêtre ouverte. Ils s'engueulent.`) give a dense line room.
- **Pronunciation fixes, in order:** regenerate, respell, move the word onto a stressed beat, inpaint. Then, and only then, try another tool.
- **WAV only, no stems.** The picture is cut to the full mix. Pro gives 20 downloads per cycle, and re-downloading a song is free.

## Edit and subtitles

- **The WAV is the clock.** Cut to the audio and trim clips. Never change a clip's speed.
- **Caption tracks sit in the song folder** as `captions/<lang>.vtt`: the sung lyric plus its translations.
- **Translate lyrics as lyrics.** A subtitle should read as a natural song in the target language, even where that means dropping the original's wording. `veut mon dos` translated literally is "wants my back", and it reads as broken.
