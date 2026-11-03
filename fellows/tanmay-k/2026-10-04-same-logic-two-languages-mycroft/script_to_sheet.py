#!/usr/bin/env python3
"""SCRIPT.md -> beat_sheet.json (narration only, for Gate P and audio). SCRIPT.md is the source of
truth for the words; shots are added to the sheet by the visual builder once the scenes are designed.
Re-run after any script change:  python3 script_to_sheet.py && python3 make_read_sheet.py"""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
s = (HERE / "SCRIPT.md").read_text()
beats = []
for m in re.finditer(r"^### (B\d\d) · (.+?)\n> (.+?)\n\n\*On screen:\*(.+?)(?=\n\n###|\n\n---|\Z)", s, re.M | re.S):
    bid, act, text, screen = m.groups()
    refs = re.findall(r"\*Refs:\*\s*(.+?)\.?$", screen.strip(), re.M)
    beats.append({"beat_id": bid, "act": act.strip(), "narration_text": text.strip(),
                  "on_screen": re.sub(r"\s*\*Refs:\*.*$", "", screen.strip(), flags=re.S).strip(),
                  "factcheck_ref": [r.strip() for r in refs[0].split(",")] if refs else [],
                  "word_count": len(text.split()), "estimated_duration_s": round(len(text.split()) / 3.17, 1),
                  "audio_file": f"mp3/beat-{bid}.mp3", "engine": "kokoro", "voice": "am_onyx"})
sheet = {"metadata": {"title": "Same Logic, Two Languages", "slug": "same-logic-two-languages",
                      "structure": "THREE MATCHES", "topic": "MYCROFT · A RECIPE PORTED FROM JAVASCRIPT TO PYTHON",
                      "presenter": "Tanmay Kulkarni, in for Humanitarians AI", "voice": "am_onyx",
                      "engine": "kokoro", "voice_kokoro": "am_onyx", "palette": "claude", "style_preset": "claude",
                      "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI", "audience": "hai",
                      "ground": "#FAF9F5", "source": "Tanmay-Kulk/mycroft @ add-contradiction-detection-recipe (d9cd514)"},
         "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
w = sum(b["word_count"] for b in beats)
print(f"{len(beats)} beats · {w} words · ~{w/3.17/60:.1f} min")
