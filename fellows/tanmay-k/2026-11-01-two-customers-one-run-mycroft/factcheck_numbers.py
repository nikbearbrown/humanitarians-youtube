#!/usr/bin/env python3
"""Every number the Week 29 work video says, read from the committed files on nikbearbrown/mycroft main (via git show upstream/main in the
local clone; read-only) and asserted. Prints a table for FACTCHECK.md. Run: python3 factcheck_numbers.py"""
import json, re, subprocess, sys
CLONE = "/Users/tanny/Humanitarians_AI/mycroft"
def show(path):
    return subprocess.run(["git", "-C", CLONE, "show", f"upstream/main:{path}"], capture_output=True, text=True, check=True).stdout
S = "scenariostresstestingagent"
rows = []
def fact(label, value, expect=None, where=""):
    ok = expect is None or value == expect
    rows.append((label, value, "ok" if ok else f"EXPECTED {expect!r}", where))
    if not ok: print("MISMATCH", label, value, expect, file=sys.stderr)

log = json.loads(show(f"logs/{S}-2026-11-01.json")); dlog = json.loads(show(f"logs/{S}-2026-11-01-defective.json"))
rep = show(f"reports/generated/{S}-2026-11-01.md"); drep = show(f"reports/generated/{S}-2026-11-01-defective.md")
qc = json.loads(show(f"data/verified/{S}/clean/quality-check.json")); qd = json.loads(show(f"data/verified/{S}/defective/quality-check.json"))
st = json.loads(show(f"data/verified/{S}/clean/stress-results.json"))["results"]
recipe = show(f"recipes/{S}.md"); selft = json.loads(show(f"logs/{S}/report-self-test-results.json")); runlog = show("logs/RUN_LOG.md")
heads = re.findall(r"^## (.+)$", rep, flags=re.M)

