#!/usr/bin/env python3
"""Pause-anchored cue timing: when is a narration phrase actually SPOKEN in a Kokoro beat?

The old rule (words before the cue ÷ words in the beat × measured duration) assumes an even pace,
but Kokoro pauses at punctuation, so cues drifted from the speech by 0.5s on average and up to
1.2s (PROOF viewer pass, 2026-09-27, `short/_qc/cue_drift.py`). This module anchors timing to the
audio itself:

1. `silencedetect` finds the beat's pauses (leading and trailing silence as well).
2. Punctuation boundaries (after . ? ! : ; ,) are aligned IN ORDER to those pauses with a monotone
   DP. A sentence end that finds no pause costs more than a comma that finds none, because Kokoro
   nearly always pauses at a full stop and only sometimes at a comma.
3. Between anchors, time is interpolated by letters spoken (not words), which tracks syllables
   better than word count.

`spoken_at(text, mp3, duration, cue)` returns absolute seconds into the beat at which the first
word of `cue` begins. Used by build_beat_sheet.py (long), short/build_short_sheet.py and both
claims_at_assertion.py scripts, so the picture and the claim checks share one clock.
"""
import re
import subprocess
from functools import lru_cache

NOISE_DB = -38      # below this is silence (Kokoro's room tone sits far below it)
MIN_PAUSE = 0.08    # seconds: catches comma and colon pauses; the DP drops any that fall mid-phrase
SKIP_SENTENCE = 1.2  # DP cost of a sentence end with no pause
SKIP_COMMA = 0.35    # DP cost of a comma with no pause (common)


@lru_cache(maxsize=None)
def pauses(mp3):
    """(lead_end, [(start, end), ...] interior pauses, tail_start) for one beat's audio."""
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(mp3), "-af",
                          f"silencedetect=noise={NOISE_DB}dB:d={MIN_PAUSE}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", str(mp3)], capture_output=True, text=True).stdout)
    spans = list(zip(starts, ends + [dur] * (len(starts) - len(ends))))
    lead = 0.0
    if spans and spans[0][0] <= 0.02:
        lead = spans.pop(0)[1]
    tail = dur
    if spans and spans[-1][1] >= dur - 0.02:
        tail = spans.pop()[0]
    return lead, spans, tail


def _letters(ws):
    return sum(len(re.sub(r"[^A-Za-z0-9]", "", w)) or 1 for w in ws)


# v2 (a speaking-rate-constrained DP) was tried on 2026-09-27 and REJECTED: Whisper showed it moved
# correct anchors (B13's tiles 0.8s early, S03 "Space" 0.24s late). v1 below agrees with Whisper
# wherever a cue follows a real pause; mid-phrase cues that need better go on the Whisper clock.
@lru_cache(maxsize=None)
def anchors(text, mp3):
    """[(word_index, speech_resumes_s, speech_stopped_s)] aligned to real pauses: the word at
    word_index starts at speech_resumes_s, and the speech before it stopped at speech_stopped_s
    (the pause's start). Interpolating only across speech, never across a pause, is what keeps a
    cue just before a long pause from landing late (Naturalist in the Short's S03, +1.07s)."""
    words = text.split()
    lead, spans, tail = pauses(str(mp3))
    bounds = []  # (word index that starts after the boundary, is_sentence_end)
    for i, w in enumerate(words[:-1]):
        m = re.search(r'([.?!:;,])["”’\')]*$', w)
        if m:
            bounds.append((i + 1, m.group(1) in ".?!:;"))
    if not bounds or not spans:
        return [(0, lead, lead), (len(words), tail, tail)]
    # word-position estimate of each boundary inside the speech window, for the DP cost
    total = _letters(words)
    est = [lead + _letters(words[:i]) / total * (tail - lead) for i, _ in bounds]
    B, P = len(bounds), len(spans)
    INF = float("inf")
    dp = [[INF] * (P + 1) for _ in range(B + 1)]
    back = {}
    dp[0] = [0.0] * (P + 1)
    for i in range(1, B + 1):
        skip = SKIP_SENTENCE if bounds[i - 1][1] else SKIP_COMMA
        for j in range(P + 1):
            best, how = dp[i - 1][j] + skip, ("skip", j)
            if j > 0:
                if dp[i][j - 1] < best:
                    best, how = dp[i][j - 1], ("drop", j - 1)           # a pause with no boundary
                m = dp[i - 1][j - 1] + abs(est[i - 1] - spans[j - 1][1])
                if m < best:
                    best, how = m, ("match", j - 1)
            dp[i][j], back[(i, j)] = best, how
    i, j, pairs = B, P, []
    while i > 0:
        how, jj = back[(i, j)]
        if how == "match":
            pairs.append((bounds[i - 1][0], spans[jj][1], spans[jj][0]))
            i, j = i - 1, jj
        elif how == "skip":
            i -= 1
        else:
            j = jj
    return [(0, lead, lead)] + sorted(pairs) + [(len(words), tail, tail)]


def spoken_at(text, mp3, cue):
    """Seconds into the beat at which the first word of `cue` starts being spoken."""
    words = text.split()
    k = len(text[:text.index(cue)].split())
    A = anchors(text, str(mp3))
    for (i0, t0, _), (i1, _, t1) in zip(A, A[1:]):   # speech runs from t0 to the NEXT pause's start
        if i0 <= k < i1 or (k == i1 == len(words)):
            if k == i0:
                return round(t0, 2)
            frac = _letters(words[i0:k]) / max(1, _letters(words[i0:i1]))
            return round(t0 + frac * (t1 - t0), 2)
    return round(A[-1][1], 2)


