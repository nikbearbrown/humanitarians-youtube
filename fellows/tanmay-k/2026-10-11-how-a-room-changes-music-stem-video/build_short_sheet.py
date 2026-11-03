#!/usr/bin/env python3
"""Writes short/beat_sheet.json: the Week 26 Short, its own script (draft 1).

Written fresh, not cut from long-form beats (memory: Shorts must feel complete). One arc for a viewer
who never sees the long film:

  the sentence in a simulated cathedral → who says rooms shape music (Byrne, the book) →
  who tested it, how (one cellist, seven halls) → the turn (slower at BOTH ends, 74%) →
  why, with his words and the researchers' reading kept apart → both rooms heard →
  the thesis, a pointer to the full film, and the name at both ends (W24/W25 convention).

Portrait-safe components only (PROOF-REVIEW-2, option a): RoomVoice, HallTempo, AskAnswer. No cards,
no outro card: both broke the Shorts UI zones. Visual state carries across every cut: each beat
opens on the picture the last one ended with. Facts cite the long film's FACTCHECK rows.
DEMO audio is COPIED from the long film's mp3/ (never hardlinked, BEATS.md #12).
"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
LONG = HERE.parent
sys.path.insert(0, str(LONG))
import build_beat_sheet as L          # noqa: E402  (helpers + constants; its main() doesn't run on import)
from cue_align import spoken_at       # noqa: E402

MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
SIGN = "Tanmay Kulkarni, for Humanitarians AI"
SRC_BOOK = "David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse”"
CATH = ("Simulated cathedral", "about a 5-second echo")
DRY = ("no room: dry voice", "no impulse response")
NORMAL = {"label": "normal pace", "ir": L.IR_MINSTER, "from": "D01"}
PAUSES = {"label": "cathedral, room between phrases: waiting for the echo to clear", "ir": L.IR_MINSTER, "from": "D03"}
HELD = {"label": "dry, held longer: filling in for an echo that never comes", "ir": None, "from": "D04"}

BEATS = []


def beat(bid, act, tone, text, shot, refs, demo_from=None, hold_after=None):
    # hold_after: seconds of held frame + silence after the beat (the viewer-task silences)
    BEATS.append((bid, act, tone, text, shot, refs, demo_from, hold_after))


def voice(heading, room, passes, caption, source, caption_cue=None, active_cue=None):
    sh = L.room_voice(heading, room[0], room[1], [dict(p) for p in passes], caption, source,
                      caption_cue=caption_cue, active_cue=active_cue)
    return sh


# ── S01: name + the cold open, in one breath ──────────────────────────────────────────────
beat("S01", "LISTEN", "quiet, inviting",
     "This is Tanmay Kulkarni, for Humanitarians AI. Listen to one sentence, inside a simulated cathedral.",
     voice("One sentence, one cathedral", CATH, [], "Listen.", L.SRC_IR, caption_cue="Listen to one"),
     ["B5"])

beat("SD1", "DEMO", "(the sentence, normal pace, in the cathedral)", L.SENTENCE,
     voice("One sentence, one cathedral", CATH, [NORMAL], "", L.SRC_IR, active_cue="Every room"),
     ["B1", "B5"], demo_from="D01")

# ── S02: who says rooms shape music, with enough context to follow ────────────────────────
beat("S02", "BYRNE", "curious, storytelling",
     "Hear how every word is still ringing when the next one arrives? David Byrne, the singer from "
     "Talking Heads, wrote a book about this, called How Music Works. His big idea is that a room "
     "doesn't just hold music. It shapes it.",
     voice("A room shapes the music in it", CATH, [NORMAL],
           "David Byrne, How Music Works: music is made to fit the place it will be heard.",
           L.SRC_IR + " · " + SRC_BOOK, caption_cue="David Byrne"),
     ["B1", "A1"])

# ── S03: the framework, BEFORE the example (Option A, 2026-10-10: framework 1 → 2) ─────────────
beat("S03", "THE FRAME", "clear, plain",
     "The way I'd put it: the room asks a question, and the player answers.",
     L.ask_answer("How a room shapes music", "echo, silence, noise", "whoever is playing",
                  "what they change", SRC_BOOK + " · the research in this video",
                  answers_cue="and the player answers"),
     ["A1"])

# ── S04: the test, set up properly ────────────────────────────────────────────────────────
beat("S04", "SEVEN HALLS", "investigative, building",
     "In two thousand fifteen, two researchers in Berlin measured how much one player changes from "
     "room to room. The cellist Jean-Guihen Queyras played all six of Bach's cello suites in seven European "
     "concert halls. They measured how much each hall echoed, and how fast he played. In the "
     "most echoing halls, he slowed down. Musicians have advised that since at least seventeen "
     "fifty-two: give the echo time to clear.",
     L.hall_tempo("One cellist, seven halls", False, "",
                  "Most echoing halls → he played slower, as Quantz advised in 1752.",
                  L.SRC_SKW + " · Quantz (1752), as cited there"),
     ["A8", "A9", "A7"])

# ── S04: the turn ─────────────────────────────────────────────────────────────────────────
beat("S05", "THE DRIEST HALL", "surprised",
     "But in the driest halls, the ones with almost no echo, he slowed down too. Too much echo, "
     "slower. Too little echo, also slower. One measure of the hall's echo accounted for about "
     "seventy-four percent of how his tempo moved.",
     L.hall_tempo("He slowed down at both ends", True, "74% of his tempo variation",
                  "Driest halls → also slower. One cellist, seven halls.", L.SRC_SKW,
                  dry_cue="But in the driest halls", stat_cue="seventy-four percent"),
     ["A9", "A10"])

# ── S05: why, with the attribution kept honest ────────────────────────────────────────────
beat("S06", "WHY BOTH ENDS", "careful, then landing",
     "Why both? In echoing halls, he told them, he lets the pauses run longer. In dry halls, the "
     "researchers think a player holds notes longer, to fill in for an echo that isn't there. Same "
     "answer. Opposite questions.",
     L.ask_answer("Same answer, opposite questions", "too much echo, or too little", "the cellist",
                  "slower, for opposite reasons", L.SRC_SKW + ", interviews and discussion",
                  answers_cue="Same answer",
                  evidence=["Echoing hall (his words): let the pauses run longer",
                            "Dry hall (the researchers' explanation): hold notes longer"]),
     ["A11", "A12"])

# ── S07–S08: the viewer's own room asks (Option A: active task 0 → 2), answered by the payoff ──
beat("S07", "YOUR ROOM", "direct, inviting",
     "Try it yourself first. In a moment, clap once. If the clap hangs in the air, your room has "
     "echo. If it dies right away, it's dry. Go ahead.",
     L.ask_answer("First: clap once, and listen.", "clap once: does it hang, or die?", "you",
                  "the pace you choose", "Our listening heuristic, not a measurement",
                  evidence=["Strong answer: names what the room did (blurred your words, or swallowed them)",
                            "Weak answer: “it felt different”"]),
     ["B3"], hold_after=2.0)

beat("S08", "SAY IT", "direct, unhurried",
     "Now say the sentence, every room you play in is asking you a question, at the pace your room "
     "seems to want.",
     L.ask_answer("Now: say the sentence at your room's pace.", "clap once: does it hang, or die?", "you",
                  "the pace you choose", "Our listening heuristic, not a measurement",
                  evidence=["Strong answer: names what the room did (blurred your words, or swallowed them)",
                            "Weak answer: “it felt different”"]),
     ["B3"], hold_after=3.0)

# ── S09 + demos: the payoff, heard ────────────────────────────────────────────────────────
beat("S09", "BOTH ROOMS", "quiet, deliberate",
     "Did you speed up, or slow down? A good answer names what your room was doing. Here's mine. "
     "First, the cathedral, with room between the phrases.",
     voice("Two rooms like the ones he slowed down in", CATH, [], "First: the cathedral.", L.SRC_IR,
           caption_cue="First"),
     ["B1", "B5"])

beat("SD2", "DEMO", "(the sentence, with pauses, in the cathedral)", L.SENTENCE,
     voice("Two rooms like the ones he slowed down in", CATH, [PAUSES], "", L.SRC_IR, active_cue="Every room"),
     ["B1", "B5"], demo_from="D03")

beat("S10", "NO ECHO", "quiet",
     "And now, almost no echo at all, holding the words longer.",
     voice("Two rooms like the ones he slowed down in", DRY, [PAUSES], "Second: no echo.",
           "Our narration with no impulse response applied", caption_cue="almost no echo"),
     ["B2"])

beat("SD3", "DEMO", "(the sentence, held longer, dry)", L.SENTENCE,
     voice("Two rooms like the ones he slowed down in", DRY, [PAUSES, HELD], "",
           "Our narration with no impulse response applied", active_cue="Every room"),
     ["B2"], demo_from="D04")

# ── S08: the thesis, the pointer, the name ────────────────────────────────────────────────
beat("S11", "EVERY ROOM IS ASKING", "warm, landing",
     "So a room doesn't write the music. It asks a question, and the player answers. The full video "
     "tries that on twelve more musicians, a city full of birds, and the skip button. Tanmay "
     "Kulkarni, for Humanitarians AI.",
     voice("Every room is asking.", ("Simulated cathedral · dry", "both passes"), [PAUSES, HELD],
           "Full video: twelve more musicians, birds in Leiden, the skip button · @HumanitariansAI",
           L.SRC_IR + " · " + L.SRC_SKW, caption_cue="The full video"),
     ["A13", "A17"])


def main():
    rows = L.factcheck_rows()
    ids = [b[0] for b in BEATS]
    assert len(ids) == len(set(ids)), "duplicate beat_id"
    MP3.mkdir(exist_ok=True)
    errors, beats = [], []
    for bid, act, tone, text, shot, refs, demo_from, hold in BEATS:
        for r in refs:
            if r not in rows:
                errors.append(f"{bid}: FACTCHECK row {r} missing")
        for s in [text, *L.walk_strings(shot)]:
            if L.PLACEHOLDER.search(s):
                errors.append(f"{bid}: placeholder text: {s[:60]!r}")
        if L.DIGIT_YEAR.search(text):
            errors.append(f"{bid}: digit year in narration: {L.DIGIT_YEAR.search(text).group()}")
        if demo_from:
            for ext in (".wav", ".mp3"):     # COPY, never link (BEATS.md #12: a hardlink un-mastered both cuts)
                shutil.copyfile(LONG / "mp3" / f"beat-{demo_from}{ext}", MP3 / f"beat-{bid}{ext}")
            est = json.loads((LONG / "envelopes" / f"{demo_from}.json").read_text())["seconds"]
        else:
            est = MEASURED.get(bid, round(len(text.split()) / L.WPS, 1))
        rem = shot["remotion"]
        rem["pattern"] += "OFL916"
        props = rem["props"]
        if rem["pattern"].startswith("RoomVoice"):
            props.pop("envelopeFrom", None)
            for ps in props["passes"]:
                env = json.loads((LONG / "envelopes" / f"{ps.pop('from')}.json").read_text())
                ps.pop("ir")
                ps.update({"dry": env["dry"], "room": env["room"], "fps": env["fps"],
                           "dryLabel": "the voice", "roomLabel": "what the room adds"})
            props["floorDb"] = -48
            props["emptyLabel"] = ""
        for k in [k for k in props if k.endswith("Cue")]:
            cue = props.pop(k)
            if cue is None:
                props[k[:-3]] = None
                continue
            if cue not in text:
                errors.append(f"{bid}: cue not in narration: {cue!r}")
                continue
            mp3 = MP3 / f"beat-{bid}.mp3"
            props[k[:-3]] = (spoken_at(text, str(mp3), cue) if bid in MEASURED and mp3.exists()
                             else round(len(text[:text.index(cue)].split()) / L.WPS, 2))
        props["durationSeconds"] = round(est + 0.1, 2)
        beats.append({"beat_id": bid, "act": act, "tone": tone, "narration_text": text, "shot": shot,
                      "estimated_duration_s": est, "word_count": len(text.split()),
                      "audio_file": f"mp3/beat-{bid}.mp3", "engine": "kokoro", "voice": L.VOICE,
                      **({"demo_audio_from": f"../mp3/beat-{demo_from}.mp3"} if demo_from else {}),
                      **({"hold_after_s": hold} if hold else {}),
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    if errors:
        sys.exit("BUILD FAILED\n  " + "\n  ".join(errors))
    # The same two checks shorts.py runs before it marks a Short "ready" (shorts.py §validation):
    # every beat's pattern has a registered portrait composition, and the total is under 180 s.
    # Computed here because this Short is its own script, not a shorts.py derivative. Never hardcoded.
    root = (LONG.parent.parent / "brutalist.art" / "runtime" / "remotion" / "src" / "Root.tsx").read_text()
    blocked = [f"{b['beat_id']}: {b['shot']['remotion']['pattern']} has no registered 9:16 composition"
               for b in beats if not b["shot"]["remotion"]["pattern"].endswith("916")
               or f'id="{b["shot"]["remotion"]["pattern"]}"' not in root]
    total = sum(b["estimated_duration_s"] + b.get("hold_after_s", 0) for b in beats)
    if total >= 180:
        blocked.append(f"Planned Short: {total:.2f}s must be strictly under 180 seconds")
    sheet = {"metadata": {
        "title": "He Slowed Down in the Driest Hall Too", "title_status": "WORKING",
        "structure": "THE VOICE CHANGES ROOMS (Short: one arc)", "slug": "how-a-room-changes-music-short",
        "aspect_ratio": "9:16", "fit": "pad", "kind": "short",
        "total_estimated_duration_seconds": round(total, 2),
        "short_validation": {"status": "blocked" if blocked else "ready", "errors": blocked},
        "voice": L.VOICE, "voice_kokoro": L.VOICE, "engine": "kokoro",
        "chip": "@HumanitariansAI", "palette": "claude", "ground": "#FAF9F5",
        "note": "Short draft 1. Generated by short/build_short_sheet.py. Its own script; needs its own Gate P.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(b["estimated_duration_s"] for b in beats)
    print(f"{len(beats)} beats · {sum(b['word_count'] for b in beats)} words · ~{total:.0f} s")
    for b in beats:
        print(f"  {b['beat_id']:4} {b['act']:22} {b['word_count']:3}w ~{b['estimated_duration_s']:5}s  {b['tone']}")


if __name__ == "__main__":
    main()
