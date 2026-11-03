# QUESTION.md

**Question:** Is a Claude "contract-review" skill acting like a lawyer using
judgment on your contract, or something else?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-contract-review`), a Teardown-register
"skill anatomy" reel under `anthropics/knowledge-work-plugins/`. Not a live
viewer submission.

**Name usable:** N/A (no submitter).

**Note on the source:** the source `beat_sheet.json`'s narration_text for
B00/B03/BVDT/BHTF carries unfilled `>` placeholder markers (the specific
worked-example detail — e.g. which contract, which clause — was never
written in). PEDAGOGY.md records only "VERDICT: PASS / Batch build — skill
teardown format," and the `source_skill` SKILL.md path is not present on
this machine. The source's REAL, non-placeholder argument is intact and
locked: a skill is a folder Claude reads before acting (B01); the pipeline
is read -> execute steps in order -> return output, linear (B02); the
design tell is specification-as-instruction-set, strength repeatable
results, weakness anything outside the spec (B03's frame minus its filled
example); the verdict is same input -> same output every run, limited to
what the file says (BVDT's frame minus its filled example). This redo
keeps that argument word-for-word in substance and supplies one concrete,
generic, true worked example (a freelance contract's termination clause)
to fill the gap the placeholder left — per hai-simple SKILL.md PHASE 1's
"when in doubt, describe behavior generically." Logged in BUILD-LOG.md.
