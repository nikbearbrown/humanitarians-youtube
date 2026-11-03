# Frictional Log — read-the-receipt-backwards (Week 24 work video)

**Record provenance:** drafted 2026-09-28 with Claude from this folder's own records (`ANGLE.md`,
`FACTCHECK.md`, `PEDAGOGY.md`, `PROOF-REVIEW.md`, `PROOF-REVIEW-SHORT.md`, `SCRIPT-SHORT.md`), after
the work was done rather than while it happened. Reviewed by Tanmay. Every entry below points at the
record it comes from.

## 2026-09-27 — An angle that wasn't new

- **Work and expectation:** make the work video from my Mastercard Agent Pay case study and its
  reference implementation. I expected the first angle to be fine.
- **Where it resisted:** when I asked for the angle to be unique across every work video I've made,
  a check of all earlier narrations found the first angle repeated Week 20's thesis and beats from
  Weeks 21 and 23.
- **What I did next:** rejected it. The replacement, "read the receipt backwards" (take the record the
  build writes and ask which step checked each line), was checked the same way. Its nearest earlier
  beat (Week 21, B11) is named in the audit as the boundary.
- **AI and other contributions:** Claude ran the narration audit and proposed both angles. I set the
  uniqueness bar and chose the final angle.
- **Evidence:** [ANGLE.md](ANGLE.md).

## 2026-09-27 — Does the build hold up?

- **What I tried:** before scripting, I asked whether the case study and the code actually held up.
- **Where it resisted:** they didn't, completely.
  - **The code:** a category written with a capital letter or different spacing ("Household_Staples")
    missed the consumer's rule, went to the Authorization Gate as if it were a new category, and was
    approved.
  - **The case study:** four lines were inconsistent with the code.
- **What I did next:** chose to fix both. The category is now normalised once, before any check, and
  there are 10 new tests plus a logged design decision (DD012). The fix itself exposed one more case,
  a category made only of separators, which is now rejected. The case study was corrected, with the
  original kept. The build went from 72 to 82 tests, all passing in a fresh environment.
- **Why it's in the film:** a bug I found and fixed in my own build is evidence the testing worked,
  so the film shows it (B06) rather than hiding it.
- **Evidence:** [FACTCHECK.md](FACTCHECK.md) (build facts B1–B17).

## 2026-09-27 — Framing what the public record doesn't say

- **Where it resisted:** Mastercard hasn't published everything. It doesn't say what happens for a
  category the consumer never set, how a merchant restriction is checked, or how the record is
  signed. Said carelessly, those limits read as gaps in my work.
- **What I did next:** my instruction was to *"frame the gaps subtly because it should not show my
  work in a negative manner"*. The script says what the build gives first. Each limit is then shown as
  the build stopping where the public record stops, on purpose, and saying so (B07, B09, B11).
- **AI and other contributions:** Claude drafted the wording from the fact-check. I checked that it
  kept every claim accurate.
- **Evidence:** [SCRIPT.md](SCRIPT.md), [PEDAGOGY.md](PEDAGOGY.md).

## 2026-09-28 — Stills before audio, reviews before renders

- **What I tried:** applying the lesson from the topic video, that time goes to late re-renders.
  - Before audio, I asked for stills of every beat and a PROOF review.
  - Gate P was signed before any audio was generated.
  - Whisper timing was run before the first render.
- **Where it still resisted:**
  - **Frame checks** found a terminal that never finished typing (B08) and empty opening panels in
    six beats.
  - **Whisper** caught two mishears ("tamper assistant", "a mountain date"), fixed by respelling for
    the voice.
- **Result:** long master clear-for-public: teaching 12/12, 22 of 22 claims on screen when spoken.
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md).

## 2026-09-28 — The Short in portrait

- **What I tried:** a Short with its own script, synced so the same receipt carries across every
  cut, as I asked from the start.
- **Where it resisted:** the portrait layout didn't fit a phone.
  - The camera zoom bled off the edge, and the text was too small.
  - Three stacked panels didn't fit.
  - Stamps sat under the Shorts buttons.
  - The seal crossed the top overlay.
  - I noticed the headings were almost touching the cards.
- **What I did next:** one panel at a time, larger text, a centred 3% zoom, and consistent heading
  spacing (my note). The seal moved inside the card. Result: 0 failures in the Shorts overlay zones,
  and 11 of 11 claims on screen when spoken.
- **Evidence:** [PROOF-REVIEW-SHORT.md](PROOF-REVIEW-SHORT.md), [SCRIPT-SHORT.md](SCRIPT-SHORT.md).

## 2026-09-28 — Publishing the build, and a surprise in mycroft

- **What I tried:** putting the build in `nikbearbrown/mycroft` so the video's repository link has
  somewhere to point. PR #53 added case study 14 and `mastercard-agent-pay-workflow`.
- **Where it resisted:** `main` no longer had my case studies 11–13, although they had been merged. A
  force-push to `main` on 2026-09-24 had replaced its history.
- **What I did next:** PR #54 restored my three case studies exactly as they were merged, with every
  test re-run (28/28, 32/32 and 49/49). Other contributors' missing commits are left for the
  maintainer.
- **Evidence:** nikbearbrown/mycroft #53 and #54.

## What I'm taking forward

- **Check first:** checking the build's correctness before scripting turned up the film's best beat.
- **Uniqueness:** check an angle against every earlier narration, not just a table of theses.
- **Portrait:** design it from stills in portrait before rendering.

**What I learnt**

- **Testing my own build:** checking the build before scripting made the film better. The
  category-spelling bug turned into the film's most concrete beat (B06), and a bug found and fixed
  in my own build, with tests, shows the review process working.
- **A complete record isn't a verified one:** every field on a receipt can be well-formed while one
  line was never checked. A seal or signature only protects what the steps before it put there.
  That's the idea I'd take to any system that writes records.
- **Stating limits:** saying where the public record stops, and what the build does there instead
  of guessing, makes the work more trustworthy, not less.
- **Portrait is its own design:** a landscape scene squeezed into 9:16 breaks in predictable places
  (edge bleed, type size, the Shorts overlay zones). Most of the Short's fixes came from not
  designing in portrait first.
- **Checking shared repos:** before stacking new work on top, check what's actually on `main`. Case
  studies 11–13 were missing from main without any sign of it, and I only noticed because I
  compared main with my own merged PRs.

**Going forward**

- Keep the order this film used: fix the build, then write the angle, fact-check, script and
  Gate P, then review stills, then audio and render.
- Add a test for every class of input problem a review finds (spelling variants, separators, bad
  numbers), not just the one case that failed.
- Design every new scene in portrait from the start, and check its stills in the overlay zones
  before any render.
- Before opening a PR, compare `main` with my earlier merged work, and flag anything missing to the
  maintainer.
- When Mastercard publishes how merchant restriction is checked, add that check and update the
  merchant line. It's the one line still carried on trust.

## Still open

- YouTube links for both films. For now, the Short's description points to the long's Drive link.
- The merchant line: no check exists until Mastercard publishes how merchant restriction works.
