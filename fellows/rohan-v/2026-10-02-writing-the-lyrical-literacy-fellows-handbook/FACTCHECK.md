# FACTCHECK — Writing the Lyrical Literacy Fellows Handbook

Every spoken and on-screen claim, where it comes from, and its verdict. Checked 2026-10-05
against the handbook file itself (`LL_Fellows_Handbook_v1.0.docx` / `.pdf`, 30 Sep 2026; the
file is not committed because it holds shared account details: its crops' page numbers and
hashes are in `pantry/handbook/crops.json`) and this session's record.

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md`, required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Until now, getting started meant asking around | Rohan V., week-02 progress reel B03 ("tribal knowledge: you find out by asking someone"); the week-05 reel B01 | ✅ his own earlier statements |
| 4 | B01 | 46 pages in 12 sections | the v1.0 PDF exported by Word: 46 pages; sections 1–12 in its contents | ✅ counted |
| 5 | B01 | Claude drafted it from the program's own pages and our nine tutorials; I reviewed and corrected it | sources used in the session: humanitarians.ai/fellows and /lyrical-literacy, the fellows README and FELLOWS-SUBMISSION, HR's renewal email, the nine Suno/Midjourney tutorial scripts; Rohan's corrections (palette, three Word comments, contact and access answers) | ✅ — the credit line on screen says the same |
| 6 | B01 | Covers every tool, Suno and Midjourney guides, weekly reporting, the video workflow, renewals; opens with a first-week checklist | handbook Sections 1.2, 4, 5, 6, 7, 8, 9 | ✅ — each shown as a crop of the real page |
| 7 | B02 | Discord first, because Suno and Midjourney both sign in through it; then Canva and Adobe | handbook 4.1–4.5 | ✅ |
| 8 | B02 | A month ago this chain lived in people's heads | week-02 reel (4 Sep): "Right now that path is tribal knowledge" | ✅ |
| 9 | B03 | The first draft used a navy and cream palette and was rebuilt to match the website | session 2026-09-29: first build on the Brand Reference PDF palette (Gunmetal / Dutch White); Rohan: "i dont like the navy and cream. not prefessional. follow the website colors and font"; rebuilt in Inter, white, #7A0000 | ✅ |
| 10 | B03 | My review comments in Word removed a step and handed the hours and logs to Claude | the three Word comments (2026-09-30): no "NEU-only" line; "Nobody has to send their username to the PM"; "Claude should do this for them" (hours and Frictional log) | ✅ — on screen the third comment's NEU line is not listed, to keep five rows |
| 11 | B03 | When the program's rules changed, the handbook changed: build files on GitHub; every video to one reviewer | fellows README rule of 2026-09-18 (build inputs on GitHub, renders on Drive), folded into the handbook 2026-09-29; Rohan, 2026-09-29: "all videos should go to sanjana … until further confirmation" | ✅ — the reviewer is not named, per the no-third-party-names instruction |
| 12 | B04 | One place, editable Word file with a version history | handbook Document control: version table + update steps; delivered as .docx at Rohan's request | ✅ |
| 13 | B04 | Shared privately with the team (on screen) | shared through Rohan's Northeastern SharePoint link, not the public repository | ✅ |
| 14 | B04 | It hasn't met a new fellow yet | no new fellow has used it as of 2026-10-05 | ✅ stated as pending |
| 15 | B05 | It closes the first item on my renewal plan, which has been approved | RENEWAL.md plan item 1, "LL onboarding documentation (5–30 Oct)"; approval reported by Rohan, 2026-10-05 | ✅ |
| 16 | B05 | Almost a month ahead of the 30 October target | v1.0 dated 30 Sep 2026 | ✅ |
| 17 | B05 | Next: test two more tools on the same footage in November, then a pipeline by mid-December | RENEWAL.md plan item 2: OpenReel + DaVinci Resolve MCP 2–20 Nov; pipeline 23 Nov – 11 Dec | ✅ |
| 18 | B06 | Team meeting on Wednesdays at 12, Eastern | Rohan, 2026-09-30/10-01: "weekly meeting … at 12pm et which is subject to change … its every wednesday" | ✅ |

## Excluded on purpose

- Every handbook page with personal contact details (Section 3, Document control) and the
  page with the shared login (Section 4.1). The six crops shown are listed in `crops.json`.
- Names of anyone other than the presenter (standing instruction): the reviewer, the
  supervisor and the program's founder are referred to by role only.
- The SharePoint link to the handbook, which is for the team only.

## Portrait (9:16) wording

Shortened on-screen strings in `vertical/beat_sheet.json` (`vertical_strings.py`); narration is
identical in both cuts. Each was checked against the rows above: "website look" (9), "step
removed" / "Claude keeps them" (10), "inputs on GitHub" / "one reviewer" (11), "not used by a new
fellow" (14), "a month early" (16), "Test 2 editors" (17), "Wednesdays, 12 pm ET" (18).
