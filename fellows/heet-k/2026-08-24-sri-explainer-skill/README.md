# `sri-explainer` — a chapter-to-video skill in Prof Sridhar's register

- **Weeks:** built 17–30 Aug 2026 · extended 31 Aug – 6 Sep · finalized 7–13 Sep
- **Project:** Medhavy · **Role:** AI Software Engineer · **PM:** Clafacio L.
- **Status:** **professor-reviewed, confirmed, and committed to GitHub** (Week 15).
  Commit hash not recorded.
- **Walkthrough recording:** `Sri-Explainer skill walkthrough-20260902_151601-Meeting Recording.mp4`
  in [Drive](https://drive.google.com/drive/folders/15BtMVhwD9_A7J0Pt2pc2DHLcuF9RWxl7)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What the skill does

Hand it one chapter of a Prof Sridhar textbook — e.g.
`quantum-mechanics-vol1/chapters/02-matter-waves.md` — and it produces a video
that teaches what that chapter is about, narrated in a register derived from
Sridhar's own textbook prose rather than a generic explainer voice.

Where its siblings take a *concept* (`ai-explainer`) or a *build*
(`cli-explainer`), this one takes a **chapter**. That is the whole design problem:
a chapter is not one mechanism, it is six to ten derivation sections plus
grounding plus dynamics, so the skill extends the multi-act `deep-explainer`
chassis by default and only falls back to the shorter `ai-explainer` arc when a
chapter really is one mechanism end to end.

## The register

Five properties lifted from how Sridhar actually writes, documented in
[reference/prof-sridhar-style.md](reference/prof-sridhar-style.md):

1. Cold-open historical hook.
2. Stepwise derivation beats that **name what is not yet true**.
3. Explicit ruling-out of edge cases *before* the real result.
4. Concrete physical-scale grounding.
5. Golden-test honesty on every number shown.

## Two looks

- **Cream/parchment** (default) — static camera, matching the other three explainers.
- **Notebook** — dark gradient background, locked-off camera on 2D beats, real 3D
  hero objects with camera orbit for physically spatial beats, glowing accent
  curves, gridlined charts, red box callouts. Spec in
  [reference/notebook-look.md](reference/notebook-look.md).

Both were rendered for each of the two test chapters, which is why the outputs
ship as a plain `.mp4` and a `-CREAM.mp4`.

## What is here

| File | What it is |
|---|---|
| [SKILL.md](SKILL.md) | The skill definition — source contract, register, lineage, gates. |
| [reference/prof-sridhar-style.md](reference/prof-sridhar-style.md) | The register, derived from Sridhar's prose. |
| [reference/notebook-look.md](reference/notebook-look.md) | The dark Notebook visual spec. |

## Gates and constraints

- **GATE P** — narration reviewed before any audio is generated. In the brutalist
  edition this is a quality gate, not a cost gate.
- **Never publishes.** The skill stops at a render.
- **Kokoro only.** Voice `am_onyx`, reused from `claude-liam`. Prof Sridhar has no
  dedicated voice; giving him one means extending `ALLOWED_VOICES` in
  `generate_audio_kokoro.py` first. That has not been done.

## Attribution

This skill is **derived, not original**. It extends `ai-explainer`, which extends
`explainer`, and borrows the multi-act chassis from `deep-explainer`. Nothing in
it repeals a parent law. The contribution claimed here is the Sridhar register,
the chapter source contract, the Notebook look, and the integration — not the
underlying skeleton.

## Test builds

- [Chapter 1 — Why Classical Physics Failed](../2026-09-02-claude-sri-why-classical-physics-failed/)
- [Chapter 2 — Matter Waves](../2026-09-02-claude-sri-matter-waves/)