def is_anchored(text, mp3, cue):
    """True when the cue starts exactly at a pause-aligned boundary (no interpolation)."""
    k = len(text[:text.index(cue)].split())
    return any(a[0] == k for a in anchors(text, str(mp3)))


def word_starts(text, mp3):
    """Start time (s into the beat) of every word, on the same pause-anchored clock as spoken_at,
    plus the time speech ends (the last word's end). Used for captions."""
    words = text.split()
    A = anchors(text, str(mp3))
    out = []
    for (i0, t0, _), (i1, _, t1) in zip(A, A[1:]):
        L = max(1, _letters(words[i0:i1]))
        for k in range(i0, i1):
            out.append(round(t0 + _letters(words[i0:k]) / L * (t1 - t0), 3))
    return out, A[-1][1]


def speech_spans(text, mp3):
    """[(first_word, last_word_exclusive, start_s, end_s)] for each run of speech between pauses."""
    A = anchors(text, str(mp3))
    return [(i0, i1, t0, t1) for (i0, t0, _), (i1, _, t1) in zip(A, A[1:])]


# ── Whisper clock (2026-09-27): exact word starts from whisper_align.py's per-beat cache ─────────
import json as _json
import os as _os
from pathlib import Path as _Path


SNAP = 0.3   # a Whisper word start this close to a real pause end can claim it (onsets are exact there)


def whisper_words(mp3):
    """(words, starts) from <reel>/_qc/whisper/<beat>.json, refined against the audio's own pauses.

    Whisper knows WHICH word; silencedetect knows exactly WHEN speech resumes. Each real pause end is
    claimed by at most ONE word, the word whose Whisper start is nearest (within SNAP), one to one and
    in order. Whisper's zero-length words (guesses, e.g. "logic" at 3.16=3.16 in S02) claim at lower
    priority, and a guess that claims nothing is interpolated by letters between its neighbours.
    Other unclaimed words keep Whisper's start. Starts are forced monotone."""
    p = _Path(mp3)
    f = p.parent.parent / "_qc" / "whisper" / (p.stem.replace("beat-", "") + ".json")
    if not f.exists():
        return None
    d = _json.loads(f.read_text())
    words, st, en = d["words"], list(d["start"]), list(d["end"])
    lead, spans, tail = pauses(str(mp3))
    merged = []
    for s0, e0 in spans:
        if merged and s0 - merged[-1][1] < 0.03:
            merged[-1][1] = e0
        else:
            merged.append([s0, e0])
    ends = [lead] + [e for _, e in merged]
    n = len(words)
    guess = [st[i] is None or en[i] is None or en[i] - st[i] < 0.03 for i in range(n)]
    # a word cannot START inside a silence: Whisper's early starts move to where speech resumes
    for i in range(n):
        if st[i] is not None:
            for s0, e0 in merged:
                if s0 + 0.02 < st[i] < e0 - 0.02:
                    st[i] = e0
                    break
    pairs = []
    for i in range(n):
        if st[i] is None:
            continue
        for j, e in enumerate(ends):
            dist = abs(e - st[i])
            if dist <= SNAP:
                pairs.append((dist * (1.6 if guess[i] else 1.0), i, j))
    pairs.sort()
    claim_w, claim_p = {}, set()
    for _, i, j in pairs:
        if i in claim_w or j in claim_p:
            continue
        # keep claims in order: no earlier word may hold a later pause, and vice versa
        if any((wi < i and pj > j) or (wi > i and pj < j) for wi, pj in claim_w.items()):
            continue
        claim_w[i] = j; claim_p.add(j)
    out = [None] * n
    for i in range(n):
        if i in claim_w:
            out[i] = ends[claim_w[i]]
        elif not guess[i]:
            out[i] = st[i]
    if out[0] is None:
        out[0] = lead
    idx = [i for i, v in enumerate(out) if v is not None]
    for i in range(n):
        if out[i] is None:
            lo = max(k for k in idx if k < i)
            hi = min([k for k in idx if k > i], default=None)
            # after punctuation, speech resumes after a pause: take the last pause end before the next
            # known word ("music, | the body" in S02; "On. | And" in S03)
            if i > 0 and re.search(r'[,.;:?!]["”’)]*$', words[i - 1]):
                lim = out[hi] if hi is not None else tail
                cands = [e for e in ends if out[lo] < e <= lim]
                if cands:
                    out[i] = cands[-1]
                    idx = sorted(idx + [i])
                    continue
            hi = min([k for k in idx if k > i], default=None)
            t1, j1 = (out[hi], hi) if hi is not None else (tail, n)
            L = max(1, _letters(words[lo:j1]))
            out[i] = out[lo] + _letters(words[lo:i]) / L * (t1 - out[lo])
    for i in range(1, n):
        out[i] = max(out[i], out[i - 1] + 0.05)
    return words, [round(x, 3) for x in out]


def spoken_at_whisper(text, mp3, cue):
    ww = whisper_words(mp3)
    if ww is None or ww[0] != text.split():
        return None
    k = len(text[:text.index(cue)].split())
    return round(ww[1][k], 2)


# CUE_CLOCK=whisper switches every caller of spoken_at to the Whisper clock (falls back to pauses)
if _os.environ.get("CUE_CLOCK") == "whisper":
    _pause_spoken_at = spoken_at

    def spoken_at(text, mp3, cue):  # noqa: F811
        w = spoken_at_whisper(text, mp3, cue)
        return w if w is not None else _pause_spoken_at(text, mp3, cue)
