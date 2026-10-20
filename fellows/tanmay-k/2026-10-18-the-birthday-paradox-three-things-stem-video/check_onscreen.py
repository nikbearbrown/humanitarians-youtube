"""PROOF mechanical pass on the stills: (1) every spoken figure is printed in the same beat,
(2) contrast of every text colour on its ground, (3) smallest type per beat, (4) content margins."""
import sys, importlib.util, re
from pathlib import Path
from PIL import Image, ImageChops
HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("bs", HERE / "build_slates.py"); bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)

# spoken figures per beat (from the signed narration) -> strings that must appear on screen in that beat
SPOKEN = {
 "B01": ["50.7%", "23"], "B02": ["PEOPLE", "EVENNESS", "DAYS"], "B03": ["253", "23", "22"],
 "B04": ["50.7%", "50.73%", "400,000", "10 people", "11.7%", "30 people", "70.6%", "50 people", "97.0%", "57 people", "99.0%"],
 "B05": ["50.7%", "5.9%", "253", "22 others"], "B06": ["+12%", "25%", "one year in four", "NCHS", "SSA"],
 "B07": ["50.7%", "50.8%"], "B08": ["96%", "10%"], "B09": ["95.4%", "50.8%", "90"],
 "B10": ["50.84%", "77.05%", "95.44%", "99.24%", "99.99%", "7 days"],
 "B11": ["23", "12", "10", "7", "5", "4"], "B12": ["12% → 99%", "50.7% → 50.8%", "50.8% → 95.4%", "95.44%", "95.40%"],
 "B13": ["23", "17", "12", "10", "7", "5", "4", "1,161", "1,999", "838", "round halves up"],
 "B14": ["50.8%", "September 1"], "B15": ["12", "3.46", "4.66", "43%", "62%"],
 "B16": ["50 slots", "25", "8 s"], "B17": ["7.07", "8.99", "53%", "45%", "25"], "B18": ["Humanitarians AI", "CC BY 4.0"],
}
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)

fails = 0
print("== 1. spoken figures printed in the same beat")
logs = {}
for bid, fn in bs.BEATS.items():
    cv = fn(); logs[bid] = cv.log
    text = " | ".join(t[0] for t in cv.log)
    miss = [t for t in SPOKEN[bid] if t not in text]
    # the source line is drawn with wrap -> logged per line; fine
    if miss: fails += 1
    print(f"  {bid}: {'OK' if not miss else 'MISSING ' + str(miss)}")
print("\n== 2. contrast (WCAG ratio) of text colours")
for name, fg, bg in [("INK on PAGE", bs.INK, bs.PAGE), ("INK on CARD", bs.INK, bs.CARD), ("INK_SOFT on PAGE", bs.INK_SOFT, bs.PAGE),
                     ("INK_SOFT on CARD", bs.INK_SOFT, bs.CARD), ("SPARK on PAGE", bs.SPARK, bs.PAGE), ("SPARK on CARD", bs.SPARK, bs.CARD),
                     ("GHOST on PAGE (inactive strip)", bs.GHOST, bs.PAGE), ("SEND on PAGE", bs.SEND, bs.PAGE)]:
    print(f"  {name}: {contrast(fg, bg):.2f}")
print("\n== 3. smallest type per beat (logical px at 1080p; text logged by size)")
for bid, lg in logs.items():
    sizes = sorted({t[2] for t in lg})
    small = [(t[0][:34], t[2]) for t in lg if t[2] < 22]
    print(f"  {bid}: min {sizes[0]} px; <22px items: {len(small)}" + (f"  e.g. {small[0]}" if small else ""))
print("\n== 4. content bounding box vs 1920x1080 (margins; logical px)")
for bid in bs.BEATS:
    im = Image.open(HERE / "_stills" / f"{bid}-16x9.png").convert("RGB")
    bg = Image.new("RGB", im.size, bs.PAGE)
    bb = ImageChops.difference(im, bg).getbbox()
    l, t, r, b = [v / 2 for v in bb]
    print(f"  {bid}: left {l:.0f}  top {t:.0f}  right {1920 - r:.0f}  bottom {1080 - b:.0f}")
print("\n== 5. enforced limits")
bad = []
for bid, lg in logs.items():
    for t, kind, size, fill in lg:
        if kind.startswith("sans") and size < 24: bad.append((bid, "small sans", t[:30], size))
        ratio = min(contrast(fill, bs.PAGE), contrast(fill, bs.CARD))
        need = 3.0 if size >= 48 else 4.5
        if ratio < need and kind not in ("run",) and not re.fullmatch(r"[\d.,%→≈×+=()\s]*", t): bad.append((bid, "contrast %.2f<%.1f" % (ratio, need), t[:30], size))
for bid in bs.BEATS:
    im = Image.open(HERE / "_stills" / f"{bid}-16x9.png").convert("RGB")
    bb = ImageChops.difference(im, Image.new("RGB", im.size, bs.PAGE)).getbbox()
    if 1080 - bb[3] / 2 < 90: bad.append((bid, "bottom margin", f"{1080 - bb[3] / 2:.0f}px", ""))
print("  violations:", len(bad)); [print("   ", b) for b in bad[:40]]
fails += len(bad)
print("\nRESULT:", "all spoken figures present, no limit violations" if not fails else f"{fails} issue(s)")
