# FACTCHECK — `yatra-this-week-gordy` ("This Week, Gordy.")

GENRE: weekly recap on the ai-explainer chassis. First-person report of the
narrator's own week, so most claims are the human's own account and are taken as
given. The exposure here is **not** statistics — this reel contains no numbers
beyond "two articles" and "five stages". The exposure is **claiming that
unfinished work is finished.**

## The hard constraint (from the human, 2026-09-03)

> "don't say they're published yet, since they're still pending approval"
> "don't invent details about the articles' content since they haven't been
> finalized/published yet — keep this at the level of 'articles are in review,
> more coming soon.'"

Enforced structurally, not by memory: `WkReview` renders the two articles as
**dashed, empty slots with a withheld band**. The component has `slots` typed as
`{label: string}[]` — there is **no title, summary, excerpt or content prop** on
it. There is no code path by which an article's contents can reach the screen.

## The claim ledger

| # | Claim as narrated / rendered | Basis | Beat |
|---|---|---|---|
| 1 | Gordy is "a two-mode music artist brand strategist and sonic identity architect" | VERBATIM from the tool page | B03, B09 |
| 2 | It covers "discovery, strategy, sonic and visual identity, campaign, and copy tools" | VERBATIM from the tool page | B03 |
| 3 | "For independent artists, music teams, and the Musinique era" | VERBATIM from the tool page | B03 |
| 4 | That one-line description is the whole public description | Verified: two fetches of the page returned only this. The page is billed as a "Complete command reference" but the reference body does not render in the fetched text | B03, B08 |
| 5 | This week's tool was Gordy; the narrator experimented with it | The human's own account | B01, B05 |
| 6 | The narrator created graphics for Humanitarians AI's LinkedIn page promoting Gordy | The human's own account | B06, B09 |
| 7 | Two articles are written and are with Nina for review; they go to Substack once approved | The human's own account | B07, B09 |
| 8 | Nothing from this week's writing is published yet | The human's own account, stated as a constraint | B01, B05, B07, B08, B09 |

Source line rendered on the Gordy beat:
`Source: humanitarians.ai/ai1/tools/gordy-tool (page description, verbatim)`

## What is NOT on screen (and why)

- **The two modes are not named.** The page says "two-mode" but never names the
  modes. The reel says "two-mode" and stops. No mode names are invented.
- **No article titles.** Unlike the previous episode in this series — where the
  human supplied partial titles that were rendered verbatim with their
  ellipses — **no titles were supplied this week**, so the slots render empty.
  Nothing was carried over from that reel.
- **No article content, themes, findings or conclusions.** Not approved, so not
  described. B08 says so out loud.
- **No count of graphics.** The human said "graphics" (plural, unspecified). The
  reel says "graphics" and never a number.
- **No claim the graphics are live/posted.** The human said they were *created
  for* the LinkedIn page. The reel says "created … for the Humanitarians AI
  LinkedIn page" and the status chip reads `MADE`, not `LIVE` or `POSTED`.
- **No mock-ups of the graphics.** Showing invented artwork as if it were the
  week's deliverable would be a fabricated artifact. `WkShip` names the
  deliverable and its destination; it draws no artwork.
- **No claim about Gordy's quality or output.** The narrator used it; the
  write-ups are the place that judgement lands, and they aren't public yet.
- **No stats, dates, engagement figures, or follower counts.** None supplied,
  none rendered, no component accepts one.

## Register corrections applied (DOUBLE-CHECK LAW)

1. **"In review" is never softened to "coming" or hardened to "done."** Every
   beat that touches the articles carries the review state explicitly, and the
   verdict beat repeats it rather than letting the summary imply completion.
2. **The narrator's own week is not inflated.** The verdict says "an honest
   week, not a finished one" — four of five stages closed, and the fifth is
   someone else's call.
3. **Nina is named only as the reviewer**, which is what was supplied. No claim
   about her opinion, timeline, or likely decision.
4. **The thin source is disclosed rather than padded.** B03 states that the
   one-line description is all the page publishes; B08 states that the
   narrator's read comes from use, not documentation.
5. **No model names or version numbers** — they date the video.

## Series-continuity note (prior art check)

This is the next episode of the same weekly series as
`yatra-one-tool-a-week-brandy` ("One Tool a Week.", tool: Brandy) and
`yatra-every-tool-every-week` ("Every Tool, Every Week."). The human asked for
"not a variation of any previous video," which cannot hold literally for a
series episode. Differentiation actually applied:

- **All seven illustration components are new** (`WeekGordy.tsx`). The Brandy
  reel's `Rcp*` family is not reused, and neither is the `Lnk*` family.
- **Different spine.** The Brandy episode's shape was "three things shipped."
  This week's defining fact is that the week ends **mid-pipeline**, so the
  five-stage method and its unclosed final stage are the reel's subject.
- **No narration reused.** Checked line by line against the Brandy episode,
  including its cold open ("Hi, I'm Yatra. Every week I pick one AI tool…") and
  its outro ("One tool a week. Next week, a different one.").
- **Fresh greeting.** `Jambo` — Namaste, Kumusta, Sawubona, Hej and Merhaba are
  already spent on the five prior reels on this channel.
