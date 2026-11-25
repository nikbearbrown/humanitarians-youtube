"""Typeset the film's two equations to SVG via the toolkit's MathText route (no LaTeX)."""
import importlib.util as u, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
tm_path = os.path.join(HERE, "..", "..", "brutalist.art", "runtime", "scripts", "typeset_math.py")
s = u.spec_from_file_location("tm", tm_path); m = u.module_from_spec(s); s.loader.exec_module(m)
eqs = {"eq0": r"q_1 k_1 + q_2 k_2 + \cdots + q_d k_d",
       "eq1": r"\mathrm{Var}(q\cdot k)=d_k",
       "eq2": r"\mathrm{Var}\,\left(\frac{q\cdot k}{\sqrt{d_k}}\right)=1"}
os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
for n, e in eqs.items():
    r = m.typeset(e)
    svg = base64.b64decode(r["src"].split(",", 1)[1])
    open(os.path.join(HERE, "assets", n + ".svg"), "wb").write(svg)
    print(n, round(r["aspect"], 2), len(svg))
