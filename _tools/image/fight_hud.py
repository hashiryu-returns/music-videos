"""Fight-game HUD layers for 0006, as 1920x1080 transparent PNGs.

Each layer is full frame so it drops onto the timeline with no positioning.
The VS screen (16): the neon `VS`, the white frame, the two names with their control-type badges, and the band of player cards and the stage name
along the bottom, after Street Fighter 6; the player IDs, ranks and points are made up. Each card has the player's own
background, from the plates in `0006-en-steel-in-bloom/characters`: her blade for the singer, the zunda mochi for the rival,
the bridge for the stage. `ROUND 1`, in Street Fighter 6's brushed silver, goes over 17, the first shot of the fight.
The fight HUD, after Street Fighter 6: every gauge is one parallelogram, leaning one way on the singer's side and mirrored
on the rival's. `hud-fight.png` is the HUD at full life and 99. `hud-fight-chorus1.mov` (ProRes 4444 with alpha, not in git) is
the HUD from the hit in 24b to the end of 24c: the timer counting down from "FIGHT!", the rival's bar draining from its
outer end with the red chip following, and `PUNISH COUNTER` sliding in on the singer's side.
`hud-bonus-stage.mov` (the same format) is the rival's bonus stage over the chase, 25b to 25h: `BONUS STAGE`, a stage
timer, P2's score and the awards on her side. `fight_hud.py <dir> bonus` renders only that clip.
Text that FCP scales is drawn at the centre of the frame, so it scales about itself.
"""
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FONTS = Path(__file__).resolve().parent.parent / "fonts"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

BAR_Y, BAR_H = 70, 46
L0, L1 = 110, 870
R0, R1 = W - L1, W - L0
SINGER, RIVAL = (178, 92, 255), (120, 235, 60)
WHITE = (255, 255, 255, 255)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def glow(layer, radius, strength=2):
    g = layer.filter(ImageFilter.GaussianBlur(radius))
    out = Image.new("RGBA", layer.size)
    for _ in range(strength):
        out = Image.alpha_composite(out, g)
    return Image.alpha_composite(out, layer)


def saira(size, width, weight=900):
    """Saira, the nearest open font to Street Fighter 6's display face: the same file, condensed for the fighters'
    names and wide for `ROUND`, as the game does."""
    f = font("Saira[wdth,wght].ttf", size)
    f.set_variation_by_axes([weight, width])
    return f


def edges(mask, width):
    return ImageChops.subtract(mask.filter(ImageFilter.MaxFilter(width)), mask.filter(ImageFilter.MinFilter(width)))


def neon_vs():
    """`VS` as the neon sign behind the two fighters in Street Fighter 6: each letter two purple tubes, the outline
    and a second line inside it, glowing. The letters are hollow, so the picture shows through.
    Small, centred across the frame and standing just above the band, between the fighters' names."""
    f = saira(700, 100, 800)
    pad = 120
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    b = probe.textbbox((0, 0), "VS", font=f)
    tw, th = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    m = Image.new("L", (tw, th))
    ImageDraw.Draw(m).text((pad - b[0], pad - b[1]), "VS", font=f, fill=255)
    outer = edges(m, 9)
    inner = edges(m.filter(ImageFilter.MinFilter(51)), 7)
    tubes = ImageChops.lighter(outer, inner)
    sign = Image.new("RGBA", (tw, th))
    for radius, col, k in ((60, (150, 30, 255), 0.55), (22, (200, 60, 255), 0.9), (7, (235, 120, 255), 1.0)):
        g = Image.new("RGBA", (tw, th), col + (255,))
        g.putalpha(tubes.filter(ImageFilter.GaussianBlur(radius)).point(lambda v, k=k: min(255, int(v * 2.6 * k))))
        sign.alpha_composite(g)
    core = Image.new("RGBA", (tw, th), (255, 222, 255, 255))
    core.putalpha(tubes.filter(ImageFilter.GaussianBlur(1.2)))
    sign.alpha_composite(core)
    sign = sign.resize((int(tw * 0.48), int(th * 0.48)), Image.LANCZOS)
    x0, _, x1, y1 = sign.getchannel("A").point(lambda v: 255 if v > 200 else 0).getbbox()
    im = Image.new("RGBA", (W, H))
    im.alpha_composite(sign, (int(W / 2 - (x0 + x1) / 2), BAND_Y0 - 30 - y1))
    return im


FRAME = (47, 19, W - 47, 1050)


def vs_frame():
    """The white frame of the VS screen and the dimmed margin outside it."""
    im = Image.new("RGBA", (W, H), (22, 12, 40, 215))
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = FRAME
    d.rectangle((x0, y0, x1, y1), fill=(0, 0, 0, 0))
    d.rectangle((x0, y0, x1, y1), outline=(250, 250, 255, 255), width=6)
    return im


