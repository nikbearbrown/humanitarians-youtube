#!/usr/bin/env python3
"""Writes short/beat_sheet.json: the Week 26 work-video Short, from short/SCRIPT-SHORT.md (Short Gate P PASS).

One morning only, the zero price, as one arc for a viewer who never sees the long film (memory: Shorts must
feel complete). Every shot is MorningDashboardOFL916, the only portrait-safe pattern here (PROOF-REVIEW-2:
B02's card fails the Shorts zones). Draft 2 (after Tanmay's "right context, not hurried" note): frame first
(who, what Mycroft is), the idea and its question before the example, the rule in plain words, both previous-close
prices (META, GOOGL), and the record line by line. Visual state carries across cuts: META flagged from S03,
GOOGL from S04, the one hand-off box from S02 (ON TRUST, then RECORDED in S05). Facts cite the long film's FACTCHECK rows. Helpers and data come
from ../build_beat_sheet.py, which reads the merged files from main @ 5097a8f (read-only `git show`).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
LONG = HERE.parent
sys.path.insert(0, str(LONG))
import build_beat_sheet as L          # noqa: E402  (helpers + constants; its main() doesn't run on import)
from cue_align import spoken_at       # noqa: E402

MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
WORD_TIMES = json.loads((MP3 / "word_times.json").read_text()) if (MP3 / "word_times.json").exists() else {}
META = L.VALIDATED["META"]
SRC_VALIDATED = f"data/verified/portfolio-price-fetcher/clean/validated.json · {L.AT_MAIN}"


def box(state, cue=None):
    """The Short's one hand-off: the dashboard taking the quote service's word for each price."""
    h = {"label": "the price, from the quote service", "state": state}
    if cue:
        h["atCue"] = cue
    return [h]


def dash(flags=None):
    """Dashboard rows; flags = {ticker: cue or None}: flagged 'previous close', from `cue` (None = from the start)."""
    out = L.rows({t: ("flagged", "previous close") for t in (flags or {})})
    for r in out:
        cue = (flags or {}).get(r["ticker"])
        if cue:
            r["atCue"] = cue
    return out


def item(label, value, cue):
    return {"label": label, "value": value, "struck": False, "atCue": cue, "struckAtCue": None}


GOOGL = L.VALIDATED["GOOGL"]
assert META["price_source"] == GOOGL["price_source"] == "previousClose" and GOOGL["regularMarketPrice"] is None
OTHERS = sorted(t for t, r in L.VALIDATED.items() if r["price_source"] == "regularMarketPrice")
assert OTHERS == ["AMD", "MSFT", "NVDA"], OTHERS
BOTH = {"META": None, "GOOGL": None}

# beat id → (shot, FACTCHECK refs, hold_after_s)
SHOTS = {
    "S01": (L.morning("A portfolio dashboard, from Mycroft", "Any morning", dash(), [],
                      "Mycroft", ["“both a book and a working agentic repository”",
                                  f"This dashboard: 5 holdings · total {L.TOTAL['value']}"],
                      f"Mycroft README · data/verified/portfolio-price-fetcher/clean/portfolio-summary.json · {L.AT_MAIN}",
                      evidence_cue="which is both a book"), ["W1", "W4"], None),
    "S02": (L.morning("Every number arrives through hand-offs", "This morning", dash(), box("idle"),
                      "One question", ["When a hand-off slips, does anything say so?"],
                      f"recipes/portfolio-price-fetcher.md (Fetch Stock Prices → Calculate Metrics) · {L.AT_MAIN}",
                      evidence_cue="So here's the one question"), ["W2"], None),
    "S03": (L.morning("One price isn't what it looks like", "This morning", dash({"META": None}), box("idle"),
                      "What happened", [],
                      f"declared workflow, Calculate Metrics · {SRC_VALIDATED}", evidence_cue="So the screen quietly",
                      compare=[item("The quote for META came back", f"{META['regularMarketPrice']}", "But the quote for Meta"),
                               item("The rule · code: regularMarketPrice || previousClose", "current price, or if missing, previous close", "The workflow picks"),
                               item("The dashboard shows", f"{META['previousClose']:.2f} (previous close)", "So the screen quietly")]),
            ["W5", "W6", "W22"], None),
    "S04": (L.morning("Not just one", "This morning", dash({"META": None, "GOOGL": "The Google stock's"}), box("idle"),
                      "Two of five", ["META: the quote said 0",
                                      "GOOGL: the quote had no current price",
                                      "Both shown at the previous close. The screen looks the same."],
                      SRC_VALIDATED, evidence_cue="Two of the five"), ["W5", "W20"], None),
    "S05": (L.morning("What says so now", "This morning", dash(BOTH), box("recorded", "What I added is a record"),
                      "What PR #64 added: the record", [], SRC_VALIDATED.replace(" · ", f" · PR #64, merged ({L.MERGE}) · step 3 · ", 1),
                      compare=[item("META · price_source", META["price_source"], "Meta, previous close"),
                               item("GOOGL · price_source", GOOGL["price_source"], "Google, previous close"),
                               item(f"{', '.join(OTHERS)} · price_source", "regularMarketPrice", "The other three")]),
            ["W3", "W7", "W8", "W20", "W21"], None),
    "S06": (L.morning("Your number", "Tomorrow morning", dash(BOTH), box("recorded"), "", [], "", dim=True,
                      question={"text": "What is it quietly taking on trust? And what would tell you if it slipped?",
                                "good": "Good answer: names the hand-off, and the thing that would say so",
                                "weak": "Not an answer: “it's always been right”"}), [], 2.0),
    "S07": (L.morning("Four mornings, one dashboard", "Any morning", dash(BOTH), box("recorded"),
                      "In the full video", ["a stock the portfolio doesn't hold", "a list written twice", "a call by name",
                                            "the morning my own test passed", "@HumanitariansAI"],
                      f"self-test results · {L.AT_MAIN}", evidence_cue="The full video"),
            ["W9", "W11", "W14", "W16"], None),
}


def main():
    script = (HERE / "SCRIPT-SHORT.md").read_text()
    src = re.findall(r"^### (S\d\d) · (.+?)(?:  _\((.+?)\)_)?\n> (.+?)\n", script, re.M | re.S)
    rows_fc = set(re.findall(r"^\| (W\d+) \|", (LONG / "FACTCHECK.md").read_text(), re.M))
    errors, beats = [], []
    if [s[0] for s in src] != list(SHOTS):
        errors.append(f"SCRIPT beats {[s[0] for s in src]} != shot table {list(SHOTS)}")
    for bid, act, tone, text in src:
        shot, refs, hold = SHOTS[bid]
        for r in refs:
            if r not in rows_fc:
                errors.append(f"{bid}: FACTCHECK row {r} missing")
        for s in [text, *L.strings(shot)]:
            if L.PLACEHOLDER.search(s):
                errors.append(f"{bid}: placeholder text: {s[:60]!r}")
        if L.DIGIT_YEAR.search(text):
            errors.append(f"{bid}: digit year in narration: {L.DIGIT_YEAR.search(text).group()}")
        props = shot["remotion"]["props"]
        if refs and not props.get("source"):
            errors.append(f"{bid}: cites {refs} but shows no source")
        est = MEASURED.get(bid, round(len(text.split()) / L.WPS, 1))
        shot["remotion"]["pattern"] += "OFL916"

        def resolve(d):
            if isinstance(d, dict):
                for k in [k for k in d if k.endswith("Cue")]:
                    cue = d.pop(k)
                    if cue is None:
                        d[k[:-3]] = None
                    elif cue not in text:
                        errors.append(f"{bid}: cue not in narration: {cue!r}")
                    else:
                        kw = len(text[:text.index(cue)].split())
                        mp3 = MP3 / f"beat-{bid}.mp3"
                        if WORD_TIMES.get(bid) and WORD_TIMES[bid][kw] is not None:
                            d[k[:-3]] = WORD_TIMES[bid][kw]          # measured: Whisper word start
                        elif bid in MEASURED and mp3.exists():
                            d[k[:-3]] = spoken_at(text, str(mp3), cue)  # measured: pause-anchored fallback
                        else:
                            d[k[:-3]] = round(kw / L.WPS, 2)          # planning clock
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)
        resolve(props)
        props["durationSeconds"] = round(est + 0.1, 2)
        beats.append({"beat_id": bid, "act": act.strip(), "tone": tone or "", "narration_text": text, "shot": shot,
                      "estimated_duration_s": est, "word_count": len(text.split()),
                      "audio_file": f"mp3/beat-{bid}.mp3", "engine": "kokoro", "voice": L.VOICE,
                      **({"hold_after_s": hold} if hold else {}),
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    if errors:
        sys.exit("BUILD FAILED\n  " + "\n  ".join(errors))
    # The same two checks shorts.py runs before marking a Short "ready": every pattern has a registered
    # portrait composition, and the total is under 180 s. Computed, never hardcoded.
    root = (LONG.parent.parent / "brutalist.art" / "runtime" / "remotion" / "src" / "Root.tsx").read_text()
    blocked = [f"{b['beat_id']}: {b['shot']['remotion']['pattern']} has no registered 9:16 composition"
               for b in beats if f'id="{b["shot"]["remotion"]["pattern"]}"' not in root]
    total = sum(b["estimated_duration_s"] + b.get("hold_after_s", 0) for b in beats)
    if total >= 180:
        blocked.append(f"Planned Short: {total:.2f}s must be strictly under 180 seconds")
    sheet = {"metadata": {
        "title": "The Price That Wasn't There", "title_status": "WORKING",
        "structure": "FOUR MORNINGS (Short: one morning, one arc)", "slug": "four-mornings-short",
        "aspect_ratio": "9:16", "fit": "pad", "kind": "short",
        "total_estimated_duration_seconds": round(total, 2),
        "short_validation": {"status": "blocked" if blocked else "ready", "errors": blocked},
        "voice": L.VOICE, "voice_kokoro": L.VOICE, "engine": "kokoro",
        "chip": "@HumanitariansAI", "palette": "claude", "ground": "#FAF9F5",
        "source_commit": f"nikbearbrown/mycroft@{L.MERGE}",
        "note": "Short draft 2 (needs Short Gate P; draft 1 passed but was rewritten for context). Generated by short/build_short_sheet.py from SCRIPT-SHORT.md.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(beats)} beats · {sum(b['word_count'] for b in beats)} words · ~{total:.0f} s · "
          f"validation {sheet['metadata']['short_validation']['status']}")
    for b in beats:
        print(f"  {b['beat_id']} {b['act']:32} {b['word_count']:3}w ~{b['estimated_duration_s']:5}s  {b['tone']}")


if __name__ == "__main__":
    main()
