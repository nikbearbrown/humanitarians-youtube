#!/usr/bin/env python3
"""Writes short/beat_sheet.json: the Week 25 Short, its OWN script (memory: shorts must feel complete).

One question carried through: why does a coin beat a learning algorithm here? Each beat answers the
line before it, and S05 carries the full film's thesis (the blindfold test, both outcomes), so the
Short gives the long film's context, not a montage of its beats. Rewritten 2026-10-01 after review:
draft 1 mapped one-to-one onto B03/B05/B07/B10/B14 and never showed the test.
Visual state carries across every cut. S1–S3 and S5 are the same portrait corridor, and its scoreline
strip keeps every score already placed. S4 is the same scores on the full curve. The token ends each
beat where the next one starts.

Presenter credit at both ends, as the W24 Short did: S1 opens with the name, S6 signs off with it and
points to the full film.

Helpers and constants come from the long-form builder, so the two cuts can't drift apart on a number.
Edit this script, not the JSON.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import build_beat_sheet as L  # noqa: E402  (defines the long form's beats on import; main() not run)

WPS = L.WPS
TOOLKIT = HERE.parent.parent.parent / "brutalist.art"
MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
from cue_align import spoken_at, spoken_at_whisper  # noqa: E402  (HERE.parent is on sys.path)
MOSTLY_RIGHT_WALK = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3]  # seed 27, P(right)=0.95, 22 steps
FULL_TITLE = "Why a Coin Flip Beats This Learning Algorithm"

BEATS = []


def beat(bid, act, tone, text, shot, refs):
    BEATS.append((bid, act, tone, text, shot, refs))


ENDS = [L.marker(1.0, None, "never finishes", None)]
HOOK_MARKS = [L.marker(0.95, -44.21, "learner −44", None), L.marker(0.5, -12.0, "coin −12", None)]


def with_outcomes(shot, rows, corridor=True):
    shot["remotion"]["props"]["outcomes"] = rows
    shot["remotion"]["props"]["showCorridor"] = corridor
    return shot


# ONE QUESTION, CARRIED THROUGH: why does a coin beat a learning algorithm here?
# Each beat answers the line before it; S05 is the full film's thesis (the blindfold test, both outcomes).

beat("S01", "THE HOOK", "curious, direct",
     "Hi, this is Tanmay Kulkarni, in for Humanitarians AI. In this puzzle, a coin flip beats a "
     "learning algorithm by more than three and a half times. Here's why, and what it says about "
     "randomness.",
     L.corridor("A coin beats a learning algorithm", "viewer", "", [0],
                "Fair coin −12 · learning algorithm −44 (3.68×)",
                L.SRC_EXACT + " · " + L.SRC_OURS, counter="none", caption_cue="three and a half",
                # in the order the sentence states them: the coin, then the learner, then the ratio
                scoreline=L.strip([L.marker(0.5, -12.0, "coin −12", "a coin flip"),
                                   L.marker(0.95, -44.21, "learner −44", "learning algorithm")])),
     ["A14", "A15", "A16"])

beat("S02", "THE PUZZLE", "explanatory, brisk",
     "It's from Sutton and Barto's reinforcement learning textbook. Four squares. The second one "
     "swaps your buttons. You can't see which square you're on, and you can't count your steps. "
     "So whatever you press, you press everywhere.",
     L.corridor("Four squares. One is swapped.", "viewer", "", [0],
                "Same reading in every square. No counting steps.",
                L.SRC_BOOK + " · Ch. 9 opening, p. 197", counter="none", caption_cue="You can't see",
                scoreline=L.strip(HOOK_MARKS)),
     ["A1", "A2", "A3", "A20", "A22"])

beat("S03", "WHY THE LEARNER FAILS", "deflated",
     "A learning algorithm that hunts for the best button settles on mostly right, and bounces off "
     "that swapped square for about forty-four steps. There is no best button here.",
     L.corridor("Hunting for the best button", "viewer", "95% right", MOSTLY_RIGHT_WALK,
                "About −44 (Sarsa, ε = 0.1: 30 of 30 runs settle on mostly right)",
                L.SRC_BOOK + " · " + L.SRC_OURS + " · walk shown: one seeded sample",
                p_right=0.95, cue="settles on", caption_cue="about forty-four", counter="none",
                # no step counter: one 22-step sample would read "score −22" beside the claimed −44 average
                scoreline=L.strip([L.marker(0.95, -44.21, "learner −44", "about forty-four"),
                                   L.marker(0.5, -12.0, "coin −12", None)]))
     | {"_stepSeconds": 0.2},
     ["A4", "A5", "A16"])

beat("S04", "THE WEIGHTED COIN", "turning, then quiet wonder",
     "A fair coin gets there in about twelve steps. And the best coin isn't even fair. Bias it to land right "
     "about fifty-eight point six percent of the time: two minus root two, exactly. That's what chapter "
     "thirteen of the book is about: learners that tune the coin itself, and find that number on "
     "their own.",
     L.dial("The best coin isn't fair", HOOK_MARKS,
            "Chapter 13's policy-gradient learner (REINFORCE) finds it: 30-run average 58.6%.",
            L.SRC_BOOK + " · Ch. 13, p. 321 · " + L.SRC_OURS, peak=True, peak_cue="two minus root two",
            caption_cue="That's what chapter", curve_cue="And the best coin",
            equation={"lhs": "p", "lhsSup": "*", "whole": "2", "radicand": "2", "approx": "0.586",
                      "note": "chance of pressing right"}),
     ["A14", "A6", "A7", "A10", "A17"])

beat("S05", "THE TEST", "firm, the payoff",
     "So why random? Give the player more information and find out. Let it see where it is, and the "
     "coin vanishes: right, left, right, three steps. But in rock, paper, scissors, against an "
     "opponent who learns your habits, the coin survives. Lean on rock, and you get punished.",
     with_outcomes(
         L.corridor("Give it more information", "sees", "right · left · right", L.SEEING_WALK,
                    "", L.SRC_OURS + " (corridor.py, rps.py) · Sutton & Barto (2018), Sec. 17.3, p. 465",
                    cue="right, left, right", counter="steps"),
         [{"label": "It can see → the coin vanishes", "value": "30 of 30 runs: right, left, right · −3 (best coin −11.66)",
           "atCue": "the coin vanishes", "accent": False},
          {"label": "Someone's watching → the coin survives",
           "value": "Rock-paper-scissors vs. an adaptive opponent: always rock −0.999 per round; lean rock −0.29; even thirds ≈ 0",
           "atCue": "the coin survives", "accent": True}]),
     ["A18", "A21", "A23", "A24"])

# S06: the active task, so the Short carries a structured viewer action, not only a pointer (12/12).
beat("S06", "THE TASK", "direct, inviting",
     "Next time the best move is random, ask what the player can't see, or who's watching. Try it on "
     "a goalkeeper at a penalty, choosing which way to dive. Does more information make the "
     "randomness vanish, or survive? Tell me in the comments, and name the clue or the watcher. "
     "Saying it's random because it's uncertain doesn't count.",
     with_outcomes(
         L.corridor("Try the test: a goalkeeper at a penalty", "viewer", "", [0],
                    "", "The blindfold test, from the full video", counter="none", caption_cue=None)
         ,
         [{"label": "When the best move is random, ask:", "value": "what can't the player see, or who's watching?",
           "atCue": "ask what the player", "accent": False},
          {"label": "Does more information make the randomness vanish, or survive?", "value": "",
           "atCue": "Does more information", "accent": True},
          {"label": "Strong answer", "value": "names the missing clue, or who's watching",
           "atCue": "name the clue", "accent": False},
          {"label": "Weak answer", "value": "\u201cit's random because it's uncertain\u201d",
           "atCue": "Saying it's random", "accent": False}], corridor=False),
     [])

beat("S07", "THE CLOSE", "warm",
     "The full video works through it, step by step. Tanmay Kulkarni, in for Humanitarians AI.",
     {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade", "remotion": {
         "pattern": "ClaudeTitleOutroFull",
         "props": {"title": FULL_TITLE, "handle": "@HumanitariansAI", "subline": L.SIGNOFF}}},
     [])


def validate_short():
    """The checks shorts.py makes before marking a Short 'ready': every beat on a registered portrait
    composition, and a runtime the toolkit accepts. Computed here, never asserted."""
    sys.path.insert(0, str(TOOLKIT / "runtime" / "scripts"))
    from build_safety import BuildError, require_short_duration
    root = (TOOLKIT / "runtime" / "remotion" / "src" / "Root.tsx").read_text()
    errors = []
    for bid, _, _, _, shot, _ in BEATS:
        pat = shot["remotion"]["pattern"]
        pat = pat if pat.endswith("OFL916") else pat + "OFL916"
        if f'id="{pat}"' not in root:
            errors.append(f"{bid}: {pat} not registered")
    try:
        require_short_duration(sum(MEASURED.get(b[0], 0) for b in BEATS), "Planned Short")
    except BuildError as exc:
        errors.append(str(exc))
    return {"status": "blocked" if errors else "ready", "errors": errors}


def main():
    def at(text, cue):
        # Whisper clock once audio exists (cue_align: Whisper's words snapped to the audio's own pauses),
        # pause clock as fallback, planning rate before audio. W24: fixed-rate cues drifted up to 1.2 s.
        if cue not in text:
            sys.exit(f"cue not in narration: {cue!r}")
        mp3 = MP3 / f"beat-{CUR['bid']}.mp3"
        if CUR["bid"] in MEASURED and mp3.exists():
            w = spoken_at_whisper(text, mp3, cue)
            return w if w is not None else spoken_at(text, mp3, cue)
        return round(len(text[:text.index(cue)].split()) / WPS, 2)

    def resolve(d, text):
        if isinstance(d, dict):
            if isinstance(d.get("stepAtCues"), list):
                d["stepAt"] = [at(text, c) for c in d.pop("stepAtCues")]
            for k in [k for k in d if k.endswith("Cue")]:
                v = d.pop(k)
                # a marker with no cue is carried from the previous beat: on screen from frame 0
                # (None), never popped in at 0.6 s, which also made two carried markers both "newest"
                d[k[:-3]] = at(text, v) if isinstance(v, str) else (None if k == "atCue" else 0.6)
            for v in d.values():
                resolve(v, text)
        elif isinstance(d, list):
            for v in d:
                resolve(v, text)

    beats = []
    CUR = {}
    for bid, act, tone, text, shot, refs in BEATS:
        CUR["bid"] = bid
        step_s = shot.pop("_stepSeconds", None)
        rem = shot["remotion"]
        rem["pattern"] += "OFL916"
        if step_s:
            rem["props"]["stepSeconds"] = step_s
        resolve(rem["props"], text)
        if bid in MEASURED and rem["pattern"].startswith(("Corridor", "CoinCurve")):
            rem["props"]["durationSeconds"] = round(MEASURED[bid] + 0.1, 2)
        words = len(text.split())
        beats.append({"beat_id": bid, "act": act, "tone": tone, "narration_text": text, "shot": shot,
                      "estimated_duration_s": round(words / WPS, 1), "word_count": words,
                      "audio_file": f"mp3/beat-{bid}.mp3", "engine": "kokoro", "voice": L.VOICE,
                      **({"actual_duration_s": MEASURED[bid]} if bid in MEASURED else {}),
                      "factcheck_ref": [f"../FACTCHECK.md {r}" for r in refs] or None})
    sheet = {"metadata": {
        "title": FULL_TITLE + " (Short)", "title_status": "FINAL", "structure": "ONE QUESTION (short-only script)",
        "slug": "why-a-coin-flip-beats-this-learning-algorithm-short",
        # the keys compile.py and shorts.py use; "aspect" was silently ignored and the first compile
        # centre-cropped every portrait beat to 16:9 (GATE V caught it, 2026-10-01)
        "aspect_ratio": "9:16", "fit": "pad", "kind": "short",
        "reformat": "short-only script; native portrait graphics (no crop)",
        "derived_from": "why-a-coin-flip-beats-this-learning-algorithm",
        "total_estimated_duration_seconds": round(sum(MEASURED.get(b[0], 0) for b in BEATS), 2),
        "short_validation": validate_short(),
        "topic": "REINFORCEMENT LEARNING", "register": "Pragmatist", "audience": "hai",
        "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI",
        "voice": L.VOICE, "engine": "kokoro", "voice_kokoro": L.VOICE,
        "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "note": "Short-only script, generated by short/build_short_sheet.py. Not a cut of the long form.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(b["word_count"] for b in beats)
    est = sum(b["estimated_duration_s"] for b in beats)
    print(f"Short: {len(beats)} beats · {total} words · ~{est:.0f}s estimated")
    for b in beats:
        print(f"  {b['beat_id']} {b['act']:14} {b['word_count']:3}w ~{b['estimated_duration_s']}s")


if __name__ == "__main__":
    main()
