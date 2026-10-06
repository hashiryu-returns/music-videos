#!/usr/bin/env python3
"""YouTube thumbnails, one look per song.

Background art is <mv>/stills/thumbnail.* (0002 uses stills/17.png). Output goes to
<mv>/exports/final/<title> [Thumbnail].jpg at 1280x720.

    python _tools/make_thumbnails.py            # all
    python _tools/make_thumbnails.py 0004 0005  # some

Fonts are the macOS system ones. Keep the bottom-right corner clear: YouTube puts the
video length there.
"""
import math
import random
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

MV = Path(__file__).resolve().parent.parent
W, H = 1280, 720
SUP = "/System/Library/Fonts/Supplemental/"
SYS = "/System/Library/Fonts/"


def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def cover(path, fx=0.5, fy=0.5, zoom=1.0):
    im = Image.open(path).convert("RGB")
    s = max(W / im.width, H / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - W) * fx)
    y = round((im.height - H) * fy)
    return im.crop((x, y, x + W, y + H)).convert("RGBA")


def grad(size, stops, vertical=True):
    w, h = size
    g = Image.new("RGBA", size)
    px = g.load()
    n = h if vertical else w
    for i in range(n):
        t = i / max(1, n - 1)
        for j in range(len(stops) - 1):
            t0, c0 = stops[j]
            t1, c1 = stops[j + 1]
            if t0 <= t <= t1:
                k = (t - t0) / max(1e-6, t1 - t0)
                c = tuple(round(c0[m] + (c1[m] - c0[m]) * k) for m in range(3)) + (255,)
                break
        if vertical:
            for x in range(w):
                px[x, i] = c
        else:
            for y in range(h):
                px[i, y] = c
    return g


def text_mask(txt, f, stroke=0, tracking=0, pad=40):
    if tracking:
        widths = [f.getlength(ch) + tracking for ch in txt]
        tw = round(sum(widths) - tracking)
    else:
        tw = round(f.getlength(txt))
    asc, desc = f.getmetrics()
    m = Image.new("L", (tw + 2 * pad + 2 * stroke, asc + desc + 2 * pad + 2 * stroke), 0)
    d = ImageDraw.Draw(m)
    if tracking:
        x = pad + stroke
        for ch, cw in zip(txt, widths):
            d.text((x, pad + stroke), ch, font=f, fill=255, stroke_width=stroke, stroke_fill=255)
            x += cw
    else:
        d.text((pad + stroke, pad + stroke), txt, font=f, fill=255, stroke_width=stroke, stroke_fill=255)
    return m


def fill(mask, color_or_img):
    if isinstance(color_or_img, Image.Image):
        src = color_or_img.resize(mask.size)
    else:
        src = Image.new("RGBA", mask.size, color_or_img)
    out = Image.new("RGBA", mask.size, (0, 0, 0, 0))
    out.paste(src, (0, 0), mask)
    return out


def glow(mask, color, radius, strength=1.0):
    m = mask.filter(ImageFilter.GaussianBlur(radius))
    if strength != 1.0:
        m = m.point(lambda v: min(255, round(v * strength)))
    return fill(m, color)


def bbox_crop(layer):
    b = layer.getbbox()
    return layer.crop(b) if b else layer


def shear(layer, k):
    w, h = layer.size
    extra = round(abs(k) * h)
    return layer.transform((w + extra, h), Image.AFFINE, (1, k, -extra if k > 0 else 0, 0, 1, 0), Image.BICUBIC)


def place(base, layer, x, y, anchor="lt"):
    w, h = layer.size
    if anchor[0] == "m":
        x -= w // 2
    elif anchor[0] == "r":
        x -= w
    if anchor[1] == "m":
        y -= h // 2
    elif anchor[1] == "b":
        y -= h
    base.alpha_composite(layer, (round(x), round(y)))


def shade(base, box_fn):
    """Darken with an L mask built by box_fn(w, h) -> Image('L')."""
    m = box_fn(W, H)
    base.alpha_composite(fill(m, (0, 0, 0, 255)))


def linear_mask(direction, start, end, max_a):
    def f(w, h):
        m = Image.new("L", (w, h), 0)
        px = m.load()
        n = h if direction in ("up", "down") else w
        for i in range(n):
            t = i / (n - 1)
            if direction in ("up", "left"):
                t = 1 - t
            a = 0 if t < start else min(1, (t - start) / (end - start))
            v = round(max_a * a * a)
            if direction in ("up", "down"):
                for x in range(w):
                    px[x, i] = v
            else:
                for y in range(h):
                    px[i, y] = v
        return m
    return f


