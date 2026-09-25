# SOURCES — humanitarians-ai-week4-navigation-cleanup-handoff

## The status check that shaped this reel

**https://humanitarians.ai** was re-measured on **2026-09-06**, at the same
1503×812 emulated viewport used in Weeks 2 and 3, specifically to check whether
the navigation cleanup had shipped.

**It had not.** Every count came back identical to the Week 2 and Week 3
measurements:

| metric | Week 2 (2026-09-04) | Week 3 (2026-09-05) | Week 4 check (2026-09-06) |
|---|---|---|---|
| Footer columns | 6 | 6 | 6 |
| Footer column links | 33 | 33 | 33 |
| Footer anchors | 39 | 39 | 39 |
| Projects-column links | 11 | 11 | 11 |
| Clickable labels / distinct | 69 / 54 | 69 / 54 | 69 / 54 |
| Onward "learn more" links | — | 13 | 13 |
| Homepage words | — | 1,201 | 1,201 |

All five names scoped for removal — Dewey, Madison, Medhavy, Mycroft, Popper —
were still present in the footer on 2026-09-06.

**This is why B08 exists.** The brief describes the cleanup in the past tense
("we removed", "what remains now"). On the evidence, the removal is a decision
taken with the developer, not a deployment. A viewer can open the site in ten
seconds and check. So the reel says decided, specified, not yet deployed — and
the before/after arithmetic is framed as **current vs agreed**, never as
current vs live.

If it turns out the cleanup did ship somewhere not publicly visible — a staging
branch, a pending deploy — B08's three lines and one narration sentence are the
only things that need changing.

## Claim-by-claim

| Beat | On-screen claim | Source |
|---|---|---|
| B01 | Stakeholder meeting still pending | presenter's own account (Week 3 prepared it; it has not taken place) |
| B04 | Projects column = 11 links | live DOM, 2026-09-06 |
| B04 | Red box = the Projects column | pixel-measured in Week 2 from `06_footer.jpg` |
| B05 | The five names | live DOM; identical to Week 1's flagged set and Week 3's bare-proper-noun count |
| B06 | 11 → 6 | 11 measured live, minus the five named |
| B06 | 33 → 28 | 33 measured live, minus the five named |
| B06 | 6 → 1 | Week 3 counted six bare proper nouns (Dewey, Madison, Medhavy, Musinique, Mycroft, Popper); five are scoped for removal, Musinique remains |
| B08 | "Not yet deployed" | live DOM check, 2026-09-06 — see the table above |
| B11–B16 | The handoff question, the four-part framework, the rollout | presenter's own account of the working sessions with the developer |

## Not verifiable from public sources

Everything about the working sessions — the question put to the developer, the
four-part framework, the feasibility mapping and the phased roadmap — is the
presenter's own account of her own work, carried on her authority. Flagged in
FACTCHECK.md.

## A note on the developer's name

The brief names her as both "Rushali" and "Rashi". The reel therefore says "the
developer" throughout, with no name on screen or in narration. Confirm the
spelling and it can be added in one edit.
