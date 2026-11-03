#!/usr/bin/env python3
"""Week 24 Short — its own script, not long-form beats stitched together (Tanmay, 2026-09-27:
"the video should feel complete like not 2-3 beats stitched together with no sync in between").

ONE HOUSE, ONE CAMERA. After the hook, every beat is the same floor plan, and each beat opens in
exactly the state the previous one ended in (lights, door, accent). The Short has its own arc:
hook (the essay's sentence) → the house → the sweep (six lights, one continuous take) → the two
personal rooms (walk into the dark one) → the answer and the correction to the hook → the full
film. It answers its own question, then points to the long for the rest.

Cues are narration phrases; any key ending in "Cue" resolves to absolute seconds under the same key
without "Cue" (measured audio once mp3/timings.json exists, else the planning rate).
Every claim traces to ../FACTCHECK.md (refs per beat).
"""
import copy, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cue_align import spoken_at, spoken_at_whisper

# Beats timed on the WHISPER clock (cue_align.whisper_words: Whisper's words snapped to the audio's
# own pauses). Whisper showed their mid-phrase cues >0.25s off the pause clock (2026-09-27). Every
# other beat stays on the pause clock, which Whisper matched within 0.23s, so its renders stand.
WHISPER_CLOCK = {"S02", "S04", "S05"}

HERE = Path(__file__).resolve().parent
WPS = 3.17            # the long's measured Kokoro pace, am_onyx (1,093 words / 345s)
VOICE = "am_onyx"
TRAVEL = 1.1          # must match EightRoomsTour.tsx
SRC_2024 = "Gardner, Furuzawa & Stachura, ‘Who Owns Intelligence?’, MI Oasis, Oct 2024"
SRC_ESSAY = "‘Introducing Theorist.ai’, Humanitarians AI, March 2026"
# PROOF fix 5: ONE source line for every plan beat (S02–S05), so the footer never changes at a cut.
SRC_HOUSE = ("Rooms: Gardner, Frames of Mind (1983) + naturalist (mid-1990s) · " + SRC_2024
             + " · " + SRC_ESSAY)
TITLE_LONG = "Which of Gardner's Eight Intelligences Can a Machine Do?"
ROOMS = ["Linguistic", "Logical-mathematical", "Spatial", "Musical",
         "Bodily-kinesthetic", "Naturalist", "Interpersonal", "Intrapersonal"]
HEADING = "Gardner's house: eight rooms"
PAST = -10            # a cue in the past: the room is already in its state at frame 0


def rooms(**over):
    """All eight rooms dark, with per-room overrides: rooms(Spatial={'state': 'lit', 'atSecondsCue': …})."""
    return [{"name": r, "state": "dark", **over.get(r.replace("-", "_"), {})} for r in ROOMS]


def plan(rms, *, caption_steps=(), source=SRC_HOUSE, follow=True, follow_until_cue=None):
    p = {"heading": HEADING, "rooms": rms, "focus": -1, "caption": "", "source": source,
         "revealAtSeconds": 0, "captionAtSeconds": -1, "focusFollow": follow,
         "captionSteps": [dict(c) for c in caption_steps]}
    if follow_until_cue:
        p["followUntilSecondsCue"] = follow_until_cue
    return p


BEATS = []


def beat(bid, act, text, pattern, props, refs, motion="illustrate"):
    BEATS.append((bid, act, text, pattern, props, refs, motion))


# ── S01 · hook: the essay's sentence ────────────────────────────────────────────────────────────
beat("S01", "HOOK",
     "Hi, this is Tanmay Kulkarni, in for Humanitarians AI. An essay I read this week says that in "
     "nineteen eighty-three, technology \"was not yet a serious competitor\" to any of Howard Gardner's intelligences. "
     "So I went and read what Gardner wrote later. He did ask. And he answered, one intelligence at a time.",
     "ClaudeComposerAskOFL916",
     {"greeting": "Hi,", "topic": "INTELLIGENCE · AI", "segment": "Gardner's eight intelligences",
      "command": "which of Gardner's intelligences can a machine do?",
      "runningText": "reading Gardner, 1983 to 2026…", "folderLabel": "@HumanitariansAI",
      "modelLabel": "Claude", "effortLabel": "High", "placeholder": "Ask about the record",
      "output": ["“not yet a serious competitor to any of them”", f"Source: {SRC_ESSAY}"]},
     ["0.3", "0.5"], motion="type-on")

# ── S02 · the house: the accent walks the rooms as they're named, then the rule ──────────────────
S02 = ("Think of his theory as a house with eight rooms. Words, logic, space, music, the body, "
       "nature, other people, and yourself. In October twenty twenty-four, he and two colleagues took machines "
       "through that house. A light only comes on where they say a machine does what the room is for.")
