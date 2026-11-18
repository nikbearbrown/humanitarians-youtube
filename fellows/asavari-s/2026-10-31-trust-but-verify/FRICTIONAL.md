# Frictional log — Trust, but Verify

_Reconstructed on 2026-11-03 from this folder's build record (git history, `beat_sheet.json` build stamps), the Mycroft commits, and the working session with Claude. It was not written while the work happened. Append new entries below; never rewrite these._

- **Renders:** `trust-but-verify.mp4` (16:9, 2:03) and `short/trust-but-verify-short.mp4` (9:16, 2:08). Not committed; to be uploaded to the Google Drive folder https://drive.google.com/drive/folders/1uIFUKAMFJr0JWP6Fy_bIu_0sWwkZ2FGE.
- **Evidence in this folder:** `beat_sheet.json` (the only source), `README.md`.
- **Commit for this folder:** [25a110c added 2026-11-02](https://github.com/nikbearbrown/humanitarians-youtube/commit/25a110cec148dd37d990f07d2e4f7c7498b376c8)
- **Code this video explains:** [be2ee7e the three fixes + 10-company golden set, 2026-10-31](https://github.com/nikbearbrown/mycroft/commit/be2ee7e515d51a4bc800241543f395a6d2e3ce55) · [Mycroft PR #13](https://github.com/nikbearbrown/mycroft/pull/13)

## 2026-10-31 — proof-of-work video for the renewal, 16:9 + 9:16

**What was tried and expected.** A video showing how expanding the SEC agent's accuracy benchmark from 2 companies to 10 caught three real extraction bugs. The render was clean: 8 beats, 0 failures. The friction was in the work behind it.

**Where it resisted, and what was done next.**
- Filling the larger golden set. Claude wouldn't invent expected values or copy them from the tool's own output, because then the test would just be checking itself. Asavari chose to fill them from an independent read of the raw EDGAR data instead of hand-checking every 10-K. Each row is marked "spot-check vs 10-K".
- SEC blocked requests sent with a generic user agent. With Asavari's OK, the fetch used the contact user agent the project already sends.
- The benchmark first came back 38 of 41 found. Three filers (Johnson & Johnson, Caterpillar, NVIDIA) had moved a figure to a different XBRL tag across years, and the agent stayed on the old tag.
- The first fix left Johnson & Johnson's equity still missing. A second look showed the year-end balance appeared under the higher-priority tag only as quarterly comparatives, while the annual figure sat under the other tag. Resolution now keys on the fiscal period as well as the dates.
- "XOM" resolved to a post-reorganization shell company with no filings; a curated override now points it at Exxon Mobil Corporation. Some filers report no single total-liabilities tag; it's now rebuilt from current plus non-current liabilities, never from assets minus equity (that would make the balance-sheet check pass by definition).
- After the fixes: 46 of 46 scored values match within 0.5% across 10 companies, all exactly.

**What Claude contributed, and what Asavari decided.**
- Claude: diagnosed the bugs, wrote the fixes, ran the benchmark; and, asked for a new video as proof, picked this topic without offering alternatives, then wrote the beat sheet and rendered it.
- Asavari: chose the raw-EDGAR cross-check as the verification method; asked for all three fixes; reviewed and committed the code.

## What is understood, and what is still open

- The narration simplifies in three places:
  - "One company had changed its XBRL tag" — three filers had this problem.
  - "I fixed each one" — Walmart's total liabilities is still unresolved (no component tag to rebuild it from) and is reported as UNKNOWN.
  - "46 of 46" counts scored rows; two rows (Walmart and Verizon total liabilities) aren't in the golden set.
  
  Correct these if the video is re-cut.
- The golden values come from raw EDGAR XBRL, not hand-audited 10-Ks. 5 of the 13 base metrics are benchmarked.
- No YouTube link yet; publishing waits on approval.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
