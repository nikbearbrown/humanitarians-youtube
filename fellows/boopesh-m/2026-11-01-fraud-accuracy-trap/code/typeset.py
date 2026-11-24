"""Typeset the film's two formulas with matplotlib MathText -> outlined SVG (no LaTeX)."""
import base64, sys
from pathlib import Path
sys.path.insert(0, "/home/user/nikbearbrown/brutalist.art/runtime/scripts")
from typeset_math import typeset

EQS = {
    "eq_recall": r"\mathrm{recall} = \dfrac{\mathrm{caught}}{\mathrm{caught} + \mathrm{missed}}",
    "eq_precision": r"\mathrm{precision} = \dfrac{\mathrm{caught}}{\mathrm{caught} + \mathrm{false\ alarms}}",
}
COLORS = {"ink": "#2B2A26", "dark": "#F5F1E8"}
for out in sys.argv[1:]:
    for name, ex in EQS.items():
        for cname, col in COLORS.items():
            d = typeset(ex, color=col)
            svg = base64.b64decode(d["src"].split(",", 1)[1])
            Path(out, f"{name}_{cname}.svg").write_bytes(svg)
            print(out, name, cname, round(d["aspect"], 2))
