#!/usr/bin/env python3
"""Week 25 work video, *Same Logic, Two Languages*: beat_sheet.json = SCRIPT.md's narration (the source of
truth for the words) + each beat's scene props.

THREE MATCHES. Two columns throughout, the original JavaScript (left) and my Python (right); a strip tracks
the three matches the film walks through; each row's gutter lands "=" or "≠".

Cues are narration phrases ("…Cue" keys). They resolve on the WORD clock (mp3/words.json from align.py:
faster-whisper timings on the known narration, 1:1 with the words). "atOffset" adds seconds to a cue
(staggered grid items).

    python3 build_beat_sheet.py            # the real sheet (cues on the word clock)
    STILLS=1 python3 build_beat_sheet.py   # _stills/plan.json: every beat's end state, 16:9 and 9:16
"""
import copy, json, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
STILLS = os.environ.get("STILLS") == "1"

# ── sources, as shown on screen (FACTCHECK.md) ──────────────────────────────────────────────────────
BRANCH = "Mycroft recipe: contradiction-detection-agent"   # Tanmay, 2026-10-04: cite the recipe, not the branch
README = "Mycroft README · nikbearbrown/mycroft main @ f596c75"
P6 = "Mycroft SNICKERDOODLE.md, principle P6"
LIVE = "Live run, Node and Python, 2026-10-04"

TICKERS = ["FXA", "FXB", "FXC", "FXD", "FXE", "FXF", "FXG", "FXH", "FXJ", "FXK", "FXL", "FXM", "FXN", "FXP", "FXQ", "FXR"]
BEFORE = [t for t in TICKERS if t not in ("FXQ", "FXR")]   # the test companies before the two edge cases
MATCHES = ["my reading ↔ the original", "my Python ↔ the original JavaScript", "my report ↔ my log"]


def scene(heading, rows=None, blocks=None, source="", eyebrow="", badge="", left="ORIGINAL · JavaScript",
          right="MY PORT · Python", active=-1, activeCue=None, matchesCue=None, show_matches=True, tableCue=None):
    p = {"eyebrow": eyebrow, "heading": heading, "badge": badge, "leftTitle": left, "rightTitle": right,
         "rows": rows or [], "blocks": blocks or [], "source": source,
         "matches": MATCHES if show_matches else [], "activeMatch": active}
    if activeCue: p["activeAtCue"] = activeCue
    if matchesCue: p["matchesAtCue"] = matchesCue
    if tableCue: p["tableAtCue"] = tableCue
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate",
            "remotion": {"pattern": "TwoLanguagesOFL", "props": p}}


def row(left, leftOut, right, rightOut, cue, verdict="none", verdictCue=None, rightCue=None, label="", center=False):
    r = {"left": left, "leftOut": leftOut, "right": right, "rightOut": rightOut, "verdict": verdict, "label": label, "labelCenter": center}
    if cue: r["atCue"] = cue
    else: r["at"] = -1          # on screen from frame 0 (carried across a cut)
    if verdictCue: r["verdictAtCue"] = verdictCue
    if rightCue: r["rightAtCue"] = rightCue
    return r


def blk(kind, cue=None, **kw):
    b = {"kind": kind, "at": -1, **kw}
    if cue: b["atCue"] = cue
    return b


def grid(title, items, cue, step=0.07):
    return blk("grid", title=title, grid=[({"label": lab, "status": st, "at": -1} if (c or cue) is None else
                                           {"label": lab, "status": st, "atCue": c or cue, "atOffset": (0 if c else j * step)})
                                          for j, (lab, st, c) in enumerate(items)])


