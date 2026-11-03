#!/usr/bin/env python3
"""live_runs.py: the terminal transcripts the film types on screen, produced by RUNNING them.

Each session is fed line by line to a real Python interactive console (code.InteractiveConsole) inside
a copy of the build, in a subprocess, and everything the console prints is captured. The film's terminal
blocks are this output, never hand-typed text (Week 24 rule: executable evidence, not screenshots).

    /opt/homebrew/bin/python3.12 live_runs.py     # writes live_runs.json
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = "/opt/homebrew/bin/python3.12"
SETUP = ["from datetime import date", "from src.orchestrator import TransactionPipeline",
         "from demo import example_gate_policy", "p = TransactionPipeline(gate_decision_fn=example_gate_policy)"]


def call(consumer, category, merchant, amount, day):
    return [f'r = p.process_transaction(agent_id="agent-concierge-01",',
            f'    consumer_id="{consumer}", category="{category}",',
            f'    merchant="{merchant}", amount={amount},',
            f'    transaction_date={day})']


SESSIONS = {
    "B05": ("reference-build", call("morgan-02", "household_staples", "greenleaf-grocery", "42.50", "date(2026, 9, 1)")
            + ["r.status, r.reason"]),
    "B06_lower_v1": ("reference-build-v1", call("devon-01", "household_staples", "greenleaf-grocery", "70.00", "date(2027, 3, 1)")
                     + ["r.status, r.reason"]),
    "B06_upper_v1": ("reference-build-v1", call("devon-01", "Household_Staples", "greenleaf-grocery", "70.00", "date(2027, 3, 1)")
                     + ["r.status, r.intent_record.authorized_via"]),
    "B06_upper_v2": ("reference-build", call("devon-01", "Household_Staples", "greenleaf-grocery", "70.00", "date(2027, 3, 1)")
                     + ["r.status, r.reason"]),
    "B08": ("reference-build", call("devon-01", "household_staples", "greenleaf-grocery", 'float("nan")', "date(2026, 9, 1)")
            + ["r.status, r.reason"]
            + call("devon-01", "household_staples", "greenleaf-grocery", "-500.00", "date(2026, 9, 1)")
            + ["r.status, r.reason"]),
    "B11": ("reference-build", call("devon-01", "footwear", "greenleaf-grocery", "60.00", "date(2026, 9, 1)")
            + ["r.status, r.intent_record.merchant"]),
}

RUNNER = r'''
import code, io, json, sys, contextlib
lines = json.loads(sys.argv[1]); setup = json.loads(sys.argv[2])
con = code.InteractiveConsole()
for s in setup:
    con.push(s)
out = []
buf = []
for ln in lines:
    cont = ln.startswith("    ")
    out.append({"kind": "cmd", "prompt": "..." if cont else ">>>", "text": ln.strip() if not cont else ln})
    f = io.StringIO()
    with contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
        more = con.push(ln)
    printed = f.getvalue().rstrip("\n")
    if printed:
        for p in printed.splitlines():
            out.append({"kind": "out", "text": p})
print(json.dumps(out))
'''


def run(build, lines):
    res = subprocess.run([PY, "-c", RUNNER, json.dumps(lines), json.dumps(SETUP)], cwd=HERE / build,
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def main():
    out = {}
    for key, (build, lines) in SESSIONS.items():
        out[key] = {"build": build, "lines": run(build, lines)}
        for l in out[key]["lines"]:
            print(f"{key:7s} {'   ' if l['kind']=='out' else l['prompt']} {l['text']}")
        print()
    (HERE / "live_runs.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
