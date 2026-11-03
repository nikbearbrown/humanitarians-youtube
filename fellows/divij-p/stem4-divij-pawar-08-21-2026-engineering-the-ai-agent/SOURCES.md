# SOURCES.md — engineering-the-ai-agent

Primary source: `04_engineering_the_ai_agent.md` (the script supplied by the
user) and `04_narration_tts_ready.txt` (the TTS-normalized narration).

**This is the third authoring pass.** The first pass wrote a case-study
walkthrough from the user's script as given. The second pass added
generalizable frameworks. **This third pass verified the case study against
the actual live repository** — `https://github.com/coding-parrot/pothole-reporter`
— fetched directly (README.md, docs/sources.html, docs/privacy.html,
docs/DEMO.md, docs/architecture.png, docs/example-pothole.jpg) on
2026-08-24. Several numbers and mechanisms in the original user-supplied
script turned out to be inaccurate or unverifiable against the real project;
they are corrected below, not just flagged.

## Corrections made this pass (previously unverified, now checked)

| Claim in the earlier draft | Real project (verified) | Beat(s) affected |
|---|---|---|
| Scope implied Bengaluru specifically ("jurisdictional boundaries of Bengaluru") | The app covers National Highways nationwide, plus full-state coverage in Maharashtra and West Bengal, Delhi NCT, Karnataka (partial — 182 of 319 urban local bodies), Tamil Nadu (Chennai only), Telangana (Hyderabad only), and Gujarat (Ahmedabad only). Bengaluru is one of many, not the setting | B03 |
| "Thousands of accidents a year" (India-wide pothole stat) | **Removed.** Not stated anywhere in the project's own README, sources page, or privacy page. Unverifiable against the actual project; dropped rather than carried as fact | B03 |
| Camera fires "every 8 meters of GPS delta" | **Removed — could not verify.** The project's own docs describe Drive mode as a continuous background scan via an Android foreground service; the public JS bundle (`docs/standalone.js`) shows a **4-second** same-drive dedupe window for repeat sightings, not a distance-gated trigger. No distance-based capture interval is documented anywhere found. Replaced with "continuous background scan" + the real dedupe behavior | B05 |
| Confidence shown as a percentage ("pothole · 92%") | **Corrected.** `docs/DEMO.md` states explicitly: "The current UI reports subtype plus clear/probable/uncertain/absent and does not display an uncalibrated model percentage." Replaced with the real 4-way categorical language throughout (B03, B04, B05) | B03, B04, B05 |
| "GIS + 42,000 contracts", queried for every report | **Corrected with real numbers.** Contract matching is **Karnataka-only** — explicitly disabled for Maharashtra, West Bengal, and Delhi ("the app has no authoritative, road-linked award and defect-liability feed for those routes," `docs/sources.html`). The real funnel: a full source snapshot of **42,283** road-related awarded works from Karnataka's KPPP → **13,577** indexed to a supported municipal body in the downloadable pack → a deterministic ranking shortlists **≤25** candidates → an OpenAI model may pick **1** above a confidence threshold. Of the 13,577-row pack, **12,456 have no known contractor name** (only 1,121 do) — "most tender-pack rows have no bidder name, and the app must not invent one" | B06 |
| "Winning bidder / commissioner" framing implied a named person is always found | Corrected — most matches have no contractor name on file; the app leaves it blank | B06 |
| Guardrails framed as three separate, unrelated tricks | Reframed around the project's own real, unifying principle: **fail closed**, applied consistently — checksum-verified data packs, weak-GPS/ambiguous-boundary refusal, and (for highways) handing off to the official channel rather than guessing the authority, all documented in `docs/sources.html` and `docs/README.md` | B07 |
| "The prompt forces words like 'probable contract'" (implied it's about the LLM's phrasing choice) | Corrected to the real mechanism: the "possibly within warranty" language is a **deterministic date-based rule** — tender published ≤1 year ago → "possibly within a defect-liability period," ≤3 years → "possibly within maintenance." "The award-search row contains no actual warranty term. This is an inference and must never be presented as a contractual fact" (`docs/sources.html`) | B07 |
| "A person reviews it and presses send" (implied a UI nudge) | Strengthened to the real, architectural guarantee: "Pothole Reporter prepares evidence but does not log in, bypass OTP, call a complaint-write API, press Send, or read complaint status" (`docs/sources.html`). There is no code path that could auto-send even if a reviewer skipped the check | B07 |
| National highway handling described as "the workflow terminates" | Corrected — it doesn't just halt. It refuses to guess the maintaining authority itself and hands off to the official Rajmargyatra/1033 channel, asking that service to identify NHAI/NHIDCL/BRO/State PWD. Uses 101 checksum-pinned map tiles covering 680 NH/NE references from a pinned OSM extract, and fails closed (refuses rather than guesses) on weak GPS, conflicting direction, nearby different highway references, missing tiles, or altered data | B07 |

