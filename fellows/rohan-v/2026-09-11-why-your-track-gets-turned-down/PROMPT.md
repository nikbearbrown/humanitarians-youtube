# PROMPT — "Why Your Track Gets Turned Down"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-09-10 — first the topic choice:

> Lets go with the loudness and lufs but keep in mind that a lot of people are
> not audio professionals. so they might not understand what a master or a
> squeezed mix is so keep that in mind

and the standing weekly brief:

> do one video for this and then one stem topic. keep it in audio. I want the
> best animations and visuals and everything should be of the best quality. aim
> for a total length of 2 mins for each video. Follow the same framework as
> last week. dont skip any steps.

| # | Constraint | How it was resolved |
|---|---|---|
| 1 | Audio topic | Loudness normalisation — the sibling of the week-02 MP3 reel: that one was inside the file, this is after the upload. |
| 2 | **Audience is not audio professionals** | No "master", "mix", "dynamics", "compression", "limiter" or "headroom" anywhere. The two measurements are "the tallest point" and "how loud it actually sounds"; the thing you lose is "the gap". Full table in PEDAGOGY.md. |
| 3 | ~2:00 total | 121.54s. First pass was 2:26 and was trimmed beat by beat rather than by dropping an act. |
| 4 | 16:9 and 9:16, both 4K | 3840×2160 landscape; 2160×3840 re-rendered natively via THE ONDA CHECK, never cropped. |
| 5 | Best visuals and animation quality | Four purpose-built components plus two new HAI-channel cards, each with one designed event. |
| 6 | Same framework, no steps skipped | Experiment → library-first search → beat sheet → audio → 4K landscape → Gate V → native portrait → 12 docs + both QC sheets → GitHub → `./art drive`. |

## Constraints inherited from earlier feedback

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | Identical start/end screens across videos | `ClaudeComposerAsk` opener; HAI end card |
| Week-01 review | Mention Humanitarians AI in intro and outro | B00 opens with it, B06 closes with it |
| Week-02 review | Name phonetic in narration only | `Row-Haan VeeJayKooMaar` |
| Week-02 review | 9:16 native re-render, never a letterbox | five new `916` siblings |
| Week-02 build | Round, don't truncate, when formatting numbers | no truncation anywhere; all figures carry one decimal as measured |
| Week-02 build | Array props must be in `defaultProps`, not just the zod schema | every array prop registered in `Root.tsx` |
| Toolkit doctrine | Library-first | four searches, four genuine misses, all recorded |

## What the factcheck changed

Running FACTCHECK as a real gate rather than a write-up caught two narration
problems before the reel was finished:

- "half a decibel apart" — measured 0.8 dB → **"under a decibel apart"**
- "sounds nearly nine times louder" — an 8.7 LU difference on a logarithmic
  scale is not a ninefold ratio → **"sits nearly nine points higher on the
  loudness scale"**

The second was a real error, not a rounding. B01's audio was regenerated.

## What Gate V changed

The visual gate blocked the final cut twice, both times correctly:

- **B04 low-contrast** (0.25 against a 0.30 floor) — the measurement spans were
  drawn at 0.16 opacity. Raised to 0.38 with heavier caps.
- **B05 underfill** (21% of safe area against a 55% floor) — the library's
  `ClaudeWindow` artifact card is too sparse for a final. Replaced with a
  purpose-built `HaiApplyCard`.

Neither would have been caught by checking dimensions or duration.

## What "2 minutes" bought

Seven beats: opener, a claim, its mechanism, the catch, the cost, the advice,
and the sign-off. The loudness-war history got cut to make room for B04, which
was the right trade — the history is interesting, the permanence is actionable.
