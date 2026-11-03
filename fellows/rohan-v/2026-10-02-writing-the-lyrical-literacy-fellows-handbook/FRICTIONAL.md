# FRICTIONAL — Writing the Lyrical Literacy Fellows Handbook

The frictional log for this piece of work: short, dated, honest entries about what was tried,
where it resisted, what was done about it and what was learned, appended as the work goes and
never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-29 – 2026-09-30 — The Fellows Handbook, v1.0

> Written 2026-10-05, from the build session's record (labelled later than the work it
> describes). The decisions and corrections are mine.

**Working on.** Item 1 of my renewal plan: one onboarding handbook for new Lyrical Literacy
fellows: access to every tool, Suno and Midjourney in depth, weekly reporting, the whole video
workflow for non-technical fellows, renewals, contacts, version tracking.

**Tried, and expected.**
- Gave Claude the sources: the Fellows and Lyrical Literacy pages, HAI's brand reference PDF,
  the Canva invite, Northeastern's Adobe request page, the shared Discord login, and our nine
  tutorials. Asked for HAI branding, a title page, a linked index and version tracking.
- Expected one pass to be close; then asked for a .docx so the team can edit it later.

**Where it resisted, and what I did next.**
- The first build followed the brand PDF (navy and cream). I rejected it as not professional
  and asked for the website's look; it was rebuilt in Inter, white and the site's deep red.
- Open questions came back highlighted in the document. I answered them: the supervisor's
  email, Claude through the Northeastern premium seat (with IT's form for anyone without one),
  Adobe through Northeastern only, every weekly video to one reviewer until further notice;
  the master copy's home is still undecided.
- I reviewed it in Word and left three comments: drop the "for Northeastern students" line,
  drop the step of emailing a GitHub username, and let Claude keep the hours and Frictional
  logs instead of making them a checklist chore. All three were applied and the comments removed.
- Mid-week the program's rules changed (build inputs on GitHub, renders on Drive; the official
  example folder for renewals), so those went into the handbook too. Added the weekly
  Wednesday meeting and the optional Brutalist playlist.
- The handbook holds a shared login, so it is kept out of the public repository and shared
  through my Northeastern SharePoint instead.
- I forgot to submit this week's videos on Friday; they were built on Monday 5 Oct.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the sources, drafted all twelve sections, built the document from code
  and checked every page as rendered.
- Rejected: the brand-PDF palette. Changed: three passages via my Word comments, the review
  routing, the scope (Northeastern only). Accepted: the structure, the guides and the
  document-control page.

**What I understand now, and what I still don't.**
- A handbook built from code can be rebuilt in minutes when a rule changes, which happened
  twice in one week.
- Still untested: whether a new fellow can follow it from page one without asking anyone.
  Undecided: where the master copy lives.

Evidence: `pantry/handbook/` (six crops of the v1.0 PDF and `crops.json` with page numbers
and hashes), `beat_sheet.json`, FACTCHECK.md, QC sheets.

## 2026-10-05 — This progress video

> Written during the build, with Claude.

**Tried, and expected.** A progress video that shows the handbook itself, not a mock-up.
**Where it resisted.** Whole pages at video size fail the type floor and can't be read, so the
video shows tight crops of real pages instead, larger on a phone; no page with
contact details or the login is shown. The phone cut was refused twice by the automatic checks
(type too small at 4K on the roadmap; content past the safe edge and an empty lower half on two
other beats) and fixed each time before it was accepted (BUILD-LOG §5, §7). **Contributed.** Claude wrote the narration and one new
scene (`HaiDocPages`); the other six beats reuse library scenes. **My review of the preview:**
pending at the time of this entry.

**My review, 2026-10-06.** Watched both cuts of this video (16:9 and 9:16) after they were built; no changes requested.
