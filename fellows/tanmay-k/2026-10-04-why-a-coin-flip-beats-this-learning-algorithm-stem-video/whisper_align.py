#!/usr/bin/env python3
"""whisper_align.py: exact word timing and a word-by-word check of what the voice actually said.

For every narrated beat: faster-whisper (base.en, local) transcribes the beat's own mp3 with word
timestamps, and the transcript is aligned to narration_text (difflib, after normalising case,
punctuation, hyphens and spelled-out numbers). The result is cached per beat in
<reel>/_qc/whisper/<beat>.json:

  {"words": [narration words], "start": [s or null per word], "end": [...],
   "heard": "whisper transcript", "match": fraction of narration words matched}

A word Whisper didn't produce (or heard differently) gets null and is filled by interpolation
between its matched neighbours, so every word still has a time.

    ../../brutalist.art/.venv/bin/python whisper_align.py <reel> [<reel> ...]
"""
import difflib, json, re, sys
from pathlib import Path

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def two(n):
    return ONES[n] if n < 20 else TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])


def spell_number(tok):
    """'1983' -> 'nineteen eighty three', '2007' -> 'two thousand seven', '6' -> 'six', '1990s' -> ..."""
    m = re.fullmatch(r"(\d+)(s?)", tok)
    if not m:
        return tok
    n, plural = int(m.group(1)), m.group(2)
    if 2000 <= n <= 2009:
        out = "two thousand" + ("" if n == 2000 else " " + ONES[n - 2000])
    elif 1100 <= n <= 2099:
        out = two(n // 100) + " " + (two(n % 100) if n % 100 else "hundred")
    elif n < 100:
        out = two(n)
    else:
        return tok
    if plural:
        out = re.sub(r"y$", "ie", out) + "s"
    return out


def norm_tokens(word):
    w = word.lower().replace("’", "'").replace("—", " ")
    w = re.sub(r"[^\w'\s-]", " ", w).replace("-", " ")
    out = []
    for t in w.split():
        t = t.strip("'")
        if not t:
            continue
        out += spell_number(t).split()
    return out


def align_beat(text, segs):
    words = text.split()
    ntoks, owner = [], []
    for i, w in enumerate(words):
        for t in norm_tokens(w):
            ntoks.append(t); owner.append(i)
    htoks, htime = [], []
    for w in segs:
        ts = norm_tokens(w["word"])
        for k, t in enumerate(ts):
            # a multi-token Whisper word ("1983") shares its span across its spelled-out parts
            frac0 = k / len(ts); frac1 = (k + 1) / len(ts)
            htoks.append(t)
            htime.append((w["start"] + (w["end"] - w["start"]) * frac0, w["start"] + (w["end"] - w["start"]) * frac1))
    sm = difflib.SequenceMatcher(a=ntoks, b=htoks, autojunk=False)
    start = [None] * len(words); end = [None] * len(words); matched = set()
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            i = owner[a + k]
            s, e = htime[b + k]
            if start[i] is None or s < start[i]:
                start[i] = s
            end[i] = e if end[i] is None else max(end[i], e)
            matched.add(i)
    tail_unmatched = 0
    for i in range(len(words) - 1, -1, -1):
        if i in matched:
            break
        tail_unmatched += 1
    # interpolate unmatched words between matched neighbours
    known = [i for i in range(len(words)) if start[i] is not None]
    for i in range(len(words)):
        if start[i] is None and known:
            lo = max([k for k in known if k < i], default=None); hi = min([k for k in known if k > i], default=None)
            if lo is not None and hi is not None:
                f = (i - lo) / (hi - lo); start[i] = end[lo] + f * (start[hi] - end[lo]); end[i] = start[i]
            elif lo is not None:
                start[i] = end[i] = end[lo]
            else:
                start[i] = end[i] = start[hi]
    return words, start, end, len(matched) / max(1, len(words)), " ".join(w["word"].strip() for w in segs), tail_unmatched


def main():
    from faster_whisper import WhisperModel
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    for reel in map(Path, sys.argv[1:]):
        sheet = json.loads((reel / "beat_sheet.json").read_text())
        out = reel / "_qc" / "whisper"; out.mkdir(parents=True, exist_ok=True)
        for b in sheet["beats"]:
            text = b.get("narration_text")
            if not text:
                continue
            mp3 = reel / "mp3" / f"beat-{b['beat_id']}.mp3"
            segments, _ = model.transcribe(str(mp3), language="en", word_timestamps=True, beam_size=5,
                                           initial_prompt=None, condition_on_previous_text=False)
            ws = [{"word": w.word, "start": w.start, "end": w.end} for s in segments for w in (s.words or [])]
            words, st, en, match, heard, tail = align_beat(text, ws)
            if tail >= 2:
                # Whisper often drops a clip's last phrase (B16: "who holds the keys" at 17.1–18.0s,
                # confirmed on a separate pass). Re-transcribe the tail alone and splice it in.
                import subprocess, tempfile
                keep = len(words) - tail
                # start well before the last matched word: Whisper's own time for it may be wrong too
                # (B16 put "It's" at 18.26s; it is at 17.08s)
                t0 = max(0.0, (st[keep - 1] or 0) - 2.5) if keep else 0.0
                with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
                    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-i", str(mp3), "-af", "apad=pad_dur=1", tmp.name], check=True)
                    seg2, _ = model.transcribe(tmp.name, language="en", word_timestamps=True, beam_size=5)
                    ws2 = [{"word": w.word, "start": w.start + t0, "end": w.end + t0} for s2 in seg2 for w in (s2.words or [])]
                ws = [w for w in ws if w["end"] <= t0 + 0.05] + ws2
                words, st, en, match, heard, tail = align_beat(text, ws)
            (out / f"{b['beat_id']}.json").write_text(json.dumps(
                {"words": words, "start": st, "end": en, "heard": heard, "match": round(match, 3), "raw": ws}, indent=1))
            print(f"{reel.name}/{b['beat_id']}: {match*100:5.1f}% of narration words matched")


if __name__ == "__main__":
    main()
