# Self-Assessment against PROOF.md — "The Pipeline That Was Lying to Me"

Scored against `PROOF.md` (copied into this folder 2026-08-26 from
`fellows/sai-pranavi-j/2026-07-27-how-facial-recognition-actually-works/PROOF.md`
— a generic protocol doc, not video-specific). This is a real assessment against
the rebuilt 9-beat, 3840x2160 master (`2026-07-26-recovering-the-silently-dropped-filings.mp4`,
106.46s), checked against actual extracted frames, not asserted from the beat sheet alone.

## Category note (read this before the score)

PROOF.md's rubric is built for PROOF's own genre: a **skeptical explainer** that
teaches a reusable framework, stress-tests it, and hands the viewer a scaffolded
task. This reel is a different, legitimate genre — a single-insight
`ai-explainer` weekly engineering report (hook -> setup -> discovery -> proof ->
fix -> takeaway -> sign-off), scored against its own act-structure rubric in
`PEDAGOGY.md` (VERDICT: PASS there). It was never built to teach a reusable
rubric a viewer could apply to a different pipeline bug. Applying PROOF's
rubric anyway is still useful — it's an honest, additional lens — but a low
score below should be read as "this isn't that kind of video," not "this video
failed at what it attempted."

## The rubric (PROOF.md §THE RUBRIC, 0–2 each, /12)

| Criterion | Score | Why |
|---|---|---|
| **Explicit framework** | 0 | No organizing structure/rubric is shown before the example. B03 (`B03_PipelineDiagram`) shows the pipeline's *architecture* (5 feeds -> normalize -> score -> Postgres -> alert), which is scene-setting for the one case, not a reusable axis set for judging silent-failure bugs in general. |
| **Reusable rubric** | 1 | B07's takeaway ("Silent filters don't fail loudly. They fail invisibly.") is a portable one-line heuristic, but it's a slogan, not an operationalized rubric (e.g., "does this filter log its rejections? does it conflate absence with invalidity?") a viewer could score a *different* pipeline against. Gestured at, not demonstrated. |
| **Worked example** | 2 | This is the video's real strength. One concrete case is walked start to finish with the actual mechanism shown, not just asserted: the removed filter line itself is legible on screen in B04 (`const hasContent = ...` / `- if (!hasContent) return null;  // drop silently`, boxed and tagged REMOVED), the four specific recovered filings are named in B05, and the measured before/after count (297 -> 370, +73) is shown as a simultaneous side-by-side count-up in B06 — verified directly from a real frame at t=89.0s (see Production Gate below; an earlier frame grabbed at t=87.5s caught the count mid-animation at "366," which is not a defect — the settled value is 370, confirmed on re-extraction). |
| **Falsifiability / edge case** | 0 | No counterexample or ambiguous case is raised. E.g., "what if an item legitimately has no content and should be dropped?" is never asked or addressed — the video doesn't stress-test its own fix. |
| **Active task** | 0 | B08's sign-off ("@HumanitariansAI — fixed with Claude Code") is a brand credit, not a scaffolded viewer task. No copyable prompt/rubric is handed over; there is no CTA at all in the PROOF sense. |
| **Friction** | 1 | The hook (B02, calm dashboard: "nothing looks wrong") sets up a real cognitive tension — a system that looks healthy while silently broken — but the video resolves that tension *for* the viewer via narration rather than asking the viewer to find/resolve it themselves. |

**Total: 4/12.**

## Production Gate (PROOF.md §THE PRODUCTION GATE — binary, checked against real frames)

- **Evidence legible at the moment of assertion** — **mostly PASS, one named exception.**
  Checked by extracting real frames from the true clean 4K master (not the
  watermarked review cut):
  - B04 (removed-filter code) at t≈64.0s: fully legible, high-contrast cream/red/gold
    text on the dark code panel, the exact removed line boxed and tagged.
  - B05 (recovered filings) at t≈77.5s: all four filing names legible in serif
    type on cream.
  - B06 (before/after count) at t≈89.0s: "297" / "370" both on screen
    simultaneously, legible, correct settled value (see worked-example note above).
  - **Exception:** B03 (`B03_PipelineDiagram`) carries a real, previously-documented
    `low-contrast` MAJOR (ink/background luminance separation 0.22–0.23, below the
    0.30 floor) — GATE V's own severity call keeps this a MAJOR, not a BLOCKER, but
    under PROOF's stricter "legible at assertion" standard this is worth naming as
    a partial miss, not a clean PASS. Pre-existing from the original 2026-07-26
    build (documented there against old-B01), not introduced by this rebuild.
- **Sources on screen, not just voiced** — **FAIL.** Filing *names* are shown
  (B05) and the *measured count itself* is shown (B06), but no claim in this
  video carries a visible citation, URL, or source line — not the filing names,
  not the "verified... against a rolled-back test transaction" claim, not the
  297/370 count. `FACTCHECK.md` documents this gap explicitly ("Exact filing
  URLs not yet pulled... not a blocker since this toolkit never publishes").
  Under PROOF's literal rule ("no source, no verdict... a skeptical video must
  show its own sources on screen"), this is a real, named miss — the artifacts
  shown are the claims themselves, not evidence pointing outside the claims.
- **Side-by-side at the moment of comparison** — **PASS.** B06 shows BEFORE
  (297, crimson) and AFTER (370, teal) on screen at the same time, held well
  past the count-up animation settles — confirmed directly from an extracted
  frame, not inferred from the beat sheet.

**Gate verdict: FAIL** (one binary criterion — sources on screen — fails outright;
per PROOF.md, "a film may score well on teaching and still FAIL the gate," and the
reverse holds too: a low teaching score doesn't need a gate failure to justify
"unlisted," but this video has both).

## Ship rule (PROOF.md §SHIP RULE)

Public requires **teaching ≥ 8/12 AND production gate PASS AND the video passes
its own standard.** This cut: 4/12, gate FAIL → **unlisted-until-fixed** by
PROOF's standard. This changes nothing operationally — `metadata.gates.publish`
was already `NOT AUTHORIZED` and stays that way; this reel's actual ship
decision is governed by its own `PEDAGOGY.md`/`BUILD-LOG.md` gates (fact-check,
narration approval, audio lock, previz), which it has passed for its own genre.

## What this assessment is actually useful for

Not as a reason to rebuild this video as a framework-teaching piece — that would
be building a different video than the one requested. It's useful as an honest
gap list if a *future* cut of this reel (or this fellow's next weekly report)
wants to borrow PROOF's discipline: naming a reusable rubric before the example,
adding one falsifiability beat, giving the viewer a real scaffolded task instead
of a brand card, and — the cheapest, most broadly applicable fix — putting an
actual source line (URL, doc reference, or "source: FINDINGS.md line N") on
screen next to the recovered-filings and before/after-count claims instead of
narrating them unsourced.
