# FR — « Je m'arrête pas »

Her side of the year, as an isekai-style adventure: a medieval French world of swords and magic that doesn't keep to its own rules. She carries a katana, and modern buildings, cars and some comedy break in. Under the action are her everyday struggles and the grief of losing Daru. It ends on October 4th, when the evening is finally hers.

- **YouTube:** [watch](https://www.youtube.com/watch?v=472scJ16qbg), unlisted
- **File:** `exports/final/[21st Anniv][FR] Je m'arrête pas [Suno][Midjourney][Vidu][Seedance].mp4`, 2:07, 1920×1080
- **Captions:** `captions/fr.vtt` (lyrics), `en.vtt`, `ja.vtt`
- **Song:** `audio/song.wav`
- **Prompts:** plates and per-scene stills in [`prompts.md`](prompts.md)

## YouTube

Title, unchanged:

```text
[21st Anniv][FR] Je m'arrête pas [Suno][Midjourney][Vidu][Seedance]
```

Description:

```text
Concept
The wife's side of the same year, as an isekai-style adventure: a medieval French world of swords and magic that doesn't play by its own rules. She carries a katana, and modern buildings, cars and a bit of comedy break in. Underneath the action are her everyday struggles, and the grief of losing a dog she still hasn't gotten over. It ends on October 4th, when the evening is finally hers.

🛠️ Production Tools & AI Models
・Lyrics & Concept: Claude Opus 5
・Music: Suno v6 Pro
・Images: Midjourney V7 (Omni Reference; character sheets started on Niji 7)
・Video: Vidu Q2, Vidu Q3 (s14), Seedance 2.5 (s27, s31, s32, s35)
・Editing: iMovie 10.4.3

📝 Behind the Scenes
The French video started the same way as the Japanese one and hit the same wall. The first storyboard kept her in the kitchen all day, which meant referencing her and the kitchen in every shot. That's exactly what Midjourney can't do.

So I threw it out. I rewrote the lyrics and regenerated the song in Suno as fast electro J-rock: the first version was nu-disco for her love of Daft Punk, this one is for her love of anime openings. Then I rebuilt the story as a journey. The same characters keep coming back, but never in the same place twice, which kept almost every shot down to one referenced character. Midjourney V7 and Vidu can carry that: 31 of the 36 scenes are a Midjourney still animated in Vidu.

Near the end I left the storyboard behind. The four scenes that needed more than one character or a fixed room went to Seedance 2.5 with several reference images each. Every cut is timed by hand in iMovie.
```

## Song

Suno v6, Custom Mode, Vocal Gender Female, Duration Auto, Weirdness 23, Style Influence 75.

Style:

```text
fast driving electro J-rock, French female vocal, 170 BPM, gritty droning synth bass, math-rock electric guitar riffs, bright electronic keys, punchy programmed drums, clipped staccato deadpan verses exploding into a powerful belted chorus, instrumental breakdown before the final chorus, aggressive defiant swagger, polished current production
```

Exclude:

```text
chanson, ballad, melancholic, wistful, downtempo, sparse, ambient, chillout, slap bass, funk, disco, nu-disco, bossa nova, yé-yé, 60s retro, 80s retro, accordion, organ, saxophone, acoustic piano, nylon guitar, seductive breathy vocal, romantic ballad, orchestral strings, gospel choir, sentimental, Japanese lyrics
```

Lyrics:

```text
[Intro]

[Verse 1]
Six heures. Le petit crie. Le chien pleure dans la cuisine.
Le thé refroidit sur le comptoir, j'y touche pas.
Ma fille veut tout décider, le petit veut mon dos.
Et personne me demande si j'ai dormi.

[Pre-Chorus]
Ça s'arrête pas
Ça s'arrête jamais
Les fourmis reviennent par le même trou
Et moi je remonte l'escalier

[Chorus]
Je m'arrête pas
Essaie de m'arrêter
Je suis pas fatiguée
Je suis en train de gagner

[Verse 2]
Je sors le chien. Midi. Les voisins en pyjama.
Le fils à papa, troisième bagnole de l'année.
La maison du coin est vide. Personne y reste.
Fenêtre ouverte. Ils s'engueulent. Je ralentis exprès.

[Pre-Chorus]
« Vous croyez en Dieu ? »
Encore eux. Sur mon perron.
Ton Dieu m'a jamais gardé les gosses
J'en ai rien à foutre de ton Dieu

[Chorus]
Je m'arrête pas
Essaie de m'arrêter
Je suis pas fatiguée
Je suis en train de gagner

[Bridge]
Le jour, il reste dans sa niche vide
Un petit lion rouge, la tête qui sourit
Le soir je le monte, je le pose près de moi
L'un me réveille, l'autre me manque

[Chorus]
Je m'arrête pas
Sauf ce soir — le 4 octobre
Vingt et un ans — c'est gagné
Toute la soirée est à moi

[Outro]
```

- `ça s'arrête jamais` is the complaint and `je m'arrête pas` is the boast: the same words turned around. The last chorus allows one exception, the anniversary.
- No `ne` anywhere. That's how she talks, and at 170 BPM the saved syllable matters.
- `veut mon dos` means she wants to be carried on my back (おんぶ). Check it with a native speaker, not a translator.
- `un petit lion rouge` is the red shisa pouch: Okinawan guardian-lion goods she buys because their flat faces look like Daru.
- An earlier take, « Debout dans la cuisine » (nu-disco, for Daft Punk), is at `audio/debout-dans-la-cuisine.wav`. It wasn't used.

## Cast

She is the only human. Everyone else is an animal, and each plate is that character's `--oref`.

| Plate | Who | Look |
| --- | --- | --- |
| `her-full.png` | her | Curly updo, black kimono, red inner collar, red obi with a hanging gold wrap, ankle-length skirt, black tabi boots. No sword on the plate |
| `her-back.jpeg` | her, from behind | Same wardrobe. The gold wrap hangs on her right |
| `her-face.jpeg` | her, close-up | For #10 |
| `panda.png` | husband | Biped panda, dark haori, sand kimono, red sash. Sheepish, empty hands |
| `hedgehog.png` | daughter | Small, cream face and belly, red cape |
| `fox.png` | son | Orange kit, white chest, red jacket, blue wrap, mouth open |
| `aramis.png` | Aramis, alive | Black Pekingese, pale muzzle, no collar |
| `daru.png` | Daru | Cream-gold sable, full black face mask, no collar, no halo |

All plates are in `characters/`. The style reference is `characters/style-sheet.png`. The pouch photo is `objects/shisa-pouch.png`. Props are written into each shot, never into a plate: the katana, the red pouch.

**Every Midjourney still has at most one plated character.** That rule is what made Midjourney → Vidu work. Characters only meet in the Seedance scenes.

## Shipped cut

36 scenes. Stills are in `stills/` and clips in `clips/` (not committed), with matching numbers.

| # | Section | Scene | Video |
| --- | --- | --- | --- |
| 1 | Intro | Sheathed sword on its stand, dawn | Ken Burns in iMovie |
| 2 | Intro | The hill village below, mist | Vidu Q2 |
| 3 | Intro | Her back, washitsu | Vidu Q2 |
| 4 | Intro | The drawn blade | Vidu Q2 |
| 5 | Verse 1 | Fox kit wailing in the doorway | Vidu Q2 |
| 6 | Verse 1 | Aramis cries in the kitchen | Vidu Q2 |
| 7 | Verse 1 | Tea going cold, steam | Vidu Q2 |
| 8 | Verse 1 | Hedgehog gives orders | Vidu Q2 |
| 9 | Verse 1 | Fox flat on the floor, missed her back | Vidu Q2 |
| 10 | Verse 1 | Her face, one blink | Vidu Q2 |
| 11 | Pre-chorus 1 | A man-sized ant smashes through the kitchen wall | Vidu Q2 |
| 12 | Pre-chorus 1 | Hedgehog runs | Vidu Q2 |
| 13 | Pre-chorus 1 | Fox runs, ants behind him | Vidu Q2 |
| 14 | Pre-chorus 1 | Up the stairs with the katana | Vidu Q3 |
| 15 | Chorus 1 | Ridge run into a winged demon (15a → 15b) | Vidu Q2, multi-image |
| 16 | Chorus 1 | Aramis casts | Vidu Q2 |
| 17 | Chorus 1 | The orb lands, the demon bursts to ash (still 15b) | Vidu Q2 |
| 18 | Chorus 1 | Daru on the ridge | Vidu Q2 |
| 19 | Chorus 1 | She walks into a hero stop (19a → 19b) | Vidu Q2, multi-image |
| 20 | Chorus 1 | The whole village below | Vidu Q2 |
| 21 | Verse 2 | Aramis leads down the alley | Vidu Q2 |
| 22 | Verse 2 | Neighbours in pyjamas, turning | Vidu Q2 |
| 23 | Verse 2 | The third gilded carriage (23a → 23b) | Vidu Q2, multi-image |
| 24 | Verse 2 | The empty corner house | Vidu Q2 |
| 25 | Verse 2 | She slows, looking up | Vidu Q2 |
| 26 | Pre-chorus 2 | Hooded sorcerer at the Notre-Dame altar | Vidu Q2 |
| 27 | Pre-chorus 2 | Notre-Dame west front, Daru | Seedance 2.5 |
| 28 | Chorus 2 | The robe tears into a flying demon (28a → 28b) | Vidu Q2, multi-image |
| 29 | Chorus 2 | Daru casts | Vidu Q2 |
| 30 | Chorus 2 | The cathedral explodes | Vidu Q2 |
| 31 | Bridge | Sunset in the ruins: Daru dissolves into the pouch | Seedance 2.5 |
| 32 | Bridge | Night in the ruins: Aramis curls up beside her and the pouch | Seedance 2.5 |
| 33 | Final chorus | She walks toward Tour Montparnasse | Vidu Q2 |
| 34 | Final chorus | The panda gaming in the penthouse | Vidu Q2 |
| 35 | Final chorus | She drags the panda across the penthouse | Seedance 2.5 |
| 36 | Outro | Aramis | Vidu Q2 |

Stills 27, 31, 32 and 35 are the background references for the Seedance scenes. The Vidu settings and motion lines are in [`prompts.md`](prompts.md).

## Seedance 2.5 prompts

The sound section is dropped because the MV uses only the song.

**s27**

```text
Cinematic 8k, emotional animation style. A Sable Pekingese dog with a full black mask, fluffy coat, clearly recognizable as a dog, walks toward the entrance of the Notre-Dame Cathedral with the characteristic Pekingese rolling, dignified gait — short legs, chest forward, slight side-to-side sway. The background is the provided image of the ruined Notre-Dame Cathedral with no dog in it; keep the Cathedral style, color, design, surrounding ruins and sky exactly as-is. The camera angle changes dynamically during the shot, moving smoothly around and slightly following the dog as it approaches the Cathedral entrance. Golden hour warm light, melancholic atmosphere, high quality.
```

**s31**

```text
Correction: the Pekingese dog color is Sable with a full black mask. The background does not need to be followed exactly, but please keep the same style for the entire scene as this movie cut will be part of a long MV, and the attached images, except the pouch picture, are consistent with other clips in terms of style. Scene story: Cinematic 8k, emotional animation style. Inside the ruined Notre-Dame Cathedral at golden hour sunset. A gentle sable Pekingese dog with a full black mask walks gracefully along the ruined stone floor illuminated by dusty sunbeams. The dog gradually dissolves into glowing blue light particles that float upward. The camera smoothly pans down to focus on a small red Shisa lion-shaped pouch resting on the stone altar. The glowing blue particles stream downward from the air and are absorbed into the red pouch. The red pouch glows warmly for a moment before fading into sunset shadows. Melancholic atmosphere, golden light and warm sunset color palette mixed with glowing blue particles, high quality.
```

**s32**

```text
Cinematic 8k, emotional animation style. Inside the ruined cathedral from the reference image, on a gentle summer night under cool blue moonlight and starry sky. A woman (wife) with a calm, reflective expression, gazing diagonally upward, lost in thought. She behaves naturally and humanly: she blinks naturally and moves subtly. When the loyal black dog slowly walks over, she notices it, looks down at the dog with a gentle smile and softly pets it. Beside her on the ground lies the small red Shisa lion pouch, and the dog curls up next to her, resting its head near the pouch. Soft warm night breeze, somber, emotional, touching moment, slow camera push-in, high quality.
```

**s35.** The references are @图1 her back, @图2 her front / three-quarter, @图3 the panda, and @图4 the penthouse (still 35).

```text
舞台は@图4（夜のパリのペントハウス室内。床から天井までのガラス窓の外にエッフェル塔とパリの夜景が広がり、室内は柔らかな暖色光、光沢のある石床）。全編この環境・光・床を基準とする。登場人物は、@图2（正面〜3/4アングルの女性武士）と@图1（女性の後ろ姿）を参照する女性キャラクター、および@图3（僧侶姿のジャイアントパンダ）を参照するパンダ。パンダの体型は女性より明らかに大きい。画風は参考画像に限りなく近い、硬朗で力強い線と平塗りによるレトロなコミック・挿絵調とし、アニメ調に寄せない。

0〜4秒：カメラは女性の正面〜3/4アングル。@图2の女性武士（黒髪を高く結い上げたまとめ髪、黒い和風武術服、背中に二本の刀、腰に赤と金色の帯）がカメラに向かって歩いてくる。片手で@图3のパンダの後ろ首をつかみ、床に座り込んだ姿勢のまま後ろへ引きずって進む。パンダは体を横向きにして進行方向へ横たわり、引きずられる。位置関係により、女性が正面のときはパンダの顔は自然に隠れて見えない。カメラはゆっくりと前進する。

4〜7秒：カメラが徐々に180度回転し、女性の背後からの視点へ切り替わる。女性の後ろ姿は@图1（まとめ髪、背中の二本の刀、黒い服）に一致させる。このときパンダは目を閉じている。パンダの表情は一切変えず、閉じた目だけで諦め・降伏の感情を伝える。引きずられる動作はそのまま続く。

7〜10秒：引きずりが続き、カメラは背後からの視点を保つ。床は終始清潔なまま。血痕のような跡やシミ、余計なエフェクト、追加の光・パーティクル・飛沫は一切描かない。

安定性：キャラクターの顔・体型・服装・刀の位置を全編で一貫させ、四肢の破綻や穿模を避ける。地面は@图4の床と一致させ、いかなる痕跡も追加しない。パンダの表情は変えず目を閉じるのみ。全編を通して参考画像のレトロで硬朗な挿絵調の画風・キャラクター・光を一貫させ、画面を安定させ、無駄なエフェクトを加えない。
```
