#!/usr/bin/env python3
"""SRT + VTT for a Week 25 work-video master, timed on the WORD CLOCK (mp3/words.json from align.py).

Why not make_captions.py: on the long master its Whisper-snapped clock ended "So the question I couldn't put down
was this." at 17.5 s although the voice runs to 18.2 s, and opened the next cue a second before "If" is spoken
(final PROOF, 2026-10-04). words.json is the clock every on-screen cue already uses, and it agrees with Whisper
word timestamps to within ~0.1 s on that passage. Display forms (0.625, Mycroft) come from make_captions.DISPLAY.

    python3 make_captions_words.py .       0.3    # the long
    python3 make_captions_words.py short   0.3    # the Short

RULES: <= 2 lines of <= 42 chars; break at a sentence end when the cue has run >= 1.5 s, else at a clause; a cue never
spans a pause > 0.6 s; a cue shorter than 1.2 s merges into a neighbour when the text still fits, otherwise it is held
on screen into the following gap; cues never overlap; each ends 0.25 s after its last word (never past the next start).
"""
import json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_captions import DISPLAY, SUBSTR, core   # noqa: E402

MAXC, MAXL, MIN_DUR, TAIL, PAUSE = 42, 2, 1.2, 0.25, 0.6


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


def wrap(text):
    """One line if it fits; two balanced lines (no one-word orphan) when they fit; else greedy (caller splits)."""
    ws = text.split()
    if len(text) <= MAXC:
        return [text]
    two = [(" ".join(ws[:k]), " ".join(ws[k:])) for k in range(1, len(ws))]
    two = [p for p in two if len(p[0]) <= MAXC and len(p[1]) <= MAXC]
    if two:
        return list(min(two, key=lambda p: max(len(p[0]), len(p[1]))))
    lines, cur = [], ""
    for w in ws:
        if cur and len(cur) + 1 + len(w) > MAXC:
            lines.append(cur); cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + ([cur] if cur else [])


def display_tokens(text, ws, fps, t0):
    """[(display text, start, end)] for one beat, DISPLAY phrases merged, SUBSTR applied."""
    words = text.split(); out = []; i = 0
    st = [t0 + w["startFrame"] / fps for w in ws]
    en = [t0 + max(w["endFrame"], w["startFrame"] + 1) / fps for w in ws]
    while i < len(words):
        for spoken, shown in DISPLAY:
            n = len(spoken)
            if [core(x).lower() for x in words[i:i + n]] == spoken:
                pre = re.match(r'^[\"“‘(]*', words[i]).group(0)
                post = re.search(r'[\"”’),.:;!?]*$', words[i + n - 1]).group(0)
                out.append((pre + shown + post, st[i], en[i + n - 1])); i += n
                break
        else:
            w = words[i]
            for a, b in SUBSTR:
                w = w.replace(a, b)
            out.append((w, st[i], en[i])); i += 1
    return out


def _txt(c):
    return " ".join(t[0] for t in c)


CLAUSE = re.compile(r"[,;:.?!][\"”’)]*$")


