#!/usr/bin/env python3
"""make_srt.py — word-timed subtitles for this reel, from the audio clock.

WHY THIS LIVES HERE
-------------------
The pared-down toolkit has `align.py` (which writes the word clock,
`mp3/words.json`) but no SRT writer — the writer lived in the publishing
machinery that the free-only cut removed. So the reel carries its own, and it
reads exactly the same clock everything else does.

THE CLOCK, END TO END
---------------------
  Kokoro mp3 durations  →  beat_sheet.actual_duration_s   (the master clock)
  faster-whisper        →  mp3/words.json                 (word timings, beat-local frames)
  this script           →  <slug>.srt                     (absolute cue times)

Beat start = the running sum of the PRECEDING beats' actual_duration_s, so the
cues stay locked to the compiled timeline including the bookends (B00 cold open,
B11 verdict, B12 handoff, B13 outro) — every beat is subtitled, not just the body.

Cues are grouped by word, not by beat: up to MAX_CHARS characters over at most
MAX_LINES lines, broken early at sentence ends so a cue never straddles a full
stop. A beat with no word timings falls back to one cue spanning the beat.

Usage:
    python3 make_srt.py [--out FILE] [--sheet beat_sheet.json]
Re-run whenever any mp3 is regenerated (after `align.py`).
"""
import argparse
import json
import pathlib

MAX_CHARS = 74          # per cue, across all lines
MAX_LINES = 2
LINE_CHARS = 40
MIN_CUE_S = 0.70        # never flash a cue shorter than this
GAP_S = 0.04            # hold-off between consecutive cues


def ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def wrap(text: str) -> str:
    """At most two lines, broken where the sentence wants to break.

    A greedy fill splits wherever the character budget runs out, which lands
    mid-phrase ("not a study / session."). That reads badly anywhere and
    especially on the one line this script exists to land. So for the two-line
    case every candidate break is scored: balance first, a bonus for breaking
    just after punctuation, a penalty for orphaning a single short word.
    """
    if len(text) <= LINE_CHARS:
        return text

    words = text.split()
    best, best_score = None, None
    for i in range(1, len(words)):
        left, right = " ".join(words[:i]), " ".join(words[i:])
        if len(left) > LINE_CHARS or len(right) > LINE_CHARS:
            continue
        score = abs(len(left) - len(right))
        if left.rstrip().endswith((',', ';', ':', '—', '.', '?', '!')):
            score -= 14                       # break at a natural pause
        if len(words[i:]) == 1 and len(right) < 10:
            score += 12                       # don't orphan one short word
        if best_score is None or score < best_score:
            best, best_score = (left, right), score
    if best:
        return "\n".join(best)

    # too long for two lines — greedy fill, then rebalance
    lines, cur = [], ""
    for w in words:
        cand = f"{cur} {w}".strip()
        if len(cand) > LINE_CHARS and cur:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    if len(lines) > MAX_LINES:
        joined = " ".join(lines)
        cut = len(joined) // 2
        left = joined.rfind(" ", 0, cut)
        lines = [joined[:left], joined[left + 1:]] if left > 0 else [joined]
    return "\n".join(lines)


def cues_for_beat(words, beat_start, beat_dur, text):
    """Group a beat's word list into cues. Falls back to one cue for the beat."""
    if not words:
        return [(beat_start, beat_start + beat_dur, text.strip())] if text.strip() else []

    out, buf, start = [], [], None
    for i, w in enumerate(words):
        if start is None:
            start = beat_start + w["startFrame"] / FPS
        buf.append(w["text"])
        end = beat_start + w["endFrame"] / FPS
        joined = " ".join(buf)
        sentence_end = w["text"].rstrip().endswith((".", "?", "!", ":"))
        nxt = words[i + 1] if i + 1 < len(words) else None
        too_long = nxt is not None and len(joined) + 1 + len(nxt["text"]) > MAX_CHARS
        if sentence_end or too_long or nxt is None:
            out.append([start, end, joined])
            buf, start = [], None

    # enforce a readable floor, then de-overlap forward
    for c in out:
        if c[1] - c[0] < MIN_CUE_S:
            c[1] = c[0] + MIN_CUE_S
    for a, b in zip(out, out[1:]):
        if a[1] > b[0] - GAP_S:
            a[1] = max(a[0] + 0.30, b[0] - GAP_S)
    return [tuple(c) for c in out]


ap = argparse.ArgumentParser()
ap.add_argument("--sheet", default="beat_sheet.json")
ap.add_argument("--words", default="mp3/words.json")
ap.add_argument("--out", default=None)
a = ap.parse_args()

here = pathlib.Path(__file__).resolve().parent
sheet = json.loads((here / a.sheet).read_text())
wordbook = json.loads((here / a.words).read_text())
FPS = float(wordbook.get("fps") or sheet["metadata"].get("fps") or 30)
beats_words = wordbook.get("beats", {})

out_path = here / (a.out or f"{sheet['metadata']['slug']}.srt")

cues, t = [], 0.0
for b in sheet["beats"]:
    dur = float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0)
    cues += cues_for_beat(beats_words.get(b["beat_id"], []), t,
                          dur, b.get("narration_text", ""))
    t += dur

blocks = []
for i, (s, e, text) in enumerate(cues, 1):
    blocks.append(f"{i}\n{ts(s)} --> {ts(e)}\n{wrap(text)}\n")
out_path.write_text("\n".join(blocks))

covered = cues[-1][1] if cues else 0
print(f"[srt] {out_path.name}  {len(cues)} cues  "
      f"covering 0.00-{covered:.2f}s of {t:.2f}s  (fps={FPS:g})")
