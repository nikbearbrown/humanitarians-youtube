#!/usr/bin/env python3
"""Week 25 work video, the Short (9:16): short/beat_sheet.json = short/SCRIPT.md's narration + each beat's portrait
scene props. A short-only script, not a cut of the long film: the same two-column table, carried across nine beats.
Cues resolve on the word clock (mp3/words.json, align.py). Reuses the long film's helpers (../build_beat_sheet.py).

    python3 build_short_sheet.py            # the real sheet
    STILLS=1 python3 build_short_sheet.py   # ../_stills/plan-short.json: every beat's end state (9:16)
"""
import copy, importlib.util, json, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("long", HERE.parent / "build_beat_sheet.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
scene, row, blk, grid = L.scene, L.row, L.blk, L.grid
TICKERS, BEFORE, README, BRANCH, LIVE = L.TICKERS, L.BEFORE, L.README, L.BRANCH, L.LIVE
STILLS = os.environ.get("STILLS") == "1"
NAME = "Tanmay Kulkarni, in for Humanitarians AI"


def s(*a, scale=1.3, **k):
    k.setdefault("show_matches", False)   # the Short tells one story, not the long film's three matches
    sc = scene(*a, **k)
    sc["remotion"]["props"]["scale"] = scale   # phone-native: larger type than the long film's 9:16 frames
    return sc


SHOTS = {
    "S01": s("One number, two answers",
             [row("(0.625).toFixed(2)", '"0.63"', 'f"{0.625:.2f}"', '"0.62"', "Ask JavaScript",
                  verdict="differ", verdictCue="and it gives", rightCue="Ask Python")],
             [blk("note", text=NAME, accent=True)],
             LIVE, left="JAVASCRIPT", right="PYTHON"),
    "S02": s("One Mycroft recipe, rewritten in Python",
             [row("Aggregate All Signals", "", "aggregate()", "", None, verdict="port", verdictCue="rewrote its core logic"),
              row("Run Pattern Detection Engine", "", "detect()", "", None, verdict="port", verdictCue="rewrote its core logic")],
             [blk("quote", "My-croft describes", text="both a book and a working agentic repository", source=README),
              blk("chips", "I picked one", title="THE RECIPE", items=["contradiction-detection-agent"])],
             f"{README} · {BRANCH}", eyebrow="WHAT I WAS WORKING ON", left="ORIGINAL WORKFLOW · JavaScript"),
    "S03": s("Five kinds of evidence, flags for a person", None,
             [blk("chips", "It reads five kinds", title="FIVE SOURCES",
                  items=["earnings guidance", "admitted risks", "analyst Q&A pressure", "news sentiment", "engineering activity"]),
              blk("note", "It flags every place", text="Every disagreement becomes a flag, for a person to review.", accent=True),
              blk("chips", "I invented sixteen", title="16 INVENTED COMPANIES",
                  items=["Alpha Fixture Co", "Bravo Fixture Co", "…", "Quebec Fixture Co", "Romeo Fixture Co"]),
              blk("note", "No real company", text="No real company is judged here.")],
             f"recipes/contradiction-detection-agent.md · sample/FIXTURE_MANIFEST.md · {BRANCH}", eyebrow="WHAT THE DETECTOR DOES"),
    "S04": s("Answers first, then the match",
             [row("Run Pattern Detection Engine", "6 patterns", "expected-flags.json", "13 flags, written first", "Before writing any Python",
                  verdict="port", verdictCue="wrote down the thirteen"),
              row("original JavaScript", "flags + evidence", "my Python", "flags + evidence", "Then I ran the original",
                  verdict="agree", verdictCue="Sixteen out of sixteen")],
             [grid("16 COMPANIES · COMPARED WORD FOR WORD", [(t, "agree", None) for t in TICKERS], "Sixteen out of sixteen"),
              blk("stat", "Sixteen out of sixteen", big="16 / 16", text="agree")],
             f"expected-flags.json · parity-check.py · {LIVE} · {BRANCH}", eyebrow="ANSWERS FIRST", left="THE ORIGINAL", right="MINE"),
    "S05": s("A match only means something if a mismatch could show up",
             [row("(0.625).toFixed(2)", '"0.63"', 'f"{0.625:.2f}"', '"0.62"', None, verdict="differ", verdictCue="like that rounding tie"),
              row("String(1.0)", '"1"', "str(1.0)", '"1.0"', None, verdict="differ", verdictCue="like that rounding tie"),
              row('[] || "x"', "[]", '[] or "x"', "'x'", None, verdict="differ", verdictCue="like that rounding tie")],
             [blk("note", "A match only", text="A match only means something if a mismatch could have shown up.", accent=True),
              blk("chips", "So I made my Python", title="MY PORT COPIES JAVASCRIPT ON EACH", items=["js_to_fixed", "js_str", "js_or"])],
             f"{LIVE} · run-approved-tools.py · {BRANCH}", eyebrow="WHY 16 / 16 TOLD ME ALMOST NOTHING", left="JAVASCRIPT", right="PYTHON"),
    "S06": s("I changed my own copy",
             [row("confidence >= 0.6", "", "confidence >= 0.61", "", "One threshold", verdict="agree",
                  verdictCue="The comparison still agreed", label="comparison: 14 / 14 agree"),
              row("toFixed rounding", "", "Python's rounding", "", "Then Python's own rounding", verdict="agree",
                  verdictCue="The comparison still agreed", label="comparison: 14 / 14 agree")],
             [], "Scratch run on a copy of my contribution with FXQ and FXR removed, 2026-10-04", eyebrow="THE TEST OF MY TEST",
             left="ORIGINAL · JavaScript", right="MY COPY · changed on purpose", badge="SCRATCH RUN · NOT THE SHIPPED CODE"),
    "S07": s("Nobody stood on the line",
             [row("confidence >= 0.6", "", "confidence >= 0.61", "", None, verdict="agree", label="comparison: 14 / 14 agree"),
              row("toFixed rounding", "", "Python's rounding", "", None, verdict="agree", label="comparison: 14 / 14 agree")],
             [grid("MY TEST COMPANIES AT THE TIME", [(t, "agree", None) for t in BEFORE], "None of my test companies"),
              blk("note", "Not one had", text="No confidence at exactly 0.6. No average exactly on a tie.", accent=True)],
             "Scratch run on a copy of my contribution with FXQ and FXR removed, 2026-10-04", eyebrow="WHERE MY TEST DATA NEVER STOOD",
             left="ORIGINAL · JavaScript", right="MY COPY · changed on purpose", badge="SCRATCH RUN · NOT THE SHIPPED CODE"),
    "S08": s("Two companies placed exactly on the line",
             [row("confidence >= 0.6", "", "confidence >= 0.61", "", None, verdict="differ",
                  verdictCue="and each one fails", label="now fails on FXR · Romeo Fixture Co"),
              row("toFixed rounding", "", "Python's rounding", "", None, verdict="differ",
                  verdictCue="and each one fails", label="now fails on FXQ · Quebec Fixture Co")],
             [grid("16 COMPANIES · WHERE EACH CHANGE NOW FAILS",
                   [(t, "agree", None) for t in BEFORE] + [("FXR", "differ", "and each one fails"), ("FXQ", "differ", "and each one fails")], None),
              blk("note", "The fix wasn't new code", text="The fix wasn't new code. It was better test data.", accent=True)],
             f"sample/FIXTURE_MANIFEST.md (FXQ, FXR) · self-test section B · {BRANCH}", eyebrow="STANDING ON THE LINE",
             left="ORIGINAL · JavaScript", right="MY COPY · the same two changes", badge="SCRATCH RUN · NOT THE SHIPPED CODE"),
    "S09": s("Where would your two versions disagree?",
             [row("your original", "", "your rewrite", "", "So, if you've rewritten", verdict="mark", verdictCue="Put one test exactly there",
                  label="↑ one test, standing exactly here", center=True)],
             [blk("results", "No database", title="SAMPLE DATA ONLY",
                  rows=[{"label": "live calls", "status": "0"}, {"label": "gate 5 · live mode", "status": "deny", "accent": True}],
                  untilCue="I'm Tanmay Kulkarni"),
              blk("note", "I'm Tanmay Kulkarni", text=NAME, accent=True),
              blk("note", "The full story", text="The full film: Same Logic, Two Languages.", accent=True)],
             f"logs/gate-decisions/contradiction-detection-agent-gate-5.json · {BRANCH}", eyebrow="WHERE I STOPPED",
             left="YOUR ORIGINAL", right="YOUR REWRITE", tableCue="So, if you've rewritten"),
}
SHOTS["S09"]["remotion"]["props"]["panelFirst"] = True   # cut PROOF: the question table arrives 9 s in; the limits come first
# Per-beat type scale (stills PROOF, 2026-10-04): 1.3 overflowed the dense beats into the source line.
for _bid, _sc in {"S02": 1.0, "S03": 0.95, "S04": 1.0, "S07": 1.0, "S08": 0.95}.items():
    SHOTS[_bid]["remotion"]["props"]["scale"] = _sc


def main():
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    words = json.loads((HERE / "mp3" / "words.json").read_text())
    timings = json.loads((HERE / "mp3" / "timings.json").read_text())
    fps = words["fps"]
    md = sheet["metadata"]
    md.update({"aspect_ratio": "9:16", "fit": "pad", "kind": "short", "structure": "ONE TABLE (short-only script)",
               "reformat": "short-only script; native portrait graphics (no crop)", "derived_from": "same-logic-two-languages",
               "short_validation": {"status": "ready", "errors": []},
               "total_estimated_duration_seconds": round(sum(timings.values()), 2)})
    jobs = []
    for b in sheet["beats"]:
        bid, text = b["beat_id"], b["narration_text"]
        shot = copy.deepcopy(SHOTS[bid])
        shot["remotion"]["pattern"] = "TwoLanguagesOFL916"
        ww = words["beats"][bid]
        assert len(ww) == len(text.split()), bid

        def at(cue):
            assert cue in text, (bid, cue)
            return round(ww[len(text[:text.index(cue)].split())]["startFrame"] / fps, 2)

        def resolve(d):
            if isinstance(d, dict):
                off = d.pop("atOffset", 0)
                for k in [k for k in d if k.endswith("Cue") and isinstance(d[k], str)]:
                    d[k[:-3]] = round(at(d.pop(k)) + (off if k == "atCue" else 0), 2)
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)
        props = shot["remotion"]["props"]
        resolve(props)
        dur = timings[bid]
        b["actual_duration_s"] = dur
        props["durationSeconds"] = round(dur + 0.1, 2)
        b["shot"] = shot
        jobs.append({"id": "TwoLanguagesOFL916", "props": props, "frame": int(max(0, dur - 0.25) * 30),
                     "out": f"{bid}-9x16.png", "scale": 1})
    if STILLS:
        (HERE.parent / "_stills" / "plan.json").write_text(json.dumps(jobs, indent=1, ensure_ascii=False))
        print(f"_stills/plan.json · {len(jobs)} Short stills (end state)")
    else:
        (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        print(f"short/beat_sheet.json · {len(sheet['beats'])} beats, TwoLanguagesOFL916, cues on the word clock")


if __name__ == "__main__":
    main()
