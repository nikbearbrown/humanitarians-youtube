# PEDAGOGY — Where the Record Stops

Week 19 work video · Humanitarians AI · presented by **Tanmay Kulkarni**, voice `am_onyx`,
Pragmatist register. Built from the DBS case study and the `dbs_credit_memo` reference
implementation. Append-only log (PLAYBOOK §8).

---

## 2026-08-25 — Authoring audit

### Laws check

- **Intro-summary beat present and it names the subject** (PLAYBOOK §1, §1c) ✓ — B02 says
  "reference implementations — working code that ships next to a case study" in plain words
  before any abstraction, names the subject (a credit-memo tool at DBS Bank), and states the
  takeaway ("how you do that honestly").
- **Framework shown before examples** (PROOF Phase 2) ✓ — `BuildLedger` at ~1:15. Later than
  the 20s the gate prefers, and deliberately: the "this is not DBS's system" premise has to
  land first or every subsequent frame reads as a claim about DBS. First example is B04 at
  ~1:47, so framework still precedes example. **Flagged rather than silently diverged.**
- **Tone is an arc** (PLAYBOOK §1a) ✓ — mapped before writing. A *conviction* peak at
  B07–B08 rather than a surprise peak, then B10 and B11 let the method correct the author,
  which keeps it from preaching.
- **Punctuation as TTS timing** (PLAYBOOK §1d) ✓ at authoring — B12's three questions are
  written as questions, not "One. Two. Three." Deliberate short landings in B06 and B08.
  **Still to do:** `silencedetect` sweep over `mp3/` after generation.
- **No fabrication** (PROOF §CORE) ✓ — every DBS claim traces to the 19 Aug 2026 newsroom
  release or Computer Weekly, 28 Jul 2026. Every other claim is about this repository, which
  is on disk and testable. All six test files were **run** (2026-08-25), not assumed.
- **Code on screen is real** ✓ — dedented excerpts of actual repository files, elisions marked
  with an ellipsis. No line invented.
- **Illustrate law** — two runs of a repeated pattern, both deliberate and recorded in
  `beat_sheet.json` `adjacency_note`: B03→B04 is one ledger *filling*, not a repeat;
  B07→B08→B09 is a three-card code walkthrough. The second is a genuine monotony risk over
  ~73s and is flagged to watch on the first review cut.

### Framing — the reviewer concern that shaped this film

The first pitch risked reading as a knock on DBS for not disclosing more, and as advertising
a hole in our own work. Both were fixed structurally, not cosmetically:

- **Method-forward, not DBS-forward.** The film is about how you build from partial
  disclosure; DBS is the worked example. That inverts the exposure — the "this is not DBS's
  system" statement becomes the **premise in the first 45 seconds** rather than a disclaimer
  at the end.
- **The empty gate is the deliverable, not the gap.** Not "we left a hole" but "at every
  point where the record stops you choose between a plausible invention and an honest blank"
  — and the `ValueError` hardening proves it was engineered, not omitted.
- **DBS is credited.** B05 says a bank stating its own governance gap in public "is unusual,
  and it's to their credit." The only thing the film says DBS did not do is publish internal
  implementation detail — normal, expected, and stated as such.

### Voice — Onyx, not Bella

`am_onyx`, chosen for the peer-conversation register of a first-person film.

Within precedent: this fellow's films have used `am_onyx` 3× and `af_bella` 4×. The repo
README's default suggestion for a male-coded fellow name is `am_*`, and it states that a
fellow's explicit preference always wins — which this is.

**Noted for someone to resolve separately:** that same README asks a fellow to settle on one
voice and keep it across a series. Practice here has alternated. Not a blocker; recorded so
it is visible rather than discovered in review.

### First person

The narration is "I", not "we". Tanmay built this reference implementation and the film says
so. It also carries the argument better: *"I could have invented that"* owns the decision in
a way *"we could have"* does not, on a film whose whole subject is owning decisions. DBS is
always "they", never merged into a "we".

### Components

Four authored or fixed for this film, each verified by render in **both** aspects rather than
assumed:

- **`BuildLedger`** (new) — three stacked groups, not columns. Groups dim rather than hide, so
  the framework's shape is visible at B03 before any row arrives. A row may carry a `note`,
  used once: the reject path renders as *"reasoned, never demonstrated"* inside BLANK rather
  than being filed under CONSTRUCTED. The component shows the ambiguity B11 discusses.
- **`StageRefinement`** (new) — plan above code, the added stage terracotta with its reason
  inline. Row in landscape, column in portrait.
- **`ClaudeCodeBeat`** (fixed) — see the defect log below.
- **`SyncSendChecklist`** (fixed) — see the defect log below.

Both new components are portrait-portable by construction, so both `916` variants are
10-line aliases.

### Pre-audio frame pass — 2026-08-25

