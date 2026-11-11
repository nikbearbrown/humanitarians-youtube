# Frictional log — Most Insider Trades Aren't Buys

*Drafted with Claude from the build logs; reviewed by me.*

## 2026-11-10 — script, both cuts and final masters

- **Drive:** https://drive.google.com/drive/folders/1ycNcATgR7NhZOC9Qd7e0tp6oIDXTWJZ6
- **Folder:** [README.md](README.md) · [SOURCES.md](SOURCES.md) · [BUILD-LOG.md](BUILD-LOG.md) · [vertical/BUILD-LOG.md](vertical/BUILD-LOG.md)

**What I was working on.** A 60-second-format explainer built from my own research
data instead of a published source: the committed audit files of my Mycroft
insider-signals module (commit `fed487c`). Of 999,542 Form 4 transactions, about 8%
are purchases, and 65,106 buys are left to test after parse checks and four
pre-registered filters. The returns analysis hasn't been done, so the reel had to
avoid stating or implying any result about returns.

**What I tried, and what I expected.**
- Every number had to come from a committed audit file and be cited by file and line
  in `SOURCES.md`; Form 4 rules had to be checked against SEC's own pages. Anything
  inferred is labelled.
- I didn't use the uncommitted ENRICH work in my working tree.
- As with the p-value reel, I reviewed the narration and on-screen text before
  anything was built.

**Where it resisted, and what I did next.**
- **The title didn't survive the data.** The working title was "Most Insider Buying
  Is Noise". The audit says otherwise: 65,106 of the 78,495 qualifying buys (83%)
  pass the filters, so most buys are *not* filtered out as noise. What the data does
  support is that most Form 4 transactions aren't buys at all (purchases are 8.2% of
  rows). The title became "Most Insider Trades Aren't Buys".
- **Runtime.** The first approved draft was 198 words and ran 80.8 s at Kokoro speed
  1.08. I trimmed it to 180 words (72.5 s). Speeding up to 1.12 only reached 71.2 s,
  so I asked for line cuts instead of more speed. Three cuts, a shorter B05 and a
  restored B10 check line brought it to 172 words and 65.8 s. I accepted that rather
  than cut content to hit 60 s.
- **Four line fixes for clarity, before finals.** I re-read the full narration and
  reworded four lines. Only those beats were re-voiced and retimed:
  - B04 "Code P means purchase" → "Those are coded P", so it follows on from B03's
    purchases.
  - B06 "eligible buys remain" → "buys are left to test", which says what the number
    is for without implying a result.
  - B07 "Twenty-five random buys, checked against…" → "We checked twenty-five random
    buys against…", which says who did the check (my audit).
  - B08 "Rules one through six were dated before any return was computed" → "Every
    filter was fixed before any return was computed", with the card changed to
    "Filters fixed first / Before any returns". Rule numbers meant nothing to a
    viewer. Claude checked the new wording against `PRE_REGISTRATION.md`: every
    filter shown in B05 was registered before any prices or returns were computed,
    with no amendments since. "Every filter" is labelled INFERENCE (scope) because
    the scoring parameters aren't registered yet and aren't filters.
  - Runtime after the fixes: 64.7 s.
- **The vertical edge-strip false positive.** On the 9:16 review cuts, strict visual
  QC (GATE V) flagged right-edge overflow on B06 and later B08. The scenes weren't
  the cause:
  - The review cut is compiled at 1216 px wide. The compiler pads the scaled
    1215-px frame with a 2-px cream strip, and after compression it read 30 colour
    units from the background, against a limit of 28.
  - The raw renders had a clean edge. The strip was the only ink past the safe area,
    and with it masked the frames passed.
  - The 4K master isn't scaled or padded, and it passed with nothing flagged.
  - The real fix is in the toolkit's compiler, so I didn't edit it here.
- **A real edge problem the review cut hid.** The first 4K vertical final was refused
  because B03's Purchases row slid in from just past the left safe edge. The smaller
  review cut had sampled it under the threshold. It was moved 0.1 units inward (same
  text and numbers) and the final passed.

**What Claude contributed, and what I did with it.**
- Claude read the committed audit files, traced every number to a file and line,
  checked the Form 4 facts against SEC's pages, flagged that the working title
  didn't match the data, and drafted the script and both cuts.
- I approved the new title and made the edits to B04, B05, B06 and B08 in the
  first review. I chose the trims over a faster voice, approved the B05 replacement
  line and the B10 check line, and chose the four pre-final line fixes after
  re-reading the full narration.
- I accepted leaving the compiler's padding issue as a documented false positive
  rather than changing the shared toolkit.

**What I understand now.**
- A title is a claim. I had the data, and checking the title against it was what
  changed it.
- The safest wording for unfinished research says what has been counted and states
  plainly what hasn't been tested.
- QC results depend on how the frame is compiled. A flag can come from the
  pipeline, and a smaller cut can hide a real problem. Checking the raw render and
  the final master tells them apart.

**Sign-off.** Pedagogy gate: reviewed and approved by me, with eight known
weaknesses accepted. Both 4K masters passed GATE T and strict GATE V.
