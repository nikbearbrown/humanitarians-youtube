#!/usr/bin/env python3
"""make_captions.py: SRT + VTT for a Week 25 master (copied from the Week 25 topic video; DISPLAY map replaced for the work video), from its beat_sheet.json and measured audio.

    python3 make_captions.py .       0.3    # the long
    python3 make_captions.py short   0.3    # the Short

TIMING. Each word's start is on the WHISPER clock (cue_align.whisper_words: Whisper's words, snapped to the
beat audio's own pauses), falling back to the pause clock (cue_align.word_starts), i.e.
sentences pinned to the real pauses in the beat's own audio, letters interpolated across speech
only. Beat starts on the master are the compiled clips' durations plus the pacing hold, exactly
as pacing_pass.py lays them out. (Week 23's captions apportioned by word count: ~0.5s error.)

TEXT. Captions show the WRITTEN form. The narration carries TTS spellings so Kokoro says things
right ("Foo-roo-zah-wah", "gee", "nineteen eighty-three"). DISPLAY maps each back ("Furuzawa",
"g", "1983") before segmenting, so a multi-word phrase can never be split across two cues.

RULES (carried from Week 23's make_captions.py; the defects they prevent are in its docstring):
  WRAP     a cue must actually wrap into <= 2 lines of <= 42 characters (attempted, not measured)
  BREAK    prefer ending a cue at a sentence end, then at a clause (, : ;), never mid-phrase
  PAUSE    a cue never spans a real pause longer than 0.35s; the caption leaves when the voice stops
  MERGE    a cue shorter than 1.2s merges BACKWARD into its predecessor
  SLUG     the output name is derived from the sheet's metadata.slug, never a literal
"""
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cue_align import word_starts, speech_spans, whisper_words, pauses

MAX_CHARS, MAX_LINES, MIN_DUR, MAX_DUR, PAUSE_BREAK = 42, 2, 1.2, 6.0, 0.35

# TTS spelling → written form. Longest first; matched on whole words, punctuation carried over.
DISPLAY = [
    # Week 25 work video: numbers the voice says in words, shown as written in the captions
    (["zero", "point", "six", "two", "five"], "0.625"),
    (["zero", "point", "six", "three"], "0.63"),
    (["zero", "point", "six", "two"], "0.62"),
    (["zero", "point", "six", "one"], "0.61"),
    (["zero", "point", "six"], "0.6"),
    (["one", "point", "zero"], "1.0"),
]
SUBSTR = [("My-croft", "Mycroft")]   # Kokoro respelling (it says MICK-roft otherwise); captions show the real name


def core(w):
    return re.sub(r'^[\"“‘(]+|[\"”’),.:;!?]+$', "", w)


def tokens(text, starts):
    """[(display_text, start_s)] with DISPLAY phrases merged into one token."""
    ws = text.split(); out = []; i = 0
    while i < len(ws):
        for spoken, shown in DISPLAY:
            n = len(spoken)
            if [core(x).lower() for x in ws[i:i + n]] == spoken:   # a sentence may open on the phrase
                pre = re.match(r'^[\"“‘(]*', ws[i]).group(0)
                post = re.search(r'[\"”’),.:;!?]*$', ws[i + n - 1]).group(0)
                out.append((pre + shown + post, starts[i], i, i + n)); i += n
                break
        else:
            w = ws[i]
            for a, b in SUBSTR:
                w = w.replace(a, b)
            out.append((w, starts[i], i, i + 1)); i += 1
    return out


def wrap(text):
    """Balanced wrap: one line if it fits, else the two-line split with the most even lengths.
    Returns lines, or None if it cannot fit in MAX_LINES x MAX_CHARS."""
    ws = text.split()
    if len(text) <= MAX_CHARS:
        return [text]
    best = None
    for k in range(1, len(ws)):
        a, b = " ".join(ws[:k]), " ".join(ws[k:])
        if len(a) <= MAX_CHARS and len(b) <= MAX_CHARS:
            score = abs(len(a) - len(b)) - (6 if re.search(r'[,:;.?!]["”’)]*$', ws[k - 1]) else 0)
            if best is None or score < best[0]:
                best = (score, [a, b])
    return best[1] if best else None


# words a cue may start with when a sentence has to be split with no punctuation to help
SOFT = {"and", "but", "or", "so", "because", "that", "which", "who", "when", "where", "while",
        "if", "to", "in", "on", "of", "for", "from", "with", "at", "by", "as", "than", "before",
        "after", "not", "the", "a", "under"}


def split_run(run):
    """Split a run of tokens into caption-sized pieces at the best-balanced break."""
    txt = " ".join(t[0] for t in run)
    span = run[-1][4] - run[0][1]
    if wrap(txt) and span <= MAX_DUR:
        return [run]
    n = len(run); best = None
    for k in range(1, n):
        left, right = run[:k], run[k:]
        lc = len(" ".join(t[0] for t in left)); rc = len(" ".join(t[0] for t in right))
        w = left[-1][0]
        if re.search(r'[.?!]["”’)]*$', w): bonus = 40
        elif re.search(r'[,:;—]["”’)]*$', w): bonus = 25
        elif core(right[0][0]).lower() in SOFT: bonus = 10
        else: bonus = 0
        if len(left) < 2 or len(right) < 2:
            bonus -= 30                                   # no one-word orphans
        score = bonus - abs(lc - rc) * 0.5
        if best is None or score > best[0]:
            best = (score, k)
    k = best[1]
    return split_run(run[:k]) + split_run(run[k:])


