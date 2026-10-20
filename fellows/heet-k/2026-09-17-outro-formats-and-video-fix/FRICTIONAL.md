# Frictional log — outro delivery formats, and a video fix

## 2026-09-20 — shipping in the formats, and closing a loose end

> Written 2026-09-28, after the week it describes. Reconstructed from the Week 16
> report and the Drive folder; not a contemporaneous entry.

- **Drive:** https://drive.google.com/drive/folders/1yKVBYPyQgFm5b8YU5RWBivLH2E-KP4Hy
- **Deferred from:** [logo reel script.md](../2026-08-17-medhavy-brand-intro/script.md) — "16:9 only … say the word and I'll add a 9:16 cut"
- **Hours:** Week 16 total 22.0 — 11.0 formats + 6.0 video fix on this thread — [HOURS.md](../HOURS.md)

**What I was working on.** Turning a confirmed outro design into the actual
deliverables — 16:9, 9:16, 4K — and separately fixing a production video that
wasn't visible.

**What I tried, and what I expected.** I expected the aspect-ratio work to be a
render setting. It isn't, and I should have known that from August, when I wrote
the 9:16 cut down as a deferred item rather than a five-minute job.

**Where it resisted, and what I did next.**

- **9:16 is a re-layout, not a re-render.** The outro's whole composition is a
  horizontal lockup — mark, wordmark, tagline, URL arranged across the frame.
  Cropping that to vertical either cuts the wordmark or shrinks everything to
  illegibility. The elements had to be re-stacked for the vertical frame while
  keeping the same tracking and proportions so it still reads as the same
  identity. This is why it took a week and not an afternoon, and why deferring it
  in August was the right call rather than a dodge.
- **4K exposed things 1080p hid.** Edges and stroke weights that looked clean at
  1080 did not at 4K. The mark is vector, so it scaled; the raster tile assets
  from the original reel build were the constraint.
- **The not-visible video was a diagnosis problem, not a fix problem.** Working
  out *why* it wasn't visible took the time; correcting it and re-uploading did
  not. I then added the YouTube link into the Medhavy codebase, because a video
  that exists but isn't referenced anywhere is a video nobody will find — the
  same failure in a different form.
- **I did not record the URL or the commit.** The task is self-verifiable in
  principle: the link works, the upload is visible, the code references it. But
  I wrote none of those three pointers down, so this log describes a verifiable
  fix that a reader cannot currently verify. That is the mistake of the week and
  it is the reason this entry is worth keeping.

**What Claude contributed, and what I accepted, changed or rejected.**

- Accepted: re-stacking the lockup for vertical rather than cropping or
  letterboxing the 16:9 master.
- Accepted: wiring the link into the codebase rather than treating the upload as
  the end of the task.

**What I understand now, and what I still do not.**

I understand that "deliver it" and "deliver it in the formats it will be used in"
are different pieces of work, and that a confirmed design is not a shipped asset.
I also understand, more concretely than before, that an integration step —
putting the link where the project can find it — is part of finishing, not
paperwork after finishing.

What I did not do was write the link down as I made it. The outro formats are in
Drive; the fixed video's URL went unrecorded at the time and is added in the
entry below. Next time the link goes into the log as I make it, not from memory
a week later.

---

## 2026-10-17 — naming the video

> Written 2026-10-17, four weeks after the entry above. Appended; that entry
> stands as written.

- **The video:** [Cancer Biology and Therapeutics – Guided Tutorial](https://www.youtube.com/watch?v=tnxC6LATugU)

**What I can now point at.** The not-visible video is identified. It is also the
`Medhavy_Cancer_Tutorial_1_4K.mp4` that had been sitting in Drive at 185.7 MB
with no beat sheet, no source and no link — listed as an unexplained artifact in
the fellow README since this folder was created. One link resolves both.

**What is still open.** The codebase commit where the link was added. The fix,
the upload and the integration were all mine; only the commit reference is
missing, which means the last step is the one a reader still cannot verify.
