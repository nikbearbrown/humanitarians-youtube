# FACTCHECK — Suno, Part One.

Every factual claim the narration or the on-screen UI makes, and how it was
verified. DOUBLE-CHECK LAW: nothing on screen may be invented, and the
recreated interface must match the real product (REBUILD LAW — the UI is
rebuilt as native Remotion scenes, never screen-recorded or screenshotted).

Last verified: 2026-08-29.

## Interface claims

| # | Claim (beat) | Status | Note |
|---|---|---|---|
| 1 | Left sidebar contains Home, Explore, Create, Studio, Library, Hooks — then the workspace chip, then Earn Credits, Labs, Notifications, More, and "Upgrade to Premier" (B04) | CORRECTED | Two earlier cuts were wrong. The first showed three items; the second invented **Search** and **Radio** nav items, which do not exist (search lives in the page header, not the sidebar). Now rebuilt from the reference screenshots. |
| 2 | Sign-in offers **Discord or Google** (B03) | VERIFIED | Earlier cut implied Discord-only. Corrected: both exist; Discord is the one that links the org Pro plan. |
| 3 | Create page has **Simple**, **Advanced** and **Sounds** tabs (B05) | CORRECTED | Earlier cut said "two tabs: Simple and Custom". There is no "Custom" tab. The real control is a three-way segment: Simple / Advanced / Sounds, and **Advanced** is where lyrics and structure live. Narration and scene both fixed; B05 audio regenerated. |
| 4 | Simple mode = description box + Instrumental toggle + Create button (B05) | VERIFIED | These are the only three controls needed for a first song. |
| 5 | A generation returns **two** versions (B07, B08) | VERIFIED | Two tracks per generation is standard behaviour. |
| 6 | Song card actions live in a **three-dot (⋯) menu** (B08) | VERIFIED | Menu: Extend · Remix/Edit · Download · Share · Move to Trash. |
| 7 | There is **no "Regenerate" button** on a song card | CORRECTED | An earlier cut of `SunoL1SongCards.tsx` invented a `▶ Play · ⬇ Download · ↺ Regenerate` action row. Removed — that row does not exist in Suno. |
| 8 | Extend adds **+15s / +30s** segments (B08) | VERIFIED | "Get Whole Song" stitches extended segments; out of scope for Part 1. |
| 9 | Library saves every generated track automatically (B04) | VERIFIED | No manual save/export step. |

## Numeric claims

| # | Claim | Status | Note |
|---|---|---|---|
| 10 | Generation takes ~30–60 seconds (B07, BVDT) | VERIFIED | Stated as a range, not a guarantee. |
| 11 | 5 credits per generation (B07, BVDT) | VERIFIED | Covers both returned versions. |
| 12 | Pro plan = 2,500 credits/month ≈ 500 songs (B07, BVDT) | VERIFIED | 2500 / 5 = 500. Arithmetic stated plainly, not as a selling point. |

## Mechanism claims (B02)

| # | Claim | Status | Note |
|---|---|---|---|
| 13 | Suno is a generative model trained on a large music catalogue | VERIFIED | Stated at this level of generality deliberately — no training-set size, no architecture claim, nothing that will date. |
| 14 | It learned patterns linking words to sound | VERIFIED | Descriptive of text-conditioned audio generation. |
| 15 | It predicts audio a segment at a time, each conditioned on the last | VERIFIED | Autoregressive generation, described without jargon. |
| 16 | The same prompt does not return the same song twice | VERIFIED | Sampling is stochastic. This is the honest framing of the non-determinism the viewer will actually observe. |

## Deliberately NOT claimed

- No model version numbers, parameter counts, or training-set sizes — these date fast (DOUBLE-CHECK LAW: strip anything that will date the video).
- No claim about what music the model was trained on, or its licensing status. Out of scope for a how-to, and not verifiable here.
- No claim that output is copyright-clear or commercially usable.
- No promotional framing of the organisation's Pro plan. Access is stated once, mechanically, in B03 as a consequence of signing in with Discord.

## Reference material

On 2026-08-29 the author supplied five screenshots of the live Suno interface at
`lyrical-literacy/youtube/Suno Screenshots/` — `Create.png`, `Library.png`,
`Home.png`, `Explore.png`, `Profile.png`. The Suno recreations are now built
against these directly.

REBUILD LAW is intact: the screenshots are **reference only**. Nothing lifted
from them appears in the video — every surface is a native Remotion scene in
`sunoKit.tsx` and the `SunoL1*` components. No screen recording, no screenshot,
no lifted image is composited into any beat.

Corrections the screenshots forced, beyond claims 1 and 3 above:

| # | Was | Now |
|---|---|---|
| 17 | Lowercase serif "suno" wordmark | `SUNO` — caps, heavy, letterspaced, with the sidebar-collapse control |
| 18 | Purple (`#8B5CF6`) treated as Suno's accent | Suno is near-black with low-chroma greys; the one saturated colour is the **magenta version badge** (`v5.5`) |
| 19 | Bright purple gradient Create button | A **muted dark control** with a music-note glyph |
| 20 | Instrumental rendered as a toggle switch | A **pill**, alongside a "+ Lyrics" pill |
| 21 | Two-column app (sidebar + one content pane) | **Three columns** on Create: sidebar, composer, workspace result list |
| 22 | No transport bar | A **bottom player bar** is present on every page |
| 23 | Waveforms drawn inside library/track rows | Suno's list views show artwork + duration badge + action icons and **no waveform**. Waveforms remain only where this series uses them as its own explanatory device (B01, B02, B08) |
| 24 | Credits shown as a sidebar panel reading "2,500" | A "♪ 2.5k" pill at the top of the Create panel |
| 25 | Missing page furniture | Added: Workspaces breadcrumb, Filters / Newest / List pills, pagination, Library sub-tabs, Suggestions chips, "+ Audio / + Voice / + Inspo" row |

## Corrections log

- 2026-08-29 — Removed the invented "Regenerate" card button (claim 7).
- 2026-08-29 — Sidebar corrected from 3 items to the real 6 (claim 1).
- 2026-08-29 — Sign-in corrected from Discord-only to Discord **or** Google (claim 2).
- 2026-08-29 — Cut all "free forever / no credit card / free Pro access" framing from B03 narration and `SunoL1DiscordLogin.tsx`. It oversold the perk and misrepresented the register: this is internal volunteer training, not promotion.