SHOTS = {
    "B01": scene("One number, two answers",
                 [row("(0.625).toFixed(2)", '"0.63"', 'f"{0.625:.2f}"', '"0.62"', "Ask JavaScript",
                      verdict="differ", verdictCue="Two answers.", rightCue="Ask Python")],
                 [blk("note", "Same number. Same request.", text="Same number. Same request. Two answers.", accent=True),
                  blk("note", "So the question", text="If my rewrite had done that somewhere, would I have noticed?")],
                 LIVE, left="JAVASCRIPT", right="PYTHON", show_matches=False),
    "B02": scene("One Mycroft recipe, rewritten in Python",
                 [row("Aggregate All Signals", "", "aggregate()", "", "rewrote its core logic", verdict="port", verdictCue="rewrote its core logic"),
                  row("Run Pattern Detection Engine", "", "detect()", "", "rewrote its core logic", verdict="port", verdictCue="rewrote its core logic")],
                 [blk("quote", "which describes itself", text="both a book and a working agentic repository", source=README),
                  blk("chips", "I picked one", title="THE RECIPE", items=["contradiction-detection-agent"]),
                  blk("note", "How I checked", text="How do I know my version still says the same thing?", accent=True)],
                 f"{README} · {BRANCH}", eyebrow="WHAT THIS IS", left="ORIGINAL WORKFLOW · JavaScript",
                 matchesCue="It came down to three matches", tableCue="rewrote its core logic"),
    "B03": scene("Five kinds of evidence, six patterns, one person reviewing", None,
                 [blk("chips", "It reads five kinds", title="FIVE SOURCES",
                      items=["earnings guidance", "admitted risks", "analyst Q&A pressure", "news sentiment", "engineering activity"]),
                  blk("chips", "Six patterns", title="SIX PATTERNS · WHERE TWO SOURCES DISAGREE",
                      items=["1 guidance vs news", "2 admitted risk vs news", "3 Q&A pressure vs analyst tone",
                             "4 tech decline vs guidance", "5 engineering burst vs disclosure", "6 optimism vs negative news"]),
                  blk("note", "and every disagreement", text="Every disagreement becomes a flag, for a person to review.", accent=True),
                  blk("chips", "I invented sixteen", title="16 INVENTED COMPANIES",
                      items=["Alpha Fixture Co", "Bravo Fixture Co", "Charlie Fixture Co", "…", "Quebec Fixture Co", "Romeo Fixture Co"]),
                  blk("note", "No real company", text="No real company is judged in this video.")],
                 f"recipes/contradiction-detection-agent.md · sample/FIXTURE_MANIFEST.md · {BRANCH}", eyebrow="THE DETECTOR", show_matches=False),
    "B04": scene("The answers, written down before the code",
                 [row("Run Pattern Detection Engine", "6 patterns", "expected-flags.json", "13 flags · 16 companies",
                      "I went through", rightCue="Thirteen flags", verdict="port", verdictCue="Thirteen flags")],
                 [blk("quote", "Thirteen flags", text="Reasoned from the ORIGINAL JavaScript before any port existed",
                      source="expected-flags.json, “basis”"),
                  blk("note", "Because if I write", text="Written after the code, expected answers copy the code, mistakes included.")],
                 f"data/raw/contradiction-detection-agent/sample/expected-flags.json · {BRANCH}", eyebrow="MATCH ONE",
                 left="THE ORIGINAL", right="MY READING, FIRST", active=0, activeCue="The first match"),
    "B05": scene("The original JavaScript, run beside my Python",
                 [row("Run Pattern Detection Engine", "flags + evidence", "run-approved-tools.py", "flags + evidence",
                      "takes the original JavaScript", verdict="agree", verdictCue="Sixteen out of sixteen",
                      label="compared field by field: every flag, every sentence of evidence")],
                 [grid("16 COMPANIES · COMPARED WORD FOR WORD", [(t, "agree", None) for t in TICKERS], "Sixteen out of sixteen"),
                  blk("stat", "Sixteen out of sixteen", big="16 / 16", text="agree"),
                  blk("note", "A match only tells you", text="A match only tells you something if a mismatch could have shown up.", accent=True)],
                 f"scripts/tools/contradiction-detection-agent-parity-check.py · {LIVE} · {BRANCH}", eyebrow="MATCH TWO",
                 active=1, activeCue="The second match"),
    "B06": scene("Three places JavaScript and Python disagree",
                 [row("(0.625).toFixed(2)", '"0.63"', 'f"{0.625:.2f}"', '"0.62"', "That rounding tie", verdict="differ", verdictCue="That rounding tie"),
                  row("String(1.0)", '"1"', "str(1.0)", '"1.0"', "Another:", verdict="differ", verdictCue="while Python prints"),
                  row('[] || "x"', "[]", '[] or "x"', "'x'", "And a fallback", verdict="differ", verdictCue="where Python's")],
                 [blk("results", "A flag's wording", title="A REAL FLAG · Quebec Fixture Co",
                      rows=[{"label": "evidence A", "status": "confidence=1"}, {"label": "evidence B", "status": "avg score 0.63"}]),
                  blk("chips", "so I made my Python", title="MY PORT COPIES JAVASCRIPT ON EACH", items=["js_to_fixed", "js_str", "js_or"])],
                 f"{LIVE} · run-approved-tools.py · logs/…/detection/FXQ.json · {BRANCH}", eyebrow="WHERE TWO LANGUAGES DIFFER",
                 left="JAVASCRIPT", right="PYTHON", active=1),
    "B07": scene("I changed my own copy. The comparison still agreed.",
                 [row("confidence >= 0.6", "", "confidence >= 0.61", "", "I moved one threshold", verdict="agree",
                      verdictCue="And the comparison said", label="comparison: 14 / 14 agree"),
                  row("toFixed rounding", "", "Python's rounding", "", "I swapped in", verdict="agree",
                      verdictCue="And the comparison said", label="comparison: 14 / 14 agree")],
                 [grid("MY TEST COMPANIES AT THE TIME", [(t, "agree", None) for t in BEFORE], "And the comparison said"),
                  blk("note", "My test companies just never", text="None of them stood on the line: no confidence at exactly 0.6, no average exactly on a tie.", accent=True)],
                 "Scratch run on a copy of my contribution with FXQ and FXR removed, 2026-10-04", eyebrow="WHERE MY TEST DATA NEVER STOOD",
                 left="ORIGINAL · JavaScript", right="MY COPY · changed on purpose", badge="SCRATCH RUN · NOT THE SHIPPED CODE", active=1),
    "B08": scene("Two companies placed exactly on the line",
                 [row("confidence >= 0.6", "", "confidence >= 0.61", "", "Run the same two changes", verdict="differ",
                      verdictCue="The threshold, on Romeo", label="now fails on FXR · Romeo Fixture Co (confidence exactly 0.6)"),
                  row("toFixed rounding", "", "Python's rounding", "", "Run the same two changes", verdict="differ",
                      verdictCue="The rounding, on Quebec", label="now fails on FXQ · Quebec Fixture Co (average exactly 0.625)")],
                 [grid("16 COMPANIES · WHERE EACH CHANGE NOW FAILS", [(t, "agree", None) for t in BEFORE] + [("FXR", "differ", "The threshold, on Romeo"), ("FXQ", "differ", "The rounding, on Quebec")],
                       "So I added"),
                  blk("note", "The fix wasn't new code", text="The fix wasn't new code. It was better test data.", accent=True)],
                 f"sample/FIXTURE_MANIFEST.md (FXQ, FXR) · self-test section B · {BRANCH}", eyebrow="STANDING ON THE LINE",
                 left="ORIGINAL · JavaScript", right="MY COPY · the same two changes", badge="SCRATCH RUN · NOT THE SHIPPED CODE", active=1),
    "B09": scene("My report and my log, describing one run",
                 [row("## Rejects", "13", '"rejects": []', "0", "The report said thirteen", verdict="differ",
                      verdictCue="Same run, two different stories", rightCue="The log said zero", label="before the fix"),
                  row("## Rejects", "13", '"rejects": [ 13 entries ]', "13", "So now one list", verdict="agree",
                      verdictCue="So now one list", label="after the fix · checked by self-test section G")],
                 [blk("note", "The log was only counting", text="The log counted only a later step, one that never got to run."),
                  blk("quote", "own rules say", text="no artifact silently wins", source=P6),
                  blk("chips", "So now one list", title="NOW",
                      items=["one list feeds both", "“not checked” when a step never ran", "a test compares the two"])],
                 f"reports/generated/…-defective.md · logs/…-defective.json · {BRANCH}", eyebrow="MATCH THREE",
                 left="HUMAN REPORT", right="MACHINE LOG", active=2, activeCue="The third match"),
    "B10": scene("Sample data only. Live mode declined.", None,
                 [blk("stat", "No database", big="0", text="live calls: no database, no news feed, no AI model"),
                  blk("chips", "Live data, the model's", title="NOT TESTED",
                      items=["live data", "the model's answers", "timeouts, 401/403/429, empty pages"]),
                  blk("results", "So at the approval step", title="GATE 5 · APPROVAL",
                      rows=[{"label": "decision", "status": "deny", "accent": True},
                            {"label": "decided by", "status": "Tanmay Kulkarni · 2026-10-04"}]),
                  blk("chips", "and wrote down", title="BEFORE ANY LIVE RUN",
                      items=["queries pass values as parameters", "keys from the environment",
                             "the model request carries its prompt", "tests for live failures"]),
                  blk("note", "That call belongs", text="That call belongs to the people with live access.", accent=True)],
                 f"logs/gate-decisions/contradiction-detection-agent-gate-5.json · {BRANCH}", eyebrow="WHERE I STOPPED", show_matches=False),
    "B11": scene("Add, never remove", None,
                 [blk("results", "Every change", title="GITHUB COMPARISON · against nikbearbrown/mycroft main",
                      rows=[{"label": "added", "status": "115", "reason": "new files for this one recipe"},
                            {"label": "modified", "status": "3", "reason": "this recipe's page + 2 shared files, appended to"},
                            {"label": "removed", "status": "0"},
                            {"label": "renamed", "status": "0"}]),
                  blk("note", "Nothing deleted", text="Nothing deleted. Nothing renamed.", accent=True)],
                 "GitHub comparison against nikbearbrown/mycroft main, 2026-10-04", eyebrow="LEAVING IT AS I FOUND IT",
                 show_matches=False),
    "B12": scene("Where would your two versions most likely disagree?",
                 [row("your original", "", "your rewrite", "", "So if you've ever", verdict="mark", verdictCue="Find that one spot", label="↑ one test, standing exactly here", center=True)],
                 # GATE V (2026-10-04): at 50% only the heading was up (47% fill). The table and the rewrite note open with the beat.
                 [blk("note", "So if you've ever", text="Rewritten something you depend on? A new language, a new tool, or just a cleaner version."),
                  blk("note", "Find that one spot", text="Find that one spot, and make sure a single test is standing exactly on it.", accent=True)],
                 "", eyebrow="ONE QUESTION", left="YOUR ORIGINAL", right="YOUR REWRITE", show_matches=False),
    "B13": {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade",
            "remotion": {"pattern": "ClaudeTitleOutroFullOFL", "props": {
                "title": "Same Logic, Two Languages.", "handle": "@HumanitariansAI",
                "subline": "Tanmay Kulkarni, in for Humanitarians AI"}}},
}


