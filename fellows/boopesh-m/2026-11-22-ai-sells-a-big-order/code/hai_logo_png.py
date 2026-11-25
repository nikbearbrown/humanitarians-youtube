#!/usr/bin/env python3
"""Rasterize the HAI mark (brutalist.art/logos/humanitarians/humanitarians-logo-1.svg) to PNG.

The SVG is three straight-edged paths (M/h/v/l/H/V/Z only). ImageMagick's SVG delegate
is broken on this machine and SVGMobject drops the <style> class fill, so the paths are
parsed here and filled with pycairo, unchanged in shape. Colour is a parameter so the
mark can sit in INK on cream.
Usage: hai_logo_png.py <svg> <out.png> <height_px> <#hex>
"""
import re
import sys

import cairo


def parse(d):
    toks = re.findall(r"[MmHhVvLlZz]|-?\d+(?:\.\d+)?", d)
    pts, x, y, i, cmd = [], 0.0, 0.0, 0, None
    while i < len(toks):
        t = toks[i]
        if re.fullmatch(r"[A-Za-z]", t):
            cmd = t
            i += 1
            if cmd in "Zz":
                continue
        if cmd in "Mm":
            nx, ny = float(toks[i]), float(toks[i + 1]); i += 2
            x, y = (nx, ny) if cmd == "M" else (x + nx, y + ny)
        elif cmd in "Ll":
            nx, ny = float(toks[i]), float(toks[i + 1]); i += 2
            x, y = (nx, ny) if cmd == "L" else (x + nx, y + ny)
        elif cmd in "Hh":
            n = float(toks[i]); i += 1
            x = n if cmd == "H" else x + n
        elif cmd in "Vv":
            n = float(toks[i]); i += 1
            y = n if cmd == "V" else y + n
        pts.append((x, y))
    return pts


def main(svg, out, height, colour):
    src = open(svg).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', src).group(1).split()]
    paths = re.findall(r'<path[^>]*\sd="([^"]+)"', src)
    s = int(height) / vb[3]
    w, h = int(round(vb[2] * s)), int(height)
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surf)
    c = colour.lstrip("#")
    ctx.set_source_rgb(*(int(c[j:j + 2], 16) / 255 for j in (0, 2, 4)))
    ctx.scale(s, s)
    ctx.translate(-vb[0], -vb[1])
    for d in paths:
        pts = parse(d)
        ctx.move_to(*pts[0])
        for p in pts[1:]:
            ctx.line_to(*p)
        ctx.close_path()
        ctx.fill()
    surf.write_to_png(out)
    print(f"{out}: {w}x{h}, {len(paths)} paths, fill {colour}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
