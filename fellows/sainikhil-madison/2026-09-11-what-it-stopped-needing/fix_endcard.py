#!/usr/bin/env python3
"""fix_endcard.py — redraw the Short's endcard at 4K portrait.

WHY THIS EXISTS. `shorts.py` draws END.png at a hardcoded 1080x1920 (`W, H` at
module scope) with hardcoded 64pt and 44pt type. That is correct for a 1080p
portrait Short and wrong for this one: the master is compiled at --height 3840,
so a 1080-wide card is upscaled 2x into a 2160x3840 frame and the handle and the
Next: line arrive visibly soft against type that was rendered natively
everywhere else in the reel.

This script redraws the same card at 2160x3840 with every dimension doubled, so
the endcard is native rather than interpolated. It imports the real colours and
the real serif lookup from shorts.py rather than restating them, so the card
cannot drift from the house one.

ORDER MATTERS — RUN THIS LAST. `shorts.py` rewrites short/media/END.png on every
run, so this must come AFTER the final shorts.py invocation and BEFORE
compile.py. If you re-run shorts.py for any reason, run this again.

Run:  python3 fix_endcard.py            # needs Pillow (system python3, NOT .venv)
      python3 fix_endcard.py --check    # report the current size, write nothing
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "runtime" / "scripts"))

from PIL import Image, ImageDraw, ImageFont            # noqa: E402
from shorts import CREAM, INK, TERRA, find_serif       # noqa: E402

HERE = Path(__file__).resolve().parent
END = HERE / "short" / "media" / "END.png"

W, H = 2160, 3840          # 2x shorts.py's 1080x1920 — 4K portrait, native
SCALE = 2


def draw(handle, next_text, dark=True):
    bg, fg = (INK, CREAM) if dark else (CREAM, INK)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    serif = find_serif()

    def f(size):
        try:
            return ImageFont.truetype(serif, size * SCALE)
        except Exception:
            return ImageFont.load_default()

    fh = f(64)
    hb = d.textbbox((0, 0), handle, font=fh)
    hw = hb[2] - hb[0]
    d.text(((W - hw) / 2, H * 0.30), handle, font=fh, fill=fg)
    y = H * 0.30 + (hb[3] - hb[1]) + 26 * SCALE
    d.line([((W - hw) / 2, y), ((W + hw) / 2, y)], fill=TERRA, width=4 * SCALE)

    fn = f(44)
    words, lines, cur = next_text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textbbox((0, 0), t, font=fn)[2] > W * 0.84 and cur:
            lines.append(cur)
            cur = wd
        else:
            cur = t
    lines.append(cur)
    ly = y + 60 * SCALE
    for ln in lines:
        lw = d.textbbox((0, 0), ln, font=fn)[2]
        d.text(((W - lw) / 2, ly), ln, font=fn, fill=fg)
        ly += 62 * SCALE
    return img


def main():
    if not END.is_file():
        print(f"[endcard] {END} not found — run shorts.py first")
        return 1
    cur = Image.open(END)
    if "--check" in sys.argv:
        print(f"[endcard] {END.relative_to(HERE)} is {cur.size[0]}x{cur.size[1]} "
              f"({'already 4K' if cur.size == (W, H) else 'NEEDS REDRAW at 2160x3840'})")
        return 0
    if cur.size == (W, H):
        print("[endcard] already 2160x3840 — nothing to do")
        return 0

    # The handle and Next: line shorts.py wrote are recovered from the short's
    # own beat sheet, so this never invents card copy of its own.
    import json
    sheet = json.loads((HERE / "short" / "beat_sheet.json").read_text())
    card = next((b.get("card", {}) for b in sheet["beats"]
                 if b["beat_id"] == "END"), {})
    handle = card.get("handle") or sheet["metadata"].get("folder_chip", "@HumanitariansAI")
    nxt = card.get("next") or ""
    draw(handle, nxt).save(END)
    print(f"[endcard] redrawn at {W}x{H} — handle {handle!r}, next {nxt!r}")
    print("[endcard] compile now; re-run this if shorts.py runs again")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
