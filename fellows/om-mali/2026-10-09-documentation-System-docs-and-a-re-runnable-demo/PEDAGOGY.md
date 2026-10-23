# PEDAGOGY — documenting-the-system-and-making-the-demo-runnable (week 11)
*Documenting the System and Making the Demo Re-runnable — Week 11 progress update · ai-explainer / claude-hai*

Tenth episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2, 4, 5, 6, 7, 8, 9 and 10. Source: `narration_script.md`
(author-written, 3:00 target) and `figdata.json`.

**This is the series' last build week, and the only one whose subject is the author being
wrong about his own work.** The code was finished. The week is an audit, and what the audit
found is the episode. The failure mode here is making the audit sound like a tidy-up, so every
beat is a thing that was not known at the start of the week.

**There is no `README.md` in this folder.** Weeks 9 and 10 each shipped one with a
figure-to-beat map and a "three things not to get wrong" section. Without it, the editorial
judgments below were made from the script and `figdata.json` directly, and every arithmetic
relationship was re-derived rather than taken from a caption. That is also why
`CHECKS-REPORT.md` carries more derivation than usual.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Carries the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | Both deliverables named, and the requirement that was met zero times ✓ |
| B02 | THE AUDIT | Six named, three absent — and an absent file has no "before" number ✓ |
| B03 | A REQUIREMENT AT ZERO | Which zero is a finding and which is a missing file ✓ |
| B04 | LOAD-BEARING | The one citation that changed a rule, against the 21 that did not ✓ |
| B05 | THE LADDER | Three layers by what each is ALLOWED to do ✓ |
| B06 | EIGHT LINKS | One published number, traced to the archive file ✓ |
| B07 | A DEMO THAT RE-RUNS | Five acts, zero writes, and the act that deliberately decides nothing ✓ |
| B08 | WHAT THE AUDIT MISSES | Four limits, each attached to the claim it narrows ✓ |
| B09 | VERDICT | One-page recap, five findings, one per spoken clause ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → AUDIT → FINDING → CORRECTION → STRUCTURE →
EVIDENCE → ARTIFACT → LIMITS → VERDICT → HANDOFF → OUTRO ✓

**The structure refuses to be a changelog.** Only B02 and B07 describe what was produced.
B03 and B04 are the author being more precise than his own plan, B05 and B06 are the system's
shape rather than the week's output, and B08 is four things the week does not establish. A
viewer who finishes this reel knows what an audit found, not what got written.

**Where this cut departs from the script.** The script has six sections; they become eight body
beats. Each split is a genuine seam:

1. *B03 narrows the script's own headline.* The script says "I grepped for every name. Zero."
   and then, correctly, "in either published document". `figdata.json` shows three documents at
   zero, but one of them did not exist. The narrower claim is the true one, and it gets drawn.
2. *B04 is new.* The script treats the Gornall & Strebulaev citation as the point of the
   section. This cut shows what makes it different from the other 21 — a four-step chain that
   ends in a rule that changed.
3. *B05 is new.* The script names the architecture document as "the one I'd keep" but no figure
   draws its spine. Fifteen tables in three layers, keyed on mutability, is that spine.
4. *2:30 and the close were split into B07 and B08* — the demo and the limits each get a frame,
   because a limits sentence at 2:52 would be heard as sign-off patter.
5. *0:00 and the deliverable description split into B00 and B01* — the standard bookends.

No claim was added or dropped by the splits, and **every added FIGURE is injected from
`figdata.json` under an assertion**, with the four exceptions named below. Four wording changes
are logged in `FACTCHECK.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line: *"Hi, I'm Om Mali. This video is about the last week
  of the build…"* ✓
- B00's ask is an **audit instruction** — "do not trust my memory" — which is what the week
  turned out to be about ✓
- B01 states both deliverables and the failed requirement in plain language. No "append-only",
  no "provenance", no "static scan" until B05–B08 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W11Bluf` — two deliverable cards, a requirement, a struck count | illustration ✓ |