def segment(tokens):
    """Token lists → cues. When a cue fills up it breaks at its last clause or sentence end (never mid-phrase if a
    clause break exists), so a cue never opens on the tail of the previous sentence."""
    cues, cur = [], []
    for tok in tokens:
        if cur:
            gap = tok[1] - cur[-1][2]
            if gap > PAUSE:
                cues.append(cur); cur = []
            elif len(wrap(_txt(cur + [tok]))) > MAXL:
                j = max((k for k in range(1, len(cur)) if CLAUSE.search(cur[k][0])), default=None)
                if j is not None and j < len(cur) - 1:
                    cues.append(cur[:j + 1]); cur = cur[j + 1:]
                elif re.search(r"[.?!][\"”’)]*$", tok[0]) and len(cur) >= 4:
                    # the overflowing word ends a sentence and there is no clause to break at: split in balanced
                    # halves so the sentence's tail travels with it (a cue must not open on "other.")
                    ks = [k for k in range(2, len(cur) - 1) if len(wrap(_txt(cur[:k]))) <= MAXL and len(wrap(_txt(cur[k:] + [tok]))) <= MAXL]
                    if ks:
                        k = min(ks, key=lambda k: abs(len(_txt(cur[:k])) - len(_txt(cur[k:] + [tok]))))
                        cues.append(cur[:k]); cur = cur[k:]
                    else:
                        cues.append(cur); cur = []
                else:
                    cues.append(cur); cur = []
        cur.append(tok)
        if re.search(r"[.?!][\"”’)]*$", tok[0]) and cur[-1][2] - cur[0][1] >= 1.5:
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)
    # short cues: merge into a neighbour if the text fits; else rebalance with the previous cue at a clause
    i = 0
    while i < len(cues):
        c = cues[i]
        if c[-1][2] + TAIL - c[0][1] < MIN_DUR:
            if i + 1 < len(cues) and len(wrap(_txt(c + cues[i + 1]))) <= MAXL and not re.search(r"[.?!][\"”’)]*$", c[-1][0]):
                cues[i + 1] = c + cues[i + 1]; cues.pop(i); continue
            if i > 0 and len(wrap(_txt(cues[i - 1] + c))) <= MAXL:
                cues[i - 1] = cues[i - 1] + c; cues.pop(i); i -= 1; continue
            if i > 0:   # rebalance: split prev+c at the clause break nearest the middle
                both = cues[i - 1] + c
                cands = [k for k in range(1, len(both) - 1) if CLAUSE.search(both[k][0])
                         and len(wrap(_txt(both[:k + 1]))) <= MAXL and len(wrap(_txt(both[k + 1:]))) <= MAXL]
                if cands:
                    mid = len(_txt(both)) / 2
                    k = min(cands, key=lambda k: abs(len(_txt(both[:k + 1])) - mid))
                    cues[i - 1], cues[i] = both[:k + 1], both[k + 1:]
        i += 1
    out = [[_txt(c), c[0][1], c[-1][2] + TAIL] for c in cues]
    for i, c in enumerate(out):
        nxt = out[i + 1][1] if i + 1 < len(out) else c[2] + 5
        if c[2] - c[1] < MIN_DUR:
            c[2] = min(c[1] + MIN_DUR, nxt - 0.04)
        c[2] = min(c[2], nxt - 0.04)
    return out


def ts(t, sep):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", sep)


def main():
    reel = Path(sys.argv[1]); hold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    words = json.loads((reel / "mp3" / "words.json").read_text()); fps = words["fps"]
    tokens, t0 = [], 0.0
    beats = sheet["beats"]
    for i, b in enumerate(beats):
        bid = b["beat_id"]
        tokens += display_tokens(b["narration_text"], words["beats"][bid], fps, t0)
        t0 += dur(reel / "clips" / f"{bid}.mp4") + (hold if i < len(beats) - 1 else 0)
    cues = segment(tokens)
    slug = sheet["metadata"]["slug"]
    srt = [f"{i + 1}\n{ts(a, ',')} --> {ts(b, ',')}\n" + "\n".join(wrap(t)) for i, (t, a, b) in enumerate(cues)]
    vtt = ["WEBVTT", ""] + [f"{ts(a, '.')} --> {ts(b, '.')}\n" + "\n".join(wrap(t)) + "\n" for t, a, b in cues]
    (reel / f"{slug}.srt").write_text("\n\n".join(srt) + "\n")
    (reel / f"{slug}.vtt").write_text("\n".join(vtt))
    d = [b - a for _, a, b in cues]
    print(f"{slug}.srt/.vtt · {len(cues)} cues · {min(d):.2f}–{max(d):.2f}s · last cue ends {cues[-1][2]:.2f}s of {t0:.2f}s")


if __name__ == "__main__":
    main()
