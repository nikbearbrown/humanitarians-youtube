# BEATS — structure, decisions, runtime

**Draft 1.** Narration below is authored directly into `beat_sheet.json` (no separate
build script yet — this project doesn't have one, unlike Week 22's `build_beat_sheet.py`).
`beat_sheet.json` is the source of truth; this file carries the structural reasoning.

**Current state:** 17 beats (B00 cut, see below) · 1034 narration words unchanged ·
audio for B01-B17 unchanged and still valid · visuals under repair — see Review 4 in
`PROOF-REVIEW.md`.

**B00 cut entirely (2026-09-20).** "This is Humanitarians." was never part of Week 22's
actual structure — checked directly, Week 22 opens on its cold open and states the
presenter's name from there, no separate brand card. Tanmay caught this by name, referring
to Week 22 as the standard. Removed along with its audio file; the film now opens directly
on B01 (HOOK).

**Visual defect found and being fixed (2026-09-20).** All 16 graphic beats were rendering
an unrelated project's leftover demo content ("Photoelectric Effect" / "Hola, Bear" /
"@NikBearBrown") because only descriptive `props_note` comments existed, never real
`props`. B17's outro component was also structurally wrong — `ClaudeTitleOutro`'s
`@NikBearBrown` handle is hardcoded, not defaulted, and explicitly documented as
off-limits for HAI content. Full root-cause and fix recorded in `PROOF-REVIEW.md` Review
4. Real props now written for all 16 beats; B17 switched to the brand-neutral `OutroCTA`
component; re-render in progress.

Audio generated 2026-09-20 via `brutalist.art`'s `generate_audio_kokoro.py` (Kokoro-onnx,
local, free, am_onyx) against the Gate-P-signed draft 3 text. `beat_sheet.json`'s
`actual_duration_s` per beat is now ground truth; `estimated_duration_s` is stale planning
data, kept for the record. Per-beat measured vs. planned spread was small (largest: B10,
planned 22s → measured 17.9s) — no beat came in wildly off pace.

**Revision history:**
1. Draft 1 (863 words, 4:31) — first pass, Gate P mechanical review caught a misquote and
   a wrong voice/persona (see `PEDAGOGY.md`).
2. Persona fix (877 words, 4:37) — corrected to this fellow's established `am_onyx` voice
   and added the presenter name to B02, matching Weeks 20-22.
