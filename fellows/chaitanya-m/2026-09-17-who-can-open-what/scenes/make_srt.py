#!/usr/bin/env python3
"""
make_srt.py — subtitles for the FULL reel, bookends included.

TIMING MODEL (stated plainly, because it matters)
  Beat boundaries are EXACT: they come from actual_duration_s, the measured
  Kokoro audio, so no cue can drift across a cut.

  Within a beat, cue durations are allocated in proportion to character
  count. That is an approximation — it is not word-level forced alignment.
  It is accurate at every beat boundary and typically within a few tenths of
  a second inside a beat, which is well under the threshold where a reader
  notices.

  Each beat's cues are clipped to where SPEECH actually ends, detected with
  ffmpeg silencedetect, rather than to the end of the mp3. Kokoro pads every
  clip with ~0.5s of trailing silence; without this the last caption of each
  beat would hang in the quiet.

  Nothing is invented: cue text is the beat's narration, split only at
  sentence and clause boundaries.
"""
import argparse, json, re, subprocess
from pathlib import Path

MAX_CHARS = 84          # two comfortable lines
MIN_CUE   = 1.0         # seconds
WRAP_AT   = 42


def speech_end(mp3: Path, dur: float) -> float:
    """Where the voice stops, ignoring Kokoro's trailing pad."""
    r = subprocess.run(["ffmpeg", "-i", str(mp3), "-af",
                        "silencedetect=noise=-45dB:d=0.25", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    ends   = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    # a trailing silence is one that starts and is never closed before EOF
    if starts and (not ends or ends[-1] < starts[-1] or abs(ends[-1] - dur) < 0.05):
        return max(0.5, starts[-1])
    return dur


def split_cues(text: str):
    """Sentence-first, then clause, then hard-wrap. Never mid-word."""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    out = []
    for p in parts:
        if len(p) <= MAX_CHARS:
            out.append(p); continue
        chunks, cur = [], ""
        for piece in re.split(r'(?<=[,;:—])\s+', p):
            if len(cur) + len(piece) + 1 <= MAX_CHARS:
                cur = (cur + " " + piece).strip()
            else:
                if cur: chunks.append(cur)
                cur = piece
        if cur: chunks.append(cur)
        final = []
        for c in chunks:
            while len(c) > MAX_CHARS:
                cut = c.rfind(" ", 0, MAX_CHARS)
                if cut <= 0: break
                final.append(c[:cut]); c = c[cut+1:]
            final.append(c)
        out.extend(final)
    return [c for c in out if c.strip()]


def wrap(cue: str) -> str:
    if len(cue) <= WRAP_AT: return cue
    cut = cue.rfind(" ", 0, WRAP_AT + 8)
    return cue if cut <= 0 else cue[:cut] + "\n" + cue[cut+1:]


def ts(t: float) -> str:
    if t < 0: t = 0.0
    h = int(t // 3600); m = int((t % 3600) // 60)
    s = int(t % 60); ms = int(round((t - int(t)) * 1000))
    if ms == 1000: s += 1; ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    # Resolve audio relative to the SHEET's own folder, not this script's.
    # The short has its own rewritten outro mp3; reading the parent's would
    # clip that beat's captions to the wrong length.
    sheet_path = Path(a.sheet).resolve() if a.sheet else (
        Path(__file__).resolve().parent.parent / "beat_sheet.json")
    reel = sheet_path.parent
    sheet = json.loads(sheet_path.read_text())
    out = Path(a.out) if a.out else reel / "who-can-open-what.srt"

    cues, clock, n = [], 0.0, 0
    for b in sheet["beats"]:
        dur = b.get("actual_duration_s")
        if dur is None:
            raise SystemExit(f"[srt] {b['beat_id']} has no measured duration")
        dur = float(dur)
        text = (b.get("narration_text") or "").strip()
        if not text:
            clock += dur; continue
        mp3 = reel / b["audio_file"]
        sp = speech_end(mp3, dur) if mp3.exists() else dur
        parts = split_cues(text)
        chars = sum(len(p) for p in parts) or 1
        t = clock
        for i, p in enumerate(parts):
            share = sp * (len(p) / chars)
            if share < MIN_CUE: share = MIN_CUE
            end = min(clock + sp, t + share)
            if i == len(parts) - 1:
                end = clock + sp
            if end - t < 0.3:
                end = min(clock + sp, t + 0.3)
            n += 1
            cues.append((n, t, end, wrap(p), b["beat_id"]))
            t = end
        clock += dur

    body = "\n".join(f"{i}\n{ts(s)} --> {ts(e)}\n{txt}\n" for i, s, e, txt, _ in cues)
    out.write_text(body, encoding="utf-8")

    total = clock
    print(f"[srt] {out.name}: {len(cues)} cues across {total:.2f}s")
    per = {}
    for _, _, _, _, bid in cues: per[bid] = per.get(bid, 0) + 1
    for b in sheet["beats"]:
        bid = b["beat_id"]
        print(f"   {bid}  {per.get(bid,0):>2} cues   {'(bookend)' if bid in ('B00','B06','B07','B08') else ''}")
    # sanity
    bad = [c[0] for c in cues if c[2] <= c[1]]
    print(f"[srt] monotonic: {not bad}   last cue ends {cues[-1][2]:.2f}s / reel {total:.2f}s")
    gaps = [c for c in cues if 'getUserAccess' in c[3]]
    print(f"[srt] 'getUserAccess' in subtitles: {len(gaps)}")


if __name__ == "__main__":
    main()
