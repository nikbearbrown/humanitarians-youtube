# SOURCES — `yatra-this-week-gordy` ("This Week, Gordy.")

## The one external source

**Gordy tool page** — `https://www.humanitarians.ai/ai1/tools/gordy-tool`
Fetched 2026-09-03. Supplies the only externally-checkable claims in the reel:

- "a two-mode music artist brand strategist and sonic identity architect"
- covers "discovery, strategy, sonic and visual identity, campaign, and copy tools"
- "For independent artists, music teams, and the Musinique era"

Rendered on B03 as a quoted italic block with the citation
`Source: humanitarians.ai/ai1/tools/gordy-tool (page description, verbatim)`
and the URL on screen in mono.

### The page is thin, and the reel says so

Two separate fetches returned essentially the one sentence above. The page bills
itself as a "Complete command reference," but the reference body does not appear
in the fetched text. Consequences, all deliberate:

- **The two modes are never named.** The page says "two-mode" and stops. So does
  the reel. No mode names appear anywhere in `WeekGordy.tsx`.
- **No feature list beyond the six coverage areas** the page itself names, which
  render as chips verbatim.
- **B03 discloses the thinness on screen** ("One line is all the page publishes.
  The two modes are not named.") rather than padding it, and B08 repeats that
  the narrator's read comes from *using* the tool, not from its documentation.

That disclosure is also the series' own thesis — the AI+1 platform describes
itself as documenting what AI cannot do "honestly, week by week, as it happens,"
and a one-line product page is exactly why a use-it-then-report series exists.

## Everything else is first-person account

The remaining claims are the human's own report of her own week, supplied
2026-09-03, and are the genre's evidence rather than citable facts:

| Claim | Beat |
|---|---|
| This week's tool was Gordy; she experimented with it | B00, B01, B05 |
| She created graphics for Humanitarians AI's LinkedIn page promoting Gordy | B01, B05, B06, B09 |
| She wrote two articles about Gordy | B01, B05, B07, B09 |
| The articles are with Nina for review | B00, B05, B07, B09 |
| They go to Substack once approved | B00, B05, B07, B09 |
| Nothing from this week's writing is published yet | B01, B05, B07, B08, B09 |

B08 exists to draw the line between what that account supports and what it does
not — see FACTCHECK.md for the full refusal list.

## Corrections applied under DOUBLE-CHECK LAW

1. **"In review" is never softened or hardened.** Not "coming soon" as if
   scheduled, not "published." Every beat touching the articles carries the
   review state, and the verdict repeats it rather than letting a summary imply
   completion.
2. **No article titles.** The previous episode in this series rendered *partial*
   titles because the human supplied them. None were supplied this week, so the
   slots render empty. Nothing was carried over from that reel.
3. **The graphics are "made," not "live."** The human said they were *created
   for* the LinkedIn page. `WkShip`'s chip reads `MADE`; the reel never claims
   they are posted.
4. **No count of graphics.** "Graphics", plural, unspecified — as supplied.
5. **Nina is named only as the reviewer.** No claim about her opinion, timeline,
   or likely decision.
6. **No stats anywhere.** The only numbers in this reel are "two articles" and
   "five stages", both structural.
7. **No model names or version numbers** — they date the video.

## Prior art check (series continuity)

This is the next episode of the same weekly series as
`yatra-one-tool-a-week-brandy` (tool: Brandy) and `yatra-every-tool-every-week`.
The human asked for "not a variation of any previous video," which cannot hold
literally for a series episode — that reel's own outro says "One tool a week.
Next week, a different one," and this is that next week.

Differentiation actually applied, and verified line by line:

- **All seven illustration components are new** (`WeekGordy.tsx` /
  `WeekGordy916.tsx`). The Brandy reel's `Rcp*` family and the
  `yatra-nobody-wrote-this` `Lnk*` family are both untouched.
- **Different spine.** Brandy's episode was shaped "three things shipped." This
  week ends mid-pipeline, so the five-stage method and its one unclosed stage
  are the subject.
- **No narration reused** — checked against Brandy's cold open ("Hi, I'm Yatra.
  Every week I pick one AI tool…") and its outro.
- **Fresh greeting.** `Jambo` — Namaste, Kumusta, Sawubona, Hej and Merhaba are
  already spent on the five prior reels on this channel.

## Scene provenance

All seven components are new for this reel. No seeds, no generative assets, no
paid API calls — Kokoro + Remotion + ffmpeg, free and local. No component
accepts an article title, an article summary, a graphics count, or a statistic.
