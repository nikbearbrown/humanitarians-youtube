# FACTCHECK.md — Claude, Rewritten.

Source: `ai1-cli/chapters/04-rewrite-a-chapter-in-another-voice.md`, read in
full. Every claim below checked verbatim/near-verbatim against that file.

| Beat | Claim | Source line | Verdict |
|---|---|---|---|
| A1-1/A1-3/A1-4 | Seven voices — Wonder, Generic, Socratic, Sardonic, Narrative, Pragmatist, Teardown — with the one-line registers shown | lines 13-21 (the table) | OK — near-verbatim |
| A1-2 | A voice = a `voices/<voice>/VOICE.md` spec file with a conversion contract; running it copies `chapters/NN-*.md` into `voices/<voice>/NN-*.md`, original never modified | line 9 | OK — verbatim mechanism |
| A1-5/A1-6 | "no single 'good' voice — only good for this reader, doing this job"; pick two voices that fight (Socratic vs. Pragmatist example) | lines 23, 31 | OK — near-verbatim |
| A2-1/A2-2 | Write only to `voices/<voice>/`; diff against the original instead of reading and nodding; `git diff --no-index` | lines 9, 35, 41 | OK |
| A2-4/A2-5 | Mark three changes better/worse/neutral for the reader your Blueprint named; a deleted definition is worse for a reference-seeker, better for a concept-builder | line 43 | OK — verbatim example |
| A2-6 | "You are judging the changes, not the agent's confidence that they're improvements" | line 41 | OK — verbatim |
| A3-1 | The verdict is a 200-word memo with quotes; "cite or it doesn't count" | lines 45, 47 | OK — near-verbatim |
| A3-2/A3-3 | The real worked-example sentence and its two real rewrites (Socratic and Pragmatist, on Chapter 3's "not a Word document you email around" line) | lines 79-82 | OK — **verbatim quotes**, copied exactly from the chapter's own "Bear's Copywriting Book" worked-example section |
| A3-4/A3-5 | The diff-level judgment (Socratic removed the mechanism + added a question; Pragmatist removed the voice + added a formula) and the verdict ("lead Socratic, land Pragmatist") | line 84 | OK — verbatim |
| A3-6 | "That verdict is only defensible because it quotes the two changes" | line 84 | OK — near-verbatim |
| A4-2 through A4-4 | The four failure symptoms and fixes (agent edits chapters/ directly; "liked it" is taste not evidence; no quotes = unfalsifiable; both voices "seem fine") | lines 62-67 (the table) | OK — verbatim/near-verbatim |
| A4-5 | This exercise rehearses "the human rewrite... [that] carries a gate no agent may ever sign" | line 5 | OK — near-verbatim |
| A4-6 | Bridge to Chapter 5: quizzes/exercises/flashcards, then auditing them for questions that quietly fail | line 71 | OK — near-verbatim |

## Honesty note on the worked example

The chapter itself flags (line 86) that its Socratic/Pragmatist rewrites
are "illustrative single-sentence rewrites, not full `voices/` files... a
full run would produce complete `voices/socratic/NN.md` and
`voices/pragmatist/NN.md` files." This reel presents them exactly as the
chapter does — as the real worked example the chapter provides, not as a
claim that a full-chapter rewrite was performed. No beat in this reel
implies more than the source itself claims.

## Corrections applied

None — no fabrication or drift found; the source is internally consistent.
