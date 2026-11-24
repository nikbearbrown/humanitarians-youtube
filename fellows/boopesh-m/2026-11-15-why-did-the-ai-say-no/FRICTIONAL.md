# FRICTIONAL — Why Did the AI Say No?

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-15
- **Tried:** read CFPB Circular 2022-03 and Regulation B on consumerfinance.gov, ecfr.gov, govinfo.gov, the
  Federal Register, Cornell LII and an NCLC copy. **Found:** every host blocked from the build container (proxy 403 /
  host not allowed). **Did:** read Regulation B § 1002.9 verbatim from a pinned GitHub mirror of the govinfo eCFR bulk
  XML (amendment date Sept. 14, 2026), and took the circular's content and dates from search-result summaries only,
  marked ⚠️ in FACTCHECK.md. No sentence of the circular is quoted.
- **Resisted (the circular is no longer in force):** search results say Circular 2022-03 was one of 67 guidance
  documents the CFPB withdrew on May 12, 2025 (90 FR 20084). The brief anchored on it as current guidance. The film
  says so plainly: issued in 2022, withdrawn in 2025, while Regulation B's own wording (specific, principal reasons;
  "failed a score" is not enough) is still in the regulation text. ⚠️ the withdrawal is from search summaries too.
- **Resisted (honesty about tuning):** Applicant A is hand-written, chosen so that both models deny and one plain
  change flips both. With the first cutoff (deny at 20 % risk) the smallest single change was a $5,950 card pay-down
  (to 12.5 % use); I moved the illustrative cutoff to 30 % (denial rate 17 % / 16 % of test applicants), which gives
  $3,850. Both are design choices, not findings; the cutoff is labelled "my choice" on screen.
- **Resisted (what the black box actually said):** I expected the two models to agree. They share only 2 of 3
  reasons, and the boosted model barely uses debt-to-income for A (+0.20 vs +0.82 in the scorecard), even though the
  true rule has a kink above 40 %. Its list also moves: against approved applicants only, or after retraining on
  another 70 % split, debt-to-income comes back into the top 3. Shown in B60 as "the list can shift".
- **Resisted (not shown):** the cheapest debt-to-income change differs wildly: the scorecard needs DTI 44 → 31 %
  (≈ $563/month less in payments), the boosted model only 44 → 42.5 % (≈ $65/month) — a step it learned. Logged in
  FACTCHECK.md; left out of the film to keep one idea.
- **Resisted:** first narration measured 2:41 (over the 2:40 target). Cut the circular's number from the spoken line
  ("two thousand twenty-two dash zero three" in Kokoro's reading), shortened B30/B40/B60/B80: 2:27.
- **Resisted:** first layouts had marker labels crossing the cutoff line and each other (B40, B70), a caption under
  the dark card (B50), tiny "list can shift" text (B60) and the Short's B20 title under the first card; fixed by
  looking at preview frames.
- **AI contribution:** Claude wrote the experiment, script, sheets and scenes. Kokoro `am_onyx` speaks the narration.
- **Still open:** read the circular and the withdrawal notice on consumerfinance.gov when reachable; check whether the
  CFPB has issued anything new on AI adverse-action reasons since May 2025; a human listen for "Shapley" and "CFPB".

---

## 2026-11-24 — Submission note for the week of Nov 8–14 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Nov 8–14. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
