# Renewal request — Chaitanya M.

- **Current agreement:** 1 Aug — 31 Oct 2026
- **Requested period:** 1 Nov 2026 — 30 Nov 2026

- **Project:** Medhavi Hub — subsystem research reels
- **Role:** AI Software Engineer
- **PM:** [Jash S.](../jash-s/)
- **Reporting folder:** [fellows/chaitanya-m](./README.md)
- **Drive (renders):** [all reels](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v)
- **GitHub:** [@malepatic](https://github.com/malepatic)

## What the current period produced

Six research-log reels on the Medhavi hub, built between 28 Aug and 15 Oct —
every one fact-checked against the hub source after filming, and every one
carrying its own verification trail in the repository.

**Twelve weeks, 256 hours** across the agreement period — the per-week
basis is in [HOURS.md](HOURS.md). The first four weeks, before any reel, were
spent reading the hub's documentation against its code on the professor's
direction. That review is where the reels came from: the first four are audits
of subsystems first read in those weeks.

The through-line is not the videos. It is that **each reel is an audit that
produced a finding**, and the findings are in the codebase, not just on camera:

- **Two subsystems documented as built-but-unconsumed.** The Concept Map's
  verified output has zero readers; the Memory API has zero callers. Both
  established by reading the code and grepping for consumers, not by asking.
- **Two security defects found by fact-checking my own narration.** Writing
  "the signature is checked" sent me to read the enforcement path, and the
  signature is not a gate — `verify/route.ts` catches the `jwt.verify` throw
  and continues on unsigned data. The same pass found the Memory API's
  shared-secret auth skipped entirely when the secret is unset.
- **A production postmortem.** The Logout button logged nobody out, every user,
  every time, production only. Root cause: the session moved to an HttpOnly
  cookie on the provider's domain, which the page's manual cookie sweep cannot
  reach. **That fix is still not on `development` as of 2026-10-25**, so a
  release cut from it reintroduces the bug.
- **A reusable validator.** `chapters.py` generates and *validates* YouTube
  chapter lists from measured audio, refusing to emit one that a single sub-10s
  chapter would silently disable. Written after that failure nearly shipped;
  used on every reel since, and it has already rejected my own bad input once.

### Evidence

| Date | Reel | Runtime | Finding | Drive | Log | Commit |
|---|---|---:|---|---|---|---|
| 28 Aug | [What Is a Concept Map](./2026-08-28-what-is-a-concept-map/) | 3:49 | Verified concept maps have **zero readers** — `writeVerifiedMap` has no counterpart | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-08-28-what-is-a-concept-map/FRICTIONAL.md) | [`efaa029`](https://github.com/nikbearbrown/humanitarians-youtube/commit/efaa029) · [#69](https://github.com/nikbearbrown/humanitarians-youtube/pull/69) |
| 13 Sep | [Memory API](./2026-09-13-memory-api/) | 2:51 | **Zero callers**; auth skipped in non-production when the secret is unset | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-09-13-memory-api/FRICTIONAL.md) | [`c79c1cf`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c79c1cf) · [#122](https://github.com/nikbearbrown/humanitarians-youtube/pull/122) |
| 17 Sep | [Who Can Open What](./2026-09-17-who-can-open-what/) | 3:48 | 15/15 claims verified; archived classes silently withdraw access with no explanation to the student | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-09-17-who-can-open-what/FRICTIONAL.md) | [`98a2f48`](https://github.com/nikbearbrown/humanitarians-youtube/commit/98a2f48) |
| 21 Sep | [One Sign-In, Many Books](./2026-09-21-one-sign-in-many-books/) | 3:28 | **Signature is not enforced** — `jwt.verify` throw is caught and the token read as unsigned base64 | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-09-21-one-sign-in-many-books/FRICTIONAL.md) | [`98a2f48`](https://github.com/nikbearbrown/humanitarians-youtube/commit/98a2f48) |
| 1 Oct | [Lookup, Not Training](./2026-10-01-lookup-not-training/) | 3:27 | 12/12 claims verified; primary source doc is uncommitted, so eight claims are unauditable | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-10-01-lookup-not-training/FRICTIONAL.md) | [`f67c94f`](https://github.com/nikbearbrown/humanitarians-youtube/commit/f67c94f) |
| 15 Oct | [The Logout That Didn't](./2026-10-15-the-logout-that-didnt/) | 3:53 | 11/11 verified; **fix still absent from `development`** on re-check 10 days later | [drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) | [log](./2026-10-15-the-logout-that-didnt/FRICTIONAL.md) | [`421668d`](https://github.com/nikbearbrown/humanitarians-youtube/commit/421668d) |

Each folder holds the beat sheet, both cuts, measured timings, subtitles with
per-word timings, the renderer, GATE P sign-off, frame QC, the fact-check and a
Frictional log. Six reels, six signed gates, six fact-checks.

### Drive

Rendered masters live in Drive, per the repo's source-to-GitHub /
renders-to-Drive rule:
[all reels](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v).

All six reels' masters sit in that single folder — there are no per-reel
subfolders. Each file is named for its reel, so the 16:9 and 9:16 cuts for a
given video are findable by name rather than by folder.

Weekly hours: [HOURS.md](HOURS.md). Frictional logs: one per work folder,
linked in the table above and in [README.md](README.md).

## Stated plainly: nothing is published yet

All six reels are built, QC'd, fact-checked and gate-signed. **None has been
published to YouTube.** There are no view counts to report and no watch links in
the table above, and I would rather say so than leave an empty column to be
noticed.

Two reasons, one good and one not:

- **One Sign-In, Many Books should not publish as-is.** Beat B04 tells viewers
  the signature stops a tampered ticket, and the code does not do that. The fix
  is one line in the hub; after it, the claim is true and the reel needs no
  re-cut. Publishing it first would mean knowingly shipping a false security
  claim.
- **The other five have no such blocker.** They are unpublished because I
  treated the repository package as the deliverable and publication as the step
  after. That ordering was a mistake and it is the first thing the next period
  fixes.

## Attribution, stated

- **Mine:** the subsystem audits, the narration for all six reels, every
  fact-check verdict, and the decisions on what to put on camera and what to
  leave off.
- **Claude:** built the reels from my scripts and briefs, wrote the build logs,
  ran the ported fact-checks against the hub, and wrote `chapters.py`. I
  directed the revisions and the corrections; where Claude's output was wrong —
  an auto-generated outro that spliced unspeakable fragments, an endcard in the
  wrong brand, centre-cuts that destroyed every two-column slide — I rejected
  and replaced it. Each reel's Frictional log records what was accepted,
  changed and rejected.
- **GATE P** is signed by me on all six. That signature covers the narration
  only — not QC, not the fact-check.
- **Honest limit on the Frictional logs:** the rule arrived 2026-09-22, after
  four reels were already built. Those logs are retrospective and labelled as
  such, with `[NOT RECORDED]` where a contemporaneous answer does not exist. I
  did not backfill them with plausible detail.

## Plan for the requested period

### Immediate — the next two weeks

**Publish the backlog, and close the two findings that are still open in the
hub.** The reels are evidence of work; unpublished, they are evidence only to
someone reading this repository.

- **Publish five reels.** Titles, descriptions and validated chapter lists are
  already written and committed for each.
- **Fix `verify/route.ts` in `medhavi-hub`** — remove the base64 fallback from
  the outer catch, or gate it on `!JWT_SECRET`. One line. It makes One Sign-In
  publishable and closes a real defect.
- **Merge `4777b36` into `development`.** The logout fix has been on `main`
  since 9 Oct and still is not there. Any release cut from that branch
  reintroduces the bug my own postmortem is about.
- **Commit `docs/how-the-tutor-uses-the-textbook.md`**, or re-cite. Eight claims
  in the Lookup reel point at a file that does not exist in the repository.

### Across the period

1. **Fact-check before recording, not after.** Every finding across six reels
   was caught at port time, after the audio was cut. On the one reel where I
   wrote the narration with the source document open, the fact-check came back
   12/12. That correlation is exact and it is the single change worth keeping.
2. **Re-test time-sensitive claims at publication.** Any claim of the form "X
   hasn't landed yet" is a claim about a moment. The logout reel's branch claim
   happened to still be true ten days later; next time it may not be.
3. **Write the Frictional log during the build.** Four of six are
   reconstructions. The rule asks for contemporaneous, and the `[NOT RECORDED]`
   gaps are the cost of not doing it.
4. **Keep auditing, and keep filing what I find.** Two security defects and two
   dead subsystems came out of six reels. The reels are a side effect of reading
   the code carefully; the findings are the product. Open an issue for each
   rather than only narrating it.

Reporting continues: a dated Frictional log per work folder, appended and never
rewritten; weekly hours; a fact-check per reel against a named commit.

## Open items I am carrying

- **`verify/route.ts` signature fallback** — unfixed in `medhavi-hub`. Blocks
  publication of One Sign-In, Many Books.
- **Logout fix not on `development`** — `4777b36`, on `main` since 9 Oct.
- **B06 `wikipedia_categories`** in the Concept Map reel shows a fabricated
  value. One line in `render_scenes.py`, then re-render that beat and re-cut.
  Outstanding since August.
- **Six reels unpublished.**
- **`docs/how-the-tutor-uses-the-textbook.md` uncommitted**, leaving eight
  Lookup claims unauditable.