def radial_mask(cx, cy, r, max_a):
    def f(w, h):
        m = Image.new("L", (w, h), 0)
        px = m.load()
        for y in range(h):
            for x in range(w):
                d = math.hypot((x - cx) / r[0], (y - cy) / r[1])
                px[x, y] = round(max_a * max(0, 1 - d) ** 1.4)
        return m
    return f


def lang_chip(base, lang, accent=(255, 255, 255)):
    f = font(SYS + "ヒラギノ角ゴシック W8.ttc", 22)
    label = f"AI MV  ·  {lang}"
    tw = f.getlength(label)
    chip = Image.new("RGBA", (round(tw) + 36, 42), (0, 0, 0, 0))
    d = ImageDraw.Draw(chip)
    d.rounded_rectangle((0, 0, chip.width - 1, 41), 8, fill=(10, 10, 14, 200))
    d.rectangle((0, 8, 4, 33), fill=accent + (255,))
    d.text((20, 7), label, font=f, fill=(255, 255, 255, 240))
    place(base, chip, 28, 26)


# ---------------------------------------------------------------- 0001 JP
def jp():
    im = cover(MV / "0001-jp-doji-setsuzoku/stills/thumbnail.jpg")
    shade(im, linear_mask("down", 0.45, 1.0, 235))
    shade(im, linear_mask("up", 0.75, 1.0, 120))

    # stream-overlay HUD: the title is the viewer count
    d = ImageDraw.Draw(im)
    hf = font(SYS + "ヒラギノ角ゴシック W8.ttc", 26)
    live = Image.new("RGBA", (128, 46), (0, 0, 0, 0))
    ld = ImageDraw.Draw(live)
    ld.rounded_rectangle((0, 0, 127, 45), 6, fill=(230, 33, 23, 255))
    ld.ellipse((16, 16, 30, 30), fill=(255, 255, 255, 255))
    ld.text((40, 7), "LIVE", font=hf, fill="white")
    place(im, live, 28, 26)
    vf = font(SYS + "ヒラギノ角ゴシック W6.ttc", 24)
    pill_w = round(vf.getlength("10 人が視聴中")) + 64
    pill = Image.new("RGBA", (pill_w, 46), (0, 0, 0, 0))
    pd = ImageDraw.Draw(pill)
    pd.rounded_rectangle((0, 0, pill_w - 1, 45), 6, fill=(0, 0, 0, 170))
    # person glyph
    pd.ellipse((18, 9, 30, 21), fill="white")
    pd.pieslice((12, 22, 36, 46), 180, 360, fill="white")
    pd.text((46, 8), "10 人が視聴中", font=vf, fill="white")
    place(im, pill, 168, 26)

    tf = font(SYS + "ヒラギノ角ゴシック W9.ttc", 150)
    nf = font(SYS + "ヒラギノ角ゴシック W9.ttc", 200)
    a = text_mask("同時接続", tf, pad=60)
    n = text_mask("10", nf, pad=60)
    r = text_mask("人", tf, pad=60)
    cyan = (90, 230, 255, 255)
    pink = (255, 70, 160, 255)
    x, base_y = 34, 676
    layers = []
    for m, col, dy in ((a, cyan, 0), (n, pink, 0), (r, cyan, 0)):
        bb = m.getbbox()
        layers.append((m, col, bb, dy))
    for m, col, bb, dy in layers:
        y = base_y - bb[3] + dy
        place(im, glow(m, col[:3] + (255,), 22, 1.6), x - bb[0], y)
        place(im, glow(m, col[:3] + (255,), 6, 1.2), x - bb[0], y)
        place(im, fill(m, (255, 255, 255, 255)), x - bb[0], y)
        x += bb[2] - bb[0] + 10
    return im


