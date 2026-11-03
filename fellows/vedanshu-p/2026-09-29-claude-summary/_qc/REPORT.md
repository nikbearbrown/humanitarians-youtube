# _qc/REPORT.md — Every Fix Has A Ceiling.

Frame-level visual QC (VISUAL QC LAW). Every verdict comes from reading
rendered PNGs in `_qc/frames/`; the mp4 probe is a FILE check, never QC.

| Field | Value |
|---|---|
| Master | `claude-rag-every-fix-has-a-ceiling.mp4` (beside this reel, per CLAUDE.md rule 3) |
| Resolution | **3840×2160** — confirmed by ffprobe after compile |
| Frame rate | 24 fps |
| Duration | 147.76s (2:28), 9 beats |
| Size | 9.8 MB |
| Audio | per-beat narration, mean −24.2 dB / peak −0.04 dB — see the audio note |
| Cut type | clean master (`compile.py` without `--review`); frame at 85s carries no beat marker |
| Voice | Kokoro `am_onyx`, local. **$0.00** |

---

## Beat-by-beat verdict

| Beat | Pattern | Verdict | Note |
|---|---|---|---|
| B00 | ClaudeComposerAsk | PASS | COLD OPEN LAW — ask shown answered; greeting "Selam, Vedanshu"; four output lines land the three chapters plus the thesis |
| B01 | BrutalistHesitantWriter | **PASS after MAJOR-01** | 13.9s; correction fires and all three lines complete |
| B02 | FaultSignatureTable | PASS | all four rows match Ch. 7's `_run-diagnose.txt`; baseline row sits back; source video named in the citation |
| B03 | GroundingDrift | PASS | both sentences equally confident, only the anchors differ; source video named |
| B04 | ShortlistReorder | PASS | connectors visibly cross; null verdict holds; absent answer keeps its terracotta |
| B05 | EvidenceTiers | PASS | solid ESTABLISHED bar against hollow NOT SETTLED; the caption states why the beat exists |
| BVDT | ClaudeVerdictArtifact | PASS | six lines legible, ending on what the ceilings buy |
| BHTF | ClaudeComposerAsk | PASS | HANDOFF LAW — layer-audit prompt complete and paste-ready |
| BOUT | TitleOutroChannel | PASS | exact title restate; **signature "Vedanshu Daxesh Patel"** renders |

---

## MAJOR-01 — B01's last line never finished typing

**Symptom.** At 10.7s of an 11.2s beat the third line read `Each one st|`. The
correction itself fired correctly — "Together they make RAG **easier to
diagnose**" — but the sentence that states the reel's thesis never completed
before the cut.

**Why the standard check missed it.** EXECUTIVE-SUMMARY LAW's post-render
verification is "media ≥ 8s and the correction on screen before the cut". Both
passed. The *full text* landing is a third condition the law does not name, and
it is the one that failed: this seed's hesitations and typo-corrections pushed
the performance past the audio.

**Fix — audio is the master clock, so the narration grew rather than the
duration being hand-edited:**

| | before | after |
|---|---|---|
| narration | 32 words | 42 words (adds "…and knowing where each of them stops is the skill this whole series has really been about") |
| measured duration | 11.16s | **13.95s** |
| `charMs` | 52 | 46 — margin for this seed's pauses |

**Verified by re-render:** all three lines complete, correction applied, beat
resolves on its full claim.

---

## Audio note — hot, but not clipped

The master peaks at **−0.039 dB**, where every earlier reel in this series sat
between −0.6 and −1.1 dB. Checked rather than assumed:

```
Peak level dB:  -0.038714
Flat factor:     0.000000
Abs Peak count:  1
```

`Flat factor: 0` means no consecutive samples sit at the ceiling — there is no
flat-topped clipping, only a single sample touching maximum. Two of Kokoro's
source files (B02, B03) peak at −0.0 dB themselves and `compile.py` applies no
normalisation, so the master inherits them.

Logged as an observation, not a defect: nothing is clipped, and platform
loudness normalisation will pull this down anyway. Worth knowing that this
series has no headroom margin built in.

---

## Compile-stage lint — both adjudicated, neither is a defect

| Lint | Verdict |
|---|---|
| `BOUT: OUTRO LAW wants ClaudeTitleOutro` | Overruled deliberately. `OUTRO-LOCK.md` §Scope restricts the locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and renders no subline, so obeying it would stamp the wrong channel and **drop the author signature**. The BOUT frame confirms the signature renders |
| `remotion carries 9/9 beats (100%)` | Accepted, consistent with Chapters 3–9 and the previous summary. Every beat's evidence is a previously-measured figure or an honesty table; VOX LAW holds a still is evidence never texture, so there is nothing to convert |

---

## Rubric sweep (9-point, VISUAL QC LAW)

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | **PASS after MAJOR-01** |
| 2 | Title-safe margins | PASS |
| 3 | Container overflow | PASS — all four body components were budget-fixed in their source reels and inherit those fixes |
| 4 | Collision | PASS |
| 5 | Offscreen anchors | PASS |
| 6 | Legibility | PASS — B02's mono cell values are the smallest and read clearly; B04's non-gold connectors sit at 55%, above the 40% floor |
| 7 | Brand bug placement | Deviation logged in SOURCES.md — `EmbedChrome`'s `FigureFrame` has no logo slot and is shared by Ch. 3–9; identity is carried by the footer chip and BOUT |
| 8 | Aspect | PASS — 3840×2160 |
| 9 | Canvas fill | PASS |

---

## Summary-specific honesty checks

| Check | Result |
|---|---|
| Every recapped number matches its source reel | PASS — B02 against Ch. 7's beat sheet, B03 against Ch. 8's, B04 against Ch. 9's, field by field |
| Each figure names the video it came from | PASS — all three citation lines |
| The two stand-ins are named, not inherited silently | **PASS — B05 exists for this** |
| The Ch. 9 null is still reported as a null | PASS — "0 promoted, 0 demoted" on screen |
| No new measurement introduced | PASS — this reel ran no code |
| Nogueira & Cho's 27% still absent | PASS |
