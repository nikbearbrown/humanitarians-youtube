# PEDAGOGY — Week 24 topic video · verdict of record

*Which of Gardner's Eight Intelligences Can a Machine Do?* (structure: EIGHT ROOMS)

## GATE P — Narration review

**VERDICT: PASS. Tanmay Kulkarni, 2026-09-26.**

Verbatim: *"Gate P PASS, say Stachura as sta-HOO-ra"*

Gate P is a human reading every line out loud against its slate and signing off. Nothing below
substitutes for that. The page-level work is done so the read can be spent on judgement: rhythm,
emphasis, and whether the turns land (B07's double-take, B12's "But hold on", B15's stillness,
B17's "Optional.").

| Step | State |
|---|---|
| Script approved as a draft | ✅ Tanmay, 2026-09-26 ("the script looks good"). Since amended by the mechanical fixes below, so the approval doesn't carry over automatically |
| Mechanical pass, `gate_p_lint.py` | ✅ **22 flags → 12.** 7 BREATH splits, 2 lone-letter and 1 acronym re-spelt for TTS, 2 ECHO accepted as deliberate parallels, 10 NAME items moved to the ear checklist |
| Say-it-right checklist | ✅ written (`READ-ALOUD.md`), with **one item needing your decision: how "Stachura" is said** |
| Continuous read-through (PLAYBOOK §1e) | ✅ done on draft 2 (5 fixes, `BEATS-DRAFT.md`), re-read after the Gate P edits |
| `preship_lint.py` | ✅ 0 errors, 0 warnings |
| Slates at 4K, all 19 beats | ✅ `media/B01–B19.mp4`, all 3840×2160, every frame checked (PROOF-REVIEW Review 5). Open fonts only, no third-party images |
| **Read aloud by Tanmay** | ✅ 2026-09-26 |
| **Reviewed on slates by Tanmay** | ✅ 2026-09-26, all 19 at 4K |
| **Signature** | ✅ `PASS — Tanmay Kulkarni, 2026-09-26` |

### How to sign

Read `READ-ALOUD.md` top to bottom, out loud, with the slate for each beat open. Then either:
- reply "Gate P PASS" (with any notes) and I'll record it here verbatim with the date, or
- list the beats that tripped you, and I'll fix them, re-run both lints, and regenerate the sheet.

## What the film teaches (for the record)

- **Subject, plain words (B02):** Gardner's theory of multiple intelligences, and which of them, by
  Gardner's own account, a machine has now walked into
- **Shown method:** before accepting a count, check how each verdict was earned (B12–B13: the six
  lights came on under a 2024 performance-style inspection, not the 1983 criteria)
- **Falsifiability:** room seven, where evidence was given and the light withheld, and the source
  doesn't say why (B14). Room eight is dark by definition, not by failed test (B15)
- **Viewer task:** one open question (B18), deliberately not a checklist. See PROOF-REVIEW Review 3
  for the rubric tradeoff

### Post-signature: spoken-form spellings (implementing the verdict, not new words)

Tanmay's instruction fixed one pronunciation. Checking every name against **Kokoro's actual
phonemes** (`tokenizer.phonemize`, not guessed) found two more the engine would mangle. The fix
is TTS spelling only, same precedent as "gee" and "M-I": on-screen text and the meaning are
unchanged, so this doesn't reopen Gate P.

| Beat | Written | Kokoro would say | Spoken form now | Kokoro now says |
|---|---|---|---|---|
| B05 | Stachura | stæʃjˈʊɹɹə (sta-SHYUR-a) | Sta-hoo-ra | stɑː-hˈuː-ɹɑː (**sta-HOO-ra**, per Tanmay) |
| B05 | Furuzawa | fjˌʊɹɹuːzˈɑːwə (fyoo-…) | Foo-roo-zah-wah | fuː-ɹuː-zɑː-wɑː |
| B03 | bodily-kinesthetic | …kaɪnsθˈɛɾɪk (kine-sthetic) | bodily-kinnesthetic | …kˌɪnɪsθˈɛɾɪk (kin-is-THET-ic) |

Checked and correct as written: Gardner, Dartmouth, obsolescence, Shinri, Kulkarni, "gee",
"M-I". **Left as-is by precedent:** "Tanmay" → tˈænmeɪ (TAN-may), the same as the published
Weeks 20–23. Change it only if Tanmay asks.

**Post-sign-off TTS spelling (2026-09-27, Tanmay approved the fix):** years in the narration are now
written in words for the voice (B01, B03, B05, B07, B12, B13), because Kokoro read digit years as
"nineteen hundred eighty three". The words spoken are the ones signed above, so this doesn't reopen
Gate P. The six beats have new audio for a listen.