# ---------------------------------------------------------------- 0002 FR
def fr():
    im = cover(MV / "0002-fr-je-marrete-pas/stills/17.png")
    shade(im, linear_mask("left", 0.35, 1.0, 215))
    f = font(SYS + "Avenir Next Condensed.ttc", 210, index=9)
    lines = [("JE", 0), ("M'ARRÊTE", 0), ("PAS.", 0)]
    block = Image.new("RGBA", (1100, 720), (0, 0, 0, 0))
    y = 0
    for i, (t, _) in enumerate(lines):
        m = text_mask(t, f, pad=30)
        bb = m.getbbox()
        m = m.crop((bb[0] - 10, bb[1] - 10, bb[2] + 10, bb[3] + 10))
        lx = 0
        if t == "PAS.":
            # slash bar behind the punchline
            bar = Image.new("RGBA", (m.width + 70, m.height - 24), (232, 22, 60, 255))
            place(block, bar, lx - 20, y + 16)
        place(block, fill(m, (0, 235, 255, 210)), lx - 7, y)
        place(block, fill(m, (255, 30, 120, 210)), lx + 7, y)
        place(block, fill(m, (255, 255, 255, 255)), lx, y)
        y += m.height - 34
    block = bbox_crop(block)
    block = block.rotate(5, Image.BICUBIC, expand=True)
    s = 540 / block.width
    block = block.resize((540, round(block.height * s)), Image.LANCZOS)
    top = (H - block.height) // 2 + 20
    shadow = glow(block.split()[3], (0, 0, 0, 255), 14, 1.3)
    place(im, shadow, 30, top + 10)
    place(im, block, 30, top)
    d = ImageDraw.Draw(im)
    for yy, h in ((0.18, 3), (0.37, 2), (0.61, 4), (0.86, 2)):
        y = top + round(block.height * yy)
        d.rectangle((0, y, 560, y + h), fill=(255, 255, 255, 60))
    lang_chip(im, "FR", (232, 22, 60))
    return im


# ---------------------------------------------------------------- 0003 EN Hamburger
def burger():
    im = cover(MV / "0003-en-hamburger-hamburger/stills/thumbnail.jpg", fy=0.3)
    shade(im, linear_mask("down", 0.55, 1.0, 150))
    f = font(SUP + "Arial Black.ttf", 112)
    palette = [(255, 201, 60), (240, 66, 44)]
    rows = ["HAMBURGER", "HAMBURGER"]
    y0 = [408, 522]
    x0 = [26, 66]
    for r, word in enumerate(rows):
        x = x0[r]
        for i, ch in enumerate(word):
            m = text_mask(ch, f, pad=30)
            ring = text_mask(ch, f, stroke=10, pad=30)
            outer = text_mask(ch, f, stroke=18, pad=30)
            g = Image.new("RGBA", m.size, (0, 0, 0, 0))
            g.alpha_composite(fill(outer, (255, 255, 255, 255)))
            g.alpha_composite(fill(ring, (74, 37, 17, 255)))
            c = palette[r] if i % 2 == 0 else tuple(min(255, v + 25) for v in palette[r])
            g.alpha_composite(fill(m, grad(m.size, [(0, c), (0.55, c), (1, tuple(round(v * 0.78) for v in c))])))
            # glossy highlight
            hl = Image.new("L", m.size, 0)
            ImageDraw.Draw(hl).rectangle((0, 0, m.width, m.height * 0.42), fill=70)
            g.alpha_composite(fill(ImageChops.multiply(m, hl), (255, 255, 255, 255)))
            ang = (-7, 5, -3, 7, -5, 4, -6, 3, -4)[i] * 0.5
            g = g.rotate(ang, Image.BICUBIC, expand=True)
            bounce = (0, -14, 4, -10, 6, -16, 2, -8, 0)[i] // 2
            sh = glow(g.split()[3], (40, 15, 0, 255), 6, 1.2)
            place(im, sh, x + 5, y0[r] + bounce + 8)
            place(im, g, x, y0[r] + bounce)
            x += f.getlength(ch) * 0.93
    lang_chip(im, "EN", (255, 201, 60))
    return im


