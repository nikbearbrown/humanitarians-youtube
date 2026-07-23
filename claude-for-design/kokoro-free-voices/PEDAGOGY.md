# PEDAGOGY.md — Kokoro: Free Voices (With Names)

Pedagogy audit against the SLATE-RUNNER checklist. Written before any audio generation
(GATE P). NOTE: only B00 spends anything (a few ElevenLabs cents for Bear's open);
B01–B99 generate at $0.00 via generate_audio_kokoro.py.

## Act structure (required: hook → argument → reveal → how → close)

| Act | Beats | Present? |
|-----|-------|----------|
| Hook / handoff | B00 | ✓ — Bear's clone opens, then hands the mic to a free cast "with names" |
| What it is | B01 | ✓ — Bella: 82M params, Apache 2.0, local, no API/meter/bill |
| The reveal | B02 | ✓ — Sarah: same-interface plug; downstream never knows |
| The honest record | B03 | ✓ — Adam reads his own F+ grade; free has a range, hear the bottom |
| The how | B04–B06 | ✓ — Michael: the casting field; Emma: the graded roster; George: previz use |
| The tradeoff | B07–B08 | ✓ — Puck: no cloning, none of us is you; Santa: the D- wink |
| The split + close | B09 + B99 | ✓ — hero: metered/flat/free, "who speaks is taste"; CTA |

Act structure: **PASS**

## Key-case cold open

B00 opens on the strongest possible contrast — the familiar cloned voice announcing its
own replacement for the next two minutes. The handoff IS the hook. **PASS**

## Gap-formula question beat

B00 raises it (a cast that costs nothing? with names?); B01–B02 answer what and why it
plugs in; B03 immediately complicates it honestly (F+ exists); B07 names the real limit
(no cloning). Tension resolved at B09's three-engine split. **PASS**

## Utility-framing lint

- B02: "downstream never knows" → no pipeline rework to adopt it
- B03: grades are the pack's own → viewer can trust the range claim
- B04: one field casts a beat → viewer knows the exact workflow
- B06: previz use → viewer knows when free beats paid
- B07: "when the video is your name, the voice is yours" → clear decision rule
- B09: three engines, one sentence each → the whole roster is memorizable

Utility framing: **PASS**

## Honesty check

Every grade spoken or shown (A-, C+, F+, B-, C, D-) comes from the pack's own VOICES.md
(hexgrad/Kokoro-82M), fetched 2026-07-13 — FACTCHECK re-verifies at build against the
installed voice pack (--list-voices) and adjusts names/grades if the pack differs. Adam
and Santa keep their failing grades on screen; the no-cloning limit gets its own beat.
Voice count stated as "about twenty-eight" — verify exact count at build. **PASS**

VERDICT: PASS