| B02 | `W11Docs` — six rows with a before column that holds words for three of them | illustration ✓ |
| B03 | `W11PriorArt` — name chips, then two real zeroes split from one that is not | illustration ✓ |
| B04 | `W11LoadBearing` — one bar splitting 21/1, then a four-step chain | illustration ✓ |
| B05 | `W11Layers` — three cards led by mutability, and one identity | illustration ✓ |
| B06 | `W11Provenance` — a connected descent of eight links | illustration ✓ |
| B07 | `W11Demo` — five acts, then one very large zero | illustration ✓ |
| B08 | `W11Limits` — claim-and-limit pairs, a rule, and the closing block | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B02 and B03 are adjacent and both about documents in a table.** B02's rows carry two numbers
each and a growth bar; its argument is that three cells are not numbers at all. B03's rows carry
a before-and-after pair and are split into two groups by a dashed rule; its argument is the
split. They are also different shapes: B02 is a six-row table with a bar column, B03 is chips
above two short stacks.

**B04 and B07 both end on one large figure.** B04's is a ratio drawn as a split bar; B07's is a
single number at headline size. The distinction is that B04's number means "one of these is
different" and B07's means "there are none" — a count of zero cannot be a bar.

**B06 is a chain and must not read as a list.** The dots are joined by drawn segments rather
than implied by vertical order, because the sentence beneath says "break any link". A bulleted
list has no links to break.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT as a framing device. B00 says "This video is about…" **once**,
  as the author's explicitly requested opening line, and then never again ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check

An audit episode can go wrong by making the audit sound more decisive than it was. The cut is
built so that every finding is stated at the width the evidence supports and no wider.

- **The reel narrows its own headline.** The source figure tabulates three documents at zero;
  two of those zeroes are findings and one is a missing file. B03 draws them apart, and the
  injection asserts the split so a data change cannot quietly re-merge them ✓
- **An absent file is not drawn as a zero.** B02 prints "did not exist" where a line count would
  go. A 0 in that column reads as "a document with no lines", which is a weaker claim than "no
  document", and it would sit in the same column as 231 and 956 ✓
- **A citation count is separated from a literature review.** 22 were added; exactly one changed
  a rule. B04 shows the 21 it is distinguishing itself from rather than only the one ✓
- **The provenance claim is limited by its own run log.** B06 says the chain is datable because
  the run log records which run produced each artifact. B08 says that log has two rows. The reel
  states the limit on its strongest claim rather than leaving it in the paperwork ✓
- **The write-statement count is called a static scan.** Zero across five files is not a proof
  that nothing writes, and B08 says so ✓
- **The audit's own blind spot is named.** It covers the six documents the plan names. A
  requirement the plan never wrote down stays invisible to this method, which is stated on B08 ✓
- **The identity is stated as an equality, not a proof.** 5,806 filed rows and 5,806 match
  decisions; the frame says "one judgment row per filed row" and claims nothing stronger than
  the counts support ✓
- **No invented figures on screen.** Everything else is a prop injected from `figdata.json`
  under assertions that fail the build ✓

---

## Length law

**Measured: 212.17s (3:32.2)** of narration across twelve beats, from the Kokoro MP3s. Duration
is an OUTPUT. The script targets 3:00; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35 → 3:21 → 3:35 → 3:45 → 3:38 → 3:32 → 3:32.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 55w · B02 48w · B03 65w · B04 63w · B05 66w · B06 64w · B07 65w · B08 63w

**All eight sit inside the 45–70 band.** B02 is the shortest at 48 words because its finding is
a single fact — three of six did not exist — and the frame does the rest.

---

## Both orientations, from one source

