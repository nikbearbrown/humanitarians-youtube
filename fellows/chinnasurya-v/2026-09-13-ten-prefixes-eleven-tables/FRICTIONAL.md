# Frictional — Ten Prefixes, Eleven Tables

## 2026-09-13 — the discrepancy that became the script

The reel exists because of a count that did not add up. I had been describing the
integration as having ten `lti_` tables, and row-level security verification kept
reporting eleven. The eleventh comes in through `03_lti_v1_credentials.sql`, the
LTI 1.1 credential and launch-session tables, which are a separate migration from
the main multi-tenant schema in `02_`.

That is a small thing, but it is the kind of small thing that ends up in a
document going to a university's IT office, and a reviewer who counts will find
it. It was worth a reel on its own.

## 2026-09-13 — script written, build not started

Same art direction system as the other three. Table and parameter names appear in
mono, spelled exactly as they are in the migration files, because a schema reel
that paraphrases identifiers is useless.

Ran out of session before building, same as `what-actually-crosses`.

## 2026-10-28 — open

Script complete and unmodified since 13 September. Render pending. Filing as a
written script, not as a video.

## 2026-10-28 — built, alongside the other pending script

Rendered in the same session as `what-actually-crosses`, on the environment I had
just rebuilt for it.

Three defects, all found on the contact sheet, none by a gate. The title cards
came out clean on the first render, which has not happened before in this series,
and the reason is that `title_card()` now derives the subtitle rule and the title
size from the footer rather than from a fraction of the frame. That fix was paid
for on the previous reel and it carried over for free here.

The defect worth recording is B06's `+ institutions` label landing on top of the
`11`. I had placed it at 52 percent of the distance between the two numerals,
which sounds reasonable and is actually a guess that ignores how wide the numerals
render at that font size. The fix was to ask the font: measure `10` with the
display font's own metrics, compute the real gap, and pass the label through
`fit()` so it cannot exceed it. The other two were the same shape of error —
B03's table names touching their arrows, B06's captions touching the numerals
above them.

Three reels in and the pattern is unmistakable. Every single visual defect in
this series has been a position I guessed as a fraction of something, when I
could have measured it from the thing it needed to clear. The gates do not catch
these because the gates check the frame edge, and all of these are collisions
in the middle of the frame between two elements I placed myself.

The harder call was B04. It states launch audit retention as one hour, which is
what the schema says and what the FERPA document says. While auditing the
security review document this month I found the published privacy policy says
twelve months, and the `pg_cron` line that would actually run the purge is
commented out, so neither number is enforced. The claim is on camera and already
rendered. I could have dropped the beat, quietly changed the number, or shipped it
with the discrepancy documented. I shipped it documented: `FACTCHECK.md` row 4 is
marked SEE NOTE, the note sets out all three figures and which one the code
actually enforces, and it says the figure must be re-measured before any rebuild.
Reconciling retention to one enforced number is now in the research plan for the
next period.

Still open: no 9:16 cut, no captions, `PEDAGOGY.md` not self-signed, and B04's
retention figure needs the code fixed rather than the reel re-cut.