def brushed(size, stops, seed):
    """Brushed metal: a vertical ramp through `stops` (position, grey), streaked along the grain."""
    w, h = size
    ramp = Image.new("L", (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        k = next(i for i in range(len(stops) - 1) if t <= stops[i + 1][0])
        (t0, a), (t1, b) = stops[k], stops[k + 1]
        ramp.putpixel((0, y), int(a + (b - a) * (t - t0) / max(1e-6, t1 - t0)))
    ramp = ramp.resize((w, h))
    rng = random.Random(seed)
    noise = Image.new("L", (24, h))
    noise.putdata([rng.randint(0, 255) for _ in range(24 * h)])
    noise = noise.resize((w, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.6))
    metal = Image.blend(ramp, noise, 0.14)
    return Image.merge("RGBA", (metal.point(lambda v: min(255, v + 6)), metal, metal.point(lambda v: min(255, v + 14)),
                                Image.new("L", (w, h), 255)))


def oxanium(size):
    """Oxanium ExtraBold: heavy, square, the corners cut, like Street Fighter 6's `ROUND`."""
    f = font("Oxanium[wght].ttf", size)
    f.set_variation_by_axes([800])
    return f


def round_title(n):
    """`ROUND n` as in Street Fighter 6: square brushed-silver letters, the number twice their height on a slash of
    purple paint, the bottoms level. Placed where SF6 puts it: a little left of centre, the bottoms at 59% of the height."""
    word_f, num_f = oxanium(220), oxanium(420)
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    wb = probe.textbbox((0, 0), "ROUND", font=word_f)
    nb = probe.textbbox((0, 0), str(n), font=num_f)
    ww, wh = 488, 159
    nw, nh = 110, 296
    gap = 60
    x0 = int(W * 0.472 - (ww + gap + nw) / 2)
    base = int(H * 0.59)

    def glyphs(text, f, bbox, w, h):
        m = Image.new("L", (bbox[2] - bbox[0] + 20, h + 20))
        ImageDraw.Draw(m).text((10 - bbox[0], 10 - bbox[1]), text, font=f, fill=255)
        return m.resize((w + 20, h + 20), Image.LANCZOS)

    word = glyphs("ROUND", word_f, wb, ww, wh).filter(ImageFilter.MaxFilter(5))
    num = glyphs(str(n), num_f, nb, nw, nh).filter(ImageFilter.MaxFilter(5))
    wpos = (x0 - 10, base - wh - 10)
    npos = (x0 + ww + gap - 10, base - nh - 10)

    im = Image.new("RGBA", (W, H))
    paint = Image.new("RGBA", (W, H))
    p = ImageDraw.Draw(paint)
    cx = npos[0] + nw / 2 + 10
    top, bot = base - nh - 30, base + 40
    p.polygon([(cx + 40, top), (cx + 150, top - 20), (cx - 40, bot + 30), (cx - 150, bot)], fill=(118, 40, 214, 235))
    p.polygon([(cx + 70, top + 60), (cx + 120, top + 50), (cx - 10, bot - 30), (cx - 70, bot - 10)], fill=(170, 96, 255, 220))
    p.polygon([(cx - 120, base - nh * 0.25), (cx - 20, base - nh * 0.32), (cx - 160, base + 10)], fill=(92, 26, 170, 230))
    rng = random.Random(1)
    for _ in range(26):
        r = rng.randint(3, 11)
        x, y = cx + rng.randint(-230, 230), rng.randint(top - 30, bot + 30)
        p.ellipse((x - r, y - r, x + r, y + r), fill=(150, 70, 245, rng.randint(150, 235)))
    im.alpha_composite(paint)

    for mask, pos, seed in ((word, wpos, 2), (num, npos, 3)):
        shadow = Image.new("RGBA", (W, H))
        sm = Image.new("L", (W, H))
        sm.paste(mask, (pos[0] + 8, pos[1] + 12))
        shadow.putalpha(sm.point(lambda v: v * 170 // 255).filter(ImageFilter.GaussianBlur(8)))
        im.alpha_composite(shadow)
        edge = Image.new("L", (W, H))
        edge.paste(mask.filter(ImageFilter.MaxFilter(9)), pos)
        dark = Image.new("RGBA", (W, H), (26, 24, 38, 255))
        dark.putalpha(edge)
        im.alpha_composite(dark)
        metal = brushed(mask.size, [(0, 252), (0.42, 224), (0.5, 168), (0.56, 214), (0.85, 246), (1, 200)], seed)
        layer = Image.new("RGBA", (W, H))
        full = Image.new("L", (W, H))
        full.paste(mask, pos)
        layer.paste(metal, pos)
        layer.putalpha(full)
        im.alpha_composite(layer)
    return im


BAND_Y0, BAND_Y1 = 872, 1036
STATS_Y = BAND_Y0 + 126
BAND_X0, BAND_X1 = 56, W - 56
CARD_L, CARD_R = 730, W - 730
SLANT = 9
STAGE_DROP = 8
DARK = (8, 8, 14, 255)
PLATES = Path(__file__).resolve().parent.parent.parent / "0006-en-steel-in-bloom" / "characters"


def bold(name, size, weight="Bold"):
    f = font(name, size)
    f.set_variation_by_name(weight)
    return f


def control_badge(im, cx, cy, r, kind):
    """The control-type badge of Street Fighter 6: `C` (Classic) a purple hexagon standing on a point, `M` (Modern)
    an orange square. The letter is white over pale below its middle, outlined in the badge's colour."""
    k = 4
    s = 2 * r * k
    b = Image.new("RGBA", (s + 8 * k, s + 8 * k))
    d = ImageDraw.Draw(b)
    c = b.width / 2
    if kind == "C":
        def hexagon(rad):
            return [(c + rad * math.cos(math.radians(90 + 60 * i)), c - rad * math.sin(math.radians(90 + 60 * i)))
                    for i in range(6)]
        d.polygon(hexagon(r * k * 1.08), fill=(250, 248, 255, 255))
        d.polygon(hexagon(r * k * 0.96), fill=(136, 60, 230, 255))
        d.polygon(hexagon(r * k * 0.74), fill=(34, 12, 70, 255))
        rim, pale = (150, 70, 240, 255), (214, 186, 255, 255)
    else:
        h = r * k * 0.95
        d.rounded_rectangle((c - h, c - h, c + h, c + h), radius=r * k * 0.14, fill=(120, 48, 12, 255))
        d.rounded_rectangle((c - h * 0.92, c - h * 0.92, c + h * 0.92, c + h * 0.92), radius=r * k * 0.1,
                            fill=(236, 132, 44, 255))
        d.rectangle((c - h * 0.72, c - h * 0.72, c + h * 0.72, c + h * 0.72), fill=(52, 24, 14, 255))
        rim, pale = (226, 64, 34, 255), (255, 210, 214, 255)
    f = bold("Oswald[wght].ttf", int(r * k * 1.15))
    d.text((c, c), kind, font=f, fill=rim, anchor="mm", stroke_width=int(r * k * 0.09), stroke_fill=rim)
    letter = Image.new("L", b.size)
    ImageDraw.Draw(letter).text((c, c), kind, font=f, fill=255, anchor="mm")
    face = Image.new("RGBA", b.size, (255, 255, 255, 255))
    ImageDraw.Draw(face).rectangle((0, c + r * k * 0.08, b.width, b.height), fill=pale)
    face.putalpha(letter)
    b.alpha_composite(face)
    b = b.resize((b.width // k, b.height // k), Image.LANCZOS)
    im.alpha_composite(b, (int(cx - b.width / 2), int(cy - b.height / 2)))


def name(title, left):
    """The fighter's name over the VS screen's player card, with the control-type badge, as in Street Fighter 6:
    the display face of `ROUND`, condensed, with a hard drop shadow."""
    im = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(im)
    f = saira(62, 82, 850)
    y = BAND_Y0 - 18
    tw = d.textlength(title, font=f)
    bx = 120 if left else W - 120
    x = bx + 30 if left else bx - 30 - tw
    soft = Image.new("RGBA", (W, H))
    ImageDraw.Draw(soft).text((x + 3, y + 5), title, font=f, fill=(10, 0, 30, 170), anchor="ls")
    im.alpha_composite(soft.filter(ImageFilter.GaussianBlur(5)))
    hard = Image.new("RGBA", (W, H))
    ImageDraw.Draw(hard).text((x + 3, y + 4), title, font=f, fill=(24, 10, 52, 235), anchor="ls")
    im.alpha_composite(hard.filter(ImageFilter.GaussianBlur(1)))
    d.text((x, y), title, font=f, fill=(240, 238, 248, 255), anchor="ls")
    control_badge(im, bx, y - 22, 21, "C" if left else "M")
    return im


def flag(d, x, y, country):
    w, h = 54, 36
    if country == "fr":
        for i, c in enumerate(((0, 85, 164), (255, 255, 255), (239, 65, 53))):
            d.rectangle((x + i * w / 3, y, x + (i + 1) * w / 3, y + h), fill=c + (255,))
    else:
        d.rectangle((x, y, x + w, y + h), fill=WHITE)
        d.ellipse((x + w / 2 - 10, y + h / 2 - 10, x + w / 2 + 10, y + h / 2 + 10), fill=(188, 0, 45, 255))
    d.rectangle((x, y, x + w, y + h), outline=(30, 30, 30, 255), width=1)


RANKS = {
    "ULTIMATE": ([(255, 240, 248), (255, 140, 185), (200, 20, 80), (255, 205, 225)], (255, 70, 150)),
    "GRAND": ([(255, 252, 215), (255, 215, 60), (200, 120, 0), (255, 240, 150)], (255, 185, 30)),
}
MASTER_STOPS = [(235, 255, 250), (110, 235, 205), (10, 130, 120), (185, 255, 235)]


def chrome_text(canvas, text, f, xy, stops, edge=(22, 18, 34), stroke=5):
    """Text with a chrome gradient: light, then a hard horizon at the middle, then light again."""
    size = canvas.size
    d = ImageDraw.Draw(canvas)
    d.text(xy, text, font=f, fill=edge + (255,), anchor="mm", stroke_width=stroke, stroke_fill=edge + (255,))
    inner = Image.new("L", size)
    ImageDraw.Draw(inner).text(xy, text, font=f, fill=255, anchor="mm")
    y0, y1 = inner.getbbox()[1], inner.getbbox()[3]
    grad = Image.new("RGBA", size)
    g = ImageDraw.Draw(grad)
    marks = (0.0, 0.5, 0.53, 1.0)
    for y in range(y0, y1 + 1):
        t = (y - y0) / max(1, y1 - y0)
        k = next(i for i in range(3) if t <= marks[i + 1])
        u = (t - marks[k]) / (marks[k + 1] - marks[k])
        g.line((0, y, size[0], y), fill=tuple(int(a + (b - a) * u) for a, b in zip(stops[k], stops[k + 1])) + (255,))
    layer = Image.new("RGBA", size)
    layer.paste(grad, (0, 0), inner)
    canvas.alpha_composite(layer)


def rank_badge(word, height):
    """A Street Fighter 6 rank emblem, near enough: crown, arch, the rank in chrome over a mint `MASTER`."""
    bw, bh, cx = 560, 280, 280
    stops, halo = RANKS[word]
    im = Image.new("RGBA", (bw, bh))
    h = Image.new("RGBA", (bw, bh))
    ImageDraw.Draw(h).ellipse((cx - 210, 40, cx + 210, 250), fill=halo + (120,))
    im.alpha_composite(h.filter(ImageFilter.GaussianBlur(40)))
    d = ImageDraw.Draw(im)
    d.arc((cx - 150, 52, cx + 150, 352), 180, 360, fill=(20, 18, 30, 255), width=12)
    d.arc((cx - 148, 54, cx + 148, 350), 180, 360, fill=(110, 235, 205, 255), width=7)
    d.arc((cx - 132, 70, cx + 132, 334), 180, 360, fill=(215, 220, 232, 255), width=3)
    crown = [(cx - 40, 74), (cx - 36, 36), (cx - 18, 58), (cx, 18), (cx + 18, 58), (cx + 36, 36), (cx + 40, 74)]
    d.polygon(crown, fill=(228, 232, 242, 255), outline=(20, 18, 30, 255), width=3)
    d.ellipse((cx - 9, 50, cx + 9, 68), fill=(40, 220, 140, 255), outline=(20, 18, 30, 255), width=2)
    chrome_text(im, word, font("DelaGothicOne-Regular.ttf", 64), (cx, 128), stops)
    chrome_text(im, "MASTER", font("DelaGothicOne-Regular.ttf", 54), (cx, 196), MASTER_STOPS)
    for i in range(3):
        y = 236 + i * 6
        d.line((cx - 170, y, cx + 170, y), fill=(200, 205, 220, 255 - i * 60), width=2)
    im = glow(im, 3, 1)
    return im.resize((int(bw * height / bh), height), Image.LANCZOS)


def paste_center(im, badge, cx, top):
    layer = Image.new("RGBA", im.size)
    layer.paste(badge, (int(cx - badge.width / 2), int(top)))
    im.alpha_composite(layer)


def tint(im, dark, light):
    """Map a picture's brightness onto a two-colour ramp, as player-card backgrounds are graded to the card."""
    g = im.convert("L")
    bands = [g.point(lambda v, a=a, b=b: int(a + (b - a) * v / 255)) for a, b in zip(dark, light)]
    return Image.merge("RGB", bands).convert("RGBA")


def cover(im, w, h, cx=0.5, cy=0.5, zoom=1.0):
    """Scale to fill w x h and crop around (cx, cy), as a fraction of the picture."""
    s = max(w / im.width, h / im.height) * zoom
    big = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x = min(max(0, int(big.width * cx - w / 2)), big.width - w)
    y = min(max(0, int(big.height * cy - h / 2)), big.height - h)
    return big.crop((x, y, x + w, y + h))


def petal(size, col):
    """A cherry petal: an almond with a notch at the tip."""
    p = Image.new("RGBA", (size * 4, size * 4))
    d = ImageDraw.Draw(p)
    s = size * 4
    d.ellipse((s * 0.3, 0, s * 0.7, s), fill=col)
    d.polygon([(s * 0.5, s * 0.02), (s * 0.42, -s * 0.05), (s * 0.58, -s * 0.05)], fill=(0, 0, 0, 0))
    d.pieslice((s * 0.4, -s * 0.08, s * 0.6, s * 0.12), 0, 180, fill=(0, 0, 0, 0))
    return p.resize((size, size), Image.LANCZOS)


def wife_bg(w, h):
    """Her own background: her blade over purple, petals falling, for `Steel in Bloom`."""
    base = Image.new("RGBA", (w, h))
    b = ImageDraw.Draw(base)
    for x in range(w):
        t = x / w
        b.line((x, 0, x, h), fill=(int(46 + 90 * t), int(14 + 40 * t), int(86 + 130 * t), 255))
    blade = Image.open(PLATES / "blade-singer.png").convert("RGB")
    blade = tint(blade, (12, 0, 30), (205, 160, 255))
    mask = Image.open(PLATES / "blade-singer.png").convert("L").point(lambda v: min(255, max(0, (168 - v) * 5)))
    blade.putalpha(mask.filter(ImageFilter.GaussianBlur(1)))
    blade = blade.resize((int(w * 0.95), int(w * 0.95 * blade.height / blade.width)), Image.LANCZOS).rotate(8, expand=True)
    base.alpha_composite(blade, (int(w * 0.3), int(h / 2 - blade.height / 2)))
    rng = random.Random(6)
    for _ in range(26):
        pt = petal(rng.randint(14, 30), (255, 190, 235, rng.randint(120, 220))).rotate(rng.randint(0, 359), expand=True)
        base.alpha_composite(pt, (rng.randint(0, w - 30), rng.randint(0, h - 30)))
    return base


def zunda_bg(w, h):
    """Her own background: the zunda mochi of her player name, from the contraband case."""
    case = Image.open(PLATES / "case.png").convert("RGBA")
    mochi = case.crop((240, 320, 1120, 600))
    base = cover(mochi, w, h, 0.5, 0.5, 1.15)
    shade = Image.new("RGBA", (w, h), (20, 70, 16, 70))
    base.alpha_composite(shade)
    return base


def stage_bg(w, h):
    bridge = Image.open(PLATES / "bridge.png").convert("RGBA")
    return cover(bridge, w, h, 0.47, 0.6, 1.35)


def band_poly(part):
    y0, y1 = BAND_Y0, BAND_Y1
    if part == "left":
        return [(BAND_X0, y0), (CARD_L - SLANT, y0), (CARD_L + SLANT, y1), (BAND_X0, y1)]
    if part == "right":
        return [(CARD_R + SLANT, y0), (BAND_X1, y0), (BAND_X1, y1), (CARD_R - SLANT, y1)]
    return [(CARD_L - SLANT, y0 + STAGE_DROP), (CARD_R + SLANT, y0 + STAGE_DROP), (CARD_R - SLANT, y1), (CARD_L + SLANT, y1)]


def fill_poly(im, poly, picture, x0):
    mask = Image.new("L", (W, H))
    ImageDraw.Draw(mask).polygon(poly, fill=255)
    layer = Image.new("RGBA", (W, H))
    layer.paste(picture, (x0, BAND_Y0))
    out = Image.new("RGBA", (W, H))
    out.paste(layer, (0, 0), mask)
    im.alpha_composite(out)


def shade_side(w, h, left, deep):
    """Darker behind the rank and the text, so the picture shows mostly on the inner half."""
    s = Image.new("RGBA", (w, h))
    d = ImageDraw.Draw(s)
    for x in range(w):
        t = x / w if left else 1 - x / w
        d.line((x, 0, x, h), fill=deep + (int(165 - 140 * t),))
    return s


def team_mark(im, cx, cy):
    """The team emblem before the team name, the same for everyone in SteelInBloom: two crossed blades with a petal
    where they meet."""
    k, r = 4, 17
    s = 2 * r * k + 8 * k
    b = Image.new("RGBA", (s, s))
    d = ImageDraw.Draw(b)
    c = s / 2
    d.ellipse((c - r * k, c - r * k, c + r * k, c + r * k), fill=(20, 20, 28, 255), outline=WHITE, width=2 * k)
    r = int(r * 0.78)
    for sign in (1, -1):
        ux, uy = sign * math.cos(math.radians(45)), -math.sin(math.radians(45))
        nx, ny = -uy, ux

        def at(t, n=0.0):
            return (c + (ux * t + nx * n) * r * k, c + (uy * t + ny * n) * r * k)
        blade = [at(-0.4, -0.13), at(0.72, -0.13), at(1.0, 0.0), at(0.72, 0.13), at(-0.4, 0.13)]
        d.polygon(blade, fill=(232, 234, 244, 255), outline=(14, 12, 22, 255), width=k)
        d.line([at(-0.4, -0.3), at(-0.4, 0.3)], fill=(14, 12, 22, 255), width=6 * k)
        d.line([at(-0.4, -0.27), at(-0.4, 0.27)], fill=(214, 180, 90, 255), width=4 * k)
        d.line([at(-0.5), at(-1.0)], fill=(14, 12, 22, 255), width=7 * k)
        d.line([at(-0.53), at(-0.97)], fill=(150, 80, 230, 255), width=5 * k)
    for i in range(5):
        a = math.radians(90 + 72 * i)
        px, py = c + math.cos(a) * r * k * 0.13, c - math.sin(a) * r * k * 0.13
        d.ellipse((px - r * k * 0.12, py - r * k * 0.12, px + r * k * 0.12, py + r * k * 0.12), fill=(255, 150, 210, 255),
                  outline=(14, 12, 22, 255), width=k // 2)
    d.ellipse((c - r * k * 0.06, c - r * k * 0.06, c + r * k * 0.06, c + r * k * 0.06), fill=(255, 226, 120, 255))
    b = b.resize((s // k, s // k), Image.LANCZOS)
    im.alpha_composite(b, (int(cx - b.width / 2), int(cy - b.height / 2)))


def card(im, left, col, deep, picture, country, player, team, comment, mr, lp, rank):
    """A player card as in Street Fighter 6: the player's own background, the rank and points at the outer end,
    then three lines, all left-aligned on both sides: flag, platform and player name; team; title or comment."""
    w = CARD_L + SLANT - BAND_X0 if left else BAND_X1 - CARD_R + SLANT
    x0 = BAND_X0 if left else CARD_R - SLANT
    pic = picture(w, BAND_Y1 - BAND_Y0)
    pic.alpha_composite(shade_side(w, BAND_Y1 - BAND_Y0, left, deep))
    fill_poly(im, band_poly("left" if left else "right"), pic, x0)
    d = ImageDraw.Draw(im)

    bx = BAND_X0 + 112 if left else BAND_X1 - 112
    paste_center(im, rank_badge(rank, 100), bx, BAND_Y0 + 6)
    stats = bold("Oswald[wght].ttf", 26, "Medium")
    d.text((bx, STATS_Y), f"{mr} MR  {lp} LP", font=stats, fill=WHITE,
           anchor="mm", stroke_width=2, stroke_fill=(10, 10, 16, 255))

    fx = BAND_X0 + 232 if left else CARD_R + 60
    y1, y2, y3 = BAND_Y0 + 34, BAND_Y0 + 82, STATS_Y
    flag(d, fx, y1 - 18, country)
    px = fx + 76
    d.ellipse((px - 16, y1 - 16, px + 16, y1 + 16), fill=(20, 20, 28, 255), outline=WHITE, width=2)
    d.text((px, y1), "PC", font=bold("Oswald[wght].ttf", 15), fill=WHITE, anchor="mm")
    latin = all(ord(c) < 0x2000 for c in player)
    pf = bold("Oswald[wght].ttf", 36, "Medium") if latin else font("DelaGothicOne-Regular.ttf", 30)
    d.text((px + 28, y1), player, font=pf, fill=WHITE, anchor="lm", stroke_width=2, stroke_fill=(10, 10, 16, 255))
    team_mark(im, px - 38, y2)
    d.text((px - 12, y2), team, font=stats, fill=WHITE, anchor="lm",
           stroke_width=2, stroke_fill=(10, 10, 16, 255))
    latin = all(ord(c) < 0x2000 for c in comment)
    cf = stats if latin else font("DelaGothicOne-Regular.ttf", 21)
    d.text((px - 12, y3), comment, font=cf, fill=WHITE, anchor="lm",
           stroke_width=2, stroke_fill=(10, 10, 16, 255))


def vs_band():
    """The player cards and the stage along the bottom of the VS screen, as in Street Fighter 6. The stage panel is
    an upside-down trapezoid between the cards, its top a few pixels below theirs."""
    im = Image.new("RGBA", (W, H))
    sw = CARD_R - CARD_L + 2 * SLANT
    stage = stage_bg(sw, BAND_Y1 - BAND_Y0)
    fade = Image.new("RGBA", stage.size)
    fd = ImageDraw.Draw(fade)
    for y in range(stage.height):
        fd.line((0, y, sw, y), fill=(0, 0, 0, int(200 * max(0, (y / stage.height - 0.35) / 0.65) ** 1.4)))
    stage.alpha_composite(fade)
    fill_poly(im, band_poly("stage"), stage, CARD_L - SLANT)
    d = ImageDraw.Draw(im)
    d.text((W / 2, STATS_Y - 4), "Lantern Bridge", font=bold("Oswald[wght].ttf", 36, "Regular"), fill=WHITE,
           anchor="mm", stroke_width=2, stroke_fill=(10, 10, 16, 255))
    card(im, True, SINGER, (30, 6, 56), wife_bg, "fr", "AngryMomochan", "SteelInBloom", "Ramène-toi !",
         2083, 912650, "ULTIMATE")
    card(im, False, RIVAL, (6, 34, 10), zunda_bg, "jp", "ずんだ屋本舗", "SteelInBloom", "よろしくなのだ！",
         1707, 206667, "GRAND")
    return im


FIGHT_FRAME = 68 * 24 + 17
HUD_START = 83 * 24 + 2
HIT = 85 * 24 + 19 - HUD_START
STRIKES = [85 * 24 + 21, 85 * 24 + 23, 86 * 24 + 1]
TRACK_Y, TRACK_H = 58, 34
LEAN = 0.6
TRACK = {True: (250, 855), False: (W - 855, W - 250)}
LIFE = {True: ((240, 185, 255), (125, 45, 215)), False: ((150, 245, 110), (40, 150, 30))}
CHIP = ((255, 110, 100), (190, 25, 35))
DRIVE = (175, 232, 40)


def para(x0, x1, y0, h, left=True):
    """The shape of every gauge in Street Fighter 6: one lean on the left, mirrored on the right."""
    s = h * LEAN * (-1 if left else 1)
    return [(x0 + s, y0), (x1 + s, y0), (x1, y0 + h), (x0, y0 + h)]


def gradient_poly(im, poly, y0, h, top, bottom, alpha=255):
    grad = Image.new("RGBA", (W, H))
    g = ImageDraw.Draw(grad)
    for i in range(h + 1):
        t = i / h
        g.line((0, y0 + i, W, y0 + i), fill=tuple(int(a + (b - a) * t) for a, b in zip(top, bottom)) + (alpha,))
    mask = Image.new("L", (W, H))
    ImageDraw.Draw(mask).polygon(poly, fill=255)
    layer = Image.new("RGBA", (W, H))
    layer.paste(grad, (0, 0), mask)
    im.alpha_composite(layer)


def life_poly(left, frac):
    """What is left of a bar: it drains from its outer end toward the timer."""
    x0, x1 = TRACK[left]
    if left:
        return para(x1 - (x1 - x0) * frac, x1, TRACK_Y, TRACK_H)
    return para(x0, x0 + (x1 - x0) * frac, TRACK_Y, TRACK_H, False)


def gradient_text(text, f, xy, anchor, top, bottom, edge, stroke):
    mask = Image.new("L", (W, H))
    ImageDraw.Draw(mask).text(xy, text, font=f, fill=255, anchor=anchor, stroke_width=stroke)
    box = mask.getbbox()
    out = Image.new("RGBA", (W, H))
    ImageDraw.Draw(out).text(xy, text, font=f, fill=edge + (255,), anchor=anchor, stroke_width=stroke)
    inner = Image.new("L", (W, H))
    ImageDraw.Draw(inner).text(xy, text, font=f, fill=255, anchor=anchor)
    grad = Image.new("RGBA", (W, H))
    g = ImageDraw.Draw(grad)
    for y in range(box[1], box[3] + 1):
        t = (y - box[1]) / max(1, box[3] - box[1])
        g.line((0, y, W, y), fill=tuple(int(a + (b - a) * t) for a, b in zip(top, bottom)) + (255,))
    fill = Image.new("RGBA", (W, H))
    fill.paste(grad, (0, 0), inner)
    out.alpha_composite(fill)
    return out


def static_hud():
    """Everything that does not change during the fight."""
    im = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(im)
    for left, who, player, mr, col, rank in ((True, "WIFE", "AngryMomochan", 2083, SINGER, "ULTIMATE"),
                                             (False, "ZUNDAMON", "ずんだ屋本舗", 1707, RIVAL, "GRAND")):
        x0, x1 = TRACK[left]
        d.polygon(para(x0 - 4, x1 + 4, TRACK_Y - 4, TRACK_H + 8, left), fill=(20, 20, 26, 150))
        d.polygon(para(x0, x1, TRACK_Y, TRACK_H, left), fill=(62, 62, 70, 210))

        plate = para(-40, 300, 8, 36, left) if left else para(W - 300, W + 40, 8, 36, left)
        d.polygon(plate, fill=(8, 8, 14, 215))
        d.polygon(plate, outline=col + (255,), width=2)
        name_f = bold("Oswald[wght].ttf", 30)
        nx = 22 if left else W - 22
        d.text((nx, 26), who, font=name_f, fill=WHITE, anchor="lm" if left else "rm",
               stroke_width=2, stroke_fill=(20, 20, 30, 255))
        bx = nx + d.textlength(who, font=name_f) + 30 if left else nx - d.textlength(who, font=name_f) - 30
        control_badge(im, bx, 26, 18, "C" if left else "M")

        info = bold("Oswald[wght].ttf", 24)
        line = f"{player}" if left else f"{player}"
        ix = 40 if left else W - 40
        d.text((ix, TRACK_Y + TRACK_H + 22), f"{mr} MR", font=info, fill=WHITE, anchor="lm" if left else "rm",
               stroke_width=2, stroke_fill=(20, 20, 30, 255))
        mrw = d.textlength(f"{mr} MR", font=info)
        px = ix + mrw + 26 if left else ix - mrw - 26
        d.ellipse((px - 14, TRACK_Y + TRACK_H + 8, px + 14, TRACK_Y + TRACK_H + 36), fill=(30, 30, 36, 255),
                  outline=WHITE, width=2)
        d.text((px, TRACK_Y + TRACK_H + 22), "PC", font=bold("Oswald[wght].ttf", 13), fill=WHITE, anchor="mm")
        if not left:
            d.text((px - 24, TRACK_Y + TRACK_H + 22), line, font=font("DelaGothicOne-Regular.ttf", 22), fill=WHITE,
                   anchor="rm", stroke_width=2, stroke_fill=(20, 20, 30, 255))
        else:
            d.text((px + 24, TRACK_Y + TRACK_H + 22), line, font=font("DelaGothicOne-Regular.ttf", 22), fill=WHITE,
                   anchor="lm", stroke_width=2, stroke_fill=(20, 20, 30, 255))
        paste_center(im, rank_badge(rank, 88), 120 if left else W - 120, TRACK_Y + TRACK_H + 38)

        seg_w, gap = 46, 6
        span = 6 * seg_w + 5 * gap
        start = x1 - 20 - span if left else x0 + 20
        for i in range(6):
            sx = start + i * (seg_w + gap)
            d.polygon(para(sx, sx + seg_w, TRACK_Y + TRACK_H + 10, 13, left), fill=DRIVE + (255,))
            d.polygon(para(sx, sx + seg_w, TRACK_Y + TRACK_H + 10, 13, left), outline=(40, 60, 10, 255), width=1)

    sup = Image.new("RGBA", (W, H))
    s = ImageDraw.Draw(sup)
    y, h = H - 70, 24
    for left, col in ((True, SINGER), (False, RIVAL)):
        x0, x1 = (150, 400) if left else (W - 400, W - 150)
        gradient_poly(sup, para(x0, x1, y, h, left), y, h, tuple(min(255, c + 70) for c in col), col)
        num = gradient_text("1", bold("Teko[wght].ttf", 110), (95 if left else W - 95, y + 14), "mm",
                            (255, 255, 255), (235, 225, 255), col, 3)
        sup.alpha_composite(num)
    im.alpha_composite(glow(sup, 7, 2))
    return im


def timer(n):
    t = gradient_text(f"{n:02d}", bold("Teko[wght].ttf", 128), (W / 2, 70), "mm",
                      (255, 250, 205), (255, 175, 15), (70, 35, 0), 3)
    return glow(t, 6, 1)


def punish_counter(slide):
    """`PUNISH COUNTER` on the attacker's side, sliding in from the left edge."""
    im = Image.new("RGBA", (W, H))
    band = Image.new("RGBA", (W, H))
    b = ImageDraw.Draw(band)
    y0, y1, x1 = 470, 530, 520
    for i in range(x1):
        t = i / x1
        b.line((i, y0, i, y1), fill=(235, 95, 40, int(230 * (1 - t) ** 0.7)))
    im.alpha_composite(band)
    txt = gradient_text("PUNISH COUNTER", bold("Oswald[wght].ttf", 44), (40, (y0 + y1) / 2), "lm",
                        (255, 255, 255), (255, 225, 200), (90, 20, 0), 2)
    im.alpha_composite(txt)
    return im.transform(im.size, Image.AFFINE, (1, 0, slide, 0, 1, 0))


def hits(n, pop):
    """The combo counter under `PUNISH COUNTER`: a big number and `HITS`, popping in on each hit."""
    im = Image.new("RGBA", (W, H))
    num = gradient_text(str(n), bold("Teko[wght].ttf", 150), (120, 610), "rm",
                        (255, 255, 255), (190, 170, 255), (50, 20, 110), 4)
    word = gradient_text("HIT" if n == 1 else "HITS", bold("Oswald[wght].ttf", 46), (130, 628), "lm",
                         (255, 255, 255), (220, 210, 255), (50, 20, 110), 3)
    im.alpha_composite(num)
    im.alpha_composite(word)
    im = glow(im, 6, 1)
    if pop > 1:
        big = im.resize((int(W * pop), int(H * pop)), Image.BICUBIC)
        cx, cy = 140 * pop - 140, 610 * pop - 610
        im = big.crop((int(cx), int(cy), int(cx) + W, int(cy) + H))
    return im


_STATIC = []


def fight_frame(rival_life, rival_chip, n, counter=None, combo=None):
    if not _STATIC:
        _STATIC.append(static_hud())
    im = _STATIC[0].copy()
    gradient_poly(im, life_poly(True, 1.0), TRACK_Y, TRACK_H, *LIFE[True])
    gradient_poly(im, life_poly(False, rival_chip), TRACK_Y, TRACK_H, *CHIP)
    gradient_poly(im, life_poly(False, rival_life), TRACK_Y, TRACK_H, *LIFE[False])
    for left in (True, False):
        x0, x1 = TRACK[left]
        s = TRACK_H * LEAN * (-1 if left else 1)
        ImageDraw.Draw(im).line((x0 + s, TRACK_Y + 4, x1 + s, TRACK_Y + 4),
                                fill=(255, 255, 255, 70), width=3)
    im.alpha_composite(timer(n))
    if counter is not None:
        im.alpha_composite(punish_counter(counter))
    if combo is not None:
        im.alpha_composite(hits(*combo))
    return im


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def render_fight_chorus1(path, frames=89 * 24 + 9 - HUD_START):
    """The HUD over 24a to 24c (1:23:02 to 1:29:09), one ProRes 4444 clip with alpha.

    Full bars first, so the hit reads as a loss. `PUNISH COUNTER` comes in on the contact in 24b (1:25:19). The blow
    lands as three hits, one on each white strobe frame (1:25:21, 1:25:23, 1:26:01): the bar drops a step on each,
    the combo counter climbs to 3, and the red chip drains after the last.
    """
    import subprocess
    import imageio_ffmpeg

    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
           "-s", f"{W}x{H}", "-r", "24000/1001", "-i", "-", "-c:v", "prores_ks", "-profile:v", "4444",
           "-pix_fmt", "yuva444p10le", "-alpha_bits", "16", str(path)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    steps = [0.14, 0.13, 0.13]
    strikes = [s - HUD_START for s in STRIKES]
    for i in range(frames):
        landed = [k for k, f in enumerate(strikes) if i >= f]
        life = 1 - sum(steps[k] for k in landed)
        chip = 1 - sum(steps) * ease((i - strikes[-1] - 8) / 10)
        combo = None
        if landed and i < strikes[-1] + 36:
            k = landed[-1]
            combo = (k + 1, 1.35 if i == strikes[k] else 1.15 if i == strikes[k] + 1 else 1)
        n = 99 - (HUD_START + i - FIGHT_FRAME) // 24
        counter = None
        if HIT <= i < HIT + 40:
            counter = -600 * (1 - ease((i - HIT) / 3))
        proc.stdin.write(fight_frame(life, chip, n, counter, combo).tobytes())
    proc.stdin.close()
    proc.wait()


BONUS_START = 94 * 24 + 1
BONUS_END = 104 * 24 + 7
BONUS_AWARDS = [(96 * 24 + 6, "PERFECT PARRY", 10000), (99 * 24 + 16, "GANTRY DOWN", 50000),
                (102 * 24 + 11, "CRASH", 30000)]
BONUS_PERFECT = 103 * 24 + 4
GOLD = ((255, 250, 205), (255, 175, 15), (70, 35, 0))
GREEN = ((235, 255, 215), (120, 235, 60), (10, 60, 0))


def popped(im, scale, cx, cy):
    """`im` scaled about (cx, cy), for a pop-in."""
    if scale == 1:
        return im
    big = im.resize((int(W * scale), int(H * scale)), Image.BICUBIC)
    x, y = cx * scale - cx, cy * scale - cy
    return big.crop((int(x), int(y), int(x) + W, int(y) + H))


def faded(im, alpha):
    if alpha >= 1:
        return im
    a = im.getchannel("A").point(lambda v: int(v * max(0.0, alpha)))
    out = im.copy()
    out.putalpha(a)
    return out


def bonus_title():
    """`BONUS STAGE`, in the rival's green, high in the frame so it clears 25b's gun."""
    t = gradient_text("BONUS STAGE", oxanium(150), (W / 2, 250), "mm", *GREEN, 5)
    return glow(t, 10, 2)


def bonus_score(score):
    """P2's score, top right, the rival's side: the stage is hers."""
    im = Image.new("RGBA", (W, H))
    im.alpha_composite(gradient_text("P2", bold("Oswald[wght].ttf", 40), (W - 110, 70), "rm", *GREEN, 2))
    im.alpha_composite(gradient_text(f"{score:06d}", bold("Teko[wght].ttf", 96), (W - 130, 150), "rm",
                                     (255, 255, 255), (220, 255, 200), (10, 60, 0), 3))
    return glow(im, 6, 1)


def bonus_award(label, points, slide):
    """An award on the rival's side, sliding in from the right edge as `PUNISH COUNTER` does on the singer's."""
    im = Image.new("RGBA", (W, H))
    band = Image.new("RGBA", (W, H))
    b = ImageDraw.Draw(band)
    y0, y1, w = 470, 530, 560
    for i in range(w):
        t = i / w
        b.line((W - 1 - i, y0, W - 1 - i, y1), fill=(60, 170, 30, int(230 * (1 - t) ** 0.7)))
    im.alpha_composite(band)
    im.alpha_composite(gradient_text(label, bold("Oswald[wght].ttf", 44), (W - 40, (y0 + y1) / 2), "rm",
                                     (255, 255, 255), (225, 255, 210), (10, 60, 0), 2))
    im.alpha_composite(glow(gradient_text(f"+{points}", bold("Teko[wght].ttf", 110), (W - 40, 600), "rm", *GOLD, 3),
                            6, 1))
    return im.transform(im.size, Image.AFFINE, (1, 0, -slide, 0, 1, 0))


def bonus_perfect(total):
    """`PERFECT` and the total, high in the frame, clear of the tail light shrinking in the middle of 25h."""
    im = Image.new("RGBA", (W, H))
    im.alpha_composite(gradient_text("PERFECT", oxanium(200), (W / 2, 270), "mm", *GOLD, 6))
    im.alpha_composite(gradient_text(f"BONUS {total}", bold("Teko[wght].ttf", 110), (W / 2, 410), "mm",
                                     (255, 255, 255), (220, 255, 200), (10, 60, 0), 3))
    return glow(im, 10, 2)


def bonus_frame(f):
    """The bonus-stage HUD at timeline frame `f`."""
    im = Image.new("RGBA", (W, H))
    shown = 0
    for at, _, points in BONUS_AWARDS:
        shown += points * ease((f - at - 2) / 12)
    im.alpha_composite(bonus_score(int(round(shown / 10)) * 10))
    n = 30 - (min(f, BONUS_PERFECT) - BONUS_START) // 24
    im.alpha_composite(timer(n))
    i = f - BONUS_START
    if i < 30:
        pop = 1.4 if i == 0 else 1.2 if i == 1 else 1.08 if i == 2 else 1
        im.alpha_composite(faded(popped(bonus_title(), pop, W / 2, 250), 1 - (i - 24) / 6))
    for at, label, points in BONUS_AWARDS:
        k = f - at
        if 0 <= k < 30 and f < BONUS_PERFECT:
            im.alpha_composite(faded(bonus_award(label, points, -620 * (1 - ease(k / 3))), 1 - (k - 24) / 6))
    k = f - BONUS_PERFECT
    if k >= 0:
        pop = 1.4 if k == 0 else 1.2 if k == 1 else 1.08 if k == 2 else 1
        im.alpha_composite(popped(bonus_perfect(sum(p for *_, p in BONUS_AWARDS)), pop, W / 2, 270))
    return im


def render_bonus_stage(path):
    """The rival's bonus stage over the chase, 25b to 25h (1:34:01 to 1:44:07), one ProRes 4444 clip with alpha.

    `BONUS STAGE` pops in on the cut to 25b and clears after a second; the stage timer counts down from 30 and P2's
    score rolls up on each award: `PERFECT PARRY` on the parry in 25d (1:36:06), the gantry on its biggest burst of
    sparks in 25e (1:39:16), the singer's crash as her sparks stop in 25g (1:42:11). `PERFECT` and the total over the
    tail light in 25h (1:43:04), the timer stopping there.
    """
    import subprocess
    import imageio_ffmpeg

    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
           "-s", f"{W}x{H}", "-r", "24000/1001", "-i", "-", "-c:v", "prores_ks", "-profile:v", "4444",
           "-pix_fmt", "yuva444p10le", "-alpha_bits", "16", str(path)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(BONUS_START, BONUS_END):
        proc.stdin.write(bonus_frame(f).tobytes())
    proc.stdin.close()
    proc.wait()


OUT.mkdir(parents=True, exist_ok=True)
if sys.argv[2:] == ["bonus"]:
    render_bonus_stage(OUT / "hud-bonus-stage.mov")
    sys.exit()
neon_vs().save(OUT / "hud-vs.png")
vs_frame().save(OUT / "hud-vs-frame.png")
name("WIFE", True).save(OUT / "hud-name-wife.png")
name("ZUNDAMON", False).save(OUT / "hud-name-zundamon.png")
vs_band().save(OUT / "hud-vs-band.png")
round_title(1).save(OUT / "hud-round1.png")
fight_frame(1.0, 1.0, 99).save(OUT / "hud-fight.png")
render_fight_chorus1(OUT / "hud-fight-chorus1.mov")
render_bonus_stage(OUT / "hud-bonus-stage.mov")