## Factual claims from the source script, re-verified (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B01 | Traditional imperative software requires explicit branching for each case; agentic design isolates the unstructured part and hands it to a model | ✓ | Standard, uncontroversial framing |
| B03 | An open-source Android app named "Pothole Reporter" (repo `coding-parrot/pothole-reporter`) exists and does what's described | ✓ **verified** | Fetched live from GitHub, 2026-08-24: README.md, docs/sources.html, docs/privacy.html, docs/DEMO.md |
| B03 | Only pothole reports use AI; garbage and manhole reports are explicit, unassisted user reports | ✓ **verified** | README.md: "Pothole photos use AI; the other two are explicit user reports and are not sent to OpenAI" |
| B04 | A vision-language model can do perception/classification without hardcoded rules, but has no jurisdictional/local context on its own | ✓ | Accurate, general property of vision models |
| B04/B07 | Guessing an authority from a photo alone risks naming the wrong office | ✓ **verified** | `docs/DEMO.md`: "Not that it produces a ticket number... Not that the contract match is certain" — the project's own design explicitly avoids this failure mode |
| B05 | GPS coordinates can be reverse-geocoded to a street address via OpenStreetMap | ✓ **verified** | `docs/DEMO.md`: "OpenStreetMap Nominatim for the street address" |
| B05 | The app dedupes nearby repeat sightings within a drive | ✓ **verified** | README.md: "Nearby repeat observations are grouped into one report; Debug mode retains each one." `docs/standalone.js` shows a 4-second same-drive dedupe constant |
| B06 | Contract matching (Karnataka only), the 42,283 → 13,577 → ≤25 → 1 funnel, and the missing-bidder-name majority | ✓ **verified** | `docs/sources.html`, exact figures quoted directly |
| B07 | Checksum-verified downloaded data, failing closed on missing/altered data | ✓ **verified** | README.md: "Every downloaded pack is checked byte-for-byte against a checksum pinned in the app before it is used... Missing, malformed, or altered required routing, contact, or highway data makes authority routing fail closed" |
| B07 | National Highway routing runs before municipal routing and fails closed on weak GPS/conflicting data | ✓ **verified** | README.md, "National Highway routing" section, quoted directly |
| B07 | Defect-liability/maintenance language is inferred only from tender publication date, never an actual warranty term | ✓ **verified** | `docs/sources.html`, quoted directly |
| B07 | The app cannot submit a complaint itself — no login, no complaint-write API, no auto-send | ✓ **verified** | `docs/sources.html`, quoted directly |

## Editorial additions — general frameworks (second authoring pass, unaffected by this verification pass)