# ---------------------------------------------------------------- 0004 EN Not Alone
def not_alone():
    im = cover(MV / "0004-en-not-alone/stills/thumbnail.png", fy=0.35)
    shade(im, linear_mask("down", 0.5, 1.0, 245))
    shade(im, radial_mask(640, 600, (700, 260), 120))
    f = font(SUP + "Copperplate.ttc", 140, index=2)
    m = text_mask("NOT ALONE", f, tracking=18, pad=50)
    m = m.crop(m.getbbox())
    pad = 50
    big = Image.new("L", (m.width + 2 * pad, m.height + 2 * pad), 0)
    big.paste(m, (pad, pad))
    m = big
    gold = grad(m.size, [(0, (255, 248, 210)), (0.42, (247, 214, 120)), (0.5, (196, 140, 40)), (1, (255, 225, 140))])
    edge = m.filter(ImageFilter.MaxFilter(7))
    layer = Image.new("RGBA", m.size, (0, 0, 0, 0))
    layer.alpha_composite(glow(m, (170, 90, 255, 255), 26, 1.8))
    layer.alpha_composite(fill(edge, (48, 22, 6, 255)))
    layer.alpha_composite(fill(m, gold))
    cx = W // 2
    place(im, layer, cx, 676, "mb")
    # ornament rules + diamond
    d = ImageDraw.Draw(im)
    gy = 676 - layer.height + pad - 30
    half = m.width // 2 - pad
    for sx in (-1, 1):
        x1, x2 = cx + sx * 40, cx + sx * (half)
        d.line((x1, gy, x2, gy), fill=(240, 205, 120, 230), width=2)
    d.polygon([(cx, gy - 10), (cx + 10, gy), (cx, gy + 10), (cx - 10, gy)], fill=(255, 230, 150, 255))
    lang_chip(im, "EN", (240, 205, 120))
    return im


# ---------------------------------------------------------------- 0005 EN Out of My Way
def out_of_my_way():
    im = cover(MV / "0005-en-out-of-my-way/stills/thumbnail.png", fx=1.0, fy=0.35, zoom=1.22)
    # speed lines trail behind him, in the open sky only
    lines = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lines)
    rnd = random.Random(7)
    for _ in range(46):
        y = rnd.randint(40, 560)
        x = rnd.randint(800, 1150)
        ln = rnd.randint(140, 420)
        d.line((x, y, x + ln, y), fill=(255, 255, 255, rnd.randint(70, 150)), width=rnd.choice((2, 3, 4)))
    im.alpha_composite(lines)
    shade(im, linear_mask("right", 0.4, 1.0, 140))
    f = font(SUP + "Arial Black.ttf", 150)
    words = [("OUT OF", 0.62), ("MY WAY!", 1.0)]
    block = Image.new("RGBA", (1300, 600), (0, 0, 0, 0))
    y = 0
    for word, scale in words:
        ff = font(SUP + "Arial Black.ttf", round(150 * scale))
        m = text_mask(word, ff, pad=40)
        m = m.crop(m.getbbox())
        p = 30
        mm = Image.new("L", (m.width + 2 * p, m.height + 2 * p), 0)
        mm.paste(m, (p, p))
        m = mm
        stroke = m.filter(ImageFilter.MaxFilter(17))
        yellow = grad(m.size, [(0, (255, 244, 120)), (0.55, (255, 210, 40)), (1, (255, 140, 20))])
        g = Image.new("RGBA", m.size, (0, 0, 0, 0))
        g.alpha_composite(fill(stroke, (16, 10, 30, 255)))
        g.alpha_composite(fill(m, yellow))
        sh = fill(stroke, (220, 30, 50, 255))
        x = 1300 - g.width
        place(block, sh, x + 14, y + 14)
        place(block, g, x, y)
        y += g.height - 44
    block = bbox_crop(block)
    block = shear(block, -0.22)
    block = block.rotate(7, Image.BICUBIC, expand=True)
    s = 470 / block.width
    block = block.resize((470, round(block.height * s)), Image.LANCZOS)
    place(im, block, W - 24, 300, "rm")
    lang_chip(im, "EN", (255, 210, 40))
    return im


SONGS = {
    "0001": ("0001-jp-doji-setsuzoku", "[AI MV][JP] 同時接続10人", jp),
    "0002": ("0002-fr-je-marrete-pas", "[AI MV][FR] Je m'arrête pas", fr),
    "0003": ("0003-en-hamburger-hamburger", "[AI MV][EN] Hamburger Hamburger", burger),
    "0004": ("0004-en-not-alone", "[AI MV][EN] Not Alone", not_alone),
    "0005": ("0005-en-out-of-my-way", "[AI MV][EN] Out of My Way!", out_of_my_way),
}

if __name__ == "__main__":
    for key in sys.argv[1:] or list(SONGS):
        folder, title, build = SONGS[key]
        out = MV / folder / "exports" / "final" / f"{title} [Thumbnail].jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        build().convert("RGB").save(out, quality=92)
        print("saved", out.relative_to(MV))
