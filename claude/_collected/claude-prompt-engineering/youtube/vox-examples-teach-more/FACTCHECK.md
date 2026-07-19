# FACTCHECK — vox-examples-teach-more

## Claim-by-claim verification

| Beat | Claim | Verdict | Source / fix |
|------|-------|---------|-------------|
| B01 | Pasting a memo as format example causes Claude to copy the tone | ✓ | Chapter 4: "The writer pasting her informal memo was not thinking about tone. She was thinking about structure. Claude learned both." |
| B02 | Priya scenario: researcher needs formal board report, pastes casual memo | ✓ | Adapted from card key case (writing instructor + memo → informal output). Illustrative. |
| B03 | Claude copied casual register, hedging language, short sentence rhythm | ✓ | Chapter 4: "A research note pasted as an example teaches Claude to hedge like a researcher." |
| B04 | Instructions are explicit; examples teach by demonstration across every feature | ✓ | Chapter 4: "An example teaches format, level, tone, reasoning pattern, length, vocabulary register, and rhetorical approach — often all at once." |
| B05 | Observable features of a memo: structure, register, sentence length, tone | ✓ | Chapter 4: same list verbatim |
| B06 | Without annotation, all features carry equal weight as teaching signal | ✓ | Chapter 4: "Claude cannot know which ones you consider essential and which are incidental unless you say." |
| B07 | Board report sounds like memo because taught by memo | ✓ | Chapter 4: direct implication of the mechanism |
| B08 | Section card content only — no factual claim | ✓ | n/a |
| B09 | Annotation narrows which features carry signal | ✓ | Chapter 4: the revised prompt example names "features to copy" and exclusions explicitly |
| B10 | Any example contains many observable features | ✓ | Chapter 4: general principle |
| B11 | Marco scenario: competitor post with exclamation points → Claude copies them | illustrative | Invented but plausible; not in chapter. Labeled illustrative. |
| B12 | Adding exclusion annotation removes the unwanted feature from output | illustrative | Illustrative extension of the chapter mechanism. |
| B13 | Two-sentence annotation practice: which to copy / which to ignore | ✓ | Chapter 4: "The revision annotated the example explicitly: it named which features to copy... It excluded which features not to copy." |
| B14 | Unannotated examples teach everything; annotation makes them precise | ✓ | Chapter 4: the core thesis |

## Terms table

| Term | Debuts | Prior beat creating need |
|------|--------|--------------------------|
| example (as instruction) | B04 | B01–B02: we see the problem first |
| observable features | B05 | B04: we know examples teach features |
| annotation | B08–B09 | B06–B07: we've seen the problem, now need the name |
| teaching signal | B06 | B05: features exist, now we name what they do |

## Exclusion confirmation
- No few-shot learning benchmark research: CONFIRMED absent
- No transformer attention mechanism: CONFIRMED absent
- No extended in-context learning theory: CONFIRMED absent (term "in-context learning" not used)

## Illustrative numbers / invented scenarios
- B11–B12: Marco scenario is invented but plausible. No numbers claimed as real.
- B02: Priya scenario adapted from card; all details illustrative.