fact("agent log: number of fields", len(log), 16, f"logs/{S}-2026-11-01.json")
fact("report: number of sections", len(heads), 15, f"reports/generated/{S}-2026-11-01.md")
fact("report: first section / last section", f"{heads[0]} / {heads[-1]}", "Run summary / Decision recommendation")
fact("clean: records_seen in the log", log["records_seen"], 12)
fact("clean: report says 12 request(s) read", "12 request(s) read" in rep, True)
fact("clean: accepted at step 3", f"12 accepted at step 3" in rep, True)
fact("clean: stress-tested / stopped at the handoff", ("11 stress-tested at step 5, 1 stopped at the Groq handoff" in rep), True)
fact("clean: reconciled on every step-4 check", len(qc["verified_records"]), 11, f"data/verified/{S}/clean/quality-check.json")
fact("clean: handed off", len(qc["handed_off"]), 1)
fact("clean: checks run on every result", len(qc["checks_run"]), 14)
fact("clean: failures / duplicates / rejects", (len(qc["failures"]), len(qc["duplicates"]), len(qc["rejects"])), (0, 0, 0))
fact("clean: advisory flags", len(qc["flags"]), 11)
fact("clean: steps_completed in the log", log["steps_completed"], [1, 3, 4, 5, 6])
fact("clean: gate decisions in the log (six gates + human clearance)", len(log["gate_decisions"]), 7)
fact("clean: gate 5 reads", [g["result"] for g in log["gate_decisions"] if g["gate"].startswith("5")][0], "NOT NEEDED (sample mode)")
fact("clean: human clearance entry", [g["result"] for g in log["gate_decisions"] if g["gate"] == "human clearance"][0], "none recorded")
fact("clean: stop conditions evaluated / triggered", (len(log["stop_conditions"]), sum(x["triggered"] for x in log["stop_conditions"])), (4, 0))
fact("clean: report's summary line on stop conditions", "Stop conditions: 0 of 4 triggered" in rep, True)
fact("clean: condition 1 evidence says 41 files scanned, none found", ("scanned 41 file(s)" in log["stop_conditions"][0]["evidence"] and log["stop_conditions"][0]["evidence"].endswith("none found")), True)
fact("clean: typed TODOs in the log", len(log["todo_items"]), 3)
fact("clean: recommendation lines", re.findall(r"- \*\*(Approve for the next phase \(sample mode only\)|Request source or schema fixes|Block live execution): (YES|NO)", rep), [("Approve for the next phase (sample mode only)", "YES"), ("Request source or schema fixes", "NO"), ("Block live execution", "YES")])
fact("clean: recipe frontmatter", re.findall(r"^(status|todos_open|recipe_version): (.+)$", recipe, flags=re.M)[:3], [("status", "DRAFT"), ("todos_open", "3"), ("recipe_version", "0.3.1")])
fact("defective: records_seen / rejects in the log", (dlog["records_seen"], len(dlog["rejects"])), (10, 10))
r6 = [r for r in dlog["rejects"] if r["id"] == "d06-all-weights-zero"][0]
fact("defective: d06 reject stage and reason", (r6["stage"], r6["reasons"]), ("step 3", ["weights total 0.0: rescaling by a zero total gives NaN weights (gate addition)"]))
fact("defective: report carries the same reason", "d06-all-weights-zero` at step 3: weights total 0.0: rescaling by a zero total gives NaN weights (gate addition)" in drep, True)
fact("defective: recommendation lines", re.findall(r"- \*\*(Approve for the next phase \(sample mode only\)|Request source or schema fixes|Block live execution): (YES|NO)", drep), [("Approve for the next phase (sample mode only)", "NO"), ("Request source or schema fixes", "YES"), ("Block live execution", "YES")])
fact("defective: 'No request was accepted' in the report", "No request was accepted" in drep, True)
fact("self-test (steps 4 and 6): checks, all passed", (len(selft["checks"]), selft["all_passed"]), (30, True))
names = [c["check"] for c in selft["checks"]]
fact("self-test: deliberate breaks (caught) / refusals", (sum(1 for n in names if "break caught" in n), sum(1 for n in names if "refuses" in n)), (12, 4))
fact("the earlier report showed sixteen steps (logged in the committed RUN_LOG)", "showed sixteen steps and \"14 of 16 step scripts exist\"" in runlog, True, "logs/RUN_LOG.md, 2026-11-01 entry")
fact("the stop-condition correction is logged", "stop condition 1 (credentials hardcoded instead of read from environment variables) was recorded as `triggered: true`" in runlog, True, "logs/RUN_LOG.md, 2026-11-02 entry")
fact("the recipe's own stop condition 1 text", log["stop_conditions"][0]["condition"], "Stop if credentials, API keys, database destinations, email addresses, or tokens are hardcoded instead of read from environment variables.")
pr = json.loads(subprocess.run(["gh", "pr", "view", "82", "--repo", "nikbearbrown/mycroft", "--json", "state,mergeCommit"], capture_output=True, text=True).stdout)
fact("PR #82 state / merge commit", (pr["state"], pr["mergeCommit"]["oid"][:7]), ("MERGED", "255ddf8"))
for n, sha in ((81, "9684f46"), (74, "5d60312")):
    p = json.loads(subprocess.run(["gh", "pr", "view", str(n), "--repo", "nikbearbrown/mycroft", "--json", "state,mergeCommit"], capture_output=True, text=True).stdout)
    fact(f"PR #{n} state / merge commit", (p["state"], p["mergeCommit"]["oid"][:7]), ("MERGED", sha))
w = max(len(r[0]) for r in rows)
for l, v, ok, wh in rows: print(f"{ok:5} {l.ljust(w)}  {str(v)[:110]}")
print(f"\n{sum(1 for r in rows if r[2]=='ok')}/{len(rows)} facts as expected")
sys.exit(0 if all(r[2] == "ok" for r in rows) else 1)
