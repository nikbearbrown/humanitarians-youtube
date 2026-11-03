#!/usr/bin/env python3
"""The work video's Short: beat_sheet.json = SCRIPT.md's narration + portrait scene props.

ONE RECEIPT, portrait (ReceiptAuditOFL916, Shorts UI zones built into the scene). After the hook, one
receipt carries the whole story, and every beat opens in exactly the state the previous one ended in
(see the continuity table in SCRIPT.md). The heading stays fixed from S02 to S06; the line under
discussion is the eyebrow. Helpers, sources and the live terminal transcripts come from the long's
builder (../build_beat_sheet.py, ../live_runs.json), so both films show the same real runs.

    python3 build_beat_sheet.py            # the real sheet (cues on the Whisper clock once audio exists)
    PREVIEW=1 python3 build_beat_sheet.py  # _preview/: every beat in its end state, for the stills review
"""
import copy, importlib.util, json, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("longb", HERE.parent / "build_beat_sheet.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
PREVIEW = os.environ.get("PREVIEW") == "1"

HEAD = "Read the receipt backwards"
EARNED_BEFORE = {  # stamped at the START of each beat = everything earned by the end of the beat before
    "S03": [], "S04": ["agent_id", "consumer_id"], "S05": ["agent_id", "consumer_id", "category"],
    "S06": ["agent_id", "consumer_id", "category", "amount", "transaction_date", "authorized_via"],
}


def portrait(shot):
    shot["remotion"]["pattern"] = shot["remotion"]["pattern"].replace("OFL", "OFL916") if "916" not in shot["remotion"]["pattern"] else shot["remotion"]["pattern"]
    return shot


SHOTS = {
    "S01": L.scene("A receipt my own build once wrote",
                   L.receipt(values=L.MORGAN, highlight=("consumer_id",), pending_all=True, focus="consumer_id", focus_cue="the receipt says Morgan"),
                   [L.note("An early version of this build wrote this receipt.", cue="Hi, this is"),
                    L.note("It says Morgan approved it. Morgan never saw it.", cue="Morgan never saw it")],
                   "Reconstruction of the early version, before review round 2 (README Finding #5); not the shipped code",
                   badge="RECONSTRUCTION · EARLY VERSION"),
    "S02": dict(L.scene(HEAD, L.receipt(pending_all=True),
                        [L.note("For every line: which step checked this, before it was written down?", cue="So now I read")],
                        L.VI, eyebrow="THE MOVE"), _sweep="Start at the bottom"),
    "S03": L.scene(HEAD,
                   L.receipt(focus="consumer_id", focus_cue="In that early version",
                             stamp_cues={"agent_id": "The agent line was checked", "consumer_id": "Now one step does"}),
                   [L.chips("REGISTERED + VERIFIED ≠ YOURS", ["agent-concierge-01 → registered to devon-01"], cue="The agent line was checked"),
                    L.term("B05", "TODAY · python3 · reference build v2", cue="Nothing compared")],   # starts early enough to finish at reading speed
                   f"{L.DD(9)} · reconstruction per README Finding #5", eyebrow="THE PERSON LINE"),
    "S04": L.scene(HEAD,
                   L.receipt(stamped=EARNED_BEFORE["S04"], focus="category", focus_cue="I found another line",
                             stamp_cues={"category": "Now every category is compared"}),
                   # portrait shows one block at a time: the original-build run types while the rule is explained,
                   # its result is up when "the demo's gate said yes" is spoken; then v2's live result as a row
                   [L.term("B06_upper_v1", "ORIGINAL BUILD · DEVON'S RULE: household_staples until 2026-12-31", cue="Then, while making"),
                    L.results("V2 · SAME PURCHASE (live run)", [L.row("Household_Staples", *eval(L.result_of("B06_upper_v2")))], cue="Now every category is compared")],
                   f"{L.BUILD} · original build, live run · {L.DD(12)}", eyebrow="THE CATEGORY LINE"),
    "S05": L.scene(HEAD,
                   L.receipt(stamped=EARNED_BEFORE["S05"],
                             stamp_cues={k: "like the ones on the rest" for k in ("amount", "transaction_date", "authorized_via")}),
                   [L.note("Both of those receipts looked perfect.", cue="Both of those receipts"),
                    L.quote("a tamper-resistant record of what a user authorized", L.VI, cue="Mastercard describes"),
                    L.note("A seal can't make the lines true. The checks before it do.", cue="It can't make the lines true")],
                   f"{L.VI} · {L.DD(5)}", eyebrow="THE SEAL", seal=True, seal_cue="and a seal like that"),
    "S06": L.scene(HEAD,
                   L.receipt(stamped=EARNED_BEFORE["S06"], focus="merchant", focus_cue="Which leaves one line",
                             stamp_cues={"merchant": "It's carried, not checked"}),
                   [L.quote("restricted by agent, merchant, category, spending limit, timeframe or usage rules", L.SIG, cue="Which leaves one line"),
                    L.note("Every line: earned, or honestly marked.", cue="Every line is either"),
                    L.note("The full video reads the whole receipt · linked below", cue="The full video")],
                   f"{L.SIG} · {L.DD(11)}", eyebrow="THE MERCHANT LINE", seal=True),
    "S07": {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade",
            "remotion": {"pattern": "ClaudeTitleOutroFullOFL916", "props": {
                "title": "Read the Receipt Backwards.", "handle": "@HumanitariansAI",
                "subline": "Tanmay Kulkarni, in for Humanitarians AI"}}},
}
SHOTS = {k: portrait(v) for k, v in SHOTS.items()}
END_S = 3.5  # the silent end card


def main():
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    tpath = HERE / "mp3" / "timings.json"
    measured = json.loads(tpath.read_text()) if tpath.exists() else {}
    for b in sheet["beats"]:
        bid, text = b["beat_id"], b["narration_text"]
        shot = copy.deepcopy(SHOTS[bid]); mp3 = HERE / "mp3" / f"beat-{bid}.mp3"

        def at(cue):
            if PREVIEW:
                return -1
            if bid in measured and mp3.exists():
                return L.spoken_at_whisper(text, mp3, cue) or L.spoken_at(text, mp3, cue)
            return round(len(text[:text.index(cue)].split()) / L.WPS, 2)

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
        end = END_S if bid == "S07" else measured.get(bid, b["estimated_duration_s"])
        props["durationSeconds"] = 1.5 if PREVIEW else round(end + 0.1, 2)
        b["shot"] = shot
        if bid == "S07":
            b["estimated_duration_s"] = END_S
            b["audio_policy"] = "silence"   # the silent end card, by design
        if bid in measured:
            b["actual_duration_s"] = measured[bid]
    # the same portrait-plan gate shorts.py applies (compile.py refuses a Short without it): every beat on a
    # native 916 composition, and the whole Short strictly under the 3:00 cap
    blocked = [f"{b['beat_id']}: {b['shot']['remotion']['pattern']}" for b in sheet["beats"]
               if not b["shot"]["remotion"]["pattern"].endswith("916")]
    total = sum(b.get("actual_duration_s", b["estimated_duration_s"]) for b in sheet["beats"])
    if total >= 180:
        blocked.append(f"Planned Short {total:.1f}s is not under 3:00")
    sheet["metadata"].update({"aspect_ratio": "9:16", "kind": "short", "fit": "pad",
                              "derived_from": "read-the-receipt-backwards (short-only script, not a cut)",
                              "total_estimated_duration_seconds": round(total, 2),
                              "short_validation": {"status": "blocked" if blocked else "ready", "errors": blocked}})
    out = HERE / ("_preview" if PREVIEW else ".") / "beat_sheet.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"{out.relative_to(HERE)} · {len(sheet['beats'])} beats{' (PREVIEW)' if PREVIEW else ''}")


if __name__ == "__main__":
    main()