def word_timing(text, mp3):
    """(starts, ends) per narration word. Starts: the Whisper clock (Whisper's words snapped to the
    audio's own pauses) when _qc/whisper/ has this beat, else the pause clock. Ends: the next word's
    start, or the start of the silence in between when there is one."""
    ww = whisper_words(mp3)
    if ww is not None and ww[0] == text.split():
        starts = ww[1]
    else:
        starts, _ = word_starts(text, mp3)
    lead, spans, tail = pauses(str(mp3))
    ends = []
    for i, s0 in enumerate(starts):
        nxt = starts[i + 1] if i + 1 < len(starts) else tail
        gap = [ps for ps, pe in spans if s0 < ps < nxt]
        ends.append(min(gap) if gap else nxt)
    return starts, ends


def cues_for_beat(text, mp3, offset):
    starts, wend = word_timing(text, mp3)
    toks = tokens(text, starts)
    span_end = {k: wend[k] for k in range(len(wend))}
    # token = (text, start, first_word, last_word_excl, end): end is the next word's start inside
    # a run of speech, or the run's end at a pause
    full = []
    for j, (w, st, a, b) in enumerate(toks):
        nxt = toks[j + 1][1] if j + 1 < len(toks) else None
        e = span_end[b - 1]
        full.append((w, st, a, b, nxt if nxt is not None and nxt <= e + 0.05 else e))
    # runs = sentences, further cut at any real pause longer than PAUSE_BREAK
    runs, cur = [], []
    for j, t in enumerate(full):
        cur.append(t)
        nxt = full[j + 1][1] if j + 1 < len(full) else None
        if re.search(r'[.?!]["”’)]*$', t[0]) or nxt is None or nxt - t[4] > PAUSE_BREAK:
            runs.append(cur); cur = []
    pieces = [p for r in runs for p in split_run(r)]
    cues = [[offset + p[0][1], offset + p[-1][4], " ".join(t[0] for t in p)] for p in pieces]
    # MERGE a too-short cue into a neighbour (backward first) when the result still wraps and
    # doesn't bridge a real pause
    i = 0
    while i < len(cues):
        s0, e0, t0 = cues[i]
        if e0 - s0 < MIN_DUR:
            if i > 0 and wrap(cues[i - 1][2] + " " + t0) and s0 - cues[i - 1][1] <= PAUSE_BREAK and e0 - cues[i - 1][0] <= MAX_DUR:
                cues[i - 1][1] = e0; cues[i - 1][2] += " " + t0; del cues[i]; continue
            if i + 1 < len(cues) and wrap(t0 + " " + cues[i + 1][2]) and cues[i + 1][0] - e0 <= PAUSE_BREAK and cues[i + 1][1] - s0 <= MAX_DUR:
                cues[i + 1][0] = s0; cues[i + 1][2] = t0 + " " + cues[i + 1][2]; del cues[i]; continue
        i += 1
    return cues


def ts(t, sep):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


def main():
    reel = (HERE / sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE
    hold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    slug = sheet["metadata"]["slug"]
    allc, t = [], 0.0
    for b in sheet["beats"]:
        if b.get("narration_text"):
            allc += cues_for_beat(b["narration_text"], reel / "mp3" / f"beat-{b['beat_id']}.mp3", t)
        t += dur(reel / "clips" / f"{b['beat_id']}.mp4") + hold
    t -= hold
    # LINGER: a caption may stay up into the pause after its words, toward a comfortable reading
    # time (CPS characters/s), but never past the next caption's start. Fast narration can't be read
    # slower than it's spoken, so this only borrows silence, never the next line's time.
    CPS = 17.0
    for k, c in enumerate(allc):
        want = c[0] + len(c[2]) / CPS
        nxt = allc[k + 1][0] - 0.04 if k + 1 < len(allc) else t
        c[1] = min(max(c[1], want), max(c[1], nxt), c[1] + 1.5)
    # no overlaps; captions end a hair before the next begins
    for a, b in zip(allc, allc[1:]):
        a[1] = min(a[1], b[0] - 0.02)
    srt, vtt = [], ["WEBVTT", ""]
    for i, (s, e, txt) in enumerate(allc, 1):
        lines = wrap(txt)
        assert lines, f"cue {i} does not wrap: {txt!r}"
        srt += [str(i), f"{ts(s, ',')} --> {ts(e, ',')}", *lines, ""]
        vtt += [f"{ts(s, '.')} --> {ts(e, '.')}", *lines, ""]
    (reel / f"{slug}.srt").write_text("\n".join(srt))
    (reel / f"{slug}.vtt").write_text("\n".join(vtt))
    # self-check: every narrated word appears, in order, in written form
    shown = " ".join(c[2] for c in allc).split()
    expect = []
    for b in sheet["beats"]:
        if b.get("narration_text"):
            expect += [x[0] for x in tokens(b["narration_text"], [0] * len(b["narration_text"].split()))]
    # compare as word sequences: a display form may contain spaces ("2 − √2", "chapter 13")
    assert shown == " ".join(expect).split(), "caption text != narration"
    d = [e - s for s, e, _ in allc]
    print(f"{slug}.srt/.vtt · {len(allc)} cues · {min(d):.2f}–{max(d):.2f}s (median {sorted(d)[len(d)//2]:.2f}s) · "
          f"last cue ends {allc[-1][1]:.2f}s of {t:.2f}s")


if __name__ == "__main__":
    main()
