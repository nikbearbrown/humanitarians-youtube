# Claude, Google Drive API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude finds a Drive file by its folder path, like a normal filesystem. There's no path API — Drive works entirely by file ID. So what does that ID-based model actually get you?" | BrutalistHesitantWriter — types "Claude finds my file by its folder path in Drive. Right?", corrects "path" → "ID" |
| B01 | 1 stakes / 2 wrong guess, falsified | In Google Drive, a folder isn't a separate kind of thing from a file — it's a file, with a mimeType that says "folder." Ask Claude to list a folder's contents and there's no "get folder" endpoint to call. It searches for every file whose parents array contains that folder's ID. | a "get folder" guess struck through; the real query revealed — files filtered by parents containing an ID |
| B02 | 3 mechanism / **4 anchor planted** | Say you want every spreadsheet modified in the last month on your team's shared drive, exported as CSV. Files there are invisible by default — the search needs three extra parameters just to see them. And once the list comes back, fields= has to explicitly ask for nextPageToken, or the results quietly stop at one page. | THE ANCHOR — the shared-drive request, three-param requirement and fields=nextPageToken both flagged |
| B03 | **4 anchor payoff / 5 both directions** | Get all three shared-drive parameters right, ask for nextPageToken, and the list comes back complete, page after page. But that spreadsheet has no downloadable bytes — it's a Google Sheet, not a binary file — so pulling it with alt=media returns a flat 403, not a helpful error. The fix is the export endpoint instead. Skip any one of these three habits and the failure never says which parameter you missed — a missing supportsAllDrives just looks like the file was never there. | THE ANCHOR RETURNS — complete pagination, then 403 on alt=media for a Sheet, then a missing param read back as "not found" |
| **BCRY** | **6 carry-out** | Every Google Drive call Claude makes turns on three habits — treat a folder as a file, add supportsAllDrives for anything shared, and export instead of download for anything Google made. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Find all spreadsheets modified in the last thirty days on our shared drive, and export the first one as CSV. Watch three things: does it pass all three shared-drive parameters on the search, does it ask for nextPageToken in fields=, and does it export the Sheet instead of trying alt=media. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Google Drive API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the file-not-folder fact; the full shared-drive/export mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude walks a folder path); B01 falsifies it with a case — there is no "get folder" endpoint at all, only a filter on `parents` |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the Google Drive API skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "spreadsheets modified this month on a shared drive, exported as CSV" request, traced through the three shared-drive parameters and `fields=nextPageToken`, then paid off against export-vs-`alt=media`) |
| Both directions | B03 — get all three habits right and the list comes back complete and the export succeeds (holds); skip `alt=media` vs. export and get a 403 that isn't a helpful error, skip `supportsAllDrives` and get a 404 that looks like the file never existed (flips, two distinct silent failure modes) |
| No design judgment | B03 states the missing-parameter behavior as a documented fact to watch for, never a verdict on whether returning 404 for a missing param was the right call |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (the three-habit rule, the silent-failure behavior) but
  states them as mechanism and a documented boundary, never a judgment on
  the skill's design quality.
- **Not that these three habits are the only rules.** `fields=` scoping
  beyond `nextPageToken`, rate limits (quota units), the `gdrive` helper's
  session-only lifetime, and the export size cap are real parts of the
  skill; the reel picks the three habits that govern every single call as
  the carry-out, not a full reference of every rule.
- **Not that every Drive operation needs the bundled scripts.** Only that
  a hand-rolled request still owes the same three habits, and that the
  shared-drive parameters and the export/download branch are where a
  hand-rolled call most often goes quietly wrong.

## Handoff prompt (BHTF, read aloud)

> "Find all spreadsheets modified in the last 30 days on our shared drive,
> and export the first one as CSV."

Why it's worth running: it forces three checks in one shot — does Claude
pass all three shared-drive parameters on the search, does it request
`nextPageToken` in `fields=` instead of assuming one page is everything,
and does it reach for the export endpoint instead of `alt=media` once it
sees the result is a Google Sheet.

---
**GATE P — signed:** ______________________  (human)
