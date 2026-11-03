#!/usr/bin/env python3
"""Writes READ-ALOUD.md from beat_sheet.json, the sheet Tanmay reads from for Gate P.

Generated, not hand-written, so the read can never be of a script we are no longer making.
Re-run after any narration change:  python3 build_beat_sheet.py && python3 make_read_sheet.py
(Week 26 version of W25's generator; this film has DEMO beats and timed holds, and no Short yet.)
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())

# Kokoro's own phonemes (kokoro_onnx Tokenizer.phonemize, en-us), checked 2026-10-10.
# "Override" = the phonemes the audio wrapper will feed with is_phonemes=True (all in Kokoro's vocab).
EAR = [
    ("Byrne", "BURN", "bˈaɪən ✗", "bˈɜːn", "B04–B07, B15–B16"),
    ("Jean-Guihen", "zhahn gee-EN", "dʒˈiːŋɡˈɪhən ✗", "ʒˈɑːn ɡiˈɛn", "B08"),
    ("Queyras", "keh-RAHSS", "kwˈaɪɹəz ✗", "kɛɹˈɑːs", "B08"),
    ("Quantz", "KVAHNTS", "kwˈɔnts ✗", "kvˈɑːnts", "B07, B08"),
    ("Johann Joachim", "YO-hahn YO-ah-kim", "jˈoʊhɑːn dʒˈoʊəkˌɪm (Joachim ✗)", "jˈoʊɑːkɪm", "B07"),
    ("Léveillé Gauvin", "lay-vay-YAY go-VAN", "lˌeɪveɪlˈeɪ ɡˈoʊvɪn (close)", "Gauvin: ɡoʊvˈæn", "B16"),
    ("Leiden", "LAY-den or LYE-den", "lˈeɪdən ✓", "—", "B14"),
    ("CBGB", "C-B-G-B", "sˌiːbˌiːdʒˌiːbˈiː ✓", "—", "B06"),
    ("seventy-eight R P M", "as written", "sˈɛvəntiˈeɪt ˈɑːɹ pˈiː ˈɛm ✓", "—", "B15"),
    ("US top ten hits", "U-S", "jˌuːˈɛs tˈɑːp tˈɛn hˈɪts ✓", "—", "B16"),
    ("Stravinsky", "struh-VIN-skee", "stɹævˈɪnski ✓", "—", "B15"),
    ("great tits", "plain, the bird's real name", "ɡɹˈeɪt tˈɪts ✓", "—", "B14"),
    ("Kulkarni", "kul-KAR-nee", "kˈʌlkɑːɹni ✓", "—", "B04, B24"),
]

ECHOES = [
    ("B09", "\"Too much echo, slower. Too little echo, also slower.\"",
     "the U-shape, said as a pair. The lint's 'too' flag is about numbers, and none are near"),
    ("B13", "\"If every player… If they answer differently…\"", "the test's two outcomes; the parallel *is* the rule"),
    ("B18", "\"If the clap hangs… If it dies right away…\"", "the clap test's two outcomes"),
    ("D01–D04", "the same sentence four times", "the film's device. Each one is a different room or pace"),
]

LISTEN = [
    ("B01–B03", "the cold open. \"Most of that got lost, right?\" should sound amused, not scripted. "
                "Imagine the cathedral line actually blurring"),
    ("B04", "**does a viewer know what the video is about after this beat alone?** (PLAYBOOK §1c) "
            "A book, Byrne, rooms shape music"),
    ("B09", "**the turn.** \"Then the part that made me stop.\" needs a real beat of surprise"),
    ("B10", "the cool-down (PLAYBOOK §1a): careful, and \"That's their reading, not his words\" plain, not defensive"),
    ("B13", "**the test.** Is it easy to remember on one hearing? Could you apply it to a song you know?"),
    ("B17", "the second cool-down: \"It still doesn't decide it\" should land quietly"),
    ("B18–B19", "**the task.** Read it as if you've never seen the script. Do you know exactly when to "
                "clap and when to speak? Actually clap, actually say the sentence, in the holds"),
    ("B23", "the landing. \"Same answer. Opposite questions.\" Unhurried, no lift"),
]


def onscreen(shot):
    p = shot.get("remotion", {}).get("props", {})
    bits = []
    for k in ("heading", "artifactTitle", "artifactHeading", "title"):
        if p.get(k):
            bits.append(p[k])
    for k, lab in (("asks", "asks"), ("hears", "hears"), ("answers", "answer")):
        if p.get(k):
            bits.append(f"{lab}: {p[k]}")
    if p.get("rule"):
        bits.append(p["rule"])
    bits += p.get("artifactLines", []) + p.get("evidence", [])
    if p.get("stat"):
        bits.append(p["stat"])
    if p.get("schematicNote"):
        bits.append(p["schematicNote"])
    for k in ("caption", "sparkLine", "source", "subline"):
        if p.get(k):
            bits.append(p[k])
    return bits


meta = sheet["metadata"]
out = ["# READ-ALOUD: Gate P sheet", "",
       f"*{meta['title']}* (working title) · structure: {meta['structure']} · voice `{meta['voice']}`", "",
       "Generated from `beat_sheet.json` by `make_read_sheet.py`. If the narration changes, this sheet is",
       "regenerated and the read starts again.", "",
       "**How to run Gate P:** read each beat out loud at speaking pace, top to bottom, in one sitting.",
       "Listen for rhythm, emphasis, and whether each turn lands. Tick the box or write a note. Also skim",
       "the *on screen* line under each beat: card text is checked too (PLAYBOOK §1). Then reply",
       "**\"Gate P PASS\"** (with any notes) or list the beats that tripped you.", "",
       "**This film has two things a page can't show:**",
       "- **DEMO beats (D01–D04)** are the same sentence played through a room. Read them aloud as",
       "  marked: normal pace for D01, then *noticeably* slower for D02–D04. Their real sound (cathedral",
       "  impulse response, or dry) is applied at the audio stage and checked by ear then.",
       "- **Holds** after B18 and B19 are silence for you, the viewer, to clap and speak. When you reach",
       "  them, *do the task*: clap, listen, say the sentence. That's the only honest way to judge it.", "",
       "**No slates yet.** `RoomVoice`, `HallTempo` and `AskAnswer` aren't built, so this is a read-aloud",
       "Gate P. Visuals are reviewed as rendered stills at the next stage, before any audio.", "",
       "## Mechanical pass (`gate_p_lint.py`), already run", "",
       "- 0 long sentences (three split: B04, B10, B12), 0 dropped units, 0 symbols or markup in narration.",
       "- 3 ECHO flags and 3 'too' flags, all deliberate (below). 16 NAME flags → the ear checklist.",
       "- 4 LONE-LETTER flags: \"R P M\" (deliberate letters) and a tokenizer split inside \"Léveillé\".", "",
       "| Beat | Parallel | Why it stays |", "|---|---|---|"]
out += [f"| {b} | {p} | {w} |" for b, p, w in ECHOES]
out += ["", "## Say-it-right checklist", "",
        "Kokoro's phonemes, checked 2026-10-10. ✗ = Kokoro gets it wrong on its own, so the audio stage feeds",
        "the override phonemes instead (the narration text and captions keep the real spelling). **Read the",
        "names the way the second column says**, and tell me if any should be said differently.", "",
        "| Word | Should sound like | Kokoro alone | Override | Where |", "|---|---|---|---|---|"]
out += [f"| {w} | {s} | `{k}` | `{o}` | {where} |" for w, s, k, o, where in EAR]
out += ["", "## Where to listen hardest", ""]
out += [f"- **{b}**: {n}" for b, n in LISTEN]
out += ["", "## The script", ""]
t = 0.0
for b in sheet["beats"]:
    m, s = divmod(int(t), 60)
    demo = b["act"] == "DEMO"
    head = f"### [{m}:{s:02d}] {b['beat_id']} · {b['act']}  _(tone: {b['tone']})_"
    out += [head, ""]
    if demo:
        fx = b.get("audio_fx", {})
        room = "cathedral (York Minster IR)" if fx.get("ir") else "dry, no echo"
        how = ("with a clear pause between the phrases" if fx.get("phrases") else
               "normal pace" if fx.get("speed", 1) >= 1 else "slower, holding the words longer")
        out += [f"> 🔊 **DEMO:** read **{how}**. At audio: {room}"
                + (f", phrases joined by {fx['pause_s']} s silences" if fx.get("phrases") else f", Kokoro speed {fx.get('speed')}")
                + ".", "",
                f"**{b['narration_text']}**", ""]
    else:
        out += [b["narration_text"], ""]
    if b.get("hold_after_s"):
        out += [f"> ⏸ **HOLD {b['hold_after_s']} s.** Silence for the viewer. Do the task now.", ""]
    scr = onscreen(b["shot"])
    if scr and not demo:
        out += ["<sub>**On screen:** " + " · ".join(x.replace("|", "/") for x in scr) + "</sub>", ""]
    out += ["> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += b["estimated_duration_s"] + b.get("hold_after_s", 0)
m, s = divmod(int(t), 60)
total_words = sum(b["word_count"] for b in sheet["beats"])
holds = sum(b.get("hold_after_s", 0) for b in sheet["beats"])
out += [f"_{len(sheet['beats'])} beats · {total_words} words · estimated runtime {m}:{s:02d} at 3.3 words/s, "
        f"including {holds:g} s of holds. Kokoro audio becomes the master clock once generated._", "",
        "---", "",
        "**The Short** isn't written yet. It gets its own script and its own Gate P after this one passes",
        "(one arc: the sentence lost in the cathedral → the cellist slowing at both ends → two rooms).", ""]
(HERE / "READ-ALOUD.md").write_text("\n".join(out))
print(f"READ-ALOUD.md · {len(sheet['beats'])} beats · {total_words} words · ~{m}:{s:02d}")
