#!/usr/bin/env python3
"""gen_mars.py — every plate used by the mars-rover-autonomy reel, generated.

Nothing here is downloaded, licensed, or lifted from a NASA image. Every plate
is a SYNTHETIC depiction built from a seeded procedural terrain, rendered the
way a rover navigation camera would see it (monochrome, low sun, hard shadows —
Navcam and Hazcam really are greyscale instruments, so a mono plate is the
honest depiction, not a stylisation).

    python assets/gen_mars.py

Deterministic: same seeds in, byte-identical PNGs out. Seeds are logged in
SOURCES.md.

WHY THESE ARE DARK PLATES, NOT LINE PLOTS
  Ep. 05 lost two GATE V passes to `low-contrast` because its neutral,
  near-white plot noise counted as "ink" against a warm cream page. Ep. 04's
  dark photographic plates never had the problem. These are dark plates: the
  terrain occupies the lower half of the value range, so mean ink luminance
  sits far below the page and the separation check is never close.

WHAT EACH PLATE IS
  navcam            what the rover sees: shaded terrain, rocks, low sun
  costmap           the same terrain reduced to a per-cell traversability cost
  pathfan           the cost map with ~1700 candidate arcs; the chosen one lit
  rockfield         a closer scene, for the science-targeting half
  rockfield_edges   Rockster-style closed contours around each detected object
  rockfield_ranked  the same contours, scored, with the winner ringed
  route             top-down: the straight line the planner wanted, and the
                    longer line the rover actually drove
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent / "plots"
OUT.mkdir(parents=True, exist_ok=True)

# Claude fidelity accent, for the one marked thing per plate.
TERRA = (217, 119, 87)
TERRA_D = (164, 74, 50)
PAGE = (255, 255, 255)


# ── procedural terrain ───────────────────────────────────────────────────────

def _value_noise(w, h, cells, rng):
    """One octave of smooth value noise on a (cells x cells) lattice."""
    g = rng.random((cells + 1, cells + 1))
    ys = np.linspace(0, cells, h, endpoint=False)
    xs = np.linspace(0, cells, w, endpoint=False)
    y0 = np.floor(ys).astype(int)
    x0 = np.floor(xs).astype(int)
    fy = (ys - y0)[:, None]
    fx = (xs - x0)[None, :]
    # smoothstep so the octaves do not read as a grid
    fy = fy * fy * (3 - 2 * fy)
    fx = fx * fx * (3 - 2 * fx)
    g00 = g[np.ix_(y0, x0)]
    g10 = g[np.ix_(y0 + 1, x0)]
    g01 = g[np.ix_(y0, x0 + 1)]
    g11 = g[np.ix_(y0 + 1, x0 + 1)]
    top = g00 * (1 - fx) + g01 * fx
    bot = g10 * (1 - fx) + g11 * fx
    return top * (1 - fy) + bot * fy


def _fbm(w, h, rng, octaves=5, base=3, gain=0.5):
    out = np.zeros((h, w))
    amp, cells, norm = 1.0, base, 0.0
    for _ in range(octaves):
        out += amp * _value_noise(w, h, cells, rng)
        norm += amp
        amp *= gain
        cells *= 2
    return out / norm


def _rocks(rng, n, w, h, rmin, rmax, y_bias=0.0, ytop=0.30, yspan=0.68):
    """Scattered rocks as (cx, cy, r, height). y_bias > 0 pushes them low in
    frame, which is where a forward-looking camera sees the near ground."""
    out = []
    for _ in range(n):
        cx = rng.uniform(0.03, 0.97) * w
        u = rng.random()
        if y_bias:
            u = u ** (1.0 / (1.0 + y_bias))
        cy = (ytop + yspan * u) * h
        # perspective: nearer (lower in frame) rocks read bigger
        scale = 0.45 + 1.25 * (cy / h)
        r = rng.uniform(rmin, rmax) * scale
        lobes = rng.uniform(-0.26, 0.26, 4)
        out.append((cx, cy, r, rng.uniform(0.70, 1.25), lobes))
    return out


def _emboss(field, rocks, w, h):
    """Add each rock to the height field as a smooth cap."""
    ys, xs = np.mgrid[0:h, 0:w]
    for cx, cy, r, hh, lobes in rocks:
        dx = (xs - cx) / r
        dy = (ys - cy) / (r * 0.62)
        th = np.arctan2(dy, dx)
        wob = (1.0 + lobes[0] * np.sin(th) + lobes[1] * np.cos(2 * th)
               + lobes[2] * np.sin(3 * th) + lobes[3] * np.cos(4 * th))
        d = np.sqrt(dx * dx + dy * dy) / np.clip(wob, 0.55, 1.6)
        cap = np.clip(1.0 - d ** 2, 0.0, None)
        field = field + hh * cap ** 0.62
    return field


def _shadow(field, sun=(-1.0, -0.58), rise=0.020, steps=110):
    """Hard cast shadows from a low sun, by marching the height field along the
    sun vector. A rover navcam at a Martian morning has exactly this look, and
    the shadows are what make a rock read as an obstacle rather than a smudge."""
    sx, sy = sun
    n = math.hypot(sx, sy) or 1.0
    sx, sy = sx / n, sy / n
    horizon = np.full_like(field, -1e9)
    for t in range(1, steps + 1):
        dx, dy = int(round(sx * t)), int(round(sy * t))
        shifted = np.roll(np.roll(field, -dy, axis=0), -dx, axis=1)
        horizon = np.maximum(horizon, shifted - rise * t)
    return (field >= horizon - 1e-6).astype(np.float64)


def _shade(field, sun=(-0.72, -0.42), strength=16.0, ambient=0.30):
    """Lambertian shading from a low sun, multiplied by the cast-shadow mask."""
    gy, gx = np.gradient(field)
    nx, ny, nz = -gx * strength, -gy * strength, 1.0
    n = np.sqrt(nx * nx + ny * ny + nz * nz)
    lx, ly, lz = sun[0], sun[1], 0.40
    ln = math.sqrt(lx * lx + ly * ly + lz * lz)
    lam = np.clip((nx * lx + ny * ly + nz * lz) / (n * ln), 0, 1)
    lit = _shadow(field, sun=(sun[0], sun[1]))
    return np.clip(ambient + (1.0 - ambient) * lam * lit, 0, 1)


def _to_plate(lum, rng, lo=0.05, hi=0.88, gamma=0.90, grain=0.010):
    """Map 0..1 luminance into a monochrome plate with real blacks, and add
    sensor grain. The wide range is deliberate: GATE V measures the separation
    between mean ink luminance and the page, and a flat mid-grey plate is what
    fails it (Ep. 05's expensive lesson, from the other direction)."""
    v = lo + (hi - lo) * np.clip(lum, 0, 1) ** gamma
    v = v + rng.normal(0, grain, v.shape)
    a = (np.clip(v, 0, 1) * 255).astype(np.uint8)
    return Image.fromarray(np.dstack([a, a, a]), "RGB")


def _terrain(w, h, seed, n_rocks, rmin, rmax, relief=1.05, y_bias=0.8,
             ytop=0.30, yspan=0.68, grit=0.30):
    rng = np.random.default_rng(seed)
    ground = _fbm(w, h, rng, octaves=4, base=3) * relief
    ground = ground + _fbm(w, h, rng, octaves=3, base=26) * grit   # visible grit
    # a gentle horizon gradient so the scene reads as ground receding
    ys = np.linspace(0, 1, h)[:, None]
    ground = ground + 0.55 * (1 - ys) ** 2
    rocks = _rocks(rng, n_rocks, w, h, rmin, rmax, y_bias=y_bias,
                   ytop=ytop, yspan=yspan)
    field = _emboss(ground, rocks, w, h)
    return field, rocks, rng


def _sky(img, h_sky):
    """Flat, slightly lighter band at the top — the horizon. Keeps the plate
    reading as a camera frame rather than an abstract texture."""
    a = np.asarray(img).astype(np.float64)
    hh = a.shape[0]
    band = np.zeros((hh, 1, 1))
    for y in range(h_sky):
        band[y, 0, 0] = (1.0 - y / max(h_sky, 1)) * 46.0
    a = np.clip(a + band, 0, 255)
    return Image.fromarray(a.astype(np.uint8), "RGB")


# ── plates ───────────────────────────────────────────────────────────────────

def navcam(name, seed=101, w=1280, h=860, n_rocks=34, tag=True):
    field, rocks, rng = _terrain(w, h, seed, n_rocks, 14, 46)
    img = _to_plate(_shade(field), rng)
    img = _sky(img, int(h * 0.20))
    if tag:
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, w - 1, h - 1], outline=(28, 26, 24), width=3)
    img.save(OUT / name)
    return rocks