3. **Human-voice rewrite (1034 words, 5:46) — current.** Tanmay signed Gate P on draft 2
   as a blanket PASS, then asked, before audio generation, for the narration to read as a
   curious human telling a story rather than a flat recitation of facts — first-person
   investigative framing ("here's what surprised me," "I went looking," "I want to be
   honest about something"), which is also, on inspection, closer to how Weeks 21-22
   actually sound ("I went and read the three studies underneath it," "Somebody went and
   checked"). Every fact, quote, and citation is unchanged from the fact-checked draft —
   only pacing, framing, and voice changed. **This is a new Gate P precondition, not a
   continuation of the prior PASS** — the words changed, so the read must happen again
   before audio runs. See `PEDAGOGY.md`.

---

## Structural differentiation

| Existing shape | Where | Avoided here |
|---|---|---|
| TESTIMONIAL — three witnesses, each cross-examined by one question chosen to break it | Week 22, `two-per-second` (mine) | No witnesses, no cross-examination framing |
| Presenter → cold open → problem → method → numbers → scope caveat → recap-with-Claude → paste-this-prompt | `claude-for-astronomy` Ep. 01–05 | No scope-caveat as its own labelled segment, no paste-this-prompt beat |
| "This is Kore for Humanitarians AI" → "Let's recap with Claude" at beat 2 → "Your turn, paste this into Claude" | the Substack auto-conversions, incl. this project's own source folder (`chinese-room-explainer-vox`) | Entire template discarded, same as Week 22 |
| Sealed-room mechanism → Turing counterpoint → "syntax is not semantics" verdict → outro | the source folder's own existing 8-beat cut (`never publish`) | Not reused — see below |

**This film's shape — LINEAGE-CORRECTION.** Four people, four decades, one popularized
flattening ("it's all the same argument") stated up front as the thing to be dismantled.
Each act adds one person's actual claim, then names exactly where it parts from the claim
before it. The correction beat (B11) is the fulcrum: it directly answers the myth stated
in B01, using a source that explicitly draws the boundary the popular retelling erases.

This is structurally close to Week 22's TESTIMONIAL (multiple sources, a myth getting
corrected) but inverted: Week 22 had three witnesses independently *agreeing* on one
number, with the payoff that the retelling claimed more than any one witness said. This
film has four people who never agreed on the question in the first place, and the payoff
is that the retelling invented an agreement that was never there.

Act map:

```
B00      greeting                  brand card, no content yet
B01      hook                      the myth, stated plainly, to be dismantled
B02      framework                 four names, four dates, one thread
B03–B05  Searle 1980       ROOM    mechanism -> named target (Schank's SAM) -> the
                                    reply Searle's own paper already rejected
B06–B08  Harnad 1990       GROUND  reframes the question -> his own example -> the
                                    irony: he is the rejected reply, a decade on
B09–B11  Bender&Koller2020 OCTOPUS mechanism -> the exact claim, illustrative not
                                    diagnostic -> correction: not a CRA repeat
B12–B14  StochParrots 2021 PARROT  the term, in the authors' own words -> the
                                    coiner's own disavowal of its misuse -> honest
                                    "this isn't settled" beat (B&K's own prediction
                                    about arithmetic has since been challenged)
B15      verdict                   four claims, four marked boundaries
B16      task                      go check what each side actually wrote
B17      outro                     sign-off
```

---

## Runtime

| Film | Beats | Runtime |
|---|---:|---:|
| Week 22 `two-per-second` (mine) | 17 | 4:49 |
| `claude-for-astronomy` Ep. 02 `exoplanet-hunting` | 20 | 2:30 |
| Source folder's own existing (unpublished) cut | 8 | 1:11 |
| Week 21 `the-cell-next-door` (mine) | 18 | 8:28 |
| **This film (planned)** | **18** | **5:46** |

1034 narration words at a slower ~3.0 words/sec planning estimate — the conversational,
first-person register reads slower than the denser draft-2 pace did. Still well inside
this fellow's own precedent range (4:37-8:28 across Weeks 20-22). Measured Kokoro audio
will overwrite this and become the master clock, same as every prior week.

No compression pass has been run yet. If one is needed, B14 (the "this isn't settled"
honesty beat) is the last beat to cut, not the first — it's the one that stops the film
from becoming exactly the kind of overclaiming its own thesis argues against.

---

## Sourcing map (every beat's factual content, in order)

| Beat | FACTCHECK.md rows |
|---|---|
| B03 ROOM | 1.1 (citing-source), Searle 1999 restatement quoted in SEP |
| B04 TARGET | 1.2, 1.3, 1.4 |
| B05 PRE-REJECTION | 1.5 |
| B06 GROUNDING | 2.1, 2.2 |
| B07 DICTIONARY | 2.3, 2.4 |
| B08 IRONY | 2.5 (cross-ref 1.5) |
| B09 OCTOPUS | 3.1, 3.3 |
| B10 SCENARIOS | 3.2, 3.3, 3.4 |
| B11 CORRECTION | 3.5 — **attributed to Julian Michael's analysis, not claimed as the paper's own disclaimer**; see open item 2 below |
| B12 PARROT | 4.1, 4.2, 4.3 |
| B13 DISAVOWAL | 4.4 |
| B14 CONTESTED | 3.6 |
| B15 VERDICT | synthesis of all four legs, no new claims |

Every other beat (B00, B01, B02, B16, B17) is framing/transition — no factual claims that
need a FACTCHECK row.

---

## Open items before render

1. **Resolved.** B03 now uses `pantry/searle-2005-oxford.jpg` — a rights-cleared Wikimedia
   Commons photo (CC BY-SA 3.0 / GFDL, Matthew Breindel, 2005), 1704×2272, sourced instead
   of the old undersized `searle_1.png` stub. Provenance recorded in
   `pantry/searle-2005-oxford.provenance.md`. No rights-cleared photo of Harnad exists
   anywhere findable (no Wikimedia Commons category, no image on his own Wikipedia page) —
   B06 was switched to a `MedhavyConceptCard` graphic instead, same treatment as 16 of the
   other 17 beats. No portrait sourcing remains open for this project.
2. **B11's attribution needs a decision before scripting, not after.** FACTCHECK 3.5 is a
   citing-source read: the "this is not a Chinese Room repeat" argument comes from Julian
   Michael's analysis of the paper and its surrounding discussion, not a line the original
   ACL paper states about itself in those words. The beat as drafted says "close readers of
   this paper are explicit," which is accurate to what was verified — it must not be
   tightened into "Bender and Koller say" without reading the original paper directly
   first (see FACTCHECK 3.1's own flag: the PDF forced a download and was never read).
3. **Turing is dropped entirely**, unlike the source folder's existing cut. He's not part
   of the verified four-step lineage this film is scoping, and adding him back would
   reintroduce the "thinking is behaviour" tangent FACTCHECK never checked for this draft.
4. **No pronunciation guide built yet** for Koller, Shmitchell (McMillan-Major's co-byline
   name), or Gebru — needed before the first Kokoro pass, same requirement Week 22 flagged.
5. **Title.** Working title used in the JSON is a placeholder (`same-room-different-argument`
   / *Same Room, Different Argument*) — not committed. It states the corrected thesis
   plainly, which is the main requirement; open to a sharper version once the cut exists to
   react to.
