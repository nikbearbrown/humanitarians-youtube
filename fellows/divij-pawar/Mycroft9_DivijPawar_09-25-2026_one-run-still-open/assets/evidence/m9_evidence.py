"""
Executable evidence for Mycroft 9 — One Run, Still Open.

Per brutalist.art/docs/EXECUTABLE-EVIDENCE.md, every figure a beat shows is computed here from
the real code and data in D:\\Code\\mycroft\\verification-layer. Run:

    python assets/evidence/m9_evidence.py

READ-ONLY against the verification layer. The database is opened with mode=ro, and no
decision is ever recorded: validate_decision() is a pure function, and calling it records
nothing. Outputs go to assets/evidence/out/.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VL = Path(r"D:\Code\mycroft\verification-layer")
OUT = Path(__file__).resolve().parent / "out"
sys.path.insert(0, str(VL))

from datasources.filings import find_in_document  # noqa: E402
from validation.gate import (DecisionError, IDENTITY_NOTE, MIN_RATIONALE, gate_state,  # noqa: E402
                             validate_decision)

FIX = VL / "web" / "frontend" / "tests" / "fixtures"
DB = VL / "web" / "data" / "accountability.db"
INPUTS = {
    "gated_auditor": FIX / "run_compare_gated_auditor.json",
    "gated_investor": FIX / "run_compare_gated_investor.json",
    "b3_aapl": FIX / "run_compare_b3_aapl.json",
    "aapl_10q": VL / "tests" / "fixtures" / "aapl_10q_2026q3_trimmed.htm",
    "stream": FIX / "stream_compare_aapl_2026-09-24.txt",
    "database": DB,
}
GATED = "ec1a3b44"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(name: str, obj) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=str) + "\n",
                                      encoding="utf-8")
    print(f"--- {name}")
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str)[:1400])


def load(key: str):
    return json.loads(INPUTS[key].read_text(encoding="utf-8"))


def db_rows(sql: str, args=()):
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        return [dict(r) for r in con.execute(sql, args)]
    finally:
        con.close()


# B00 / B07 — the gated run, as stored right now, with its recorded decisions (expected: none).
def b00_b07():
    run = db_rows("select run_id, payload_json, created_at from runs where run_id like ?", (GATED + "%",))
    decisions = db_rows("select * from gate_decisions where run_id like ? order by decided_at", (GATED + "%",))
    payload = json.loads(run[0]["payload_json"]) if run else {}
    state = gate_state(payload, decisions) if payload else None
    rows = [(r["metric"], r["status"], r["raw_a"], r["raw_b"])
            for r in (payload.get("cross_agent_comparison") or {}).get("metric_comparisons") or []]
    dump("B00_B07_gated_run_now", {
        "run_id": run[0]["run_id"] if run else None, "stored_at": run[0]["created_at"] if run else None,
        "subject": payload.get("subject") or payload.get("ticker"), "rows": rows,
        "gate_status_now": state and state["status"], "pending": state and state["pending"],
        "decisions_recorded": len(decisions), "identity_note": IDENTITY_NOTE,
    })


# B02 — what gates and what doesn't: the gated run vs a run with only one-sided rows.
def b02():
    gated, aapl = load("gated_auditor"), load("b3_aapl")
    dump("B02_trigger", {
        "gated_run": {"id": gated["run_id"][:8], "gate": gated["gate"]["status"],
                      "rows": [(r["label"], r["status"]) for r in gated["cross_agent_comparison"]["metric_comparisons"]]},
        "one_sided_run": {"id": aapl["run_id"][:8], "gate": aapl["gate"]["status"],
                          "contradiction_flag": aapl["cross_agent_comparison"].get("contradiction_flag"),
                          "rows": [(r["label"], r["status"]) for r in aapl["cross_agent_comparison"]["metric_comparisons"]]},
        "pre_gate_run_status": gate_state({}, [])["status"],
    })


# B03 / B04 — the decision rules, exercised on the real gated payload. Pure function: nothing
# is written. Each body is deliberately wrong in one way; the refusal text is the server's.
def b03_b04():
    payload = load("gated_auditor")
    good = {"decision": "accept_a", "decided_by": "J. Reviewer",
            "rationale": "Pokemon Red and Blue reached North America in September 1998.",
            "cited_items": ["release_year"]}
    trials = {
        "looks good (10 chars)": {**good, "rationale": "looks good"},
        "no name": {**good, "decided_by": "J"},
        "cites an undisputed figure": {**good, "cited_items": ["revenue"]},
        "value without override": {**good, "final_value": 1998},
        "override without a value": {**good, "decision": "override_value"},
        "valid (NOT recorded)": good,
    }
    out = {}
    for name, body in trials.items():
        try:
            validate_decision(payload, body)
            out[name] = "accepted by validate_decision (this script records nothing)"
        except DecisionError as e:
            out[name] = f"refused: {e}"
    dump("B03_B04_decision_rules", {"min_rationale": MIN_RATIONALE, "trials": out})


# B06 — the investor read: search both stored reads for the disputed years.
def b06():
    aud = INPUTS["gated_auditor"].read_text(encoding="utf-8")
    inv = INPUTS["gated_investor"].read_text(encoding="utf-8")
    invj = json.loads(inv)
    live = None
    try:  # the running server, read at investor scope (a read; records nothing)
        import urllib.request
        req = urllib.request.Request("http://127.0.0.1:8000/api/auth/token", data=b'{"scope": "investor"}',
                                     headers={"Content-Type": "application/json"})
        tok = json.loads(urllib.request.urlopen(req, timeout=10).read())["access_token"]
        body = urllib.request.urlopen(urllib.request.Request(
            f"http://127.0.0.1:8000/api/runs/{invj['run_id']}", headers={"Authorization": "Bearer " + tok}),
            timeout=10).read().decode("utf-8")
        at = body.find("1998")
        live = {"1998": body.count("1998"), "1996": body.count("1996"),
                "where_1998_appears": body[max(0, at - 160): at + 40] if at >= 0 else None}
    except Exception as e:  # server not running: say so, don't guess
        live = {"error": f"live read skipped: {e}"}
    at = inv.find("1998")
    dump("B06_investor_view", {
        "investor_read_live": live,
        "where_1998_appears_in_fixture": inv[max(0, at - 160): at + 40] if at >= 0 else None,
        "auditor_read": {"1998": aud.count("1998"), "1996": aud.count("1996")},
        "investor_read": {"1998": inv.count("1998"), "1996": inv.count("1996")},
        "investor_rows": [(r["label"], r["status"], r.get("raw_a"), r.get("raw_b"))
                          for r in invj["cross_agent_comparison"]["metric_comparisons"]],
        "investor_note": invj.get("withheld_pending_review") or invj.get("gate", {}).get("status"),
    })


# B08-B11 — accounting checks as stored on real runs.
def checks(payload: dict) -> list[dict]:
    flags = (payload.get("cross_agent_comparison") or {}).get("structural_flags") or []
    if isinstance(flags, dict):
        flags = flags.get("checks") or []
    keep = ("key", "rule", "kind", "scope", "who", "outcome", "plain", "math", "reason", "gates")
    return [{k: c.get(k) for k in keep if k in c} for c in flags]


def b08_b11():
    aapl = load("b3_aapl")
    googl = [r for r in db_rows("select run_id, ticker, payload_json from runs where ticker = 'GOOGL' order by created_at desc")
             if '"structural_flags"' in r["payload_json"]]
    g = json.loads(googl[0]["payload_json"]) if googl else {}
    import re
    msft_slip = []
    for r in db_rows("select run_id, payload_json from runs where ticker = 'MSFT'"):
        m = re.search(r".{60}\$828,86.{80}", r["payload_json"])
        if m:
            msft_slip.append({"run_id": r["run_id"][:8], "excerpt": m.group(0)})
    dump("B08_B11_checks", {
        "aapl_run": aapl["run_id"][:8], "aapl_checks": checks(aapl),
        "googl_run": googl[0]["run_id"][:8] if googl else None,
        "googl_unusual": [c for c in checks(g) if c.get("kind") == "heuristic" and c.get("outcome") != "pass"],
        "msft_slip": msft_slip,
    })


# B12 — locate a companyfacts figure in the real (trimmed) Apple 10-Q, offline.
def b12():
    html = INPUTS["aapl_10q"].read_text(encoding="utf-8")
    out = {}
    for concept in ("Revenues", "NetIncomeLoss", "EarningsPerShareDiluted"):
        occ, note = find_in_document(html, concept, "2026-03-29", "2026-06-27")
        o = occ[0] if occ else None
        out[concept] = None if o is None else {
            "row_label": o.row_label, "column_header": o.column_header, "displayed": o.displayed,
            "value": o.value, "scale": o.scale, "occurrences": len(occ), "note": note,
            "excerpt": o.excerpt[:220]}
    dump("B12_filing_excerpt", {"filing": "Apple 10-Q, accn 0000320193-26-000020 (trimmed fixture)",
                                "period": ["2026-03-29", "2026-06-27"], "found": out,
                                "live_batch_logged": "24 of 24 figures found, every filed value equal to companyfacts (RUN_LOG BP+U4)"})


# B13 — the live-lane events, from the real captured stream.
def b13():
    kinds, phases = {}, {}
    kind = None
    for line in INPUTS["stream"].read_text(encoding="utf-8").splitlines():
        if line.startswith("event:"):
            kind = line[6:].strip()
            kinds[kind] = kinds.get(kind, 0) + 1
        elif line.startswith("data:") and kind == "step_started":
            d = json.loads(line[5:])
            phases.setdefault(d.get("phase"), []).append(d.get("label"))
    dump("B13_stream_events", {"event_counts": kinds, "steps_by_phase": phases})


# B18 — the ledger entries the honest-ledger beat cites.
def b18():
    from web.self_report import KNOWN_ISSUES
    ids = ("audit-criticals", "gate-identity-self-declared", "ollama-hangs-under-compare", "filing-excerpt-coverage")
    dump("B18_ledger", [{k: i.get(k) for k in ("id", "severity", "status", "title", "detail")}
                        for i in KNOWN_ISSUES if i.get("id") in ids])


def env():
    head = subprocess.run(["git", "-C", str(VL), "log", "-1", "--format=%h %cs %s"], capture_output=True, text=True).stdout.strip()
    dirty = len(subprocess.run(["git", "-C", str(VL), "status", "--short"], capture_output=True, text=True).stdout.splitlines())
    dump("run_env", {"ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "python": platform.python_version(), "platform": platform.platform(),
                     "verification_layer_head": head, "uncommitted_paths": dirty,
                     "inputs_sha256": {k: sha(p) for k, p in INPUTS.items()},
                     "note": "the database hash changes whenever a run is stored"})


if __name__ == "__main__":
    env()
    b00_b07()
    b02()
    b03_b04()
    b06()
    b08_b11()
    b12()
    b13()
    b18()