def _cost_grid(w, h, seed, n_rocks, cell):
    """Reduce the terrain to what a navigation planner actually consumes: a grid
    of cells scored on step height and slope. Returns cost in 0..1."""
    field, rocks, rng = _terrain(w, h, seed, n_rocks, 16, 50,
                                 y_bias=0.0, ytop=0.06, yspan=0.90)
    gh, gw = h // cell, w // cell
    cost = np.zeros((gh, gw))
    for j in range(gh):
        for i in range(gw):
            blk = field[j * cell:(j + 1) * cell, i * cell:(i + 1) * cell]
            step = blk.max() - blk.min()       # the thing that high-centres a rover
            slope = abs(np.gradient(blk)[0]).mean() * 26.0
            cost[j, i] = step + slope
    lo, hi = np.percentile(cost, 45), np.percentile(cost, 99)
    cost = np.clip((cost - lo) / (hi - lo + 1e-9), 0, 1) ** 0.75
    return cost, field


def _draw_cost(img, cost, cell, floor=0.16):
    """Paint the grid: white where the rover may drive, darkening with cost.
    Cells under the floor stay page-white — a traversability map is mostly
    empty, and that emptiness is the point."""
    d = ImageDraw.Draw(img)
    gh, gw = cost.shape
    for j in range(gh):
        for i in range(gw):
            c = cost[j, i]
            if c < floor:
                continue
            g = int(round(238 - 214 * min((c - floor) / (1 - floor), 1.0)))
            d.rectangle([i * cell, j * cell, (i + 1) * cell - 1, (j + 1) * cell - 1],
                        fill=(g, g - 1, g - 4))
    for i in range(0, gw * cell + 1, cell):
        d.line([(i, 0), (i, gh * cell)], fill=(206, 201, 187), width=1)
    for j in range(0, gh * cell + 1, cell):
        d.line([(0, j), (gw * cell, j)], fill=(206, 201, 187), width=1)
    return d


