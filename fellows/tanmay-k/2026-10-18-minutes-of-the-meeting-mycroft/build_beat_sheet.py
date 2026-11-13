#!/usr/bin/env python3
"""beat_sheet.json (the source of truth for the build) and SHOTLIST.md, from SCRIPT.md (the signed words) + the slate stages.

SCRIPT.md holds narration, the on-screen description and the FACTCHECK refs per beat. build_slates.py holds each beat's
reveal stages (cv.k); CUES below maps every stage to the narration phrase that triggers it. Until audio exists the cue
clock is the PLANNING clock (3.3 words a second); make_audio.py replaces it with the measured Whisper word times.

Guards: every stage of a slate has exactly one cue; every cue phrase occurs in its beat's narration; cues run in
narration order; every ref is a W-row in FACTCHECK.md; no placeholder text, no digit years in narration.
Run:  /opt/homebrew/bin/python3.12 build_beat_sheet.py
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import build_slates  # noqa: E402

WPS, LEAD = 3.3, 0.25
HOLD = {"B01": 1.0, "B05": 1.0, "B07": 2.0, "B08": 1.0, "B09": 1.0, "B11": 1.5, "B12": 2.5}
GAP = 0.6
ACT = {"B01": "COLD OPEN", "B02": "SETUP", "B03": "THE MEETING", "B04": "THE MEETING", "B05": "THE MEETING", "B06": "THE MEETING",
       "B07": "THE MEETING", "B08": "THE MINUTES", "B09": "THE TURN", "B10": "ADJOURNED", "B11": "CLOSE", "B12": "OUTRO"}
CUES = {
    "B01": ["your action plan must strictly match", "so who decided the verdict"],
    "B02": ["a book and a working repository", "asks three different questions", "then hands an AI the answers",
            "who had a vote, and how much", "my pull request, now merged", "every company you'll see is invented"],
    "B03": ["today's stock is ironbridge power", "i'll call the workflow the chair", "if a request arrives with nothing",
            "a company called unknown company"],
    "B04": ["first voice", "ironbridge is low and low", "the voice says strong sell"],
    "B05": ["second voice", "aggressive has the loosest limits", "growth at least five percent", "sentiment at least point three five",
            "price-to-earnings no more than eighty", "debt to equity no more than one and a half", "four out of four"],
    "B06": ["how close is it to changing its mind", "three of the six nudges change it", "the stability score"],
    "B07": ["the first voice says strong sell", "forty-five, thirty-five and twenty", "the chair's scale runs from one to five",
            "the voices contribute", "together, two point one seven", "writes down as sell"],
    "B08": ["then the chair writes the minutes", "about four hundred and seventy words", "and one last instruction", "a number somebody typed",
            "looks exactly like a number the chair", "filled in"],
    "B09": ["to check the original", "on two requests", "python and javascript disagree", "i fixed it", "all twenty-three requests"],
    "B10": ["the step that would call the ai", "five items in the recipe are still open", "it still says draft"],
    "B11": ["have you read the minutes", "who had a vote", "and how much of one", "a good answer"],
    "B12": ["tanmay kulkarni", "signing off"],
}


def norm(s): return re.sub(r"[^a-z0-9' ]+", " ", s.lower().replace("-", " ").replace("’", "'")).split()


src = (HERE / "SCRIPT.md").read_text()
fact = (HERE / "FACTCHECK.md").read_text()
FACT_IDS = set(re.findall(r"^\| (W\d+) \|", fact, re.M))
blocks = re.findall(r"^### (B\d\d) · (.+?)\n> (.+?)\n\n\*On screen:\* (.+?) \*Refs:\* (.+?)\.?\n", src, re.M | re.S)
assert len(blocks) == 12, len(blocks)
beats, t = [], 0.0
for bid, title, text, screen, refs in blocks:
    refs = [] if refs.strip().startswith("none") else [r.strip().rstrip(".") for r in refs.split(",")]
    assert all(r in FACT_IDS for r in refs), (bid, refs)
    assert not re.search(r"\b(19|20)\d\d\b", text), f"{bid}: digit year in narration"
    assert not re.search(r"\bTODO\b|\bTBD\b|lorem|XXX", text + screen, re.I), f"{bid}: placeholder"
    words = norm(text)
    cues, pos = [], 0
    for stage, ph in enumerate(CUES[bid], 1):
        p = norm(ph)
        idx = next((i for i in range(pos, len(words) - len(p) + 1) if words[i:i + len(p)] == p), None)
        assert idx is not None, f"{bid}: cue '{ph}' not found (after word {pos}) in narration"
        cues.append({"stage": stage, "phrase": ph, "at_s": round(idx / WPS + LEAD, 2)})
        pos = idx
    maxk = build_slates.BEATS[bid]().maxk
    assert maxk == len(cues), f"{bid}: slate has {maxk} stages but {len(cues)} cues"
    nar = len(text.split()) / WPS
    dur = nar + HOLD.get(bid, 0.0)
    beats.append({"beat_id": bid, "act": ACT[bid], "title": title.strip(), "narration_text": text.strip(), "on_screen": screen.strip(),
                  "refs": refs, "slate": f"_stills/{bid}-16x9.png", "word_count": len(text.split()),
                  "start_s": round(t, 2), "narration_s": round(nar, 2), "hold_after_narration_s": HOLD.get(bid, 0.0),
                  "duration_s": round(dur, 2), "reveal_cues": cues})
    t += dur + GAP
MEAS = HERE / "mp3" / "timings.json"; PLAN = HERE / "_motion" / "plan.json"; STARTS = HERE / "_beats" / "beat_starts.json"
clock = "PLANNING (3.3 words/s) until make_audio.py replaces it with measured Whisper word times"
if MEAS.exists() and PLAN.exists() and "--planning" not in sys.argv:
    tm, pl = json.loads(MEAS.read_text()), json.loads(PLAN.read_text())
    st = json.loads(STARTS.read_text()) if STARTS.exists() else None
    t = 0.0
    for b in beats:
        k = b["beat_id"]; m = tm[k]
        b["narration_s"], b["duration_s"] = round(m["narration_end_s"], 2), round(m["duration_s"], 2)
        b["start_s"] = round(st[k] if st else t, 2)
        stage_at = dict((s_, at) for s_, at in pl[k]["cues"])
        for c in b["reveal_cues"]: c["at_s"] = stage_at[c["stage"]]
        t += m["duration_s"]
    clock = "MEASURED: Kokoro audio (mp3/timings.json) and Whisper word times (_motion/plan.json); not hand-edited"
    t = beats[-1]["start_s"] + beats[-1]["duration_s"] + GAP
sheet = {"metadata": {"title": "Minutes of the Meeting: What an AI Is Handed", "title_status": "working", "structure": "MINUTES OF ONE MEETING",
                      "voice_kokoro": "am_onyx", "master": "3840x2160 @ 30 fps", "beats": len(beats),
                      "duration_s": round(t - GAP, 2), "clock": clock,
                      "source": f"nikbearbrown/mycroft main @ {build_slates.MERGE} (PR #70)",
                      "note": "words come from SCRIPT.md (Gate P signed, draft 2); figures on slates are read from the merged repository, never typed"},
         "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
rows = ["# SHOTLIST: Minutes of the Meeting", "",
        "Generated by `build_beat_sheet.py` from `SCRIPT.md`. One slate per beat, drawn in code (`build_slates.py`, Pillow); no generated imagery, no stock, no third-party images. Cue times are the planning clock until audio exists.",
        "", "| Beat | Start | Length | On screen | FACTCHECK | Reveals (stage at seconds) |", "|---|---|---|---|---|---|"]
for b in beats:
    cues = ", ".join(f"{c['stage']}@{c['at_s']:.1f}" for c in b["reveal_cues"])
    rows.append(f"| {b['beat_id']} {b['title'].title()} | {b['start_s']:.1f} s | {b['duration_s']:.1f} s | {b['on_screen'][:150]}… | {', '.join(b['refs']) or 'none'} | {cues} |")
(HERE / "SHOTLIST.md").write_text("\n".join(rows) + "\n")
print(len(beats), "beats;", sheet["metadata"]["duration_s"], "s planned; all guards passed")
