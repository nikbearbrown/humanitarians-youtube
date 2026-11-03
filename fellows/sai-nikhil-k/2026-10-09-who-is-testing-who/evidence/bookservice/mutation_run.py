#!/usr/bin/env python3
"""mutation_run.py — line coverage and mutation score for each suite, by the same tools.

experiment.py uses five bugs a person chose. This uses mutmut 3, which plants hundreds of
small mechanical changes (flip a comparison, change a string or a number, drop an
argument…) one at a time and reruns a suite on each. A "killed" mutant made the suite
fail; a "survived" one did not; "no tests" means no test in the suite even runs that
line. Mutation score = killed / all mutants.

  mock    — tests_mock/ on the BookService package (pricing.py left out)
  db      — tests_db/   on the same package
  pricing — tests_pricing/ on pricing.py alone (pure logic, no mocks)

Each run happens in a fresh scratch copy, so nothing here is modified.
Needs a Python with pytest, coverage and mutmut 3. Run:
    python mutation_run.py > mutation_run.out     (also writes mutation_run.json)
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
BIN = Path(sys.executable).parent
BOOK_MODULES = ["__init__.py", "models.py", "parts.py", "repository.py", "service.py"]
SUITES = {
    "mock": ("tests_mock", BOOK_MODULES),
    "db": ("tests_db", BOOK_MODULES),
    "pricing": ("tests_pricing", ["__init__.py", "pricing.py"]),
}


def stage(tmp, tests, modules):
    (tmp / "bookstore").mkdir()
    for m in modules:
        shutil.copy(HERE / "bookstore" / m, tmp / "bookstore" / m)
    shutil.copytree(HERE / tests, tmp / tests)
    (tmp / "pyproject.toml").write_text(
        "[tool.mutmut]\n"
        'source_paths = ["bookstore/"]\n'
        f'pytest_add_cli_args_test_selection = ["{tests}/"]\n'
        f'also_copy = ["{tests}/"]\n\n'
        "[tool.pytest.ini_options]\n"
        'pythonpath = ["."]\n')


def coverage(tmp, tests):
    subprocess.run([BIN / "python", "-m", "coverage", "run", "--branch", "--source=bookstore",
                    "-m", "pytest", "-q", "-p", "no:cacheprovider", tests],
                   cwd=tmp, capture_output=True, text=True, check=True)
    rep = subprocess.run([BIN / "python", "-m", "coverage", "json", "-o", "-"],
                         cwd=tmp, capture_output=True, text=True, check=True)
    files = json.loads(rep.stdout)["files"]
    return {Path(f).name: {"lines": d["summary"]["num_statements"],
                           "covered": d["summary"]["covered_lines"],
                           "percent_lines": round(100 * d["summary"]["covered_lines"]
                                                  / max(1, d["summary"]["num_statements"]), 1)}
            for f, d in files.items() if not f.endswith("__init__.py")}


def classify(old, new):
    """Sort a mutant by what it changes, so a score can leave out the ones no test should
    care about. 'message': only the text of an exception message changed. 'sql-case': the
    SQL differs only in letter case (SQL keywords and these identifiers ignore case).
    Everything else is 'behavior'."""
    if old.strip().startswith("raise ") and re.sub(r"\(.*\)", "()", old) == re.sub(
            r"\(.*\)", "()", new):
        return "message"
    if "SELECT" in old.upper() and old.lower() == new.lower():
        return "sql-case"
    return "behavior"


def mutate(tmp):
    subprocess.run([BIN / "mutmut", "run"], cwd=tmp, capture_output=True, text=True)
    out = subprocess.run([BIN / "mutmut", "results", "--all", "true"], cwd=tmp,
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        m = re.match(r"\s*(bookstore\.(\w+)\.\S+__mutmut_\d+): (.+)$", line)
        if not m:
            continue
        diff = subprocess.run([BIN / "mutmut", "show", m.group(1)], cwd=tmp,
                              capture_output=True, text=True).stdout.splitlines()
        old = next((l[1:] for l in diff if l.startswith("-") and not l.startswith("---")), "")
        new = next((l[1:] for l in diff if l.startswith("+") and not l.startswith("+++")), "")
        rows.append({"id": m.group(1), "file": m.group(2) + ".py", "status": m.group(3).strip(),
                     "kind": classify(old, new), "old": old.strip(), "new": new.strip()})
    return rows


def main():
    import coverage as cov_mod
    import pytest
    ver = subprocess.run([BIN / "pip", "show", "mutmut"], capture_output=True, text=True).stdout
    mver = re.search(r"Version: (\S+)", ver).group(1)
    print("date", time.strftime("%Y-%m-%d %H:%M %Z"), "· python", sys.version.split()[0],
          "· pytest", pytest.__version__, "· coverage", cov_mod.__version__, "· mutmut", mver)
    out = {}
    for name, (tests, modules) in SUITES.items():
        with tempfile.TemporaryDirectory() as t:
            tmp = Path(t)
            stage(tmp, tests, modules)
            cov = coverage(tmp, tests)
            rows = mutate(tmp)
        tot = Counter(r["status"] for r in rows)
        n = len(rows)
        score = round(100 * tot["killed"] / n, 1) if n else 0
        beh = [r for r in rows if r["kind"] == "behavior"]
        kb = sum(r["status"] == "killed" for r in beh)
        out[name] = {"coverage": cov, "mutants": rows, "total": dict(tot), "score": score,
                     "behavior_killed": kb, "behavior_total": len(beh),
                     "kinds": dict(Counter(r["kind"] for r in rows))}
        print(f"\n=== {name} ({tests}/)  mutation score {tot['killed']}/{n} = {score}%  "
              f"{dict(tot)}")
        print(f"  by kind: {dict(Counter(r['kind'] for r in rows))} · behaviour mutants "
              f"killed {kb}/{len(beh)} = {round(100 * kb / max(1, len(beh)), 1)}%")
        for f in sorted(set(cov) | {r["file"] for r in rows}):
            c = cov.get(f, {})
            fr = [r for r in rows if r["file"] == f]
            k = sum(r["status"] == "killed" for r in fr)
            print(f"  {f:14} lines covered {c.get('covered', 0):>3}/{c.get('lines', 0):<3} "
                  f"({c.get('percent_lines', 0):5.1f}%) · mutants killed {k:>2}/{len(fr):<2} "
                  f"{dict(Counter(r['status'] for r in fr))}")
        print("  not killed (status, kind: old → new):")
        for r in rows:
            if r["status"] != "killed":
                print(f"    {r['status']:9} {r['kind']:8} {r['old'][:62]}  →  {r['new'][:62]}")
    (HERE / "mutation_run.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
