# CAPTURE.md — How the Tutor Stays Grounded in Your Textbook

**Status: CAPTURE COMPLETE (2026-09-24). Footage locked.**

## Observed result (what actually happened)

**Wrapper.** `capture/capture_masked.py` was built to the design below and passed its offline self-test, 11/11 checks, with the dummy term `Testname`, before any Medhavy run.

**Runs, all through the wrapper:**

| Run | Settings | Result |
|---|---|---|
| `run-signin` | `--no-session`, 1600×900 @2.4 | Signed out; nothing typed. Feeds B02 in both versions. |
| `run-pilot` | 1600×900 @2.4 | Discovery only; not in the cut. Confirmed the 5.4.2 card; showed the follow-up was off-screen (fixed in the plan). V7 "Thanks!" verified here. |
| `run-book` | 1600×900 @2.4 | Corrected landscape capture, locked. Hub tab → B03; book tab → B04–B12. |
| `run-portrait-test` | 1280×720 @3 | Layout test with no tutor requests. Passed. |
| `run-portrait` | 1280×720 @3 | Portrait-source capture, 2 tutor requests, locked. Feeds vertical B03–B12. |

`run-signin-916src` (optional) was **not** run. Vertical B02 reuses `run-signin`.

**Redaction reviews passed for every run.**
- The hub header reads "Admin account" from its first rendered frame.
- No personal name, email or `CLS-` code is visible.
- No wrapper abort, leak or canary occurred.
- The temporary contact sheets were deleted after review.

**Other outcomes:**
- **Tutor memory:** never cleared. No visible interference from earlier turns in any run.
- **Credentials:** Prarthana signed in herself (`save_session.py`) and set `MW_MASK_TEXT` privately in her own shell for each signed-in run. The agent typed no credentials.

Everything below is the **planned design** as reviewed before capture. It is kept for the record. Where the plan and the result differ, the result above and FACTCHECK.md are authoritative.

## Source

| Item | Value |
|---|---|
| Textbook app | `medhavi-cancer@b8b6c21` |
| Hub | `medhavi-hub@efcc3f5` |
| Hub `build_id` | `b179d0bba0a1bac2b78a5209d305c80ac9cd7359fd6e508512fe0ce1a2f73fc6` (SHA-256 of `git archive HEAD` of `medhavi-hub@efcc3f5`; recorded in `coverage.json`). The live deploy commit isn't verifiable. |
| Sites | `https://hub.medhavy.com` → `https://cancer.medhavy.com` |

If production behaves differently from AI-TUTOR-SOURCE.md, record what actually happened and revise the narration. Never stage the expected behaviour.

## Account: admin (confirmed)

- **Route:** Admin Dashboard → **View All Textbooks** → *Cancer textbook* → **Open Textbook** → book tab → **5. Oncogenes** → **5.1 Introduction to Oncogenes** → **Open AI chat**.
- **No student branch.**
- **Sign-in:** Prarthana signs in herself via `save_session.py` (headed, not recorded). The session file stays outside the reel. The agent types no credentials.

---

## Redaction wrapper: `capture/capture_masked.py` (design; built 2026-09-24, self-test passed)

### Why it is needed (from source)

- **The header name is one word.** The admin header renders `{currentUser.firstName || currentUser.email}` as a single word in a `<span>` inside `<nav>` (`medhavi-hub/components/AdminDashboard.tsx:578-580`).
- **The toolkit's name mask misses it.** It only replaces names of two or more capitalised words, and only inside list, card or row containers (`capture_admin.py:23, 37-40`). It also skips text inside `BUTTON`, `A` and `H1`–`H3`.
- **The toolkit's leak counter doesn't look for names.** It counts only emails and `CLS-` codes (`:46`).
- **The toolkit's observer misses in-place text changes.** It watches `childList` only, so text that React changes in place (`characterData`) goes unmasked until the next per-step walk.

### What the wrapper changes (and what it does not)

