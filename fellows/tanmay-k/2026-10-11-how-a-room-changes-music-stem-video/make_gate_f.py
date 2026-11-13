#!/usr/bin/env python3
"""Writes the GATE F records compile.py requires for a final: SHOTLIST.md and PROMPTS.md (both cuts)
and short/FACTCHECK.md. Generated from the beat sheets, so they can't describe a different film.
(Week 26 version of W25's generator.)"""
import json
from pathlib import Path

HERE = Path(__file__).parent

PROMPTS = """# PROMPTS

No AI-image, AI-video or CLI-explainer beats in this project, and so no prompts to record.

- **Pictures:** every beat is a Remotion scene drawn in code (`RoomVoiceOFL`, `HallTempoOFL`,
  `AskAnswerOFL`, `ClaudeArtifactCardFullOFL`, `ClaudeTitleOutroFullOFL`, and the Short's 916 variants).
  Its content is written into `shot.remotion.props` by `build_beat_sheet.py` / `short/build_short_sheet.py`.
- **Waveforms:** the RoomVoice envelopes are measured from our own DEMO audio (`envelopes/*.json`,
  written by `room_voice.py`), never drawn by hand.
- **Narration:** Kokoro TTS (`am_onyx`, local), voicing the Gate P-signed scripts (`PEDAGOGY.md`),
  with the signed pronunciation overrides (`make_audio.py`).
- **The cathedral:** a synthetic impulse response we generated (`make_ir.py`, seeded, measured T30 4.7 s).
  No third-party recording is used. A measured York Minster IR was cut on licence grounds
  (FACTCHECK §C).
"""


def heading(p):
    return p.get("heading") or p.get("artifactHeading") or p.get("title") or ""


def shotlist(sheet, title):
    rows = [f"# SHOTLIST: {title}", "",
            "Generated from `beat_sheet.json` by `make_gate_f.py`. Every beat is a code-drawn Remotion scene,",
            "rendered in SIL OFL fonts only (`withOflFonts`).",
            "- No photographs, stock, logos, album art, or AI-generated imagery.",
            "- No commercial music and no third-party recordings.",
            "- The only sounds are our Kokoro narration, and that narration run through our own simulated echo.",
            "- The tempo arch is a labelled schematic (\"Shape only\"), not the paper's figure.", ""]
    for b in sheet["beats"]:
        r = b["shot"]["remotion"]
        fx = b.get("audio_fx") or {}
        audio = (" · audio: simulated cathedral IR" if fx.get("ir") else " · audio: dry") if b["act"] == "DEMO" else ""
        rows.append(f"{b['beat_id']} {r['pattern']} (Remotion, {b['shot'].get('motion', '')}) · "
                    f"{b.get('actual_duration_s') or b['estimated_duration_s']}s · {heading(r['props'])}{audio}")
    return "\n".join(rows) + "\n"


def short_factcheck(short):
    rows = ["# FACTCHECK: the Short", "",
            "The Short makes no claim the long film doesn't. Every row it cites lives in `../FACTCHECK.md`,",
            "with its verdict and evidence there. This table maps each Short beat to those rows, generated from",
            "`short/beat_sheet.json` by `make_gate_f.py`.", "",
            "| Beat | FACTCHECK rows (../FACTCHECK.md) |", "|---|---|"]
    for b in short["beats"]:
        refs = ", ".join(r.split()[-1] for r in (b.get("factcheck_ref") or [])) or "none (no factual claim)"
        rows.append(f"| {b['beat_id']} | {refs} |")
    return "\n".join(rows) + "\n"


def main():
    long = json.loads((HERE / "beat_sheet.json").read_text())
    short = json.loads((HERE / "short" / "beat_sheet.json").read_text())
    (HERE / "SHOTLIST.md").write_text(shotlist(long, long["metadata"]["title"]))
    (HERE / "short" / "SHOTLIST.md").write_text(shotlist(short, short["metadata"]["title"]))
    (HERE / "PROMPTS.md").write_text(PROMPTS)
    (HERE / "short" / "PROMPTS.md").write_text(PROMPTS)
    (HERE / "short" / "FACTCHECK.md").write_text(short_factcheck(short))
    print("GATE F records written: SHOTLIST.md, PROMPTS.md (both cuts), short/FACTCHECK.md")


if __name__ == "__main__":
    main()