All 13 beats rendered at estimated durations and inspected **before** generating audio, on
the PLAYBOOK §1b principle that a miss caught at prop stage costs a prop string and the same
miss caught after audio costs a rebuild. Frames in `frames-preaudio/`.

**Two component defects found and fixed, both the same underlying kind:**

1. **`ClaudeCodeBeat` scaled its font from `height`.** In portrait (1080×1920) that produced a
   *larger* font in a *narrower* column than landscape, and `whiteSpace: 'pre'` with
   `overflow: 'hidden'` then **silently clipped** the overflow. Five of twelve lines lost
   their right-hand end, including the exact sentence B08 exists to show. Now scales from
   `Math.min(width, height)` and wraps rather than clips. Landscape is visually unchanged
   (0.026% of subpixels differ, sub-pixel repositioning only).
2. **`SyncSendChecklist` had "WHAT THE LABEL ACTUALLY SAYS" hardcoded** — correct for the
   topic video it was built for, meaningless above this film's CONFIRMED/CONSTRUCTED/BLANK
   badges. Now a `badgeHeader` prop defaulting to the original string, so the topic video is
   untouched.

Defect 2 is worth naming plainly: it is the same mistake as `WantQuote`'s baked-in Anthropic
credit, which had been found and fixed two days earlier — and then reproduced by the same
author in a new component. **A display string that is not a prop is a defect waiting for the
next film.** A scan of every component this film uses found no others.

### PROOF gate

- **Phase 1 — PREMISE: CLEARED.** Framework (CONFIRMED / CONSTRUCTED / BLANK), rubric (the
  three-way label plus three gate questions), worked example (the pipeline walked element by
  element), falsifiability (the reject path, which genuinely strains the framework), active
  task, friction.
- **Phase 2 — BUILD: teaching 12/12**, ship bar 8.
- **Production gate: PROVISIONAL.** Legibility verified on rendered frames in both aspects.
  Moment-of-assertion timing and truncation cannot be settled until measured audio exists —
  re-check after generation.

**AUTHORING VERDICT: PASS.**

---

## GATE P — narration sign-off

Read-aloud pack: `GATE-P-READ-ALOUD.md` (script v2 — first person, both continuous-read
defects fixed).

```
VERDICT: PASS
Signed by: Tanmay Kulkarni (Humanitarians AI)
Date:      2026-08-25
Basis:     Read aloud in full and approved. No lines marked for rewrite.
           Script v2 followed two revisions: first person throughout, and the
           two defects found by reading v1 as continuous prose (B04/B05
           contradiction at the join; B11 unfollowable at speed).
Timing:    Not hand-timed. Estimated 5:23 from word count at Kokoro's measured
           rate; measured audio is the clock and is checked immediately after
           generation.
```

**Audio generation is authorised.** Next: `generate_audio_kokoro.py` with per-beat speeds
tracking the tone arc, then measure, then a `silencedetect` sweep over `mp3/` before
compiling (PLAYBOOK §1d).


---

## 2026-08-26 — Build complete, deliverables assembled

**Shipped:** 16:9 at 3840×2160, 4:47.9 · 9:16 trailer at 2160×3840, 1:41.2. Both paced, both
clean masters, both watched end to end by a human before being called done.

**Two PROOF rounds.** Review 1 returned *unlisted-until-fixed* on a single production-gate
failure: B04 asserted four of DBS's facts with no citation in frame, on a film whose whole
subject is labelling where a claim came from. `BuildLedger` had no source field at all, and a
grep found exactly one citation in the entire film. Review 2 closed it and three other items
— the trailer never naming its presenter (reviewer-raised), the 16:9 having no pacing pass,
and B10's stage names readable as DBS's. Verdict now clear-for-public.

**Seven defects found and fixed during the build** — full detail in `QC-REPORT.md`. Three
share one root cause worth stating plainly: an internal string leaking into viewer-facing
output. The Anthropic data credit, `SyncSendChecklist`'s hardcoded badge header, and a
hero-protection bookkeeping note that the Short's auto-outro **read aloud**. Any field a
component or script may render must be treated as viewer-facing.

**A defect returned that was already in the playbook.** The 44.1 kHz endcard against Kokoro's
24 kHz was written into PLAYBOOK §6 after the topic video — but fixed there only in that
film's output file, never in `shorts.py`. It reappeared here as a 97-second trailer reporting
178.8s. Now fixed at source. Writing the lesson down is not the same as fixing the cause.

**Two process notes for the next build:**

- The **pre-audio frame pass** is worth doing every time. It caught the badge-header leak and
  confirmed all 13 beats' props before a single mp3 existed. But it structurally cannot see
  moment-of-assertion timing — B12's artifact landing 1.4s after the claim only became a
  defect once measured audio replaced the estimate.
- **Two films in a row now sit at 100% Remotion** against MOTION.md's ~40% cap. The topic
  video's own report said two in a row makes it a house pattern rather than a per-film
  choice. That is now true and should be addressed next build, not recorded again.

Deliverables in . Not published.
