"""Typeset the film's equations with matplotlib MathText -> outlined SVG (no LaTeX)."""
import base64, sys
from pathlib import Path
sys.path.insert(0, "/home/user/nikbearbrown/brutalist.art/runtime/scripts")
from typeset_math import typeset

EQS = {
    "eq_delta": r"\Delta = N(d_1)",
    "eq_d1": r"d_1 = \frac{\ln(S/K) + \frac{1}{2}\sigma^2\tau}{\sigma\sqrt{\tau}}",
    "eq_obj": r"\max_{\delta}\ U\left(Z_T + \sum_t \delta_t\,\Delta S_t - \gamma\sum_t S_t\,|\delta_t - \delta_{t-1}|\right)",
    "eq_z": r"Z_T = p_0 - (S_T - K)^{+}",
    "eq_ent": r"U(X) = -\frac{1}{\lambda}\,\log\,\mathbb{E}\left[e^{-\lambda X}\right]",
}
COLORS = {"ink": "#2B2A26", "dark": "#F5F1E8"}
for out in sys.argv[1:]:
    for name, ex in EQS.items():
        for cname, col in COLORS.items():
            d = typeset(ex, color=col)
            svg = base64.b64decode(d["src"].split(",", 1)[1])
            Path(out, f"{name}_{cname}.svg").write_bytes(svg)
            print(out, name, cname, round(d["aspect"], 2))