def costmap(name, seed=101, w=1280, h=860, n_rocks=54, cell=40):
    cost, _ = _cost_grid(w, h, seed, n_rocks, cell)
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = _draw_cost(img, cost, cell)
    d.rectangle([0, 0, w - 1, h - 1], outline=(61, 57, 41), width=3)
    img.save(OUT / name)
    return cost, cell


def _arc(x0, y0, x1, y1, bulge, n=26):
    """A smooth candidate arc from the rover to a waypoint."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px, py = -dy / L, dx / L
    cx, cy = mx + px * bulge, my + py * bulge
    pts = []
    for i in range(n):
        t = i / (n - 1)
        a = (1 - t) ** 2
        b = 2 * (1 - t) * t
        c = t * t
        pts.append((a * x0 + b * cx + c * x1, a * y0 + b * cy + c * y1))
    return pts


def pathfan(name, seed=101, w=1280, h=860, n_paths=96, cell=40, block=0.34):
    """The cost map with the candidate fan on it.

    ENav scores about 1,700 paths per planning step; a plate that drew 1,700
    arcs is a solid hairball, so this draws a legible subset and the scene
    captions the real number.

    The ranking here is the real shape of the decision, not a stand-in: a path
    is FEASIBLE if no cell it crosses exceeds the clearance limit, and among the
    feasible ones the winner is simply the one that gets furthest forward. That
    is why the light arcs are allowed to run straight through obstacles — the
    candidates are generated blind, and the scoring is what throws them out.
    """
    cost, _ = _cost_grid(w, h, seed, 30, cell)
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = _draw_cost(img, cost, cell)
    rng = np.random.default_rng(seed + 7)
    x0, y0 = w * 0.5, h * 0.95                    # the rover, bottom centre

    def worst(pts):
        c = 0.0
        for (px, py) in pts:
            i = min(max(int(px // cell), 0), cost.shape[1] - 1)
            j = min(max(int(py // cell), 0), cost.shape[0] - 1)
            c = max(c, cost[j, i])
        return c

    cands = []
    for _ in range(n_paths * 6):
        ang = rng.uniform(-1.05, 1.05)
        reach = rng.uniform(0.66, 1.0)
        x1 = x0 + math.sin(ang) * w * 0.40 * reach
        y1 = y0 - math.cos(ang) * h * 0.60 * reach
        pts = _arc(x0, y0, x1, y1, rng.uniform(-34, 34), n=44)
        if min(p[0] for p in pts) < 10 or max(p[0] for p in pts) > w - 10:
            continue
        if min(p[1] for p in pts) < 10:
            continue
        cands.append((worst(pts), y0 - y1, pts))
        if len(cands) >= n_paths:
            break

    feasible = [c for c in cands if c[0] <= block]
    blocked = [c for c in cands if c[0] > block]
    feasible.sort(key=lambda t: -t[1])             # furthest forward wins
    if not feasible:                               # never happens at these seeds
        cands.sort(key=lambda t: t[0])
        feasible, blocked = cands[:1], cands[1:]

    # three plates, so a beat can build the decision instead of asserting it:
    #   _a  every candidate, undifferentiated
    #   _b  the ones that survive the clearance limit, darkened
    #   _c  the winner, in the one accent colour
    stem = name[:-4] if name.endswith(".png") else name

    def _rover(dd):
        dd.ellipse([x0 - 15, y0 - 15, x0 + 15, y0 + 15], fill=TERRA_D)
        dd.rectangle([0, 0, w - 1, h - 1], outline=(61, 57, 41), width=3)

    for _, _, pts in cands:
        d.line(pts, fill=(184, 179, 162), width=3)
    a = img.copy()
    _rover(ImageDraw.Draw(a))
    a.save(OUT / f"{stem}_a.png")

    for _, _, pts in feasible:
        d.line(pts, fill=(61, 57, 41), width=5)
    b = img.copy()
    _rover(ImageDraw.Draw(b))
    b.save(OUT / f"{stem}_b.png")

    d.line(feasible[0][2], fill=TERRA, width=11)
    ex, ey = feasible[0][2][-1]
    d.ellipse([ex - 17, ey - 17, ex + 17, ey + 17], outline=TERRA, width=7)
    _rover(d)
    img.save(OUT / name)
    return len(cands), len(feasible)


def _contour(cx, cy, r, rng, n=34, wob=0.20):
    """A closed, slightly irregular contour — what an edge-grouping step
    returns when it closes a rock's boundary."""
    k = rng.uniform(-wob, wob, 4)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        rr = r * (1.0 + k[0] * math.sin(t) + k[1] * math.cos(2 * t)
                  + k[2] * math.sin(3 * t) + k[3] * math.cos(4 * t))
        pts.append((cx + rr * math.cos(t), cy + rr * 0.72 * math.sin(t)))
    pts.append(pts[0])
    return pts


