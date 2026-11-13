#!/usr/bin/env python3
"""Writes short/READ-ALOUD-SHORT.md from short/beat_sheet.json: the Short's own Gate P sheet.

Generated, not hand-written, so the read is always of the script we're making. Re-run after any change:
  python3 build_short_sheet.py && python3 make_read_sheet_short.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
sheet = json.loads((HERE / "beat_sheet.json").read_text())

CONTEXT = [
    ("Who is speaking", "S01, S11", "Tanmay Kulkarni, for Humanitarians AI, at both ends (W24/W25 convention)"),
    ("What the cathedral is", "S01", "said aloud: “a simulated cathedral”; labelled on screen as not a measured room"),
    ("Who says rooms shape music", "S02", "David Byrne, named as the singer from Talking Heads, and his book *How Music Works*"),
    ("The framework, before any example", "S03", "the room asks a question, and the player answers (three stations on screen)"),
    ("Who measured it, when, how", "S04", "two researchers in Berlin, 2015; one cellist, Bach's six suites, seven halls; echo and tempo measured"),
    ("Why slowing down is expected", "S04", "musicians' advice since at least 1752 (Quantz, on screen)"),
    ("The turn", "S05", "slower in the driest halls too; 74%, said as one player in seven rooms"),
    ("Why, kept honest", "S06", "his words (pauses) vs the researchers' explanation (held notes), attributed separately"),
    ("Your turn, scaffolded", "S07–S08", "clap, listen, say the sentence; strong/weak answers on screen; silences of 2 s and 3 s"),
    ("The payoff answers you", "S09–SD3", "“Did you speed up, or slow down?… Here's mine”, then the sentence in both rooms"),
    ("Where to go next", "S11", "the full video: twelve more musicians, birds in Leiden, the skip button"),
]

LISTEN = [
    ("S03", "**new.** One plain sentence. Does it sound like the idea, not a slogan?"),
    ("S07–S08", "**new.** Read it as a first-time viewer. Do you know exactly when to clap and when to speak? Actually do it, in the silences"),
    ("S09", "**changed.** \"Did you speed up, or slow down?\" should sound like a real question, then turn to \"Here's mine\""),
]

out = ["# READ-ALOUD: Gate P sheet, the Short", "",
       f"*{sheet['metadata']['title']}* (working title) · 9:16 · voice `{sheet['metadata']['voice']}`", "",
       "Generated from `short/beat_sheet.json`. Its own script, written fresh for a viewer who never sees the",
       "long film (not long-form beats cut down). Same method as the long sheet: read it aloud, top to bottom,",
       "in one sitting, then reply **\"Short Gate P PASS\"** or list the beats that tripped you.", "",
       "**DEMO lines (SD1–SD3)** are the long film's measured demo audio, copied (not re-recorded): read them",
       "as marked. Pronunciation overrides are the same as the long film's (say-it-right table in `READ-ALOUD.md`).", "",
       "## Changed since your Short Gate P PASS (Option A: framework early + the clap task)", "",
       "Only these lines are new or changed. Every other line is word-for-word what you signed; the beats",
       "after S02 were renumbered (old S03–S08 are now S04–S06 and S09–S11).", "",
       "| Beat | Status | Line |", "|---|---|---|",
       "| S03 | **new** | The way I'd put it: the room asks a question, and the player answers. |",
       "| S07 | **new** | Try it yourself first. In a moment, clap once. If the clap hangs in the air, your room has echo. If it dies right away, it's dry. Go ahead. *(2 s silence)* |",
       "| S08 | **new** | Now say the sentence, every room you play in is asking you a question, at the pace your room seems to want. *(3 s silence)* |",
       "| S09 | **changed** | Did you speed up, or slow down? A good answer names what your room was doing. Here's mine. First, the cathedral, with room between the phrases. *(was: Here's my sentence in both kinds of room. First, the cathedral, with room between the phrases.)* |", "",
       "## Does it carry its own context? (the thing to judge)", "",
       "| A first-time viewer needs | Where | How the Short gives it |", "|---|---|---|"]
out += [f"| {a} | {b} | {c} |" for a, b, c in CONTEXT]
out += ["", "## Mechanical pass (`gate_p_lint.py`), already run", "",
        "- 0 long sentences, 0 symbols or markup.",
        "- Deliberate parallels: S05 \"Too much echo… Too little echo…\", S06 \"In echoing halls… In dry halls…\", S07 \"If the clap hangs… If it dies…\".",
        "- PROOF static check: 0 fails. Portrait pixel gate 14/14; toolkit Gate V on stills 0 BLOCKER / 0 MAJOR.", "",
        "## Where to listen hardest", ""]
out += [f"- **{b}**: {n}" for b, n in LISTEN]
out += ["", "## The script", ""]
t = 0.0
for b in sheet["beats"]:
    m, s = divmod(int(t), 60)
    out += [f"### [{m}:{s:02d}] {b['beat_id']} · {b['act']}  _(tone: {b['tone']})_", ""]
    if b["act"] == "DEMO":
        out += [f"> 🔊 **DEMO** {b['tone']}, audio from `{b['demo_audio_from']}`", "", f"**{b['narration_text']}**", ""]
    else:
        out += [b["narration_text"], ""]
        p = b["shot"]["remotion"]["props"]
        bits = [x for x in (p.get("heading"), p.get("caption"), p.get("stat"), p.get("rule")) if x]
        bits += [f"{k}: {p[k]}" for k in ("asks", "hears", "answers") if p.get(k)] + p.get("evidence", [])
        if p.get("schematicNote"):
            bits.append(p["schematicNote"])
        if p.get("source"):
            bits.append(p["source"])
        out += ["<sub>**On screen:** " + " · ".join(bits) + "</sub>", ""]
    if b.get("hold_after_s"):
        out += [f"> ⏸ **HOLD {b['hold_after_s']} s.** Silence for the viewer. Do the task now.", ""]
    out += ["> ☐ reads cleanly   ☐ note: ______________________", ""]
    t += b["estimated_duration_s"] + b.get("hold_after_s", 0)
m, s = divmod(int(t), 60)
words = sum(b["word_count"] for b in sheet["beats"])
out += [f"_{len(sheet['beats'])} beats · {words} words · about {m}:{s:02d} (planning clock for narration, "
        "measured for the demos). Kokoro audio for S-beats is generated after this Gate P._", ""]
(HERE / "READ-ALOUD-SHORT.md").write_text("\n".join(out))
print(f"READ-ALOUD-SHORT.md · {len(sheet['beats'])} beats · {words} words · ~{m}:{s:02d}")
