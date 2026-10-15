"""Shift a plate's hair to the hue, saturation and value of another plate's hair.

    python match_hair_hue.py <plate> <reference> <out> [lo hi]

The hair is every saturated pixel whose hue lies in [lo, hi] degrees (default 45-140,
the yellow-green to green band). The plate must have nothing else in that band.
"""
import sys

import numpy as np
from PIL import Image


def hair(hsv, lo, hi):
    h = hsv[..., 0] * 360 / 255
    return (h > lo) & (h < hi) & (hsv[..., 1] > 40) & (hsv[..., 2] > 40)


def main():
    plate, ref, out = sys.argv[1:4]
    lo, hi = (float(v) for v in sys.argv[4:6]) if len(sys.argv) > 5 else (45, 140)

    src = Image.open(plate).convert("RGBA")
    hsv = np.asarray(src.convert("RGB").convert("HSV")).astype(float)
    rhsv = np.asarray(Image.open(ref).convert("RGB").convert("HSV")).astype(float)
    m, rm = hair(hsv, lo, hi), hair(rhsv, lo, hi)

    dh = np.median(rhsv[rm][:, 0]) - np.median(hsv[m][:, 0])
    ks = np.median(rhsv[rm][:, 1]) / np.median(hsv[m][:, 1])
    kv = np.median(rhsv[rm][:, 2]) / np.median(hsv[m][:, 2])

    res = hsv.copy()
    res[..., 0][m] = (hsv[..., 0][m] + dh) % 256
    res[..., 1][m] = np.clip(hsv[..., 1][m] * ks, 0, 255)
    res[..., 2][m] = np.clip(hsv[..., 2][m] * kv, 0, 255)

    rgb = Image.fromarray(res.astype(np.uint8), "HSV").convert("RGB")
    rgb.putalpha(src.getchannel("A"))
    rgb.save(out)
    print(f"{m.sum()} px, hue {dh * 360 / 255:+.0f} deg, sat x{ks:.2f}, val x{kv:.2f}")


if __name__ == "__main__":
    main()
