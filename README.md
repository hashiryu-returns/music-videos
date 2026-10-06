# music-videos

Original music videos. One numbered folder per MV, in one language. A song gets the next number when its MV is made, whether it is Japanese, English, or French. Songs that never get an MV live in the `lyrics.md` of the MV they were written alongside.

Shared notes on the tools live in [`DESIGN.md`](DESIGN.md).

## Songs

| # | Folder | Title | YouTube |
| --- | --- | --- | --- |
| 0001 | [`0001-jp-doji-setsuzoku`](0001-jp-doji-setsuzoku/README.md) | 同時接続10人 | [watch](https://www.youtube.com/watch?v=-LidPJsmBTc) |
| 0002 | [`0002-fr-je-marrete-pas`](0002-fr-je-marrete-pas/README.md) | Je m'arrête pas | [watch](https://www.youtube.com/watch?v=472scJ16qbg) |
| 0003 | [`0003-en-hamburger-hamburger`](0003-en-hamburger-hamburger/README.md) | Hamburger Hamburger | [watch](https://www.youtube.com/watch?v=S67cE91-6NI) |
| 0004 | [`0004-en-not-alone`](0004-en-not-alone/README.md) | Not Alone | [watch](https://www.youtube.com/watch?v=_w9ba2ul8fI) |
| 0005 | [`0005-en-out-of-my-way`](0005-en-out-of-my-way/README.md) | Out of My Way! (working title) | — |

0001–0003 are three songs made for the 21st anniversary, 2026-10-04. They cover the same year from three sides. 0004 is one of three songs written on one story, the first Dragon Quest, each with its own sound; the other two are in its [`lyrics.md`](0004-en-not-alone/lyrics.md). 0005 is our daughter's, with the hedgehog from 0002 as the hero. Later songs do not have to belong to a set.

## YouTube metadata

Every video uses the same format. Each song README has the text to paste.

**Title:** `[AI MV][<sung language>] <title as sung> (<English title, if not English>) [<tool>][<tool>]…`

- `[AI MV]` and the language tag lead. The language is the one the song is sung in: `JP`, `FR`, `EN`.
- The tools go last. Search cuts a title at about 60 characters, so the tools are the part that gets cut off.
- Anniversary, tribute and every other piece of context goes in the description, not the title.
- The Japanese translation keeps the same title and swaps only the English title for a Japanese one, if it has one.

**Description**, in this order:

1. What it is and why it exists, in two to four sentences. The first line shows above "more" and in search, so it has to stand on its own.
2. `Lyrics: turn on CC (…)`.
3. Related videos.
4. Tools and models.
5. Behind the scenes: what was hard and what was done about it, with the time it took.
6. The note article, in English on the English side (`?hl=en`) and Japanese on the Japanese side.
7. Three hashtags on the last line. YouTube shows them above the title.

English is the default. In YouTube Studio, set the video language and the title/description language to English, then add the Japanese under Subtitles → Add language → Japanese → Title & description.

**Tags** don't localize, so one list per video covers both languages. Each README lists them.

## A song folder

```text
NNNN-lang-slug/
├── README.md      title, tools, lyrics, how the picture was made
├── prompts.md     only if the song was built shot by shot
├── lyrics.md      versions and sibling songs that weren't shipped
├── captions/      sung lyric plus translations, as <lang>.vtt
├── characters/    plates
├── stills/
├── objects/       reference photos of things, never of people
├── clips/         per-scene video, not committed
├── audio/         the song and song-only previews, not committed
├── references/    external or private references, not committed
└── exports/
    ├── final/     finished MV and thumbnail
    └── drafts/
```

Copy the pieces the song actually has. Video and audio stay out of git. Drawings, stills, object photos, captions, and the thumbnail do not.

Real photos of people do not go in this repo.
