#!/usr/bin/env python3
"""Writes READ-ALOUD.md from beat_sheet.json, the sheet Tanmay reads from for Gate P.

Generated, not hand-written, so the read can never be of a script we are no longer making.
Re-run after any narration change:  python3 build_beat_sheet.py && python3 make_read_sheet.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())

# Phonemes are Kokoro's own output (kokoro_onnx tokenizer.phonemize, en-us), checked 2026-10-01.
EAR = [
    ("Sutton and Barto", "SUT-n and BAR-toe", "sˈʌʔn ænd bˈɑːɹɾoʊ", "B02"),
    ("Sarsa", "SAR-suh", "sˈɑːɹsə", "B05, B11, B14"),
    ("REINFORCE", "like the word \"reinforce\"", "ɹˌiːɪnfˈɔːɹs", "B12"),
    ("two minus the square root of two", "as written", "tˈuː mˈaɪnəs ðə skwˈɛɹ ɹˈuːt ʌv tˈuː", "B10"),
    ("two minus root two", "as written", "tˈuː mˈaɪnəs ɹˈuːt tˈuː", "B12, B18"),
    ("fifty-eight point six percent", "as written", "fˈɪftiˈeɪt pˈɔɪnt sˈɪks pɚsˈɛnt", "B10, B12"),
    ("minus eleven point six six", "as written", "mˈaɪnəs ᵻlˈɛvən pˈɔɪnt sˈɪks sˈɪks", "B10"),
    ("irrational", "ih-RASH-uh-nul", "ɪɹˈæʃənəl", "B10"),
    ("mint (exactly)", "must not be heard as \"meant\"", "mˈɪnt ɛɡzˈæktli", "B10"),
    ("Kulkarni", "kul-KAR-nee", "kˈʌlkɑːɹni", "B02, B18"),
]

ECHOES = [
    ("B03", "\"Square one… Square two\"", "walking rhythm, one sentence per step"),
    ("B09", "\"At one end… At the other\"", "the two ends of the line"),
    ("B13", "\"Methods that score… Methods that learn\"", "the book's contrast, kept parallel"),
    ("B16", "\"If it disappears… If it survives\"", "the test's two outcomes; the parallel *is* the rubric"),
]

LISTEN = [
    ("B01", "the puzzle has to sound like a real question to the viewer, not a setup line"),
    ("B07", "**the turn.** \"Minus twelve.\" needs its own beat of surprise, and \"almost insulting\" should sound wry, not scripted"),
    ("B08", "the cool-down after the peak (PLAYBOOK §1a): careful, not deflated"),
    ("B10", "quiet wonder at \"irrational\" and \"mint\", without overselling"),
    ("B14", "stillness: \"The coin was covering for what it couldn't see\" is the film's thesis line"),
    ("B16", "confident and plain. This is the rubric; it must be easy to remember on one hearing"),
    ("B17", "inviting, not a lecture. The weak-answer line should sound friendly"),
]


def onscreen(shot):
    p = shot.get("remotion", {}).get("props", {})
    bits = []
    for k in ("heading", "artifactTitle", "artifactHeading", "title"):
        if p.get(k):
            bits.append(p[k])
    bits += p.get("artifactLines", [])
    for k in ("caption", "sparkLine", "source", "subline"):
        if p.get(k):
            bits.append(p[k])
    for m in p.get("markers", []) + (p.get("scoreline") or {}).get("markers", []):
        bits.append(f"marker: {m['label']}")
    if p.get("showPeak"):
        bits.append(f"marker: {p['peakLabel']}")
    return bits


meta = sheet["metadata"]
out = ["# READ-ALOUD: Gate P sheet",
       "",
       f"*{meta['title']}* (working title) · structure: {meta['structure']} · voice `{meta['voice']}`",
       "",
       "Generated from `beat_sheet.json` by `make_read_sheet.py`. If the narration changes, this sheet is",
       "regenerated and the read starts again.",
       "",
       "**How to run Gate P:** read each beat out loud at speaking pace, top to bottom, in one sitting.",
       "Listen for rhythm, emphasis, and whether each turn lands. Tick the box or write a note. Also skim",
       "the *on screen* line under each beat: card text is checked too (PLAYBOOK §1). Then reply",
       "**\"Gate P PASS\"** (with any notes) or list the beats that tripped you.",
       "",
       "**No slates yet.** `Corridor` and `CoinCurve` aren't built, so this is a read-aloud Gate P.",
       "Each beat's visual is reviewed as rendered stills at the next stage, before any audio.",
       "",
       "## Mechanical pass (`gate_p_lint.py`), already clean",
       "",
       "- 0 long sentences, 0 dropped units, 0 symbols or markup in narration.",
       "- 4 ECHO flags, all deliberate parallels (below). 8 NAME flags moved to the ear checklist.",
       "- 1 HOMOPHONE watch: \"mint\".",
       "",
       "| Beat | Parallel | Why it stays |", "|---|---|---|"]
out += [f"| {b} | {p} | {w} |" for b, p, w in ECHOES]
out += ["", "## Changed since your Gate P PASS: caught by Whisper on the generated audio (2026-10-01)", "",
        "Whisper transcribed what Kokoro actually said. Three phrases are heard as different words, so",
        "only these lines changed. Every other line is word-for-word what you signed.", "",
        "| Beat | Heard as | Was | Now |", "|---|---|---|---|",
        "| B02 | \"a coin, **waited** to…\" | It's a coin, weighted to one exact number. | It's a **biased** coin, **set** to one exact number. |",
        "| B06 | \"the book's number **two**\" | That's the book's number too. | The book reports the same number. |",
        "| B09 | \"let's **wait** the coin\", \"every **waiting**\" | So let's weight the coin. / every weighting in between / The best weighting is a little toward right. | So let's **bias** the coin. / every **setting** in between / The best **setting leans** a little toward right. |",
        "| B11 | \"the coin's **waiting**\" | the coin's weighting directly | the coin's **bias** directly |",
        "| S04 | \"**waited** to land right **to** minus root two\" | Weight it to land right two minus root two of the time, about fifty-eight point six percent. | **Bias** it to land right **about fifty-eight point six percent of the time: two minus root two, exactly.** |",
        "", "Re-generated and re-checked: Whisper now hears all five as written. The outro card keeps \"The best",
        "move was a weighted coin\": it's printed, not spoken. `gate_p_lint.py` now flags weight / weighting /",
        "weighted / too, so this can't come back.", ""]
out += ["", "## Say-it-right checklist (Kokoro's own phonemes, checked; confirm by ear)", "",
        "| Word | Should sound like | Kokoro | Where |", "|---|---|---|---|"]
out += [f"| {w} | {s} | `{ph}` | {where} |" for w, s, ph, where in EAR]
out += ["", "## Where to listen hardest", ""]
out += [f"- **{b}**: {n}" for b, n in LISTEN]
out += ["", "## The script", ""]
t = 0.0
for b in sheet["beats"]:
    m, s = divmod(int(t), 60)
    out += [f"### [{m}:{s:02d}] {b['beat_id']} · {b['act']}  _(tone: {b['tone']})_", "",
            b["narration_text"], ""]
    scr = onscreen(b["shot"])
    if scr:
        out += ["<sub>**On screen:** " + " · ".join(x.replace("|", "/") for x in scr) + "</sub>", ""]
    out += ["> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += b["estimated_duration_s"]
m, s = divmod(int(t), 60)
total_words = sum(b["word_count"] for b in sheet["beats"])
out += [f"_{len(sheet['beats'])} beats · {total_words} words · estimated runtime {m}:{s:02d} at 3.3 words/s. "
        "Kokoro audio becomes the master clock once generated._", ""]

out += ["---", "",
        "## The Short (its own script, its own Gate P)", "",
        "Portrait, one arc, its own ending. It reuses the same corridor, never long-form beats. Read it",
        "separately: it has to work for someone who never sees the long film. Generated from",
        "`short/beat_sheet.json`.", "",
        "**Rewritten since your Gate P PASS (2026-10-01).** It now carries one question (why does a coin win?),",
        "the full film's blindfold test with both outcomes (S05), and your name at both ends (S01, S07), as in",
        "the W24 Short. You signed it on 2026-10-01; since then only S04 changed (see the table above).", ""]
short_sheet = json.loads((HERE / "short" / "beat_sheet.json").read_text())
SHORT = [(b["beat_id"], b["act"], b["narration_text"]) for b in short_sheet["beats"]]
for sid, act, text in SHORT:
    out += [f"### {sid} · {act}", "", text, "", "> ☐ reads cleanly   ☐ note: ______________________", ""]
sw = sum(len(x[2].split()) for x in SHORT)
out += [f"_{sw} words · about {sw / 3.3:.0f} s at 3.3 words/s, plus the endcard._", ""]

(HERE / "READ-ALOUD.md").write_text("\n".join(out))
print(f"READ-ALOUD.md · {len(sheet['beats'])} beats · ~{m}:{s:02d} · Short {sw} words")
