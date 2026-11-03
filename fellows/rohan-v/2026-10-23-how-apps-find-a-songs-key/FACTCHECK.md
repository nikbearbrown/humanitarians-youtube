# FACTCHECK — How Apps Find a Song's Key

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-23. "The run" means
`key.py` → `evidence/run.log` / `evidence/results.json` / `evidence/scene.json` (SHA-256 in
`MEASUREMENTS.txt`). The songs are **synthetic** Western songs (`songs.py`, generated from seeds); no
recording is used, measured or played. Outside facts, with URLs and confidence levels:
`week-09/_research/facts-key.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | DJ apps show a key next to a track | Serato and rekordbox display options (official pages, facts-key §5) | ✅ |
| 4 | B01 | A key is seven notes with one home; C major = the white keys, home C; A minor = the same seven notes, home A | music theory: the relative major/minor share a key signature (facts-key §6) | ✅ |
| 5 | B02 | Every frequency is folded into one of twelve note names, whatever the octave; that's chroma | Fujishima 1999 (pitch-class profile); librosa `chroma_stft` 12 bins (facts-key §1) | ✅ |
| 6 | B02 | In my C major pop song, C, G and E stand tallest | run: profile C 0.234, G 0.200, E 0.133 (next A 0.120, D 0.114) | ✅ measured |
| 7 | B02 | The listening clip is that song | `evidence/song_c_major_pop.wav` (first 6 s), appended unedited by `mix_listen.py` (level matched only) | ✅ |
| 8 | B03 | In 1982 psychologists asked listeners how well each note fits a key; the ratings give every key a shape | Krumhansl & Kessler 1982, *Psychological Review* 89(4):334–368, probe-tone ratings (facts-key §2) | ✅ |
| 9 | B03 | The app slides the song's bars against all 24 shapes and keeps the best correlation | Krumhansl–Schmuckler algorithm (facts-key §2); `key.py correlate()` | ✅ |
| 10 | B03 | C major scores 0.98; the next best, G major, only 0.72 | run: C major r = 0.976, G major 0.721 (the second-highest of 24; A minor 0.685 is third). Caught before render: the first script called A minor the closest rival | ✅ measured |
| 11 | B04 | Sixty songs: pop, rock, blues, two kinds of minor ballad, each in all twelve keys | `songs.STYLES` × 12 tonics, 20 s each | ✅ |
| 12 | B04 | Right on fifty of sixty; pop, rock and blues every one | run: right 50/60; pop, rock (flat 7th), 12-bar blues 12/12 each | ✅ measured |
| 13 | B05 | The ten misses were all natural-minor ballads; ten of twelve came out as the major key with the same notes | run: minor ballad relative 10, right 2; every other style 12/12 | ✅ measured |
| 14 | B05 | For A minor: 0.886 against 0.891 for C major | run EXAMPLE: A minor r = 0.886, C major r = 0.891 (6-decimal values in scene.json) | ✅ measured |
| 15 | B05 | Raise the seventh, and all twelve come out right | run: minor with raised 7th (harmonic minor, major V) 12/12 | ✅ measured |
| 16 | B05 | The standard test gives this mistake partial credit | MIREX audio key detection: relative major/minor = 0.3 (facts-key §4) | ✅ |
| 17 | B06 | This one moves up a semitone halfway | `songs.render("pop", 0, …, modulate_at=10, modulate_by=1)`: C major → C♯ major at 10 s | ✅ |
| 18 | B06 | Asked for one key, my detector said C minor | run KEY CHANGE: whole song → C minor | ✅ measured |
| 19 | B06 | In eight-second windows it hears C major, then C sharp major | run: windows centred 4.0–9.6 s C major; 12.4–16.1 s C♯ major (two windows across the change read C minor and F minor) | ✅ measured |
| 20 | B07 | Harmonic-mixing charts put the relative keys side by side | Mixed In Key's Camelot docs: the same number, A = minor, B = major; switch A↔B (facts-key §5) | ✅ |
| 21 | B07 | On a song with a key change, check each section | follows from B06 | ✅ as advice |

## Algebra, checked separately (MATH-TYPESETTING.md)

- **Correlation.** r = Σ(xᵢ − x̄)(yᵢ − ȳ) / √(Σ(xᵢ − x̄)² Σ(yᵢ − ȳ)²), x = the song's 12-value profile, y = a key's
  profile rotated to its tonic; `np.corrcoef` in `key.py`. Shown values are the run's, rounded to 2 decimals
  (B03) or 3 (B05).
- **Profiles.** Krumhansl–Kessler major 6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88;
  minor 6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17 (tonic first), matching Essentia
  and music21 (facts-key §2).

## Not claimed

- That relative and fifth errors are the most common errors in general (it depends on the system and genre).
- Any app's internal method or accuracy; MIREX accuracy figures (its classic set is classical MIDI renders).
- That synthetic songs behave exactly like recordings: the result is stated as my test, on my songs.