def rockfield(base, seed=202, w=1180, h=760, n_rocks=13):
    """Three plates from one scene: the picture, the closed contours a
    detector returns, and the ranking a scene profile produces."""
    field, rocks, rng = _terrain(w, h, seed, n_rocks, 40, 84, relief=0.85,
                                 y_bias=0.5, ytop=0.34, yspan=0.56, grit=0.22)
    plain = _sky(_to_plate(_shade(field), rng), int(h * 0.16))
    ImageDraw.Draw(plain).rectangle([0, 0, w - 1, h - 1],
                                    outline=(28, 26, 24), width=3)
    plain.save(OUT / f"{base}.png")

    # only the rocks a detector would actually close a contour around: big
    # enough, clear of the frame edge, and not overlapping another candidate.
    cands = [r for r in rocks
             if r[2] > 46
             and r[2] * 1.35 + 24 < r[0] < w - (r[2] * 1.35 + 24)
             and 0.40 * h < r[1] < h - (r[2] * 1.05 + 30)]
    cands.sort(key=lambda r: -r[2])
    det = []
    for r in cands:
        if all(math.hypot(r[0] - q[0], r[1] - q[1]) > (r[2] + q[2]) * 1.05
               for q in det):
            det.append(r)
        if len(det) == 6:
            break

    crng = np.random.default_rng(seed + 3)
    contours = [_contour(cx, cy, rr * 1.14, crng) for (cx, cy, rr, _, _) in det]

    edges = plain.copy()
    de = ImageDraw.Draw(edges)
    for c in contours:
        de.line(c, fill=(20, 18, 16), width=9)
        de.line(c, fill=(250, 247, 240), width=4)
    edges.save(OUT / f"{base}_edges.png")

    # the score: what a scene profile weighs — size, brightness, and how near
    # the object is (lower in the frame is nearer to the rover).
    arr = np.asarray(plain.convert("L")).astype(np.float64) / 255.0
    scored = []
    for (cx, cy, rr, _, _), c in zip(det, contours):
        x0, x1 = int(max(cx - rr, 0)), int(min(cx + rr, w - 1))
        y0, y1 = int(max(cy - rr * 0.7, 0)), int(min(cy + rr * 0.7, h - 1))
        bright = arr[y0:y1 + 1, x0:x1 + 1].mean() if x1 > x0 and y1 > y0 else 0.0
        s = 0.50 * min(rr / 110.0, 1.0) + 0.32 * bright + 0.18 * (cy / h)
        scored.append((s, cx, cy, rr, c))
    scored.sort(key=lambda t: -t[0])

    ranked = plain.copy()
    dr = ImageDraw.Draw(ranked)
    for rank, (s, cx, cy, rr, c) in enumerate(scored):
        if rank == 0:
            dr.line(c, fill=(20, 18, 16), width=11)
            dr.line(c, fill=TERRA, width=6)
        else:
            dr.line(c, fill=(20, 18, 16), width=8)
            dr.line(c, fill=(214, 210, 199), width=3)
    ranked.save(OUT / f"{base}_ranked.png")
    return [(round(float(s), 3), int(cx), int(cy), int(rr))
            for (s, cx, cy, rr, _) in scored]


