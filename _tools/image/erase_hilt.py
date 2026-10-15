"""Erase a katana hilt and guard that stand out against a plain background.

The hilt is a capsule from `top` to `guard`; the guard a rotated box at `guard`.
Masked pixels take the median background of the same row, sampled on `side`.
The scabbard is then cut square at `--cut` px past the guard along the hilt's
axis and capped with the oval of its open mouth.
"""
import argparse

import numpy as np
from PIL import Image


def capsule(h, w, a, b, r):
    yy, xx = np.mgrid[0:h, 0:w]
    a, b = np.array(a, float), np.array(b, float)
    ab = b - a
    t = np.clip(((xx - a[0]) * ab[0] + (yy - a[1]) * ab[1]) / (ab @ ab), 0, 1)
    dx, dy = xx - (a[0] + t * ab[0]), yy - (a[1] + t * ab[1])
    return dx * dx + dy * dy <= r * r


def box(h, w, c, u, half_u, half_p):
    yy, xx = np.mgrid[0:h, 0:w]
    p = np.array([u[1], -u[0]])
    dx, dy = xx - c[0], yy - c[1]
    return (np.abs(dx * u[0] + dy * u[1]) <= half_u) & (np.abs(dx * p[0] + dy * p[1]) <= half_p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--top", type=float, nargs=2, required=True)
    ap.add_argument("--guard", type=float, nargs=2, required=True)
    ap.add_argument("--radius", type=float, default=18)
    ap.add_argument("--guard-half", type=float, nargs=2, default=(9, 30), help="half thickness, half width")
    ap.add_argument("--side", choices=["left", "right"], required=True)
    ap.add_argument("--cut", type=float, default=14, help="px past the guard where the scabbard ends")
    ap.add_argument("--half-width", type=float, default=16, help="half the scabbard's width")
    a = ap.parse_args()

    img = np.asarray(Image.open(a.src).convert("RGB")).astype(float)
    h, w, _ = img.shape
    u = np.array(a.guard) - np.array(a.top)
    u /= np.linalg.norm(u)
    mask = capsule(h, w, a.top, a.guard, a.radius) | box(h, w, a.guard, u, *a.guard_half)

    yy, xx = np.mgrid[0:h, 0:w]
    pv = np.array([u[1], -u[0]])
    su = (xx - a.guard[0]) * u[0] + (yy - a.guard[1]) * u[1]
    sp = (xx - a.guard[0]) * pv[0] + (yy - a.guard[1]) * pv[1]
    stub = (su < a.cut) & (su > -40) & (np.abs(sp) < a.half_width + 6) & (img.mean(2) < 140)
    mask |= stub

    out = img.copy()
    for y in np.where(mask.any(1))[0]:
        xs = np.where(mask[y])[0]
        lo, hi = (xs.min() - 45, xs.min() - 4) if a.side == "left" else (xs.max() + 4, xs.max() + 45)
        sample = img[y, max(lo, 0):min(hi, w)]
        sample = sample[sample.mean(1) > 170]
        if len(sample):
            out[y, xs] = np.median(sample, 0)
    hw, depth = a.half_width, a.half_width * 0.35
    e = ((su - a.cut) / depth) ** 2 + (sp / hw) ** 2
    out[e <= 1] = (62, 66, 74)
    out[e <= 0.55] = (8, 8, 10)
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(a.dst)


if __name__ == "__main__":
    main()