As weeks 5–10, at the author's standing request: **16:9 (3840×2160) and 9:16 (2160×3840)**. The
vertical cut is a **re-layout, not a crop**. Portrait values are TUNED, not inherited: week 9
shipped four beats whose 9:16 cut was the landscape layout scaled down, and week 10 needed three
rescaled after the first portrait read. Every week-11 component was written with both
orientations from the start — B03's rows stack their document name above the before-and-after
pair in portrait, B04's and B08's claim/limit pairs become two lines instead of two columns, and
B06's link names wrap rather than ellipsing because the chain's names are the evidence. Both cuts
render from the same components and the same props, so a number cannot differ between them, and
they carry the identical narration MP3s.

---

## Source fidelity

Every number traces to `figdata.json` — see `FACTCHECK.md`, 20 rows, with rows 5, 6, 13, 17 and
19 flagged as the ones worth challenging. Rows 6, 10, 17 and 20 are the four values that are not
in the figure data at all.

**Row 5 is the load-bearing one, and it is not one of those four.** It is a derivation that
*contradicts the source figure's table*: `w12-priorart.png` shows three documents at BEFORE 0,
and this reel shows two. The figure's own caption agrees with the reel. If that reading is
wrong, B03 is wrong and B09's second finding goes with it.

The four source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved there from
`images/` because `run.sh` uses that directory for compile OUTPUT and the series keeps reference
art in `pantry/`.

`w12-demo.png` carries an edge-bleed defect of its own — its layer-summary line runs off the
right edge, ending "resolved 3 (rebuil". The rebuild does not inherit it, and B05 carries the
layer summary properly instead.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2, 4–10: this rebuild renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.** The source figures' rule that red is the primary series and never a warning colour is
preserved in effect: terracotta marks the absent documents, the real zero, the load-bearing
citation, the append-only layer, the two ends of the chain and the zero write statements — the
subject of each beat, never a hazard.

---

**What the author is being asked to sign off on**, having watched
`documenting-the-system-and-making-the-demo-runnable-slate.mp4`:

1. The five structural changes above (6 script sections → 8 body beats), in particular **adding
   B04 and B05**, neither of which is in the script's figure list.
2. **Narrowing the prior-art finding from three documents to two on camera**, against what
   `w12-priorart.png`'s table shows — on the grounds that the third file did not exist, which
   the figure's own caption already implies. `FACTCHECK.md` row 5.
3. Printing "did not exist" rather than 0 in B02's before column.
4. Saying on camera that the run log behind the provenance chain has two rows in it.
5. `FACTCHECK.md` rows 6, 10, 17 and 20 — the five prior-art names, what the load-bearing
   citation changed, the eight-link chain's structure, and the two language-model sites.
6. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
7. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-10-09.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather
than passed silently. **The gate has since been re-run WITHOUT the override and passes on its
own.** The audio was NOT regenerated after signing: the mp3s that were measured, locked and
rendered against are the mp3s in the masters, so the signed cut is bit-for-bit the cut that
cleared GATE V.

**Both cuts are built and measured.** 3840×2160 and 2160×3840, 24fps, 212.17s each — the same
narration files, not two renderings of the same script. GATE L clean; **GATE V clean on both
cuts**, 24 frames sampled each, 0 BLOCKER and 0 MAJOR, re-run explicitly with `--mp4` against
the exact files being delivered.

**GATE V blocked the 9:16 cut on the first attempt** — 2 BLOCKERs, `edge-bleed` on the outro.
The cause was a toolkit defect this reel was simply the first to expose: `ClaudeTitleOutro916`
sized the title without regard for its longest word, and "Documenting" at 138px overflows a
936px content box. A longest-word guard now shrinks the font only when needed, so weeks 1–10
render byte-identically. `BUILD-LOG.md` records the full sequence, including a misdiagnosis of
mine that preceded it.

Five frame-level defects were found and fixed before this cut, every one by LOOKING at a
rendered frame. The one worth the author's attention is **B02's bar column, which was measuring
the wrong thing**: scaled to total lines, it gave the longest bar to the document that grew
least, on a frame whose entire argument is that three documents were written from nothing. It
is now stacked — pale for what was already there, solid for this week.
