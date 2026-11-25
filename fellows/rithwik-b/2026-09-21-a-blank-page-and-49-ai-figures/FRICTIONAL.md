# FRICTIONAL — A Blank Page and 49 AI Figures

The frictional log for this piece of work — appended, never rewritten.
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-21 — Clone, blank page, audit, reel

> **Written 2026-11-02, six weeks after the build.** Reconstructed from the beat sheet,
> the audit and the viewer diff, then drafted with Claude from that record.

**Working on.** Getting the Medhavy bio-art viewer to render, then judging whether the
figures it shows are any good.

**Tried, and expected.** Clone, `npm install`, open the viewer. I expected a gallery.

**Where it resisted, and what I did next.**

- The clone bounced off a password prompt — GitHub no longer takes passwords. Fixed with a
  personal access token.
- The viewer opened to a blank page with no console error. A corrupted npm cache from an
  old `sudo` install had to be cleared first.
- The real crash: the loader read `entry.file` on every entry, and 234 of 245 don't have
  one. Normalized both entry shapes into one, and made the dev server serve `figures/`.
- Once it rendered, I looked at all 49 molecule/drug figures one at a time against their
  prompts. Most were the same few shapes with different labels.

**What Claude contributed — accepted, changed, rejected.**

- Claude traced the blank page to the property read and wrote the normalize fix; accepted.
- Claude helped grade the 49 figures against their prompts and wrote up the audit; the
  rubric and the verdicts are mine.
- Claude built the reel from the session.

**Understand now / still don't.**

- Now: a generator that returns an image for every prompt can still be ignoring most of
  each prompt. Checking output against its own input is the audit.
- Now (2026-11-02 re-check): "pixel-identical" was a word I should have tested. The files
  differ; the pictures are near-identical. The reel says the stronger thing.
- Still open: the fix is uncommitted, and the reel needs a one-beat re-cut before it can publish.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) · [`viewer-fix.diff`](./viewer-fix.diff) ·
[`audit-molecule-drug-figures.md`](./audit-molecule-drug-figures.md)
