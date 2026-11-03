"""Executed evidence for weekly_updates/09-18-2, beat B04.

Measures on the REAL Prot2Vec v0.3.0 source tree how many executable
statements coverage.py stops measuring under the v0.2.0 exclude_lines entry
("\\.\\.\\.", unanchored) versus the v0.3.0 replacement ("^\\s*\\.\\.\\.$").

prot2vec itself is never imported or executed: coverage's PythonParser decides
exclusions statically, and that static decision is the thing that misfired.
Requires only `coverage` and a checkout.

Usage: python3 coverage_exclusion.py <path-to>/src/prot2vec
"""
import pathlib, sys
from coverage.parser import PythonParser

BUGGY = r"\.\.\."          # pyproject.toml @ 405b00e (v0.2.0)
FIXED = r"^\s*\.\.\.$"     # pyproject.toml @ 40ff686 (v0.3.0)
NEVER = r"(?!x)x"          # matches nothing: the no-exclusion control

def measured(path: pathlib.Path, regex: str) -> int:
    p = PythonParser(text=path.read_text(), filename=str(path), exclude=regex)
    p.parse_source()
    return len(p.statements)

def main(root: str) -> None:
    files = sorted(pathlib.Path(root).rglob("*.py"))
    base = fixed = buggy = 0
    rows = []
    for f in files:
        b, x, g = measured(f, NEVER), measured(f, FIXED), measured(f, BUGGY)
        base += b; fixed += x; buggy += g
        if x - g:
            rows.append((x - g, f.name, x))
    print(f"source tree          : {root}")
    print(f"python files         : {len(files)}")
    print(f"executable statements: {base}")
    print()
    print(f'  exclude "{FIXED}"  (v0.3.0) -> {fixed} statements measured  ({100*fixed/base:.1f}%)')
    print(f'  exclude "{BUGGY}"      (v0.2.0) -> {buggy} statements measured  ({100*buggy/base:.1f}%)')
    print()
    print(f"statements the unanchored pattern removed from measurement: {fixed - buggy}")
    print()
    print("per-file (statements hidden / statements that should be measured):")
    for d, name, x in sorted(rows, reverse=True):
        print(f"  {d:5d} / {x:<5d}  {name}")

if __name__ == "__main__":
    main(sys.argv[1])
