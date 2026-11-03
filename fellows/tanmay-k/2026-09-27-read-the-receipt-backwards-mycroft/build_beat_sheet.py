#!/usr/bin/env python3
"""Week 24 work video, *Read the Receipt Backwards*: beat_sheet.json = SCRIPT.md's narration (the
source of truth for the words) + each beat's scene props.

ONE RECEIPT. A single Verifiable Intent record is on screen, read bottom to top. The lines are
ordered so the agent line is at the BOTTOM (the narration says "start at the bottom", then reads
agent → person → category → amount/date → path → merchant), and each line's stamp lands on its cue.

Cues are narration phrases ("…Cue" keys). With measured audio they resolve on the WHISPER clock
(cue_align.spoken_at_whisper, falling back to the pause clock); before audio, on the planning rate.

    python3 build_beat_sheet.py            # the real sheet
    PREVIEW=1 python3 build_beat_sheet.py  # _preview/beat_sheet.json: every beat in its end state,
                                           # 1.5s long, for the stills review before audio
"""
import copy, json, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent / "topic-video"
sys.path.insert(0, str(TOPIC))
from cue_align import spoken_at, spoken_at_whisper  # noqa: E402

PREVIEW = os.environ.get("PREVIEW") == "1"
WPS = 3.17

# --- sources, as shown on screen (FACTCHECK Part 1) ------------------------------------------------
VI = "Mastercard, “How Verifiable Intent builds trust in agentic AI commerce,” Mar 5 2026"
FW = "Mastercard, “Agentic token framework: Driving trusted AI transactions,” Oct 14 2025"
SIG = "Mastercard Signals report release (EEMEA newsroom), Aug 2026"
BUILD = "Reference build v2 (public information only) · live run, 82/82 tests"
DD = lambda n: f"Reference build v2 · docs/DESIGN_DECISIONS.md, DD{n:03d}"

# --- the receipt: a real v2 receipt (Devon's shoes, through the Gate), top → bottom ----------------
RECEIPT = [
    ("created_at", "2026-09-28 04:19 UTC"),
    ("merchant", "trailhead-running-co"),
    ("authorized_via", "authorization_gate"),
    ("transaction_date", "2026-09-01"),
    ("amount", "68.00"),
    ("category", "footwear"),
    ("consumer_id", "devon-01"),
    ("agent_id", "agent-concierge-01"),
]
STAMPS = {   # short enough to sit on one line; the review round is named in the panel, not the stamp
    "created_at": ("earned", "set by the build"),
    "agent_id": ("earned", "registered + verified"),
    "consumer_id": ("earned", "ownership check"),
    "category": ("earned", "permissions · one spelling"),
    "amount": ("earned", "validation + limit"),
    "transaction_date": ("earned", "validation + window"),
    "authorized_via": ("earned", "path taken"),
    "merchant": ("open", "carried · not checked"),
}
ORDER = ["agent_id", "consumer_id", "category", "amount", "transaction_date", "authorized_via", "merchant"]  # the film's reading order


def receipt(stamped=(), focus=None, focus_cue=None, stamp_cues=None, values=None, highlight=(), pending_all=False):
    """Lines top → bottom. stamped: keys whose stamp is already down; stamp_cues: {key: phrase} for
    stamps that land during this beat; focus: the line under discussion."""
    stamp_cues = stamp_cues or {}
    out = []
    for k, v in RECEIPT:
        state, stamp = STAMPS[k]
        line = {"key": k, "value": (values or {}).get(k, v), "state": "pending", "stamp": stamp, "stampAt": -1,
                "highlight": k in highlight, "dim": k == "created_at"}
        if not pending_all and (k in stamped or k in stamp_cues or k == "created_at"):
            line["state"] = state
            if k in stamp_cues:
                line["stampAtCue"] = stamp_cues[k]
        if k == focus:
            if focus_cue:
                line["focusAtCue"] = focus_cue
            else:
                line["focusAt"] = -1
        out.append(line)
    return out


def done_before(key):
    return ORDER[:ORDER.index(key)]


def scene(heading, lines, blocks, source, eyebrow="", badge="", seal=False, seal_cue=None):
    p = {"eyebrow": eyebrow, "heading": heading, "recordTitle": "VERIFIABLE INTENT RECORD · reference build",
         "badge": badge, "lines": lines, "blocks": blocks, "seal": seal, "sealAt": -1, "source": source}
    if seal_cue:
        p["sealAtCue"] = seal_cue
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate",
            "remotion": {"pattern": "ReceiptAuditOFL", "props": p}}


def quote(text, source, cue=None):
    b = {"kind": "quote", "text": text, "source": source}
    if cue: b["atCue"] = cue
    return b


def results(title, rows, cue=None):
    b = {"kind": "results", "title": title, "rows": rows}
    if cue: b["atCue"] = cue
    return b


def row(label, status, reason="", accent=False):
    return {"label": label, "status": status, "reason": reason, "accent": accent}