These remain original synthesis, not claims about Pothole Reporter specifically, and were unaffected by the repo verification: the truth-table test (B01), the pipeline-vs-agent-loop framework (B02), the three-question guardrail-derivation method (B07's framing), and the anti-pattern beat (B08). See the second-pass notes retained below.

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B01 | "Can you write a truth table for this decision?" is a workable test for whether a task belongs in deterministic code vs. a model | ✓ **sound heuristic** | Generalizable operationalization of "isolate the unstructured piece" |
| B02 | Two broad orchestration patterns exist in practice: an autonomous agent loop vs. a fixed deterministic pipeline | ✓ | Maps onto the real, widely-discussed ReAct-style vs. hand-orchestrated distinction |
| B02 | Fixed pipelines are generally preferred where consequences are real | ⚠ **judgment** | Reasonable, widely-held engineering opinion; consistent with Pothole Reporter's own architecture (confirmed this pass — it is in fact a fixed, staged pipeline, not an autonomous loop) |
| B07 | Guardrails can be systematically derived from three questions (stale? irreversible? refuse?) | ✓ **sound method, now demonstrated by a verified real system** | Confirmed this pass: Pothole Reporter's real mechanisms map cleanly onto exactly these three questions, converging on one answer (fail closed) |
| B08 | Skipping human review because a model is "usually right" is a common, real failure mode | ✓ | Consistent with widely-reported automation-bias incidents; stated generally |
| B08 | "The one case in a hundred" is illustrative, not a measured error rate | ✓ **declared as illustrative** | Reinforced this pass: the real project explicitly states "No field-validated accuracy percentage is claimed" (README.md, "Important limits") — the video's own refusal to invent a number matches the project's own stated position |

## Real assets used (with attribution)

- **`assets/example-pothole.jpg`** — the project's own documentation photo (`docs/example-pothole.jpg` in the repo), used in B03. Repo is MIT-licensed; this is a genuine archival photo from the actual project being covered, not a generic stand-in, so it is a legitimate nopunt HOLD rather than a PUNT costume. Attribution recorded here rather than burned into the frame; add an on-screen credit if the human reviewer wants one.
- **`docs/architecture.png`** (viewed, not embedded) — the project's own hand-drawn pipeline diagram: Photo → Pothole? → Whose road? → Complaint → Send, with a "the phone does this" vs. "it asks the network for this" legend. Not embedded directly (its Excalidraw hand-drawn style and blue/tan palette don't match this series' Claude fidelity palette), but it independently confirms the pipeline-stage framing used in B05/B06 is the project's own mental model, not an invented structure.
- **`docs/sources.html`, `docs/DEMO.md`, README.md** — quoted directly for the factual corrections above. Not reproduced at length; only short phrases quoted where the exact wording matters (e.g., "probable record match, kindly verify" — `docs/DEMO.md` explicitly says this wording should stay, so B06's email draft uses it).

## Anti-staleness check (DOUBLE-CHECK LAW)

No model name, vendor, version number, or benchmark appears in the
narration (the real project does use OpenAI's vision API specifically, per
its own docs — kept generic here as "a vision model" to preserve this
reel's existing no-vendor-names design choice, consistent with the rest of
the STEM series). The specific numbers now cited (42,283 / 13,577 / 25 /
1,121 / 4-second dedupe) are pinned to a specific fetch date (2026-08-24) —
if this reel is rebuilt much later, these should be re-verified, since the
project's own docs describe versioned, dated data packs that could change.

## Simplifications (declared)

- **The case study is treated as representative, not as the only correct
  design.** Other valid agentic pipelines exist.
- **B08's "one case in a hundred" and its 96-dot visual remain illustrative
  framing, not a measured statistic** — now additionally supported by the
  real project's own explicit refusal to claim an accuracy percentage.
- **The pipeline-vs-agent-loop framework (B02) simplifies a spectrum into a
  binary**, as declared in the second pass; unaffected by this verification.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| Intro + Act 1 + Act 2 + Act 3 + Conclusion narration | **All carried**, condensed, expanded, and now fact-corrected | See the corrections table above for what changed and why |
| `[Visual]` dashcam video/photo of a real pothole (Intro) | **Replaced with the real project photo** | Previously rebuilt as a drawn abstraction (a legitimate but generic PUNT-avoidance); now uses the actual project's own real documentation photo instead, which is a stronger nopunt HOLD |
| `[Visual]` phone mounted on a dashboard, "every 8 meters" timer (Act 2, step 1) | **Rebuilt as a drawn diagram, corrected** | The specific 8-meter claim is dropped as unverifiable; rebuilt at B05 as a continuous-scan diagram matching the real documented behavior |
| `[Visual]` "AI Thought Bubble" over the vision model (Act 1) | Rebuilt without a literal bubble (unchanged from second pass) | B04 |
| `[Visual]` red stop sign / shield icon (Act 3 title card) | Rebuilt as behavior, corrected this pass | B07's fork now shows "hands off," not "terminate" — matching the real, more precise behavior |

## Scene / beat map

| Beat | Scene / pattern | Notes |
|------|------------------|-------|
| B00 | ClaudeComposerAsk (Remotion) | Cold open — self-intro + topic |
| B01 | B01_TwoWaysToWriteCode (Manim) | Framework 1 — if/else tangle vs. hub-and-spoke, plus the truth-table test |
| B02 | B02_OrchestrationPatterns (Manim) | Framework 2 — agent loop vs. fixed pipeline |
| B03 | B03_ThePotholeCase (Manim) | Worked example intro — **real project photo**, real categorical confidence language |
| B04 | B04_TheContextGap (Manim) | Perception isolated + blast radius named, then the context gap |
| B05 | B05_PipelinePerceptionTool (Manim) | Real continuous-scan + dedupe behavior, then reverse-geocoding |
| B06 | B06_PipelineGroundingAction (Manim) | Real Karnataka-only contract funnel, then the real never-auto-sends guarantee |
| B07 | B07_TheGuardrails (Manim) | Real fail-closed mechanisms: checksum verification, highway hand-off, date-based hedging, architectural non-send |
| B08 | B08_TheAntiPattern (Manim) | Falsifiability/stress-test beat |
| B09 | ClaudeVerdictArtifact (Remotion) | Verdict |
| B10 | ClaudeComposerAsk (Remotion) | Your Turn |
| B11 | ClaudeTitleOutro (Remotion) | Outro |

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no
paid services. No publishing — the master stays in this folder. The GitHub
API/raw-content fetches used for this verification pass are free, read-only,
and unauthenticated.