def route(name, seed=303, w=1240, h=880, n_boulders=190):
    """Top-down: the straight line through a boulder field, and the route the
    rover actually drove around it. Real numbers live in the scene, not here."""
    rng = np.random.default_rng(seed)
    img = Image.new("RGB", (w, h), (250, 247, 240))
    d = ImageDraw.Draw(img)
    ax, ay = w * 0.12, h * 0.82
    bx, by = w * 0.88, h * 0.20

    # boulders, densest across the middle of the straight line
    for _ in range(n_boulders):
        t = rng.random()
        jitter = rng.normal(0, 0.16)
        px = ax + (bx - ax) * t + (by - ay) * jitter * 0.55
        py = ay + (by - ay) * t - (bx - ax) * jitter * 0.55
        if not (10 < px < w - 10 and 10 < py < h - 10):
            continue
        r = rng.uniform(5, 19)
        g = int(rng.uniform(96, 150))
        d.ellipse([px - r, py - r * 0.82, px + r, py + r * 0.82],
                  fill=(g, g - 4, g - 12))

    d.line([(ax, ay), (bx, by)], fill=(150, 145, 128), width=5)

    # the driven route: a detour that bows around the densest band
    pts = []
    for i in range(60):
        t = i / 59
        bow = math.sin(t * math.pi) * h * 0.30
        px = ax + (bx - ax) * t + bow * 0.42
        py = ay + (by - ay) * t + bow * 0.62
        pts.append((px, py))
    d.line(pts, fill=TERRA, width=9)
    d.ellipse([ax - 14, ay - 14, ax + 14, ay + 14], fill=(61, 57, 41))
    d.ellipse([bx - 14, by - 14, bx + 14, by + 14], fill=(61, 57, 41))
    d.rectangle([0, 0, w - 1, h - 1], outline=(61, 57, 41), width=3)
    img.save(OUT / name)


def main():
    navcam("navcam.png", seed=101)
    navcam("navcam_far.png", seed=104, n_rocks=22)
    costmap("costmap.png", seed=101)
    n, k = pathfan("pathfan.png", seed=101)
    top = rockfield("rockfield", seed=202)
    route("route.png", seed=303)
    print("[gen_mars] wrote:")
    for p in sorted(OUT.glob("*.png")):
        im = Image.open(p)
        print(f"  {p.name:26s} {im.size[0]}x{im.size[1]}")
    print(f"[gen_mars] pathfan: {n} candidates drawn, {k} feasible")
    print(f"[gen_mars] rockfield scores: {top}")


if __name__ == "__main__":
    main()
