# FACTCHECK-THE-FACTCHECK — humanitarians-ai-week1-diagnostic-audit

The toolkit's DOUBLE-CHECK LAW: a fact-check on its own claims still deserves
a second pass, especially where I did pixel measurement myself and could
have measured wrong. Re-derived independently below, not just re-read.

## Re-verification of FACTCHECK.md's ✓ PASS rows

**Row 2 (About Us / Contact Us / Donate bounding boxes).** Re-ran the maroon
color-threshold detection (target RGB ≈ 100,20,14, tolerance 40) on
`01_hero_section.jpg` a second time, this time splitting the image into
quadrants independently instead of upper/lower halves, to make sure the
first pass hadn't accidentally merged two different buttons into one
bounding box. Result matched: About Us + Contact Us together span
x∈[0.073,0.261] y∈[0.762,0.812]; the nav Donate button alone spans
x∈[0.811,0.888] y∈[0.016,0.065]. Confirmed independently — PASS holds.

**Row 3 (program cards count).** Re-counted card headers directly from the
visible text in `03_program_cards.jpg` rather than trusting the first pass's
memory of the image: "FELLOWS PROGRAM," "BOTSPEAK: AI FLUENCY," "LYRICAL
LITERACY," "AI FOR GOOD" — four distinct card headers, each with its own
icon and body copy. Confirmed — PASS holds.

**Row 5 (footer project count).** Re-counted the Projects column a second
time, top to bottom, reading only that column and no others: Dewey,
Irreducibly Human, Lyrical Literacy, Madison, Medhavy, Musinique, Mycroft,
Popper. That's 8 by direct count both times. Confirmed — PASS holds.

**Row 7 (video embed area).** Re-measured using a different method than the
first pass — instead of a brightness threshold alone, cross-checked against
the visible edges of the black video card in the crop preview generated
during scenes.py's build. The two methods agree within a few percent.
Confirmed — PASS holds.

## Re-verification of ⚠ rows — checking I didn't under-claim

Rows 1, 4 (partial), 6, and 8 are marked unverifiable-from-screenshots or
judgment calls. Re-checked each against the SAME six screenshots one more
time to make sure there wasn't in fact a way to verify them that the first
pass missed:

- Row 1 / Row 8 (project scope history): confirmed there is no screenshot
  among the six supplied that documents an internal brief or scope
  decision — these are photographs of the live site, not of a project
  planning doc. The UNVERIFIABLE flag is correct, not a cop-out.
- Row 4 ("documentation system"): checked all six screenshots again for any
  visible reference to something nameable as a "documentation system" —
  none of the six frames shows one. The flag is correct.
- Row 6 (font-weight claim): confirmed a JPEG screenshot genuinely cannot
  establish an exact font-weight value (compression + rendering + no
  access to the underlying CSS) — this has to stay a design judgment call,
  not a measured fact, regardless of how visually obvious it looks.

## Verdict

No changes to FACTCHECK.md's table. The three open checkboxes in that file
(rows 1, 4, 8's "documentation system" phrase, and row 5's exact count) are
still open — they require your own project records, not another look at
the same six screenshots. **GATE F remains NOT YET SIGNED** until you check
those boxes.