def main():
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    words = json.loads((HERE / "mp3" / "words.json").read_text())
    global TIMINGS
    TIMINGS = json.loads((HERE / "mp3" / "timings.json").read_text())
    fps = words["fps"]
    jobs = []
    for b in sheet["beats"]:
        bid, text = b["beat_id"], b["narration_text"]
        shot = copy.deepcopy(SHOTS[bid])
        ww = words["beats"][bid]
        assert len(ww) == len(text.split()), bid

        def at(cue):
            assert cue in text, (bid, cue)
            k = len(text[:text.index(cue)].split())
            return round(ww[k]["startFrame"] / fps, 2)

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
        dur = TIMINGS[bid]
        b["actual_duration_s"] = dur
        props["durationSeconds"] = round(dur + 0.1, 2)
        b["shot"] = shot
        pat = shot["remotion"]["pattern"]
        frame = int(max(0, dur - 0.25) * 30)   # end state: everything on screen
        jobs += [{"id": pat, "props": props, "frame": frame, "out": f"{bid}-16x9.png", "scale": 1},
                 {"id": pat + "916", "props": props, "frame": frame, "out": f"{bid}-9x16.png", "scale": 1}]
    if STILLS:
        out = HERE / "_stills" / "plan.json"
        out.parent.mkdir(exist_ok=True)
        out.write_text(json.dumps(jobs, indent=1, ensure_ascii=False))
        print(f"_stills/plan.json · {len(jobs)} stills (end state, both aspects)")
    else:
        (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
        print(f"beat_sheet.json · {len(sheet['beats'])} beats with props, cues on the word clock")


if __name__ == "__main__":
    main()
