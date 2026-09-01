"""Author beat_sheet.json for the reel `data-contract-simulation`.

Kept as a script rather than hand-edited JSON so the 16:9 sheet and its 9:16
derivative can never drift: `make_916.py` reads this sheet and rewrites only the
pattern ids. Narration is authored once, here.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

TOPIC = "DATA CONTRACTS · SCHEMA CHANGE"
SEGMENT = "Prove The Number Changed"

# ── the real source, trimmed to the lines that teach (THE ACTUAL-CODE LAW) ──
CODE_BUILD = '''# simulate.py - the DAG is rebuilt straight from the dbt manifest
def build_models(con, graph, order, patched_sql=None):
    """Materialize every model as a table, sources-first."""
    errors = {}
    for model in order:
        node = graph.models[name_to_id[model]]
        sql  = patched_sql.get(model) or graph.normalize_sql(
                   node.get("compiled_code") or "")
        try:
            con.execute(f'CREATE OR REPLACE TABLE "{model}" AS {sql}')
        except Exception as exc:          # a build failure IS the finding
            errors[model] = f"{type(exc).__name__}: {_first_line(exc)}"
    return errors'''

CODE_TWOPASS = '''# simulate.py - build twice: the loud half, then the quiet half
drop_models(con, order)
as_is_errors = build_models(con, graph, order)      # pass 1: what stops compiling
report.as_is_failures = as_is_errors

if auto_patch:                                       # pass 2: the reviewer's fix
    patched_sql, records = _patch_map(infer_renames(changes), graph, index)
    drop_models(con, order)
    errors = build_models(con, graph, order, patched_sql=patched_sql)
    snap   = snapshot(con, order, errors)

# ...and the patch is scoped by LINEAGE, never by name:
for pair in renames:
    for model in index.models_reading(pair.table, pair.old_column):
        per_model.setdefault(model, {})[pair.old_column] = pair.new_column'''


def beat(bid, act, pattern, narration, props, est, shot_type="GRAPHIC",
         motion="type-on", show=None):
    return {
        "beat_id": bid,
        "act": act,
        "narration_text": narration,
        "shot": {
            "type": shot_type,
            "source": "remotion",
            "motion": motion,
            "show": show or [],
            "remotion": {
                "pattern": pattern,
                "props": props,
                "rendered": {"out": f"media/{bid}.mp4", "at": ""},
            },
        },
        "estimated_duration_s": est,
        "audio_file": f"mp3/beat-{bid}.mp3",
        "actual_duration_s": None,
    }


BEATS = [
    # ── B00 INTRO ───────────────────────────────────────────────────────────
    beat(
        "B00", "INTRO", "ClaudeComposerAsk",
        "Hi, I am Hussain, and this video is about a data contract agent I built, "
        "and the feature I shipped into it today. It catches schema changes that "
        "compile, run, pass every test, and return a number that is simply wrong.",
        {
            "greeting": "Konnichiwa, Hussain",
            "topic": TOPIC,
            "segment": SEGMENT,
            "command": "here is an Alembic migration and my dbt manifest. tell me which "
                       "analytics models this change breaks - and which ones will keep "
                       "running while returning the wrong number.",
            "runningText": "tracing column lineage…",
            "output": [
                "parsed 4 schema changes · 9 dbt models indexed",
                "2 models read the dropped column - they will fail loudly",
                "1 metric will keep compiling and be wrong",
            ],
            "folderLabel": "Mohammed Hussain",
            "modelLabel": "Opus 5",
            "effortLabel": "High",
        },
        est=20,
        show=[
            {"at": "0.00", "event": "cream page, spark + serif greeting above an empty composer"},
            {"at": "0.15", "event": "the ask types itself in, character by character"},
            {"at": "0.70", "event": "send arms terracotta; running indicator reads 'tracing column lineage…'"},
            {"at": "0.85", "event": "three result lines stagger in - the ask lands answered"},
        ],
    ),

    # ── B01 PROBLEM ─────────────────────────────────────────────────────────
    beat(
        "B01", "PROBLEM", "SimSilentBreak",
        "Here is the shape of it. An engineer renames amount cents to amount, and "
        "divides by a hundred to match. Nothing crashes. But the staging layer was "
        "already dividing by a hundred. Monthly revenue is now a hundred times too "
        "low, and not one test fires.",
        {
            "durationSeconds": 18,
            "sparkLine": "It compiles. It lies.",
            "opColumn": "subscriptions.amount_cents",
            "newColumn": "subscriptions.amount",
            "backfill": "UPDATE subscriptions SET amount = amount_cents / 100.0",
            "stagingLine": "amount_cents / 100.0  AS amount_usd",
            "beforeLabel": "fct_mrr",
            "beforeValue": 108176.33,
            "afterValue": 1081.76,
            "verdict": "every model compiles · zero tests fail",
        },
        est=18, motion="reveal",
        show=[
            {"at": "0.00", "event": "the operational column on the left, the staging line on the right"},
            {"at": "0.35", "event": "the rename lands; the /100 in staging stays put, ringed terracotta"},
            {"at": "0.70", "event": "the MRR figure rolls down two decimal places and settles"},
            {"at": "0.88", "event": "'every model compiles - zero tests fail' types beneath"},
        ],
    ),

    # ── B02 CLI (cycle 1) ───────────────────────────────────────────────────
    beat(
        "B02", "CLI", "ClaudeComposerAsk",
        "My agent already proved which models read that column. That is not the same "
        "as knowing what breaks. So I asked for the layer that measures: build the "
        "warehouse before and after, and diff the marts.",
        {
            "greeting": "The ask,",
            "topic": TOPIC,
            "segment": SEGMENT,
            "command": "add a simulation layer. stand up a throwaway DuckDB warehouse, "
                       "materialize the dbt DAG from the manifest's compiled_code, replay "
                       "the parsed migration onto the source tables, rebuild, and diff "
                       "every mart total before against after.",
            "runningText": "building the simulation…",
            "output": [
                "contract_agent/simulate.py · new",
                "sources → DAG → replay → rebuild → diff",
            ],
            "folderLabel": "Mohammed Hussain",
            "modelLabel": "Opus 5",
            "effortLabel": "High",
        },
        est=15,
    ),

    # ── B03 CODE ────────────────────────────────────────────────────────────
    beat(
        "B03", "CODE", "ClaudeCodeBeat",
        "This is the real code. Notice what it never does: call dbt. Every model's "
        "compiled S Q L already sits in the manifest, so it just runs it, in "
        "dependency order, against a throwaway database. A model that fails to "
        "build is the finding.",
        {
            "title": "contract_agent/simulate.py",
            "code": CODE_BUILD,
            "sparkLine": "The failure is the finding.",
        },
        est=19, motion="type-on",
    ),

    # ── B04 OUTPUT 1 ────────────────────────────────────────────────────────
    beat(
        "B04", "OUTPUT", "SimLoudHalf",
        "And the first run failed. Usefully. Dropping the old column means every model "
        "that reads it stops compiling. Four go red. But that is the loud half - "
        "your build would have caught it. It tells me nothing new.",
        {
            "durationSeconds": 16,
            "sparkLine": "The loud half.",
            "heading": "Build as-is",
            "rows": [
                {"model": "stg_subscriptions", "state": "fail",
                 "detail": "BinderException: column \"amount_cents\" not found"},
                {"model": "fct_mrr", "state": "blocked", "detail": "blocked by stg_subscriptions"},
                {"model": "fct_revenue", "state": "blocked", "detail": "blocked by stg_subscriptions"},
                {"model": "dim_users", "state": "blocked", "detail": "blocked by stg_subscriptions"},
                {"model": "stg_users", "state": "pass", "detail": "built"},
                {"model": "fct_engagement", "state": "pass", "detail": "built"},
            ],
            "footer": "4 red · loud · already proved by the deterministic layer",
        },
        est=16, motion="stagger",
    ),

    # ── B05 CLI (cycle 2 = the revision) ────────────────────────────────────
    beat(
        "B05", "CHANGE", "ClaudeComposerAsk",
        "So here is the change. Nobody merges a red pipeline. A reviewer renames the "
        "column in staging and moves on, and that is exactly the state where the "
        "number is wrong. So build twice: once as it is, then again with the "
        "reviewer's fix.",
        {
            "greeting": "The change,",
            "topic": TOPIC,
            "segment": SEGMENT,
            "command": "build twice. pass one records what fails outright. pass two "
                       "applies the mechanical rename a reviewer would apply, then diffs "
                       "from there. scope the rename by lineage, not by name - "
                       "transactions has its own amount_cents and must not be touched.",
            "runningText": "updating…",
            "output": [
                "pass 1 · as-is        → 4 models fail",
                "pass 2 · post-fix     → 0 models fail",
                "patched: stg_subscriptions only",
            ],
            "folderLabel": "Mohammed Hussain",
            "modelLabel": "Opus 5",
            "effortLabel": "High",
        },
        est=18,
    ),

    # ── B06 CODE (the revision) ─────────────────────────────────────────────
    beat(
        "B06", "CODE", "ClaudeCodeBeat",
        "Two things to verify. Pass one records what breaks. Pass two applies the "
        "rename and measures from there. And the patch is scoped by lineage, not by "
        "name - transactions has its own amount cents column, and a find and "
        "replace would have corrupted a second metric.",
        {
            "title": "contract_agent/simulate.py  ·  the revision",
            "code": CODE_TWOPASS,
            "sparkLine": "Scoped by lineage, not by name.",
        },
        est=21, motion="type-on",
    ),

    # ── B07 OUTPUT 2 — the money shot ───────────────────────────────────────
    beat(
        "B07", "OUTPUT", "SimMoneyShot",
        "Now the second run. Everything compiles. Nothing is red. And monthly "
        "recurring revenue reads one hundredth of what it read before. The warning "
        "is a number now, not a hunch.",
        {
            "durationSeconds": 16,
            "sparkLine": "A number, not a hunch.",
            "heading": "Post-fix · everything compiles",
            "rows": [
                {"metric": "sum(monthly_amount_usd)", "before": 108176.33, "after": 1081.76, "scale": "x0.01"},
                {"metric": "avg(monthly_amount_usd)", "before": 93.90, "after": 0.94, "scale": "x0.01"},
                {"metric": "rows", "before": 1152, "after": 1152, "scale": "unchanged"},
            ],
            "verdict": "fct_mrr · rescaled x0.01 while still compiling — units changed",
        },
        est=16, motion="count",
    ),

    # ── B08 SUMMARY ─────────────────────────────────────────────────────────
    beat(
        "B08", "SUMMARY", "SimThreeLayers",
        "Three layers, each earning its place. The deterministic layer proves "
        "structure. The language model reads intent. The simulation measures "
        "damage. And the row count never moved - which is exactly why schema tests "
        "sail straight past this.",
        {
            "durationSeconds": 17,
            "sparkLine": "Prove. Read. Measure.",
            "layers": [
                {"name": "Deterministic", "verb": "proves structure",
                 "detail": "column lineage from the dbt manifest · what reads what"},
                {"name": "Language model", "verb": "reads intent",
                 "detail": "the PR says “standardize the amount column” · is that a unit change?"},
                {"name": "Simulation", "verb": "measures damage",
                 "detail": "rebuild both sides · diff the marts · 108,176.33 → 1,081.76"},
            ],
            "footer": "row count: unchanged — which is why the tests stayed green",
        },
        est=17, motion="stack",
    ),

    # ── B09 NEXT STEPS ──────────────────────────────────────────────────────
    beat(
        "B09", "NEXT STEPS", "ClaudeComposerAsk",
        "Your turn. Paste this into Claude Code, pointed at your own warehouse. Replay "
        "a migration you already shipped, and ask which mart totals move. The "
        "interesting answer is the one you were not expecting.",
        {
            "greeting": "Your turn.",
            "topic": TOPIC,
            "segment": SEGMENT,
            "command": "take my dbt manifest and my last schema migration. replay it "
                       "against a throwaway DuckDB copy of my sources, rebuild every "
                       "model, and show me which mart totals moved - and by what ratio.",
            "runningText": "paste this into Claude…",
            "output": [
                "start with a migration you already shipped",
                "look for a clean power-of-ten ratio - that is a unit change",
            ],
            "folderLabel": "Mohammed Hussain",
            "modelLabel": "Opus 5",
            "effortLabel": "High",
        },
        est=17,
    ),

    # ── B10 OUTRO ───────────────────────────────────────────────────────────
    beat(
        "B10", "OUTRO", "ClaudeTitleOutro",
        "Prove the number changed.",
        {
            "title": "Prove The Number Changed.",
            "handle": "Mohammed Hussain",
            "subline": "A data contract agent that measures the damage instead of guessing at it.",
        },
        est=5, motion="reveal",
    ),
]

SHEET = {
    "metadata": {
        "title": "Prove The Number Changed.",
        "youtube_title": "Prove The Number Changed — Catching Schema Breaks That Compile Clean",
        "slug": "data-contract-simulation",
        "topic": TOPIC,
        "register": "Teardown",
        "audience": "Claude",
        "brand": "claude",
        "palette": "claude",
        "style_preset": "claude",
        "ground": "#FAF9F5",
        "engine": "kokoro",
        "voice_kokoro": "am_onyx",
        "aspect_ratio": "16:9",
        "fit": "contain",
        "greeting": "Konnichiwa, Hussain",
        "narrator": "Hussain",
        "folder_chip": "Mohammed Hussain",
        "note": (
            "cli-explainer build reel. Required spine honoured: B00 INTRO (cold open, "
            "ask lands answered) - B01 PROBLEM (stakes before the build) - B02/B03/B04 "
            "cycle 1 (CLI - CODE - moving OUTPUT) - B05/B06/B07 cycle 2, THE REVISION "
            "LAW (CHANGE - CODE - better OUTPUT) - B08 SUMMARY - B09 NEXT STEPS handoff "
            "- B10 OUTRO. Bespoke Remotion components for the four non-UI beats "
            "(SimSilentBreak, SimLoudHalf, SimMoneyShot, SimThreeLayers), one file, each "
            "registered twice so the 9:16 is a native reflow and never a centre-cut. "
            "NARRATOR OVERRIDE: first-person 'Hi, I am Hussain' intro; no IN-FOR-BEAR "
            "sign-off; folderLabel and outro handle read 'Mohammed Hussain'. "
            "ACTUAL-CODE LAW: B03 and B06 show real trimmed source from "
            "Mycroft/Data_Quality_Agent/data-contract-agent/contract_agent/simulate.py."
        ),
        "color_semantics": (
            "Claude fidelity palette. One terracotta moment per beat: the surviving /100 "
            "(B01), the failing model (B04), the x0.01 ratio (B07), the measuring layer "
            "(B08)."
        ),
        "tags": ["data contracts", "dbt", "data quality", "schema migration",
                 "DuckDB", "Claude Code", "data engineering", "AI"],
    },
    "beats": BEATS,
}

out = HERE / "beat_sheet.json"
out.write_text(json.dumps(SHEET, indent=1, ensure_ascii=False), encoding="utf-8")
words = sum(len(b["narration_text"].split()) for b in BEATS)
print(f"wrote {out}  ({len(BEATS)} beats, {words} words, "
      f"~{words / 2.7:.0f}s at 2.7 w/s, est {sum(b['estimated_duration_s'] for b in BEATS)}s)")
