"""seed_demo.py — a TOY image generator (not Midjourney) that shows what a seed does.

Midjourney: every image starts from random noise, and the seed picks which noise.
This toy does the same two steps in miniature, with no AI model:
  1. noise = random numbers from a generator started with `seed` (NumPy PCG64)
  2. "generate" = smooth the noise at a few scales (the LAYOUT comes from the noise),
     then colour it with a palette chosen by the prompt's words (the prompt sets the LOOK).
It measures: same seed twice -> identical? four random seeds -> how different?
same seed, one prompt word changed -> same layout, new colours?
Writes seed_output.json and PNGs used by the video.
"""
import json
import numpy as np
from PIL import Image, ImageFilter

SIZE = 256
PALETTES = {  # prompt word -> sky top, sky bottom, sun, far hills, near hills
    "sunset": [(70, 48, 96), (240, 170, 120), (255, 226, 160), (150, 82, 92), (60, 36, 58)],
    "forest": [(150, 196, 214), (226, 236, 214), (255, 250, 220), (96, 140, 98), (34, 72, 46)],
}


def noise(seed):
    return np.random.default_rng(seed).random((SIZE, SIZE))


def ridge(row, scales=((40, 0.7), (12, 0.25), (3, 0.05))):
    """Smooth one row of noise into a hill line (0..1)."""
    out = np.zeros(SIZE)
    for r, w in scales:
        k = np.exp(-0.5 * (np.arange(-3 * r, 3 * r + 1) / r) ** 2); k /= k.sum()
        out += w * np.convolve(np.pad(row, 3 * r, mode="wrap"), k, mode="same")[3 * r:-3 * r]
    return (out - out.min()) / (out.max() - out.min() + 1e-9)


def generate(prompt, seed):
    """Toy generator: the seed's noise sets the LAYOUT (hills, sun); the prompt word sets the LOOK."""
    n = noise(seed)
    sun_x, sun_y = 40 + n[0, 0] * 176, 50 + n[0, 1] * 60
    far = 120 + ridge(n[10]) * 70
    near = 165 + ridge(n[20]) * 70
    layout = np.zeros((SIZE, SIZE), dtype=np.uint8)  # 0 sky, 1 sun, 2 far hill, 3 near hill
    yy, xx = np.mgrid[0:SIZE, 0:SIZE]
    layout[(xx - sun_x) ** 2 + (yy - sun_y) ** 2 < 22 ** 2] = 1
    layout[yy > far[None, :]] = 2
    layout[yy > near[None, :]] = 3
    word = next(k for k in PALETTES if k in prompt)
    top, bot, sun, c_far, c_near = (np.array(c, dtype=float) for c in PALETTES[word])
    t = (yy / SIZE)[..., None]
    rgb = top + (bot - top) * t
    for code, col in ((1, sun), (2, c_far), (3, c_near)):
        rgb[layout == code] = col
    return layout, rgb.astype(np.uint8)


def save(rgb, name):
    Image.fromarray(rgb).resize((512, 512), Image.NEAREST).save(name)


P = "a sunset over hills"
out = {"prompt": P, "toy": True, "rng": "numpy PCG64", "size": SIZE}

# noise itself
n42a, n42b, n43 = noise(42), noise(42), noise(43)
out["noise_seed42_twice_identical"] = bool(np.array_equal(n42a, n42b))
out["noise_seed42_vs_43_identical"] = bool(np.array_equal(n42a, n43))
Image.fromarray((n42a * 255).astype(np.uint8)).resize((512, 512), Image.NEAREST).save("noise_42.png")
out["noise_42_first_values"] = [round(float(v), 4) for v in n42a[0, :4]]

# 1. no seed chosen -> four random seeds (like one Midjourney job)
seeds4 = [int(s) for s in np.random.default_rng(2026).integers(0, 2**32, 4)]
out["four_random_seeds"] = seeds4
lays = []
for i, s in enumerate(seeds4):
    lay, rgb = generate(P, s)
    lays.append(lay)
    save(rgb, f"four_{i}.png")
diffs = [float((lays[i] != lays[j]).mean()) for i in range(4) for j in range(i + 1, 4)]
out["four_share_of_pixels_different"] = round(sum(diffs) / len(diffs), 3)

# 2. same seed twice -> identical
la, a = generate(P, 1234)
lb, b = generate(P, 1234)
save(a, "seed1234_a.png"); save(b, "seed1234_b.png")
out["seed1234_twice_identical_pixels"] = bool(np.array_equal(a, b))
out["seed1234_twice_mean_difference"] = float(np.abs(a.astype(int) - b.astype(int)).mean())

# 3. same seed, one word changed -> same layout, new colours
P2 = "a forest over hills"
lc, c = generate(P2, 1234)
save(c, "seed1234_forest.png")
out["prompt2"] = P2
out["layout_same_after_word_change"] = bool(np.array_equal(la, lc))
out["colours_changed_after_word_change"] = bool(not np.array_equal(a, c))
json.dump(out, open("seed_output.json", "w"), indent=2)
print(json.dumps(out, indent=2))

# --- for the video: the starting noise of each of the four, and "four more" from new random seeds ---
for i, s in enumerate(seeds4):
    Image.fromarray((noise(s) * 255).astype(np.uint8)).resize((512, 512), Image.NEAREST).save(f"noise_four_{i}.png")
seeds_more = [int(s) for s in np.random.default_rng(2027).integers(0, 2**32, 4)]
for i, s in enumerate(seeds_more):
    save(generate(P, s)[1], f"more_{i}.png")
out["four_more_seeds"] = seeds_more
json.dump(out, open("seed_output.json", "w"), indent=2)
