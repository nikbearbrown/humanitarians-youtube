# Fact-Checking Chapter 25 — frictional log

## 2026-09-24 — building the week 4 project update

I expected this chapter to be a smaller version of Chapter 23: find the errors in the
textbook, write them up, report the count. What actually happened is that the interesting
finding was in my own earlier work rather than in the textbook.

Chapter 25 already had a completed workbook from an earlier pass. Re-checking it against
the sources changed six of its calls, and twice the earlier plan was going to correct a
sentence that was already right. The EMA really did authorise ctDNA testing for EGFR status
in September 2014. The NCI omics checklist really does carry 30 criteria. Both had been
marked "could not verify, revise it", which is not the same thing as wrong.

That reframed the whole video. I had planned to lead on the cetuximab class error, a
monoclonal antibody filed among tyrosine kinase inhibitors, and that is still in there
because it is the cleanest example of the error type that runs through the chapter. But the
line the video actually closes on is that a fact-check can be wrong in both directions, and
nobody audits the corrections.

The daraxonrasib row is the one I keep thinking about. It was true when the chapter was
written, true when the workbook was built, and false about a month before I checked it,
because the FDA approved a RAS inhibitor for metastatic pancreatic adenocarcinoma on 26
August 2026. Nobody made a mistake. Accuracy and currency are separate questions and I had
been treating them as one.

Three audit passes on my own review. The second found five wrong first authors and a quote
I had linked to a page that words it differently. The third found nine quotations ending in
a full stop the source did not have, and four statements I could not tie back to a source I
had actually read. Final state is 44 sources with every quoted fragment located in the page
its link opens.

### Where the build resisted

Claude Code drafted the beat sheet from my review record and I checked every figure against
the workbook before audio was generated. The arithmetic on screen (14 + 8 = 22, 45 of 288
flagged, 22 of 45 in scope) was recomputed rather than copied.

The visual QC gate failed the first master on the overview beat: the text filled 42% of the
safe area against a 55% minimum. Raising the font from 128 to 150 cleared it. Worth noting
because the same fix caused a different failure in the vertical cut, logged in the week 5
folders.

### Still open

The text edits for this chapter are written but not yet applied to the repo, and the
character-encoding repair has to land before any find-and-replace will work.
