# SHOTLIST — vox-photoelectric-effect

 handsome man with short buzz-cut hair, slight smirk,

Typed work order. Archive slots: drop restored assets into `pantry/` prefixed
by beat id (the pantry law — nanobanana restoration, WARMONO for period
plates, upscaled), then `python3 scripts/vox_pantry.py reels/vox-photoelectric-effect`.
Set `shot.focus` per still after intake. GRAPHIC beats render from this
reel's `vox_scenes.py` after audio lock.

Shot-type histogram: GRAPHIC 10 · STILL 6 · CARD 2 · COMPOSITE 1 (19 beats).
GRAPHIC 53% — accepted, same rationale as the UV film (evidence section).

---

## Archive slots (YOURS)

### B01 — STILL · Hertz (cold open)
Want: Heinrich Hertz portrait, or his spark-gap apparatus, 1880s.
- https://commons.wikimedia.org/w/index.php?search=Heinrich+Hertz+portrait&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/w/index.php?search=Hertz+spark+gap+apparatus&title=Special:MediaSearch&type=image

People prompt (route two — generated stand-in => source: ai + disclosure):
```
Hyper-realistic portrait of a 30-year-old Heinrich Rudolf Hertz, 1887, German physicist, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B03 — STILL · Lenard / cathode-ray-era lab
- https://commons.wikimedia.org/w/index.php?search=Philipp+Lenard&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/w/index.php?search=cathode+ray+tube+laboratory+1900&title=Special:MediaSearch&type=image

People prompt:
```
Hyper-realistic portrait of a 40-year-old Philipp Lenard, 1902, Hungarian-German physicist at cathode-ray apparatus, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B04 — COMPOSITE · arc lamp plate
Want: carbon arc lamp / searchlight, early 1900s (the "blinding red arc lamp").
Annotation chips land at assembly; plate slots now.
- https://www.loc.gov/photos/?q=arc+lamp+searchlight&fa=rights:public+domain
- https://commons.wikimedia.org/w/index.php?search=carbon+arc+lamp&title=Special:MediaSearch&type=image

### B06 — STILL · electroscope / precision instrument
- https://commons.wikimedia.org/w/index.php?search=gold+leaf+electroscope&title=Special:MediaSearch&type=image
- https://www.si.edu/search/collection-images?edan_q=electroscope

### B08 — STILL · Einstein, patent-office era
Want: young Einstein ~1905 (Bern years; the patent office portrait).
- https://commons.wikimedia.org/w/index.php?search=Einstein+1905+patent+office&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/wiki/Category:Albert_Einstein_by_year

People prompt:
```
Hyper-realistic portrait of a 26-year-old Albert Einstein, 1905, German-born physicist at a patent office desk in Bern, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B12 — STILL · Millikan
- https://commons.wikimedia.org/w/index.php?search=Robert+Millikan+laboratory&title=Special:MediaSearch&type=image

People prompt:
```
Hyper-realistic portrait of a 47-year-old Robert Millikan, 1915, American physicist in a vacuum-apparatus laboratory, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B15 — STILL · Einstein portrait ~1905 (bio kicker)
Period-correct young Einstein — NOT the elderly icon. Name + dates at assembly.
- https://commons.wikimedia.org/w/index.php?search=Albert+Einstein+1904+OR+1905+portrait&title=Special:MediaSearch&type=image

People prompt:
```
Hyper-realistic portrait of a 26-year-old Albert Einstein, 1905, German-born physicist, direct gaze, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

## GRAPHIC slots (PIPELINE — render after audio lock)

| beat | scene | what |
|---|---|---|
| B05 | B05_MoreNotFaster | isotype: one row of electron squares doubles to two rows, every square the same size; "same energy each" chip |
| B07 | B07_WavesCant | three classical expectations, each struck through in terracotta on cue |
| B09 | B09_LightQuanta | smooth navy wave greys out; discrete terracotta photon stream replaces it; "Lichtquanten" label |
| B10 | B10_OnePhotonOneElectron | photon dot in → electron dot out at a slate metal edge; sub-threshold photon fades with nothing |
| T01–T03 | T01_EqSentences / T02_EqGlossary / T03_EqExample | equation tangent K_max = hν − Φ (zones 2→3→4; spotlight Φ in T02) |
| B11 | B11_ThreeFactsFall | the three impossible facts return, each earning a navy check — mirror of B07 |
| B13 | B13_MillikanSlope | stopping potential vs frequency: three parallel navy lines, different thresholds, one crimson "h/e — same for every metal" |
| B14 | B14_NobelIrony | two slate cards: EINSTEIN 1921 / MILLIKAN 1923; ring on "not relativity" |

## CARD slots (PIPELINE)

B02 title, B16 next-tease (MATTER WAVES) — copy in beat_sheet.

## VERIFY before render

- 1240/300 = 4.13 eV; 4.13 − 2.28 = 1.85 eV; V_stop = 1.85 V (chapter)
- 1240/546 = 2.271 eV vs Φ = 2.28 eV — short by 0.009 eV (chapter)
- Slope h/e = 4.136×10⁻¹⁵ V·s, identical across metals (chapter)
- Dates: Hertz 1887 · Lenard 1902 · Millikan campaign 1914–16, Nobel 1923 ·
  Einstein 1905, Nobel 1921 (for THIS, not relativity)
