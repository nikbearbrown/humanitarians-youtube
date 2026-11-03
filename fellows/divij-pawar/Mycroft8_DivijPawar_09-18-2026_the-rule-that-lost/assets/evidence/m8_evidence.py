"""
Executable evidence for Mycroft 8 — The Rule That Lost.

Per brutalist.art/docs/EXECUTABLE-EVIDENCE.md: every number a beat shows is computed here from
the real code and data in D:\\Code\\mycroft\\verification-layer, not typed into a scene. Run:

    python assets/evidence/m8_evidence.py

It only READS the verification layer (fixtures, the corpus, the stored-run database). It writes
nothing there. Outputs land in assets/evidence/out/: one JSON per beat plus run_env.json (Python
version, the checkout's HEAD and dirty-path count, SHA-256 of every input file).
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

VL = Path(r"D:\Code\mycroft\verification-layer")
OUT = Path(__file__).resolve().parent / "out"
sys.path.insert(0, str(VL))

from datasources.edgar import select_fact  # noqa: E402
from validation.concept_linkage import contradiction_flag_concept_aware, tag_numbers  # noqa: E402
from validation.facts import contradiction_flag_canonical  # noqa: E402

FIX = VL / "web" / "frontend" / "tests" / "fixtures"
INPUTS = {
    "companyfacts": VL / "tests" / "fixtures" / "edgar_aapl_companyfacts_sample.json",
    "corpus": VL / "tests" / "fixtures" / "cross_agent_real_runs_corpus.json",
    "stream": FIX / "stream_compare_aapl_2026-09-24.txt",
    "run_pre_b1": FIX / "run_compare_auditor.json",
    "run_b1_msft": FIX / "run_compare_b1.json",
    "run_b3_aapl": FIX / "run_compare_b3_aapl.json",
}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(name: str, obj) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=str) + "\n",
                                      encoding="utf-8")
    print(f"--- {name}")
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str)[:1500])


def load(key: str):
    return json.loads(INPUTS[key].read_text(encoding="utf-8"))


# B02 — what the pre-B0 rule handed the agents (the legacy rule reproduced verbatim from
# tests/test_edgar_facts.py::_legacy_latest_entry), next to what the entry actually was.
def legacy_latest_entry(facts: dict, concept: str) -> dict:
    units = facts["facts"]["us-gaap"][concept]["units"]
    entries = [e for es in units.values() for e in es if isinstance(e.get("val"), (int, float))]
    return max(entries, key=lambda e: e.get("end", ""))


def days(e: dict) -> int | None:
    if not e.get("start"):
        return None
    return (date.fromisoformat(e["end"]) - date.fromisoformat(e["start"])).days


def b02_b03():
    facts = load("companyfacts")
    rows = []
    for concept in ("Revenues", "EarningsPerShareDiluted", "NetIncomeLoss", "Assets"):
        old = legacy_latest_entry(facts, concept)
        new = select_fact(facts, concept)
        rows.append({
            "concept": concept,
            "legacy_handed": old.get("val"),
            "legacy_entry": {k: old.get(k) for k in ("start", "end", "fy", "fp", "form", "frame")},
            "legacy_span_days": days(old),
            "b0_selected": new.value if new else None,
            "b0_describe": new.describe() if new else None,
        })
    dump("B02_B03_what_they_were_handed", {"source": str(INPUTS["companyfacts"].name), "rows": rows})


# B05 — the two agents' overlap, from the real captured stream's started_at stamps.
def b05():
    events, kind = [], None
    for line in INPUTS["stream"].read_text(encoding="utf-8").splitlines():
        if line.startswith("event:"):
            kind = line[6:].strip()
        elif line.startswith("data:"):
            try:
                events.append((kind, json.loads(line[5:].strip())))
            except json.JSONDecodeError:
                pass
    spans: dict[str, list[datetime]] = {}
    for kind, step in events:
        # step_finished carries both started_at and duration_ms; phase is shared / agent slot
        if kind != "step_finished" or not step.get("started_at") or step.get("duration_ms") is None:
            continue
        who = str(step.get("phase") or "")
        t0 = datetime.fromisoformat(step["started_at"])
        end = t0.timestamp() + float(step["duration_ms"]) / 1000
        spans.setdefault(who, []).extend([t0, datetime.fromtimestamp(end, tz=timezone.utc)])
    summary = {k: {"first": min(v).isoformat(), "last": max(v).isoformat()} for k, v in spans.items() if k}
    agents = [k for k in summary if k and k.lower() not in ("shared", "none")]
    result = {"events": len(events), "per_agent_span": summary}
    if len(agents) >= 2:
        a, b = agents[:2]
        sa, ea = min(spans[a]), max(spans[a])
        sb, eb = min(spans[b]), max(spans[b])
        result["start_gap_ms"] = round(abs((sa - sb).total_seconds()) * 1000, 1)
        result["overlap_s"] = round(max(0.0, (min(ea, eb) - max(sa, sb)).total_seconds()), 1)
    result["logged_values"] = "RUN_LOG 2026-09-24 BL: AAPL start gap 1 ms, overlap 39.4 s"
    dump("B05_overlap_from_stream", result)


# B06 / B13 — rows straight from stored runs.
def rows(run: dict, *metrics: str) -> list[dict]:
    cmp_ = run.get("cross_agent_comparison") or {}
    return [r for r in cmp_.get("metric_comparisons") or [] if not metrics or r.get("metric") in metrics]


def b06_b13():
    aapl = load("run_b3_aapl")
    dump("B13_first_shared_match", {"run_id": aapl["run_id"], "ticker": aapl.get("ticker"),
                                    "rows": rows(aapl, "net_income", "eps")})


# B07 / B08 / B09 — replay the labelled corpus through both rules, exactly as
# tests/test_facts.py::TestAgainstLabeledCorpus does.
def b07_b09():
    corpus = load("corpus")
    replay, derived = [], []
    for run in corpus["runs"]:
        a, b = run.get("agent_a_conclusion"), run.get("agent_b_conclusion")
        if not (a and b):
            continue
        flag, divergent, mrows = contradiction_flag_canonical(a, b)
        ca_flag = contradiction_flag_concept_aware(a, b)[0]
        replay.append({"run_id": run["run_id"][:8], "label": run["label"],
                       "concept_aware": ca_flag, "canonical": flag, "divergent": sorted(divergent)})
        for r in mrows:
            if r.status in ("DERIVED_WRONG", "DERIVED_OK"):
                derived.append({"run_id": run["run_id"][:8], "status": r.status, "label": r.label,
                                "stated": r.raw_a or r.raw_b, "note": r.note,
                                "conclusion_opening": (a if r.raw_a else b)[:140]})
    disjoint = [r for r in replay if r["label"] == "disjoint_concepts"]
    dump("B09_corpus_replay", {
        "disjoint_concepts_runs": len(disjoint),
        "concept_aware_flags": sum(r["concept_aware"] for r in disjoint),
        "canonical_flags": sum(r["canonical"] for r in disjoint),
        "canonical_flagged_ids": sorted(r["run_id"] for r in disjoint if r["canonical"]),
        "all": replay,
    })
    dump("B07_derivation_checks", {"rows": derived,
                                   "arithmetic": {"revenue_B": 265.6, "assets_B": 383.3,
                                                  "revenue_over_assets": round(265.6 / 383.3, 4)}})
    # B08 — how the old tagger files "Return on Assets": the real function on the real phrase.
    phrases = [r["agent_a_conclusion"] for r in corpus["runs"] if "Return on Assets" in (r.get("agent_a_conclusion") or "")]
    phrases += [r["agent_b_conclusion"] for r in corpus["runs"] if "Return on Assets" in (r.get("agent_b_conclusion") or "")]
    sample = phrases[0] if phrases else "Return on Assets of 18.85%"
    at = sample.find("Return on Assets")
    dump("B08_old_tagger_on_return_on_assets", {
        "excerpt": sample[max(0, at - 40): at + 80] if at >= 0 else sample,
        "tag_numbers": [list(t) for t in tag_numbers(sample) if "%" in t[0] or "." in t[0]][:6],
        "source": "first corpus conclusion containing 'Return on Assets'" if phrases else "constructed phrase",
    })


# B10 — stored-record growth: a pre-B1 stored run vs a B1 one.
def b10():
    pre, post = load("run_pre_b1"), load("run_b1_msft")
    dump("B10_record_growth", {"pre_b1": {"run_id": pre["run_id"][:8], "keys": sorted(pre)},
                               "b1": {"run_id": post["run_id"][:8], "keys": sorted(post)},
                               "counts": [len(pre), len(post)]})


# B06 — (a) the Microsoft-format revenue pair, replayed exactly as tests/test_facts.py line ~114
# builds it. This is a CONSTRUCTED test input in Microsoft's filed format, not a stored run:
# label it that way on screen. (b) The real stored NVDA run whose self-rated "Confidence level:
# 90%" the pre-B1 rule treated as a figure.
DB = VL / "web" / "data" / "accountability.db"


def stored_run(prefix: str) -> dict | None:
    import sqlite3
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    try:
        row = con.execute("select payload_json from runs where run_id like ?", (prefix + "%",)).fetchone()
    finally:
        con.close()
    return json.loads(row[0]) if row else None


def conclusions(run: dict) -> list[str]:
    return [o.get("conclusion") or "" for o in run.get("reasoning_objects") or [] if o.get("conclusion")]


def b06():
    from core.numeric import extract_numbers
    from validation.facts import extract_facts

    a = "Q3 FY2026 revenue was 82,886,000,000.0 USD."
    b = "Q3 FY2026 revenue of $82.9 billion."
    _, _, mrows = contradiction_flag_canonical(a, b)
    test_case = [{"label": r.label, "status": r.status, "raw_a": r.raw_a, "raw_b": r.raw_b,
                  "variance_pct": r.variance_pct} for r in mrows]
    old_divergent = sorted(set(extract_numbers(a)) ^ set(extract_numbers(b)))

    nvda = stored_run("2220eba0")
    conf = None
    if nvda:
        texts = conclusions(nvda)
        conf = {
            "run_id": "2220eba0", "ticker": nvda.get("ticker"),
            "stored_flag": (nvda.get("cross_agent_comparison") or {}).get("contradiction_flag"),
            "stored_divergent": (nvda.get("cross_agent_comparison") or {}).get("divergent_numbers"),
            "b1_facts_per_agent": [[(f.metric, f.raw) for f in extract_facts(t)] for t in texts],
            "confidence_90_in_b1_facts": any(f.raw.startswith("90") for t in texts for f in extract_facts(t)),
        }
    dump("B06_figures_not_strings", {
        "msft_format_test_case": {"source": "tests/test_facts.py (constructed input, Microsoft's filed format)",
                                  "a": a, "b": b, "canonical_rows": test_case,
                                  "old_set_difference": old_divergent},
        "nvda_confidence_stored_run": conf,
    })


# B04 — real tool steps where the model's own search arguments failed and the one
# query-only retry recovered (recorded after the B0 fix, which added args/retried_query_only).
# The pre-fix "status: ok" line itself was never stored with its arguments; show it only as a
# labelled reconstruction from RUN_LOG 2026-09-24 B0.
def b04():
    import sqlite3
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    rows = con.execute("select run_id, ticker, payload_json from runs order by created_at").fetchall()
    con.close()
    steps = []
    for rid, ticker, p in rows:
        d = json.loads(p)
        for st in d.get("steps") or []:
            if st.get("kind") == "tool" and st.get("retried_query_only"):
                steps.append({"run_id": rid[:8], "ticker": ticker, "status": st.get("status"),
                              "args": st.get("args"), "urls": len(st.get("urls") or [])})
    dump("B04_search_args_and_retry", {"retried_steps": len(steps), "first_three": steps[:3],
                                       "reconstruction_note": "pre-fix recorder stored no args; the 'ok' line is a reconstruction (RUN_LOG B0)"})


# B11 — replay the directive-echo detector over every stored conclusion, today.
def b11():
    import sqlite3
    from core.directive import _DIRECTIVE_REGISTRY
    from core.parsing import find_directive_echo

    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    payloads = [json.loads(p) for (p,) in con.execute("select payload_json from runs")]
    con.close()
    total, echoed, examples = 0, 0, []
    for p in payloads:
        for c in conclusions(p):
            total += 1
            hit = next((find_directive_echo(c, d.text) for d in _DIRECTIVE_REGISTRY.values()
                        if find_directive_echo(c, d.text)), None)
            if hit:
                echoed += 1
                if len(examples) < 3:
                    examples.append({"run_id": p.get("run_id", "")[:8], "echoed_window": hit})
    dump("B11_echo_replay_today", {"conclusions": total, "echoed": echoed, "examples": examples,
                                   "logged_on_2026_09_24": "17 of 135 (RUN_LOG 'Directive echo, properly')",
                                   "note": "More runs have been stored since; the logged figure is the one the script cites."})


def env():
    head = subprocess.run(["git", "-C", str(VL), "log", "-1", "--format=%h %cs %s"], capture_output=True, text=True).stdout.strip()
    dirty = len(subprocess.run(["git", "-C", str(VL), "status", "--short"], capture_output=True, text=True).stdout.splitlines())
    dump("run_env", {"ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "python": platform.python_version(), "platform": platform.platform(),
                     "verification_layer_head": head, "uncommitted_paths": dirty,
                     "inputs_sha256": {k: sha(p) for k, p in INPUTS.items()}})


if __name__ == "__main__":
    env()
    b02_b03()
    b05()
    b06_b13()
    b04()
    b06()
    b07_b09()
    b10()
    b11()
