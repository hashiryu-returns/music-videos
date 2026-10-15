"""The character select screen of 0006 (shot 4) as a 16-bit arcade screen, 1920x1080 PNGs.

Everything is drawn on a 320x180 canvas and scaled up 6x with no smoothing, so every pixel is a real one.
Each state is a full frame: they go on the timeline one after another, nothing to position.
The portraits are sprites made from the face plates: cut off their grey backdrop, shrunk to the card,
cut to a small palette, with dark pixel outlines on the strong edges and round the silhouette.

    pixel_select.py <out dir>
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

LW, LH, S = 320, 180, 6
ROOT = Path(__file__).resolve().parents[2]
FONT = ImageFont.truetype(str(ROOT / "_tools/fonts/PressStart2P-Regular.ttf"), 8)
PLATES = ROOT / "0006-en-steel-in-bloom/characters"
OUT = Path(sys.argv[1])

WHITE, BLACK, GREY = (255, 255, 255), (0, 0, 0), (150, 150, 165)
PURPLE, GREEN, RED = (200, 120, 255), (130, 240, 70), (255, 50, 50)
CW, CH, CY = 72, 90, 26
CX = {"singer": 36, "rival": 124, "master": 212}
COLOUR = {"singer": PURPLE, "rival": GREEN, "master": RED}
CARD_BG = {"singer": (70, 30, 110), "rival": (25, 80, 30), "master": (60, 60, 70)}
TITLE = {"singer": "AGENT", "rival": "SMUGGLER", "master": "???"}
STATS = {"singer": (4, 5, 0), "rival": (5, 4, 5)}
PANEL = (36, 128, 284, 174)
ROW_Y = (139, 151, 163)
STAT_X, STAR_X = 96, 144

# Clothes as light as the plate's grey backdrop, which no colour test can tell apart: polygons on the plate.
CLOTHES = {
    "singer": [
        [(0, 700), (170, 674), (300, 630), (330, 602), (350, 604), (330, 1344), (0, 1344)],
        [(530, 565), (590, 600), (725, 650), (896, 660), (896, 1344), (550, 1344), (540, 630)],
    ],
}

STAR = ["...#...", "...#...", "..###..", "#######", ".#####.", ".##.##.", "#.....#"]


def fill_holes(mask):
    """Backdrop that can't be reached from the card's edge is a light patch inside her: hers."""
    h, w = mask.shape
    outside = np.zeros_like(mask)
    todo = [(y, x) for y in range(h) for x in (0, w - 1)] + [(y, x) for x in range(w) for y in (0, h - 1)]
    while todo:
        y, x = todo.pop()
        if 0 <= y < h and 0 <= x < w and not mask[y, x] and not outside[y, x]:
            outside[y, x] = True
            todo += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return ~outside


def clean_rim(px, body, worn, depth=2):
    """Light pixels just inside the outline are backdrop blended into thin hair: they take the colour inside."""
    inner = body.copy()
    for _ in range(depth):
        inner &= np.roll(inner, 1, 0) & np.roll(inner, -1, 0) & np.roll(inner, 1, 1) & np.roll(inner, -1, 1)
    ring = body & ~inner & ~worn & (px @ [0.3, 0.59, 0.11] > 140)
    out = px.copy()
    for y, x in zip(*np.nonzero(ring)):
        win = (slice(max(y - 3, 0), y + 4), slice(max(x - 3, 0), x + 4))
        near = px[win][inner[win]]
        if len(near):
            out[y, x] = near[np.argsort(near @ [0.3, 0.59, 0.11])[len(near) // 2]]
    return out


def sprite(who, size):
    """The face plate as a pixel portrait: head and shoulders, on a card background in her colour."""
    im = Image.open(PLATES / f"{who}-face.png").convert("RGB")
    w, h = im.size
    clothes = Image.new("L", im.size, 0)
    for poly in CLOTHES.get(who, []):
        ImageDraw.Draw(clothes).polygon(poly, fill=255)
    cw = int(w * 0.62)
    ch = int(cw * size[1] / size[0])
    x0, y0 = (w - cw) // 2, int(h * 0.03)
    box = (x0, y0, x0 + cw, y0 + ch)
    big = (size[0] * 8, size[1] * 8)
    im = im.crop(box).resize(big, Image.LANCZOS)
    a = np.asarray(im).astype(int)
    backdrop = np.median(np.concatenate([a[:20, :20].reshape(-1, 3), a[:20, -20:].reshape(-1, 3)]), axis=0)
    person = (np.abs(a - backdrop).sum(2) > 40) | (np.asarray(clothes.crop(box).resize(big)) > 127)
    body = np.asarray(Image.fromarray(person.astype(np.uint8) * 255).resize(size, Image.BOX)) > 150
    body &= np.roll(body, 1, 0) | np.roll(body, -1, 0) | np.roll(body, 1, 1) | np.roll(body, -1, 1)
    body = fill_holes(body)
    src = np.asarray(im.resize(size, Image.BOX)).astype(int)
    worn = np.asarray(clothes.crop(box).resize(size, Image.BOX)) > 127
    for _ in range(3):
        edge_px = body & ~(np.roll(body, 1, 0) & np.roll(body, -1, 0) & np.roll(body, 1, 1) & np.roll(body, -1, 1))
        body &= ~(edge_px & ~worn & (np.abs(src - backdrop).sum(2) < 90))
    im = ImageEnhance.Color(ImageEnhance.Contrast(im).enhance(1.25)).enhance(1.35).filter(ImageFilter.ModeFilter(5))
    px = np.asarray(im.resize(size, Image.BOX).quantize(22, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")).astype(int)
    px = clean_rim(px, body, worn)
    lum = px @ [0.3, 0.59, 0.11]
    edge = np.zeros(lum.shape, bool)
    for dy, dx in ((0, 1), (1, 0)):
        edge |= np.abs(lum - np.roll(np.roll(lum, dy, 0), dx, 1)) > 95
    px[edge & body] = (px[edge & body] * 0.45).astype(int)
    rim = body & ~(np.roll(body, 1, 0) & np.roll(body, -1, 0) & np.roll(body, 1, 1) & np.roll(body, -1, 1))
    shade = 0.55 + 0.6 * (np.arange(size[1]) / size[1])
    bg = (np.array(CARD_BG[who])[None, None, :] * shade[:, None, None]).repeat(size[0], 1)
    bg[::4] *= 0.8
    out = np.where(body[..., None], px, bg)
    out[rim] = (10, 8, 16)
    return Image.fromarray(out.clip(0, 255).astype(np.uint8))


def backdrop():
    im = Image.open(PLATES / "rooftop.png").convert("RGB")
    im = ImageOps.fit(im, (LW, LH), Image.BOX)
    im = im.quantize(24, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")
    return ImageEnhance.Brightness(im).enhance(0.45)


def text(d, xy, s, fill, anchor="la", shadow=True):
    if shadow:
        d.text((xy[0] + 1, xy[1] + 1), s, font=FONT, fill=BLACK, anchor=anchor)
    d.text(xy, s, font=FONT, fill=fill, anchor=anchor)


def star(d, x, y, fill):
    for j, row in enumerate(STAR):
        for i, c in enumerate(row):
            if c == "#":
                d.point((x + i, y + j), fill=fill)


def base():
    im = backdrop()
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, LW, 16), fill=(10, 8, 24))
    text(d, (LW // 2, 5), "SELECT YOUR FIGHTER", WHITE, "ma")
    for who in ("singer", "rival", "master"):
        x = CX[who]
        face = sprite(who, (CW - 4, CH - 4))
        if who == "master":
            face = ImageEnhance.Brightness(ImageOps.grayscale(face).convert("RGB")).enhance(0.22)
        d.rectangle((x, CY, x + CW - 1, CY + CH - 1), fill=BLACK)
        im.paste(face, (x + 2, CY + 2))
        d.rectangle((x, CY, x + CW - 1, CY + CH - 1), outline=GREY)
        if who == "master":
            text(d, (x + CW // 2, CY + CH // 2 - 4), "???", RED, "ma")
    d.rectangle(PANEL, fill=(8, 6, 18), outline=GREY)
    return im


def cursor(im, who, tag, colour):
    d = ImageDraw.Draw(im)
    x = CX[who]
    for k in (0, 1):
        d.rectangle((x - 1 - k, CY - 1 - k, x + CW + k, CY + CH + k), outline=colour)
    w = 18
    d.rectangle((x + CW // 2 - w // 2, CY - 11, x + CW // 2 + w // 2, CY - 3), fill=colour)
    d.polygon([(x + CW // 2 - 3, CY - 3), (x + CW // 2 + 3, CY - 3), (x + CW // 2, CY)], fill=colour)
    text(d, (x + CW // 2 + 1, CY - 10), tag, BLACK, "ma", shadow=False)


def panel(im, who, rows):
    d = ImageDraw.Draw(im)
    x0, y0 = PANEL[0] + 6, PANEL[1] + 4
    text(d, (x0, y0), TITLE[who], COLOUR[who])
    if who == "master":
        text(d, (PANEL[2] - 6, y0 + 20), "LOCKED", RED, "ra")
        return
    for r in range(rows):
        y = ROW_Y[r]
        text(d, (x0 + STAT_X, y - 1), ("SPEED", "POWER", "ZUNDA")[r], GREY)
        n = STATS[who][r]
        for i in range(5):
            star(d, x0 + STAR_X + i * 9, y - 1, COLOUR[who] if i < n else (60, 60, 70))


def overflow():
    """The rival's ZUNDA row past five stars, off the right edge. Revealed in FCP by Crop Right."""
    im = Image.new("RGBA", (LW, LH))
    d = ImageDraw.Draw(im)
    x = PANEL[0] + 6 + STAR_X + 5 * 9
    while x < LW + 9:
        star(d, x, ROW_Y[2] - 1, GREEN + (255,))
        x += 9
    return im


def save(im, name):
    big = im.resize((LW * S, LH * S), Image.NEAREST)
    if big.mode == "RGB":
        lines = Image.new("L", big.size, 255)
        d = ImageDraw.Draw(lines)
        for y in range(S - 2, big.size[1], S):
            d.rectangle((0, y, big.size[0], y + 1), fill=185)
        big = Image.composite(big, Image.new("RGB", big.size, BLACK), lines)
    big.save(OUT / name)


OUT.mkdir(parents=True, exist_ok=True)
save(base(), "px-00-screen.png")
n = 1
for who, tag, colour in (("singer", "P1", PURPLE), ("master", "P2", GREEN), ("rival", "P2", GREEN)):
    for rows in ((0, 1, 2, 3) if who != "master" else (0,)):
        im = base()
        cursor(im, who, tag, RED if who == "master" else colour)
        panel(im, who, rows)
        save(im, f"px-{n:02d}-{who}-{rows}.png")
        n += 1
save(overflow(), "px-zunda-overflow.png")
mission = Image.new("RGB", (LW, LH), BLACK)
text(ImageDraw.Draw(mission), (LW // 2, LH // 2 - 4), "MISSION START", WHITE, "ma")
save(mission, "px-mission-start.png")
