# PEDAGOGY — hai-brutalist-week-1

## The one thing a viewer should leave with

*A tool that says nothing is not telling you that it passed.*

## Why this is the subject

A first-week progress report could have been a tour of a new toolkit. This one reports a
mistake instead: a quality gate that had been silently skipping for the entire week because
a library was missing, while the work it was supposed to check was treated as finished.

The reason that is worth a film is that the failure mode is general. A check that exits zero
when it cannot run looks exactly like a check that ran and passed. Nothing on screen
distinguishes them. Every viewer has a command they trust in precisely that way.

## Structure

1. **Ask** (B00) — who, what week, and the AI-voice disclosure, spoken not just written.
2. **BLUF** (B01) — the result before the story: four masters shipped, and a check found
   broken. Nothing is held back for a reveal.
3. **What the toolkit is** (B02) — the minimum context needed to follow the rest.
4. **Four terms** (B03) — beat sheet, lane, gate, master.
5. **Evidence** (B04) — the week's output, probed.
6. **Finding** (B05) — the silent skip, in four real terminal lines.
7. **Judgement** (B06) — the gate was right and the frames were wrong. Vertical is its own
   design, not a crop.
8. **Your turn** (B07) — the transfer.
9. **Outro** (B08).

## The transferable move

Report the mistake as the headline. The reel puts a personal failure in the BLUF position,
where a progress update would normally put an achievement, and the four masters become
supporting evidence rather than the point. That ordering is the skill being modelled: a
week where you found a broken check is more useful to a team than a week where you shipped
four things and noticed nothing.

The second move is subtler. The finding is only credible because the numbers are real —
`No module named 'scipy'`, `float | None` on Python 3.9.6, `FAIL (8 pixel beats)`, 38px
against a 72px floor. A vaguer version of the same story would persuade nobody.

## What the viewer is asked to do

Take the build or test command they trust most — the one they assume is passing — and make
it fail on purpose, once. Then watch whether it actually tells them.