- **It does not edit** `brutalist.art`. It imports `skills/make/medhavy-walkthrough/scripts/capture_admin.py` as a module and calls that module's own, unmodified `main()`. The plan format, CLI flags, recording, ffmpeg transcode and output files are all the toolkit's.
- **It keeps all toolkit masking.** It **appends** extra JavaScript to `capture_admin.MASK`, the toolkit's own mask for emails, names and `CLS-` codes. The toolkit already injects that mask as a context init script, which runs in every page and popup (including the textbook tab) before page scripts. It also re-runs it after each `goto` and `open_textbook`, so the appended code rides the same injection points.
- **What the appended JavaScript does, per page:**
  1. **Term mask.** Replaces every whole-word, case-insensitive occurrence of each mask term in every text node on every host with the neutral label `Admin account`. This includes text inside buttons, links and headings, which the toolkit skips.
  2. **Structural header mask.** On the hub, sets the text of the `<span>` directly before the `nav a[href="/admin/analytics"]` link to `Admin account`, whatever it contains. This covers the email fallback and any spelling variant.
  3. **Observer.** Its own `MutationObserver` watches `childList` **and** `characterData` on the whole subtree. It re-masks synchronously in the mutation callback, which runs before the next paint. An in-place React text update therefore can't reach a painted frame unmasked.
  4. **Leak check.** Wraps the toolkit's `window.__mwLeaks()` so it returns *toolkit leaks + term leaks* (see below). The toolkit already calls it after every plan step.
- **The mask terms come only from the environment.** They are read from `MW_MASK_TEXT`, which may be a comma-separated list such as the first name. The source contains no name.
  - The terms are passed into the browser **only** inside the injected script string, which lives in browser memory.
  - They are never printed, logged, put in filenames, or written to `actions.jsonl`, `redaction.jsonl`, screenshots, summaries or error messages.
- **Error messages refer to "mask term 1" etc., never the value.**
- **Refusals (fail closed):**
  - It refuses to run any signed-in plan (no `--no-session`) when `MW_MASK_TEXT` is unset or empty.
  - It refuses terms shorter than 3 characters, which would over-match.

### How the real-name leak check works

**Layer 1: DOM, after every plan step (and continuously).**

- **What is checked, and what isn't:**
  - `document.body.innerText` is checked. That is the rendered, visible text: it excludes `<script>`, `<style>` and `display:none`, which is what reaches a frame.
  - The `value` and `placeholder` of every `input` and `textarea` are also checked.
  - Hidden framework data is deliberately **not** checked, for example the Next.js payload inside `<script>` tags. It is never painted, and it would abort every run.
- **How the check runs:**
  - The term is matched as a whole word, case-insensitive, after masking.
  - Any hit sets a **sticky** per-page flag (`window.__mwTermLeak`) at the moment the observer sees it, not only at step end.
  - `__mwLeaks()` then returns a nonzero count.
- **Where it runs:** the wrapper checks **every open page** in the browser context at each step, not only the active one. That matters because the hub tab keeps recording in the background after the textbook tab opens.

**Layer 2: abort on the first leak (as built 2026-09-24; no Playwright patching).**

