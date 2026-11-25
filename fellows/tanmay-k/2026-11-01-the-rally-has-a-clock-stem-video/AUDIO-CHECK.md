# Audio check — Pong long film, first generation (2026-10-30)

Voice `am_onyx` (as Week 28), Kokoro v1.0, each beat synthesised **whole** (B13 in two whole pieces with a 5 s silent hold between
"Work it out." and the answer). Stage-1 loudness -16 LUFS / -2 dBTP; master normalisation to -14 LUFS comes at assembly.
Files: `mp3/beat-B00.wav` ... `B13.wav`, `mp3/timings.json` (Whisper word times, sentence spans, `inner_hold_at_s` for B13). Log: `_audio.log`.

## Pace and length
| | This film | Week 28 |
|---|---|---|
| Words | 875 | 854 |
| Narration, excluding the 5 s hold | 236 s | 244 s |
| Words per narration second | 3.7 | 3.5 |
| Total audio with holds | 267 s (4:27) | 286 s (4:46) |

Slightly brisker than last film (3.7 vs 3.5 words/s); within the 3.3-3.6 band plus a short-sentence effect. Listen to B00's count-off.

## Phonemes (front-loaded, no audio)
Checked: every ordinal (sixth ... twenty-seventh), "defense", "speed-ups", the decimals (point two one five, point one eight eight,
point two two five), "Pong", both names. All clean. Names: `tˈænmeɪ kˈʌlkɑːɹni`, `hjˌuːmɐnɪtˈɛɹiənz ˌeɪˈaɪ`.

## Whisper vs the signed text (small.en; medium.en to arbitrate)
Most differences are **spelling, not speech**: Whisper writes numerals and ordinals ("6th", "14th", "215", "1,200"), and "past"/"passed", "here is"/"heres".
No missing or extra words in B02, B03, B04, B12.

**Three words both Whisper models hear differently from the signed text** (these are real flags, not spelling):
| Beat | Signed | Heard (small.en and medium.en agree) | Likely cause |
|---|---|---|---|
| B05 | "half the field, **less** the paddle's own reach" | "lest the paddle's own reach" | "less the" runs together |
| B11 | "never **broke in** two hundred shots" | "never **broken** two hundred shots" | "broke in" links into "broken" |
| B01 | "I **liked** that line enough to wonder" | "I **like** that line" | final d drops before "that" |

None is a Kokoro fault in the sense of a mispronounced name; they are sound-alike joins. I have **not** changed the signed narration.
Any change voids Gate P for the lines touched, so this is your call. Options, each a one- or two-word edit:
- B05: "less the paddle's own reach" -> "minus the paddle's own reach".
- B11: "never broke in two hundred shots" -> "held for two hundred shots" (or "did not break in two hundred shots").
- B01: "I liked that line" -> "I like that line" (what is heard already; present tense reads naturally).
Or keep all three as signed and listen to them on the audio first.

---
## Update after the three edits (2026-10-30)
Applied at Tanmay's go-ahead: B01 "I like that line", B05 "minus the paddle's own reach", B11 "held for two hundred shots ... it always will".
Only B01, B05, B11 were regenerated (`make_audio.py B01 B05 B11`); the other eleven beats are byte-identical to the first generation.
Whisper (small.en) after: B05 1.000, B11 1.000, B01 0.976 (one weak form: signed "laws, and a game" heard as "laws in a game"; ear check).
Gate P re-signed for those lines (`GATE-P-SIGNOFF.md`, `PEDAGOGY.md`, `READ-ALOUD-v2-signed.md`). Total audio now 267.4 s (4:27).

## Cue timing (`cues.py` -> `CUES.json`)
Every cue is placed on the Whisper clock and leads its anchor word by 0.15 s. Whisper writes numbers and ordinals as numerals ("10th", "225"),
so the stored sentence spans were unreliable for the count-off lines; `cues.py` normalises numerals and ordinals before aligning.
Checked against `medium.en` and the audio's energy envelope: B09 "the tenth" starts about 15.54 s and "the nineteenth" about 16.14 s, as cued.
B13: the answer ("Point two two five") is placed at the end of the 5 s inner hold, 13.85 s. All cues are in order and inside each narration.
