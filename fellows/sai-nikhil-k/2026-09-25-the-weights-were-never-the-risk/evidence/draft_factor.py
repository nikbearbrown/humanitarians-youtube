"""What does Pillow's JPEG draft() do to the validation photos, and does
Gavia's Rust draft_factor() reproduce it?

Run with the same Pillow the Python backend pinned (12.3.0):
    <venv>/bin/python draft_factor.py ~/Documents/loonet/data/annotated/loonnet_v1/val.txt

For every JPEG in the split it opens the file, asks Pillow for a 640 draft
(what gavia-py's loader did before letterboxing), and records the reduction
Pillow chose. It then applies the formula read out of
desktop/src-tauri/src/detection/loader.rs::draft_factor at 78b383e,
    ratio = min(w // 640, h // 640);  f = first of [8, 4, 2, 1] with ratio >= f
and checks that the two agree. Finally it evaluates the letterbox scale
s = min(640 / w', 640 / h', 1) on the drafted size (preprocess.rs::letterbox).
Nothing is resized or saved; only headers and the draft decision are read.
"""
import sys
from collections import Counter
from pathlib import Path

import PIL
from PIL import Image, ImageOps

TARGET = 640


def rust_draft_factor(w, h, target=TARGET):
    ratio = min(w // target, h // target)
    return next((s for s in (8, 4, 2, 1) if ratio >= s), 1)


def main(split):
    print(f"Pillow {PIL.__version__}  target {TARGET}")
    paths = [Path(p) for p in Path(split).read_text().split()]
    agree = 0
    jpegs = 0
    sizes = Counter()
    for p in paths:
        with Image.open(p) as im:
            if im.format not in ("JPEG", "MPO"):
                print(f"{p.name:34} {im.format:5} not a JPEG, no draft")
                continue
            jpegs += 1
            w, h = im.size
            im.draft("RGB", (TARGET, TARGET))
            dw, dh = im.size
            pillow_f = round(w / dw)
            rust_f = rust_draft_factor(w, h)
            ok = pillow_f == rust_f
            agree += ok
            sizes[(w, h, pillow_f)] += 1
            s = min(TARGET / dw, TARGET / dh, 1.0)
            print(f"{p.name:34} {w}x{h} -> draft {dw}x{dh}  Pillow f={pillow_f}  "
                  f"Rust f={rust_f}  {'agree' if ok else 'DIFFER'}  letterbox s={s:.4f}")
    print(f"\n{agree} of {jpegs} JPEGs: Rust draft_factor == Pillow draft()")
    print("sizes (w, h, f):", dict(sizes))
    # The worked case typeset on screen: the three 5568x3712 validation photos.
    w, h = 5568, 3712
    print(f"\nworked case {w}x{h}: floor(w/640)={w // TARGET} floor(h/640)={h // TARGET} "
          f"min={min(w // TARGET, h // TARGET)} -> f={rust_draft_factor(w, h)} "
          f"-> {w // rust_draft_factor(w, h)}x{h // rust_draft_factor(w, h)}; "
          f"s = 640/{w // 4} = {640 / (w // 4):.4f}")


if __name__ == "__main__":
    main(sys.argv[1])
