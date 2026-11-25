#!/usr/bin/env python3
"""contrast.py — WCAG 2.2 contrast ratios of Gavia's colour tokens, before and after.

Before = desktop/src/index.css at commit 5dd8471 (Gavia 0.5.0), read with `git show`.
After  = desktop/src/index.css in the branch design/hai-brand working tree
         (uncommitted; the proposed redesign, built before approval).

The formula is WCAG 2.2's own (Understanding SC 1.4.3, "relative luminance"):
    c  = C/255;  c_lin = c/12.92 if c <= 0.04045 else ((c + 0.055)/1.055)^2.4
    L  = 0.2126 R_lin + 0.7152 G_lin + 0.0722 B_lin
    CR = (L_lighter + 0.05) / (L_darker + 0.05)
Thresholds: 4.5:1 for normal text (1.4.3), 3:1 for control edges (1.4.11).

usage: python3 contrast.py ~/Documents/gavia
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else Path.home() / "Documents/gavia")
CSS = "desktop/src/index.css"
BEFORE_COMMIT = "5dd8471"


def tokens(css):
    """{'light': {...}, 'dark': {...}} from the :root block and the dark-theme block."""
    blocks = re.findall(r"([^{}]+)\{([^{}]*)\}", css)
    out = {"light": {}, "dark": {}}
    for sel, body in blocks:
        sel = sel.strip()
        kv = dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;", body))
        if not kv:
            continue
        if sel.endswith(":root") and "dark" not in sel:
            out["light"].update(kv)
        elif "dark" in sel:
            out["dark"].update(kv)
    return out


def lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main():
    before = subprocess.run(["git", "-C", str(REPO), "show", f"{BEFORE_COMMIT}:{CSS}"],
                            capture_output=True, text=True, check=True).stdout
    after = (REPO / CSS).read_text()
    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--abbrev-ref", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()
    import hashlib
    print(f"before: {CSS} @ {BEFORE_COMMIT}  sha256 {hashlib.sha256(before.encode()).hexdigest()[:16]}")
    print(f"after:  {CSS} @ {head} working tree  sha256 {hashlib.sha256(after.encode()).hexdigest()[:16]}")
    pairs = [("text-subtle", ("bg", "surface", "surface-muted"), 4.5),
             ("text-muted", ("bg", "surface", "surface-muted"), 4.5),
             ("border-strong", ("bg", "surface"), 3.0)]
    for side, css in (("before", before), ("after", after)):
        t = tokens(css)
        for theme in ("light", "dark"):
            for fg, bgs, need in pairs:
                rs = [(bg, ratio(t[theme][fg], t[theme][bg])) for bg in bgs if bg in t[theme]]
                worst = min(rs, key=lambda x: x[1])
                cells = "  ".join(f"{bg}={r:.2f}" for bg, r in rs)
                flag = "PASS" if worst[1] >= need else "FAIL"
                print(f"{side:6} {theme:5} {fg:13} {t[theme][fg]}  {cells}  "
                      f"worst {worst[1]:.2f}:1 on {worst[0]} ({t[theme][worst[0]]})  need {need}  {flag}")
    # the worked case shown on screen, step by step
    for side, css in (("before", before), ("after", after)):
        t = tokens(css)["light"]
        fg, bg = t["text-subtle"], t["bg"]
        print(f"worked {side}: text-subtle {fg} L={lum(fg):.4f} on bg {bg} L={lum(bg):.4f} -> "
              f"({lum(bg):.4f}+0.05)/({lum(fg):.4f}+0.05) = {ratio(fg, bg):.2f}")


if __name__ == "__main__":
    main()