- **Active tab:** the extended `window.__mwLeaks()` throws `MW_MASK_TERM_LEAK` when the term is visible. The toolkit's own per-step `evaluate` raises that error in Python, so the run stops at that step. The toolkit's normal leak count is returned unchanged otherwise.
- **Background tab** (the hub tab that keeps recording after the book opens): the toolkit only checks the active tab. So on detection the page blanks itself to solid magenta (#FF00FF) *before paint*. After the run, the wrapper scans every recorded video (4 fps, downscaled) for that canary colour and purges the run if it finds it.
- **Logs:** after a successful run, the wrapper also checks that run's action log and redaction records for the term.

**Layer 3: delete the affected capture.**

On a leak, and also on **any** crash or abort, because a crashed run's video can't be verified, the wrapper deletes:
- `capture/.<run>-raw/` (the raw WebM)
- `capture/<run>*.mp4`
- `capture/<run>-*.png`
- `capture/<run>-actions.jsonl`

It writes nothing to `redaction.jsonl` for that run. It leaves a name-free `capture/<run>-ABORTED.txt` with the step index, the reason, the page host and the leak counts. The toolkit's own end-of-run leak path (delete and exit) stays in place as a second net.

**On a non-leak abort** (for example the provisional card title isn't found), the screenshots from steps that each passed the leak check are **kept** for pilot discovery. The video is still deleted.

**Layer 4: human frame review before any footage is used.**

A DOM check can't see pixels. So for the pilot and every real run:
- Build a frame contact sheet of the hub tab at 1 fps, plus every frame in the first 2 s after each navigation.
- Review it for the name, emails and codes before the footage is accepted.
- Any hit means the run is deleted and the mask fixed. Frames are never blurred afterwards.

**Self-test before any Medhavy run.**

`capture_masked.py --self-test` runs headless Chromium against local `file://` pages, with no network and no Medhavy. The design said `data:`; the build uses `file://`, so it can drive the toolkit's own `main()` end to end. The page contains a synthetic test term in a nav span, a button, and a text node updated in place after 500 ms. The self-test must show all of the following:
- masked → no hit
- an unmaskable injected hit → abort with deletion
- an unset `MW_MASK_TEXT` → refusal

The self-test uses a dummy term (`Testname`), never the real one.

**Keeping the name out of shell history.**

Set the variable without echoing it, and clear it afterwards:
```bash
read -rs MW_MASK_TEXT && export MW_MASK_TEXT
# ... runs ...
unset MW_MASK_TEXT
```

**Known limits (stated, not hidden):**
- Text drawn inside `<canvas>`, images or closed shadow DOM is invisible to both the DOM mask and the check. None of these appear in the hub header markup; Layer 4 covers them.
- The saved session file written by the toolkit's `save_session.py` holds Clerk session data. It lives outside the reel (`~/.medhavy-walkthrough/`) and is never an artifact of this project.

---

## Tutor memory: inspect, never clear automatically

- **No clear is scripted.**
- **Inspect in the pilot:**
  - Does `ai-panel.png` show prior messages?
  - Does the first answer refer to things that weren't asked?
- **Foreseeable issue.** The hub keeps the latest tutor turns for this account, and the model receives them as recent conversation context. Each run sends real questions, so:
  - the **pilot's** turns will be in context for the **real landscape run**
  - the landscape turns will be in context for the **portrait run**
- **Watch for:** an answer saying something like "as I explained before", or a follow-up anchoring to the wrong turn.
- **If that materially interferes,** I stop and explain exactly what **Clear** deletes, then wait for Prarthana's decision. She performs any clear herself. A clear:
  - removes this book's panel history from the browser
  - deletes **all** stored tutor turns for this account's memory key on the hub, possibly including other Medhavy books
  - is permanent
  - leaves the learner-style profile in place

---

## Landscape capture order (planned; executed as listed, see "Observed result")

1. **`save_session.py`.** Prarthana signs in manually. This browser is not recorded.
2. **`run-signin`**, `plan-signin.json`, `--no-session`, through the wrapper. Signed out; no mask term needed. Feeds B02.
3. **`--self-test`** of the wrapper (local only, dummy term).
4. **Masked landscape pilot `run-pilot`**, `plan-book.json`, `MW_MASK_TEXT` set. Discovery only; not in the cut.
5. **Review redaction:** ABORTED file absent, `redaction.jsonl` all zeros, header screenshot, frame contact sheet (Layer 4).
6. **Review live tutor behaviour:** memory state (M1) and V1–V10.
7. **Resolve:**
   - the real card title for steps 19 and 22
   - whether steps 17–18 stay
   - which conditional beats and lines survive
   - any memory-clear recommendation, which stops for Prarthana's decision
8. **Corrected landscape capture `run-book`,** through the wrapper. Repeat the redaction review.
9. **Stop for review.** Fill in timings, promote or delete conditional lines, and update FACTCHECK statuses.

## Portrait-source test (planned; run 2026-09-24 and PASSED)

**Plan:** `capture/plan-portrait-test.json`, run through the wrapper with `--css-size 1280x720 --dpr 3` (1280×3 = 3840, 720×3 = 2160). The plan navigates the same route and opens the tutor panel. It **types nothing into the tutor**. It takes these stills:

| Still | Shows |
|---|---|
| `shelf` | Hub at 1280 wide; header masked |
| `book-home` | Book tab layout |
| `chapter` | 5.1 page: sidebar, content, whether "On this page" shows |
| `ai-panel` | Panel open: header, **Clear** and **Close panel**, chips, empty message area, input, send button, footer |
| `panel-closed-toc` | Panel closed on 5.1. Is the "On this page" list visible? The landscape plan needs it for step 22's section link. |

**Pass criteria** (each must hold, checked on the stills and the short test video):

- The page is in the normal desktop layout: sidebar visible, content column readable, no mobile menu takeover, no horizontal scroll.
- The tutor panel opens at its usual width (420 CSS px initial) as a right-hand column, not full-screen or overlapping. Every control is visible and unclipped: title, **Clear**, **Close panel**, chips, input, send, footer.
- The message area has room for a card row. Cards are fixed at 180×110 CSS, so they need about 420 CSS of width, which is unchanged from landscape.
- The footer warning is fully visible at the bottom.
- With the panel closed, the section link for step 22 is reachable. If "On this page" is hidden at 1280, plan a `scroll` to the section heading instead, measured on the still.
- Redaction: same review as landscape (Layer 4).

**If any criterion fails:** stop and report with the stills. Send no tutor requests.

## Portrait capture order (planned; `run-portrait` executed, `run-signin-916src` skipped)

1. **`run-signin-916src`** (optional, no tutor use; **not run**): `plan-signin.json`, `--no-session`, at 1280×720 DPR 3. Gives a portrait-friendly sign-in card for vertical B02.
2. **`run-portrait`:** `plan-portrait.json` through the wrapper at 1280×720 DPR 3. Same route, **Q1 and Q2 only**. That is **2 tutor requests**, because "Thanks!" was already verified in landscape. The card title in steps 18 and 21 is the one confirmed in the landscape run.
3. **Review:**
   - Redaction (Layer 4).
   - Memory interference from the landscape turns (see above).
   - Whether each behaviour the landscape narration relies on (V1, V2, V3, V4, V6 as promoted) **also appears in this take**. The vertical narration may only claim what its own footage shows. If the portrait take differs, the vertical line follows the portrait footage, or the claim is dropped from the vertical.
4. Build the separate vertical beat sheet from this capture (SHOTLIST.md "Vertical strategy"). **Stop for review.**

---

## Verification map

| ID | Check | Evidence | Beat |
|---|---|---|---|
| R1 | Name, emails, names, codes masked | ABORTED absent, `redaction.jsonl`, contact sheet | all hub footage |
| M1 | Prior tutor history / interference | `ai-panel.png`, answer content | gate |
| V1 | Cards before answer text | `sources-arrive.png` + footage | B06 |
| V2 | "Dive deeper (N)" | `answer-1.png`, `all-sources.png` | B08 |
| V3 | Card opens its section; titles match | `source-page.png`, `source-section.png` | B09 |
| V4 | Card from another page or chapter | Card vs. 5.1 | B09 |
| V5 | Off-topic card | Screenshots | only if seen |
| V6 | Follow-up cards and context | `answer-2.png` + footage | B11 |
| V7 | "Thanks!" shows no cards | `thanks.png` (landscape only) | not in cut |
| V8 | No "Most Relevant" badge, no auto-switch | Book footage | not narrated unless contradicted |
| V9 | Footer legible | `ai-panel.png`, `footer.png` | B05, B12 |
| V10 | Chips contain the page title | `ai-panel.png` | B05 |
| P1 | Portrait layout test passes | `run-portrait-test-*.png` | gate for `run-portrait` |

## Method and limits

- **Method:** `scripted-browser`, headless Chromium, 30 fps, native 3840×2160 in both passes (1600×900 at DPR 2.4 for landscape; 1280×720 at DPR 3 for the portrait source). Real clicks only. No API calls, no cookie edits, and no DOM changes beyond the disclosed text masks.
- **Server-side behaviour:** retrieval, prompt assembly and memory are evidenced from code, not from the screen.
- **Not visible:** production configuration.
