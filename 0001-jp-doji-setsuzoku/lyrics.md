# 0001 同時接続10人 — lyrics

His side of the anniversary year (2025-10-04 to 2026-10-03). Fun and self-deprecating, not sad and not a love song. Three versions were written; B shipped.

| Version | Title | Sound | Status |
| --- | --- | --- | --- |
| A | 21年目 | narrative folk-rock | not used |
| B | 同時接続10人 | contemporary J-pop | shipped, lyric in [README.md](README.md#song) |
| C | 6週間 | driving folk-rock | not used |

## What every version shares

**Every single thing he did this year happened in one room.** Streaming, trading, AI, writing, raging at mahjong, importing ramen, reading manga: same chair. He knows it. That's the joke, and it's what makes the other two songs land: they're about the people on the other side of the door.

**No dogs in the shipped version.** The song stays inside one room, and a 15-year-old dog barking at 2am pulls the camera out of it. Aramis belongs to 0002, where he's the work of the year, and to one line of 0003. The pouch and the shisa are 0002's too. A and C still carry them because they were written before B was chosen.

## A — 21年目

**The calendar walk.** The year, month by month, from the chair. The most faithful to the three-song structure, and it cuts cleanest against the other two.

B won as the funnier song. A's bridge also carries the dogs and the pouch, which the shipped song leaves to 0002.

Style:

```text
Japanese narrative folk-rock, male vocal, mid-tempo driving acoustic guitar and drums, talky conversational verses, dry self-deprecating delivery, warm analog production, subtle electric guitar
```

Exclude:

```text
sweeping strings, orchestral swell, gospel choir, ballad piano, key change, romantic
```

```text
[Intro: acoustic guitar alone]

[Verse 1]
10月の夜　配信オン
同時接続　10人ちょっと
三人麻雀　東場から
家族はもう　二階で寝てる

[Verse 2]
12月　息子が2歳
俺は椅子から　見てただけ
ダイエットコーラ　やめました
体重80　変わらない

[Chorus]
21年目
この部屋を　出てない
ドアの向こうで
誰かが　ちゃんと生きてる

[Verse 3]
3月　ファンドから　請求が来た
2年で　少しずつ　払うはずが
6週間で　全額　コールされた
資産はあるのに　現金がない

[Verse 4]
5月15日　47歳
AIがSlackを　返してる
Jiraもコードも　全部そう
俺は何を　してるんだろう

[Chorus]
21年目
この部屋を　出てない
ドアの向こうで
誰かが　ちゃんと生きてる

[Verse 5]
ノートに書いた　金と人生
新書になるって　褒められた
それでも夜中に　ふざけんなよ
台パンして　ドアを閉める

[Bridge: stripped down, almost spoken, no strings]
アラミスは　15歳
床で　寝てる
ダルは　赤いポーチの中
夜は　ワイフの隣で　寝てる

[Chorus]
21年目
この部屋を　出てない
10月4日
ドアを　開けるところ

[Outro: fade to guitar alone]
```

## B — 同時接続10人 (shipped)

**The streamer's year, told entirely as an apology to ten strangers.** The funniest of the three and the most self-deprecating; the title alone is the joke. The family arrives late and wins: the last chorus doesn't stream, and he goes upstairs.

Lyric and Suno prompt: [README.md](README.md#song).

## C — 6週間

**The March money thriller.** The fund called 100% of a $1M commitment in six weeks instead of two years, and a $300k distribution from another fund landed just in time. Driving and tense, with the strongest verse-to-verse momentum of the three.

It lost because its hook had to change. The first idea was him hiding the panic at dinner, and he didn't hide it: they share everything. Rewritten as two people watching the same number, it's truer but less of a thriller. B keeps the episode as one verse.

Style:

```text
Japanese driving folk-rock, male vocal, urgent strummed acoustic and bass, tense mid-tempo build, talky breathless verses, dry delivery, warm analog production
```

Exclude:

```text
orchestral swell, gospel choir, ballad piano, key change, romantic, triumphant
```

```text
[Intro: single muted guitar, tense]

[Verse 1]
3月　100万ドル　コミットした
18ヶ月から　24ヶ月
分割で　払えるって　書いてあった
だから　余裕だと思ってた

[Verse 2]
6週間で　全額だった
100パーセント　いますぐ払え
資産はあるのに　現金がない
家賃も危ないと　ワイフに言った

[Chorus]
6週間
2年のはずが　6週間
二人で　毎晩
数字だけ　見てた

[Verse 3]
別のファンドから　30万
来るはずのない　分配金
ギリギリで　間に合った
送金ボタン　押した夜

[Verse 4]
まだ楽じゃない　他にもある
でも3月ほど　じゃない
47歳　誕生日
何も言わずに　ケーキ食べた

[Chorus]
6週間
2年のはずが　6週間
二人で　毎晩
数字だけ　見てた

[Verse 5]
家では何も　起きてない
息子は泣いて　娘は歌う
アラミスは　15歳になった
俺は部屋で　画面を見てた

[Bridge: stripped down, almost spoken, no strings]
ワイフも知ってた　あの6週間
それでも別のものを　運んでた
子供二人と　老いた犬
毎晩　隣で　寝てる赤いポーチ

[Chorus]
6週間
あれは終わった
21年目
まだ　続いてる

[Outro: guitar resolves, quiet]
```

## Notes on the shipped lyric

- **Sung, not talked.** Exclude carries `rap, talk-singing, spoken word, monotone vocal`. The genre is `contemporary J-pop`, not city pop, so `city pop, 80s retro, funk revival` are excluded too. Bare section tags, four lines a section.
- **The rage is at the game, never the viewers.** Calm on stream, then 台パン and 「ロンにゃじゃねーよ」. 「感情むき出し」 and the quote stay together.
- **Chorus 1 is 東1局, chorus 2 is 南3局**: the first hand and オーラス, the last hand of three-player mahjong. The Suno field spells them `とんいっきょく` and `なんさんきょく` so they're sung right.
- **Numbers are Arabic in the subtitles.** If Suno sings a digit in English, it goes in kana in the Suno field only: `ひゃくまんドル`, `さんがつ`, `じゅうにん`, `いっかげつ`, `にじゅういちねんめ`, `じゅうがつよっか`. Never write 十分 for 10分.
- **`Jira` and `Slack` stay in Latin letters.**
- **The money verse sings `1ヶ月`.** The real window was about six weeks, which C keeps. It uses the finance words コミット, 全額請求 and `資金ショート`. He told her. `ワイフ`, not 妻.
- **Two audiences, never merged.** Ten to twenty watch the stream live; hundreds read the writing.
- **The ramen is a flex**, not a health story. His weight and the diet cola stay out.
- **The office is downstairs and the family upstairs.** The last line is 上がっていく.
- **The bridge goes 上手上手 then 下手くそ,** never the other way round, and the praise goes out `世界に流れる`.
- Not in it: dogs, March 8, 愛してる, 運命, 君のために.