def chips(title, items, cue=None):
    b = {"kind": "chips", "title": title, "items": items}
    if cue: b["atCue"] = cue
    return b


def note(text, cue=None):
    b = {"kind": "note", "text": text}
    if cue: b["atCue"] = cue
    return b


LIVE = json.loads((HERE / "live_runs.json").read_text())   # real console transcripts (live_runs.py)


def term(key, title, cue=None):
    b = {"kind": "terminal", "title": title, "term": LIVE[key]["lines"]}
    if cue: b["atCue"] = cue
    return b


def result_of(key):
    """The last printed line of a live session, e.g. "('ESCALATED', 'outside_timeframe')"."""
    return [l["text"] for l in LIVE[key]["lines"] if l["kind"] == "out"][-1]


MORGAN = {"consumer_id": "morgan-02", "category": "household_staples", "merchant": "greenleaf-grocery",
          "amount": "42.50", "created_at": "(early version)"}

SHOTS = {
    "B01": scene("A receipt my own build once wrote",
                 receipt(values=MORGAN, highlight=("consumer_id",), pending_all=True, focus="consumer_id", focus_cue="authorized for Morgan"),
                 [note("An early version of this build wrote this receipt.", cue="Here's a receipt"),   # PROOF master fix: no empty opening panel
                  note("Every field is well-formed. It says Morgan authorized the purchase.", cue="Every line is filled in"),
                  note("Morgan never saw it. The agent belonged to Devon.", cue="Morgan never saw it")],
                 "Reconstruction of the early version, before review round 2 (README Finding #5); not the shipped code",
                 badge="RECONSTRUCTION · EARLY VERSION"),
    "B02": scene("Agent Pay's checks, built from public information",
                 receipt(pending_all=True),
                 [{"kind": "pipeline", "items": ["validation", "agent", "owner", "permissions", "gate", "receipt"], "active": 5, "atCue": "I built a working version"},
                  {"kind": "stat", "big": "82", "text": "tests · all passing", "atCue": "eighty-two tests"},
                  quote("a tamper-resistant record of what a user authorized", VI, cue="Mastercard has described")],
                 f"{VI} · {BUILD}", eyebrow="WHAT THIS IS"),
    "B03": dict(scene("Read it backwards: which step checked this line?",
                 receipt(pending_all=True),
                 [note("Start at the bottom. For every line: which step checked this?", cue="So here's how I read it now"),
                  note("Earned: a step checked it before it was written down.", cue="A line with an answer"),
                  note("Carried: nothing did.", cue="A line without one"),
                  quote("How do we know an agent is doing exactly what we asked — and nothing more?", VI, cue="Mastercard asks the same thing")],
                 VI, eyebrow="THE MOVE"), _sweep="Backwards."),
    "B04": scene("The agent line",
                 receipt(focus="agent_id", stamp_cues={"agent_id": "This line is earned"}),
                 [quote("begins by registering and verifying AI agents before they are permitted to transact", FW, cue="Mastercard's framework"),
                  chips("TWO SEPARATE CHECKS, TWO REASONS", ["unregistered_agent", "unverified_agent"], cue="two separate checks")],
                 f"{FW} · {DD(6)}"),
    "B05": scene("The person line",
                 receipt(stamped=done_before("consumer_id"), focus="consumer_id", stamp_cues={"consumer_id": "Now one step asks first"}),
                 [chips("REGISTERED + VERIFIED ≠ YOURS", ["agent-concierge-01 → registered to devon-01"], cue="An agent can be registered"),
                  results("EARLY VERSION (RECONSTRUCTION)", [row("Devon's agent, “for Morgan”", "COMPLETED", "receipt names morgan-02", accent=True)], cue="So Devon's agent could buy"),
                  term("B05", "TODAY · python3 · reference build v2", cue="Now one step asks first"),
                  quote("It confirms the cardholder authorizing the AI agent", VI, cue="Mastercard says its record")],
                 f"{VI} · {DD(9)} · reconstruction per README Finding #5"),
    "B06": scene("The category line",
                 receipt(stamped=done_before("category"), focus="category", stamp_cues={"category": "So now every category is compared"}),
                 [chips("DEVON'S RULE (mock data)", ["household_staples", "limit 150.00", "until 2026-12-31"], cue="Devon set a rule"),
                  results("ORIGINAL BUILD · $70, AFTER DEVON'S WINDOW", [row("household_staples", *eval(result_of("B06_lower_v1")))], cue="A grocery order dated after that"),
                  term("B06_upper_v1", "ORIGINAL BUILD · python3", cue="But write the category"),
                  term("B06_upper_v2", "V2 · python3", cue="So now every category is compared")],
                 f"{BUILD} · original build, live run · {DD(12)}"),
    "B07": scene("Where that fix stops, on purpose",
                 receipt(stamped=done_before("category") + ["category"], focus="category"),
                 [results("V2", [row("groceries", "NEW CATEGORY", "goes to the gate, by design")], cue="What I didn't do"),
                  note("Mapping synonyms would mean inventing a category list Mastercard hasn't published.", cue="That would mean inventing"),
                  chips("PINNED BY A TEST", ["test_synonym_is_still_unconfigured"], cue="in a test")],
                 DD(12)),
    "B08": scene("Amount and date",
                 receipt(stamped=done_before("amount"), focus="amount", stamp_cues={"amount": "Now they're stopped", "transaction_date": "Now they're stopped"}),
                 [term("B08", "ROUND 1 · NOW STOPPED AT THE DOOR · python3 · v2", cue="The first review round")],
                 f"{BUILD} · {DD(7)}"),
    "B09": scene("The path line",
                 receipt(stamped=done_before("authorized_via"), focus="authorized_via", stamp_cues={"authorized_via": "The path line says"}),
                 [chips("TWO PATHS", ["within_configured_limits", "authorization_gate"], cue="The path line says"),
                  note("The gate ships with no built-in rule, by design. Whoever runs the build decides.", cue="And that gate ships")],
                 DD(4)),
    "B10": scene("A seal can only seal what it's handed",
                 receipt(stamped=done_before("merchant")),
                 [quote("a tamper-resistant record of what a user authorized", "", cue="Mastercard describes its record"),
                  quote("It provides cryptographic proof of authorization", VI, cue="Mastercard describes its record"),
                  note("This build's record has no cryptography, on purpose: the signing scheme isn't public.", cue="Mine has no cryptography"),
                  note("The truth of every line comes from the checks before it.", cue="The truth of every line")],
                 f"{VI} · {DD(5)}", seal=True, seal_cue="A seal protects a record"),
    "B11": scene("The merchant line",
                 receipt(stamped=done_before("merchant"), focus="merchant", stamp_cues={"merchant": "checks it against nothing"},
                         values={"merchant": "greenleaf-grocery", "amount": "60.00"}, highlight=("merchant",)),
                 [quote("restricted by agent, merchant, category, spending limit, timeframe or usage rules", SIG, cue="Mastercard says a token"),
                  term("B11", "LIVE · python3 · reference build v2", cue="Buy running shoes")],
                 f"{SIG} · {DD(11)}", seal=True),
    "B12": scene("Your turn: stamp every line",
                 [dict(l, value="…", state="pending", stamp="", highlight=False) for l in receipt(pending_all=True)],
                 [chips("ONE RECORD YOUR SYSTEM WRITES", ["a receipt", "an approval", "a line in a log"], cue="So try it"),
                  note("For every line, write down the step that checked it.", cue="Go through it"),
                  note("Nothing next to a line? Add the check, or say on the record it isn't verified.", cue="For any line with nothing"),
                  {"kind": "stat", "big": "82", "text": "tests · Python 3.10+ · standard library only", "atCue": "The build's repository"}],
                 "Repository linked in the description", eyebrow="YOUR TURN"),
    "B13": {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade",
            "remotion": {"pattern": "ClaudeTitleOutroFullOFL", "props": {
                "title": "Read the Receipt Backwards.", "handle": "@HumanitariansAI",
                "subline": "Tanmay Kulkarni, in for Humanitarians AI"}}},
}


