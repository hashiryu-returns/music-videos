#!/usr/bin/env python3
"""YouTube thumbnails, one look per song.

Background art is <mv>/stills/thumbnail.* (0002 uses stills/17.png). Output goes to
<mv>/exports/final/<title> [Thumbnail].jpg at 1280x720.

    python _tools/make_thumbnails.py            # all
    python _tools/make_thumbnails.py 0004 0005  # some

Display fonts live in _tools/fonts. Keep the bottom-right corner clear: YouTube puts the
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



# ---------------------------------------------------------------- logo builder
FONTS = Path(__file__).resolve().parent / "fonts"


def gfont(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight:
        f.set_variation_by_axes([weight])
    return f


def word(text, f, tracking=0):
    m = text_mask(text, f, tracking=tracking, pad=10)
    return m.crop(m.getbbox())


def fit(text, name, width, tracking=0, weight=None):
    m = word(text, gfont(name, 200, weight), tracking)
    return word(text, gfont(name, max(20, round(200 * width / m.width)), weight), tracking)


def pad_mask(m, p):
    out = Image.new("L", (m.width + 2 * p, m.height + 2 * p), 0)
    out.paste(m, (p, p))
    return out


def grow(m, px):
    """Dilate by px, in steps so MaxFilter stays cheap."""
    while px > 0:
        step = min(px, 6)
        m = m.filter(ImageFilter.MaxFilter(2 * step + 1))
        px -= step
    return m


def logo(mask, face, depth=12, d=(1, 1), side=((120, 60, 10), (40, 16, 4)),
         rim=(4, (30, 14, 4)), outer=(), bevel=True, gloss=0, halo=None, drop=True):
    """A title that reads as an object: extruded sides, an outline, a lit face.

    face is a colour or an image sized to the mask. outer is [(px, colour), ...] from the
    inside out, drawn around the whole silhouette including the extrusion.
    """
    widest = max([w for w, _ in outer] + [rim[0] if rim else 0])
    p = depth + widest + 40
    M = pad_mask(mask, p)
    sil = M.copy()
    for i in range(1, depth + 1):
        sil = ImageChops.lighter(sil, ImageChops.offset(M, i * d[0], i * d[1]))
    out = Image.new("RGBA", M.size, (0, 0, 0, 0))
    if halo:
        col, r, k = halo
        out.alpha_composite(glow(grow(sil, 4), col, r, k))
    if drop:
        out.alpha_composite(fill(ImageChops.offset(sil, 6, 12).filter(ImageFilter.GaussianBlur(12)), (0, 0, 0, 200)))
    for w, col in reversed(outer):
        out.alpha_composite(fill(grow(sil, w), col))
    for i in range(depth, 0, -1):
        t = (i - 1) / max(1, depth - 1)
        c0, c1 = side
        col = tuple(round(c0[k] + (c1[k] - c0[k]) * t) for k in range(3)) + (255,)
        out.alpha_composite(fill(ImageChops.offset(M, i * d[0], i * d[1]), col))
    if rim:
        out.alpha_composite(fill(grow(M, rim[0]), rim[1] + (255,)))
    if isinstance(face, Image.Image):
        f_img = Image.new("RGBA", M.size, (0, 0, 0, 0))
        f_img.paste(face.resize(mask.size), (p, p))
        out.alpha_composite(fill(M, f_img))
    else:
        out.alpha_composite(fill(M, face))
    if bevel:
        lit = ImageChops.subtract(M, ImageChops.offset(M, 3, 4))
        dark = ImageChops.subtract(M, ImageChops.offset(M, -3, -4))
        out.alpha_composite(fill(lit, (255, 255, 255, 170)))
        out.alpha_composite(fill(dark, (0, 0, 0, 120)))
    if gloss:
        top = Image.new("L", M.size, 0)
        b = M.getbbox()
        ImageDraw.Draw(top).rectangle((0, 0, M.width, b[1] + (b[3] - b[1]) * 0.45), fill=gloss)
        out.alpha_composite(fill(ImageChops.multiply(M, top), (255, 255, 255, 255)))
    return bbox_crop(out)


def scale_to(layer, width):
    return layer.resize((width, round(layer.height * width / layer.width)), Image.LANCZOS)


def sparkle(base, x, y, r, color=(255, 255, 255), a=255):
    """Four-point star glint."""
    s = Image.new("RGBA", (r * 4, r * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    c = r * 2
    t = max(1, r // 7)
    d.polygon([(c, c - r * 2 + 2), (c + t, c), (c, c + r * 2 - 2), (c - t, c)], fill=color + (a,))
    d.polygon([(c - r * 2 + 2, c), (c, c + t), (c + r * 2 - 2, c), (c, c - t)], fill=color + (a,))
    g = s.filter(ImageFilter.GaussianBlur(r / 3))
    base.alpha_composite(g, (x - c, y - c))
    base.alpha_composite(g, (x - c, y - c))
    base.alpha_composite(s, (x - c, y - c))


def embers(base, box, n, colors, seed, rmax=5):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = box
    for _ in range(n):
        x, y = rnd.randint(x0, x1), rnd.randint(y0, y1)
        r = rnd.uniform(1.2, rmax)
        col = rnd.choice(colors) + (rnd.randint(150, 255),)
        d.ellipse((x - r, y - r, x + r, y + r), fill=col)
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(2.2)))
    base.alpha_composite(layer)


def ribbon(text, f, fg, bg, padx=26, pady=10, tracking=6, slant=0.25):
    m = word(text, f, tracking)
    w, h = m.width + 2 * padx, m.height + 2 * pady
    r = Image.new("RGBA", (w, h), bg + (255,))
    r.alpha_composite(fill(pad_mask(m, 0), fg + (255,)), (padx, pady))
    return shear(r, slant)


def slash(base, p0, p1, width=10, core=(255, 255, 255), bloom=(255, 40, 60)):
    """A tapered streak: white core, coloured bloom. Used as a sword cut across a title."""
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy)
    nx, ny = -dy / n * width / 2, dx / n * width / 2
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    d.polygon([(x0, y0), (mx + nx, my + ny), (x1, y1), (mx - nx, my - ny)], fill=core + (255,))
    a = layer.split()[3]
    base.alpha_composite(glow(a, bloom + (255,), 18, 2.2))
    base.alpha_composite(glow(a, bloom + (255,), 6, 1.5))
    base.alpha_composite(layer)


STEEL = [
    (0, (255, 255, 255)),
    (0.35, (200, 208, 220)),
    (0.5, (110, 118, 132)),
    (0.56, (235, 240, 248)),
    (1, (140, 148, 162)),
]


# ---------------------------------------------------------------- 0001 JP
def jp():
    im = cover(MV / "0001-jp-doji-setsuzoku/stills/thumbnail.jpg")
    shade(im, linear_mask("down", 0.42, 1.0, 235))
    shade(im, linear_mask("up", 0.78, 1.0, 120))

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
    pd.ellipse((18, 9, 30, 21), fill="white")
    pd.pieslice((12, 22, 36, 46), 180, 360, fill="white")
    pd.text((46, 8), "10 人が視聴中", font=vf, fill="white")
    place(im, pill, 168, 26)

    # one mask, "10" coloured separately so it lands on the same baseline as the kanji
    f = gfont("DelaGothicOne-Regular.ttf", 200)
    full = "同時接続10人"
    m = word(full, f)
    head = word("同時接続", f)
    split = head.width + 4
    tail = word("人", f)
    face = Image.new("RGBA", m.size)
    face.paste(grad(m.size, [(0, (255, 255, 255)), (0.45, (190, 245, 255)), (0.55, (90, 210, 255)), (1, (225, 250, 255))]), (0, 0))
    pink = grad((m.width - split - tail.width, m.height), [(0, (255, 225, 240)), (0.5, (255, 90, 175)), (1, (255, 160, 210))])
    face.paste(pink, (split, 0))
    t = logo(m, face, depth=14, d=(1, 2), side=((40, 40, 140), (12, 8, 40)), rim=(5, (8, 10, 40)),
             outer=[(5, (255, 255, 255))], gloss=0, halo=((60, 200, 255, 255), 28, 1.3))
    t = scale_to(t, 900)
    place(im, t, 22, 640, "lb")
    sub = ribbon("ABOUT TEN ONLINE", font(SYS + "Avenir Next Condensed.ttc", 34, index=8),
                 (255, 255, 255), (230, 40, 130))
    place(im, sub, 52, 646)
    return im


# ---------------------------------------------------------------- 0002 FR
def fr():
    im = cover(MV / "0002-fr-je-marrete-pas/stills/17.png")
    shade(im, linear_mask("left", 0.35, 1.0, 215))
    rows = []
    for text, width in (("Je m'arrête", 580), ("pas", 330)):
        m = fit(text, "PirataOne-Regular.ttf", width, tracking=2)
        rows.append(logo(m, grad(m.size, STEEL), depth=8, d=(1, 1), side=((60, 64, 74), (14, 14, 18)),
                         rim=(4, (8, 8, 10)), halo=((220, 20, 50, 255), 22, 0.9)))
    block = Image.new("RGBA", (900, 600), (0, 0, 0, 0))
    place(block, rows[0], 0, 0)
    place(block, rows[1], 220, rows[0].height - 60)
    block = scale_to(bbox_crop(block), 580)
    top = (H - block.height) // 2 - 10
    place(im, block, 30, top)
    slash(im, (14, top + block.height - 20), (560, top + 70), width=9)
    sub = ribbon("I DON'T STOP", font(SYS + "Avenir Next Condensed.ttc", 30, index=8),
                 (255, 255, 255), (200, 16, 40), slant=0)
    place(im, sub, 40, top + block.height + 26)
    lang_chip(im, "FR", (232, 22, 60))
    return im


# ---------------------------------------------------------------- 0003 EN Hamburger
def burger():
    im = cover(MV / "0003-en-hamburger-hamburger/stills/thumbnail.jpg", fy=0.3)
    shade(im, linear_mask("down", 0.6, 1.0, 140))
    lines = []
    for text, top, bottom in (("HAMBURGER", (255, 230, 90), (245, 160, 20)),
                              ("HAMBURGER", (255, 120, 90), (210, 35, 25))):
        m = fit(text, "LuckiestGuy-Regular.ttf", 700)
        face = grad(m.size, [(0, top), (0.6, top), (1, bottom)])
        lines.append(logo(m, face, depth=12, d=(0, 1), side=((120, 60, 20), (70, 30, 8)),
                          rim=(5, (70, 30, 8)), outer=[(9, (255, 255, 255))], gloss=60))
    block = Image.new("RGBA", (1000, 500), (0, 0, 0, 0))
    place(block, lines[0], 0, 0)
    place(block, lines[1], 40, lines[0].height - 40)
    block = bbox_crop(block).rotate(3, Image.BICUBIC, expand=True)
    block = scale_to(block, 720)
    place(im, block, 18, 712, "lb")
    lang_chip(im, "EN", (255, 201, 60))
    return im


# ---------------------------------------------------------------- 0004 EN Not Alone
def not_alone():
    im = cover(MV / "0004-en-not-alone/stills/thumbnail.png", fy=0.28)
    shade(im, linear_mask("down", 0.55, 1.0, 200))
    m = fit("NOT ALONE", "Cinzel[wght].ttf", 1100, tracking=10, weight=900)
    t = logo(m, grad(m.size, STEEL), depth=16, d=(1, 1), side=((70, 60, 110), (14, 10, 30)), rim=None,
             halo=((160, 90, 255, 255), 34, 1.5))
    t = scale_to(t, 1120)
    bottom = 618
    place(im, t, W // 2, bottom, "mb")
    embers(im, (0, 360, W, 700), 80, [(200, 140, 255), (170, 110, 255), (235, 225, 255)], seed=4, rmax=4)
    top = bottom - t.height
    for x, y, r in ((300, top + 42, 22), (1010, top + 70, 14)):
        sparkle(im, x, y, r, (235, 225, 255))
    lang_chip(im, "EN", (190, 160, 255))
    return im


# ---------------------------------------------------------------- 0005 EN Out of My Way
def out_of_my_way():
    im = cover(MV / "0005-en-out-of-my-way/stills/thumbnail.png", fx=1.0, fy=0.35, zoom=1.22)
    lines = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lines)
    rnd = random.Random(7)
    for _ in range(46):
        y = rnd.randint(40, 560)
        x = rnd.randint(800, 1150)
        ln = rnd.randint(140, 420)
        d.line((x, y, x + ln, y), fill=(255, 255, 255, rnd.randint(70, 150)), width=rnd.choice((2, 3, 4)))
    im.alpha_composite(lines)
    shade(im, linear_mask("right", 0.45, 1.0, 120))
    parts = []
    for text, width in (("OUT OF", 300), ("MY WAY!", 520)):
        m = fit(text, "Bangers-Regular.ttf", width, tracking=4)
        face = grad(m.size, [(0, (255, 250, 170)), (0.5, (255, 214, 40)), (1, (255, 130, 10))])
        parts.append(logo(m, face, depth=14, d=(1, 1), side=((210, 30, 40), (90, 0, 20)),
                          rim=(4, (20, 10, 30)), outer=[(7, (255, 255, 255))], gloss=50,
                          halo=((255, 60, 80, 255), 22, 1.0)))
    block = Image.new("RGBA", (900, 600), (0, 0, 0, 0))
    place(block, parts[0], 880, 0, "rt")
    place(block, parts[1], 880, parts[0].height - 100, "rt")
    block = bbox_crop(block).rotate(6, Image.BICUBIC, expand=True)
    block = scale_to(block, 480)
    place(im, block, W - 22, 300, "rm")
    sparkle(im, 900, 175, 16, (255, 240, 200))
    sparkle(im, 1210, 420, 11, (255, 240, 200))
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
    args = sys.argv[1:]
    preview = "--preview" in args
    keys = [a for a in args if a != "--preview"] or list(SONGS)
    for key in keys:
        folder, title, build = SONGS[key]
        if preview:
            out = Path("/tmp/yt") / f"{key}.jpg"
        else:
            out = MV / folder / "exports" / "final" / f"{title} [Thumbnail].jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        build().convert("RGB").save(out, quality=92)
        print("saved", out)
