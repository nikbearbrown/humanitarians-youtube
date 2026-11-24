import importlib.util as u, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "..", "..", "brutalist.art", "runtime", "scripts", "typeset_math.py")
s = u.spec_from_file_location("tm", p); m = u.module_from_spec(s); s.loader.exec_module(m)
eqs = {"eq0": r"\cos\theta=\frac{a\cdot b}{|a|\,|b|}",
       "eq1": r"\frac{14}{4.12\times 3.61}=0.94"}
os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
for n, e in eqs.items():
    r = m.typeset(e)
    open(os.path.join(HERE, "assets", n + ".svg"), "wb").write(base64.b64decode(r["src"].split(",", 1)[1]))
    print(n, round(r["aspect"], 2))