names = ["Words,", "logic,", "space,", "music,", "the body,", "nature,", "other people,", "yourself."]
beat("S02", "THE HOUSE", S02, "EightRoomsOFL916",
     plan(rooms(**{r.replace("-", "_"): {"atSecondsCue": n} for r, n in zip(ROOMS, names)}),
          caption_steps=[{"atCue": "A light only comes on",
                          "text": "A light comes on only when Gardner's own writing says a machine does it."}],
          follow_until_cue="In October twenty"),
     ["1.1", "1.2", "3.2"])

# ── S03 · the sweep: six lights, one continuous take, each with its own quote ────────────────────
S03 = ("Words and logic go first. Language models, they write, \"clearly exhibit the signs\" of both. "
       "Two lights. Space: on, and that one surprised me, because chess and Go are filed there, not "
       "under logic. Music: on, even new pieces in distinctive styles. The body, the room I'd have bet stayed dark: programs that \"adroitly\" "
       "handle objects. On. And nature: on. That's six.")
beat("S03", "SIX LIGHTS", S03, "EightRoomsOFL916",
     plan(rooms(Linguistic={"state": "lit", "atSecondsCue": "Two lights."},
                Logical_mathematical={"state": "lit", "atSecondsCue": "Two lights."},
                Spatial={"state": "lit", "atSecondsCue": "Space: on"},
                Musical={"state": "lit", "atSecondsCue": "Music: on,"},
                Bodily_kinesthetic={"state": "lit", "atSecondsCue": "On. And nature",
                                    "accentAtSecondsCue": "The body,"},   # accent on the room being described
                Naturalist={"state": "lit", "atSecondsCue": "And nature"}),   # anchored cue (the pause before "And")
          caption_steps=[
              # opens on S02's closing caption, so nothing blinks at the cut
              {"at": 0, "text": "A light comes on only when Gardner's own writing says a machine does it."},
              {"atCue": "Language models", "text": "LLMs “clearly exhibit the signs of high logical-mathematical and high linguistic intelligence”"},
              {"atCue": "Space: on", "text": "Spatial: “Mastering games like chess or Go”"},
              {"atCue": "Music: on,", "text": "Musical: “creating credible new ones in distinctive styles”"},
              {"atCue": "The body,", "text": "Bodily-kinesthetic: “adroitly manipulating objects of various shapes and sizes”"},
              {"atCue": "And nature", "text": "Naturalist: grouping “human-created entities … from thimbles to airplanes”"},
          ]),
     ["3.3", "3.11"])

# ── S04 · the personal rooms: door ajar, then walk into the dark one ─────────────────────────────
# PROOF fix 2: the quote lands mid-interior, and the beat closes on the long's own resolution (B15)
# while the camera pulls back, so the evidence holds inside the room instead of 0.3s.
S04 = ("Two rooms are left, the personal ones, and here the paper says \"one should be more cautious.\" "
       "Other people, it leaves ajar: it lists diplomacy, salesmanship, therapeutic interactions. And "
       "knowing yourself stays dark. Using that word for a program at all, they write, \"can be seen "
       "as a 'category error.'\" So it isn't dark because a machine failed. It's dark because, on "
       "their reading, the question doesn't apply.")
LIT6 = {r: {"state": "lit", "atSeconds": PAST} for r in
        ["Linguistic", "Logical_mathematical", "Spatial", "Musical", "Bodily_kinesthetic"]}
s04_plan = plan(rooms(**LIT6,
                      Naturalist={"state": "lit", "atSeconds": PAST + 1},   # S03 ended on nature's accent
                      Interpersonal={"state": "ajar", "atSecondsCue": "Other people"},
                      Intrapersonal={"state": "dark", "atSecondsCue": "knowing yourself"}),
                caption_steps=[
                    {"at": 0, "text": "Naturalist: grouping “human-created entities … from thimbles to airplanes”"},
                    # PROOF fix 3: one caption for the whole of room 7 (was two, the first held 1.3s)
                    {"atCue": "one should be more cautious", "text": "Personal intelligences: “one should be more cautious” · Interpersonal evidence: “diplomacy, salesmanship, gamesmanship, therapeutic interactions”"},
                    # still up when the camera pulls back out of room 8
                    {"atCue": "can be seen", "text": "Intrapersonal: “can be seen as a ‘category error’”"},
                ])
s04_plan["focus"] = 7          # the camera's target; the accent itself follows the cues
beat("S04", "THE PERSONAL ROOMS", S04, "EightRoomsTourOFL916",
     {"plan": s04_plan, "_in_cue": "stays dark", "_out_cue": "It's dark because",
      "interior": {"kind": "intrapersonal", "title": "Room 8 · Intrapersonal",
                   "caption": "“can be seen as a ‘category error’”", "source": SRC_2024,
                   "captionAtSecondsCue": "can be seen", "extraAtSecondsCue": "stays dark"}},
     ["3.3", "3.5"], motion="push-in")

# ── S05 · the answer, and the correction to the hook ─────────────────────────────────────────────
S05 = ("So: six lights on, one door ajar, one room dark on purpose. And that essay's sentence? "
       "The same paper's history of the field puts programs doing logic and math back in nineteen fifty-six, before the house was "
       "even built. So one of those lights may have been on all along.")