def main():
    sheet = json.loads((HERE / "beat_sheet.json").read_text())   # narration from script_to_sheet.py
    tpath = HERE / "mp3" / "timings.json"
    measured = json.loads(tpath.read_text()) if tpath.exists() else {}
    for b in sheet["beats"]:
        bid, text = b["beat_id"], b["narration_text"]
        shot = copy.deepcopy(SHOTS[bid])
        mp3 = HERE / "mp3" / f"beat-{bid}.mp3"

        def at(cue):
            if PREVIEW:
                return -1
            if bid in measured and mp3.exists():
                return spoken_at_whisper(text, mp3, cue) or spoken_at(text, mp3, cue)
            return round(len(text[:text.index(cue)].split()) / WPS, 2)

        def resolve(d):
            if isinstance(d, dict):
                for k in [k for k in d if k.endswith("Cue") and isinstance(d[k], str)]:
                    d[k[:-3]] = at(d.pop(k))
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)
        sweep = shot.pop("_sweep", None)
        props = shot["remotion"]["props"]
        if sweep:
            props["sweepAtCue"] = sweep
        resolve(props)
        end = measured.get(bid, b["estimated_duration_s"])
        props["durationSeconds"] = 1.5 if PREVIEW else round(end + 0.1, 2)
        b["shot"] = shot
        if bid in measured:
            b["actual_duration_s"] = measured[bid]
    out = HERE / ("_preview" if PREVIEW else ".") / "beat_sheet.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"{out.relative_to(HERE)} · {len(sheet['beats'])} beats{' (PREVIEW: end states, 1.5s)' if PREVIEW else ''}")


if __name__ == "__main__":
    main()