beat("S05", "THE ANSWER", S05, "EightRoomsOFL916",
     plan(rooms(**{**LIT6,
                   "Logical_mathematical": {"state": "lit", "atSeconds": PAST, "accentAtSecondsCue": "back in nineteen"},
                   "Naturalist": {"state": "lit", "atSeconds": PAST},
                   "Interpersonal": {"state": "ajar", "atSeconds": PAST},
                   "Intrapersonal": {"state": "dark", "atSeconds": PAST + 1}}),    # S04 ended on room 8
          caption_steps=[
              # carried over from S04, then the count as it's spoken: no caption change AT the cut
              {"at": 0, "text": "Intrapersonal: “can be seen as a ‘category error’”"},
              {"atCue": "six lights on", "text": "Six lights on · one door ajar · one room dark on purpose"},
              # PROOF fix 4: the correction shown WITH the sentence it corrects (the long's B07 fix)
              {"atCue": "that essay's sentence", "text": "Essay: in 1983, technology “was not yet a serious competitor to any of them” · Record: 1956 programs “carried out mathematical and logical operations”"},
          ]),
     ["3.3", "3.4", "3.5", "0.3"])

# ── S06 · the full film ──────────────────────────────────────────────────────────────────────────
beat("S06", "THE FULL FILM",
     "The full video opens every door, and asks what it would take to switch on room seven. "
     "It's linked right below. Tanmay Kulkarni, in for Humanitarians AI.",
     "ClaudeTitleOutroFullOFL916",
     {"title": "Which of Gardner's eight intelligences can a machine do?", "handle": "@HumanitariansAI",
      "subline": "Tanmay Kulkarni, in for Humanitarians AI"},
     [], motion="fade")


def main():
    tpath = HERE / "mp3" / "timings.json"
    measured = json.loads(tpath.read_text()) if tpath.exists() else {}
    out = []
    for bid, act, text, pattern, props, refs, motion in BEATS:
        props = copy.deepcopy(props)
        words = len(text.split())

        def at(cue):
            # pause-anchored once audio exists (../cue_align.py); planning rate before
            before = len(text[:text.index(cue)].split())
            mp3 = HERE / "mp3" / f"beat-{bid}.mp3"
            return ((bid in WHISPER_CLOCK and spoken_at_whisper(text, mp3, cue)) or spoken_at(text, mp3, cue)) if bid in measured and mp3.exists() else round(before / WPS, 2)

        def resolve(d):
            if isinstance(d, dict):
                for k in [k for k in d if k.endswith("Cue") and isinstance(d[k], str)]:
                    d[k[:-3]] = at(d.pop(k))
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)

        ic = props.pop("_in_cue", None)
        oc = props.pop("_out_cue", None)
        resolve(props)
        end_s = measured.get(bid, words / WPS)
        if ic:
            props["interiorInAt"] = round(at(ic) + TRAVEL, 2)
            out_t = (at(oc) - 0.25) if oc else (end_s - 1.6)
            props["interiorOutAt"] = round(max(props["interiorInAt"] + 1.0, out_t), 2)
        # PROOF fix 6: every scene renders to the measured audio (no freeze-filled tails). Before
        # audio, the estimate, so a silent layout proof covers every frame (safe-zone check, pre-Gate P).
        props["durationSeconds"] = round(measured[bid] + 0.1, 2) if bid in measured else round(end_s + 0.1, 2)
        out.append({"beat_id": bid, "act": act, "narration_text": text,
                    "shot": {"type": "GRAPHIC", "status": "PROPS SET", "motion": motion,
                             "remotion": {"pattern": pattern, "props": props}},
                    "estimated_duration_s": round(words / WPS, 1), "word_count": words,
                    "audio_file": f"mp3/beat-{bid}.mp3",
                    **({"actual_duration_s": measured[bid]} if bid in measured else {}),
                    "engine": "kokoro", "voice": VOICE,
                    "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    derived = json.loads((HERE / "beat_sheet.json").read_text())["metadata"] if (HERE / "beat_sheet.json").exists() else {}
    meta = {**derived, "title": TITLE_LONG + " (Short)", "slug": "gardner-eight-rooms-short",
            "structure": "ONE HOUSE, ONE CAMERA (short-only script)",
            "note": "Short-only script (build_short_sheet.py). Not a cut of the long: own arc, own narration, "
                    "state carried across every cut. Gate P required on all narration.",
            "total_estimated_duration_seconds": round(sum(b.get("actual_duration_s", b["estimated_duration_s"]) for b in out), 1)}
    meta.pop("dropped_beats", None)
    (HERE / "beat_sheet.json").write_text(json.dumps({"metadata": meta, "beats": out}, indent=1, ensure_ascii=False))
    total = sum(b["word_count"] for b in out)
    print(f"{len(out)} beats · {total} words · ~{meta['total_estimated_duration_seconds']}s "
          f"({'measured' if measured else 'estimated'})")


if __name__ == "__main__":
    main()
