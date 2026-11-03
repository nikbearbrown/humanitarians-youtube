# BUILD-LOG — The Reversal Curse

Reel: `claude-stem-reversal-curse` · Series: STEM & AI Architecture, Week 2
Skill: `ai-explainer` (claude-explainer) · Voice: Onkar, Kokoro `am_onyx` (free)
Built: 2026-09-13

---

## Environment

Toolkit installed and smoke-passing. Every shell needs this preamble — Git Bash does
not inherit the post-install PATH, and the scripts print Unicode that Windows' cp1252
console cannot encode:

```bash
export PATH="/c/Users/Tapan/AppData/Local/Programs/Python/Python312:/c/Users/Tapan/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/Tapan/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.1-full_build/bin:$PATH"
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Five Windows/ffmpeg fixes to the toolkit itself were made during the previous reel
(slug regex, ffmpeg filtergraph path escaping, title-safe review overlays, `npx`
resolution via `shutil.which`, channel registration). They are documented in
`../claude-hai-gatekeeper-ground-truth/BUILD-LOG.md` and are load-bearing for this
build too. The repo is **not under git** — no version-control safety net for any of it.

---

## Decisions

### D1 — Channel `claude-stem`

GATE L (`beat_lint.py` rule 7) enforces a fixed per-channel kicker from
`runtime/qc/brand_labels.json`. This is a third distinct series on the same org
channel, so it got its own entry:

```json
"claude-stem": { "kicker": "STEM & AI Architecture", "chip": "@HumanitariansAI" }
```

Existing siblings: `claude-hai` (*Irreducibly Human*) and `claude-gatekeeper`
(*Provenance Gatekeeper*). Chip is `@HumanitariansAI` for all three.

### D2 — The red→green arrow flip is carried by FORM, not colour

The script's Scene 4 asks for a one-way **red** arrow snapping into a two-way **green**
arrow. Not built that way, for two independent reasons:

1. A claude-explainer is a FIDELITY brand (`CLAUDE-BRAND.md` forbids retinting) with
   exactly ONE accent. A green arrow is a second accent and a brand violation.
2. Red/green is precisely the pair that collapses under the most common
   colour-blindness. Encoding the beat's whole point in that contrast loses the beat
   for those viewers.

Built instead as **one arrowhead versus two** — terracotta single-headed on the
autoregressive side, solid-ink double-headed on the bidirectional side — each with a
stamped result line (`FAILS THE REVERSAL` / `PASSES THE REVERSAL`). The double head is
the literal visual claim the narration makes ("reads from both ends at once"), so the
form carries more meaning than the colour did.

### D3 — Narrator is Onkar, first person

The script's own Scene 1 VO is first person ("I am Onkar Bhujbal, a software
engineer"), and the author's standing instruction from the previous reel was to use his
own name rather than the Liam stand-in persona. The Scene 5 sign-off in the supplied
script still reads "Liam, for Onkar Bhujbal and Humanitarians AI" — template carry-over.
Built as **"Onkar Bhujbal, for Humanitarians AI."** Reverting is a one-line change to
`BOUT.narration_text` plus a re-render of that beat.

### D4 — Generic aliases instead of `Gatekeeper*` ids

`GatekeeperIngestFlow` and `GatekeeperTitleOutro` are reel-neutral components with
reel-specific names. Rather than reference them from a STEM beat sheet, two alias
composition ids were registered against the same components: **`ThreeStageBand`** and
**`HaiTitleOutro`**. No behaviour change, nothing broken, and the library reads
honestly for Week 3+.

`GatekeeperIngestFlow` also gained a `payloadLabel` prop — the travelling token was a
hardcoded `doc_01`, which is meaningless in a reel about token prediction. Defaulted to
`doc_01` so existing reels render byte-identically.

### D5 — "Fresh chat" added to the scaffolded task

The script's Scene 5 asks the viewer to run two prompts but does not say to start a new
session. Run back-to-back, the answer sits in the context window and the model "passes"
for the wrong reason — the test falsifies nothing. B06 adds the caveat. Flagged in
SOURCES.md as the reel's addition, not the author's.

### D6 — B01 is authored, not from the script

The script carries no BLUF, but `EXECUTIVE-SUMMARY LAW` makes beat 2 mandatory.
`facts` → `directions` is the reel's actual misconception. Single-word trigger by
necessity: `BrutalistHesitantWriter` matches whitespace-delimited word cores only,
despite the SKILL.md asking for phrase-level corrections.

---

## Dual render — status

The script asks for 16:9 **and** 9:16. Per `RENDER-TARGETS.md` §3, 9:16 is a different
beat sheet, never a crop.

| Beat | Pattern | Portrait variant |
|---|---|---|
| B00, B03, BHTF | `ClaudeComposerAsk` | ✅ `…916` shipped with the toolkit |
| B01 | `BrutalistHesitantWriter` | ✅ `…916` shipped |
| B02 | `ThreeStageBand` | ❌ **none — will be flagged** |
| B04 | `ReversalTrainingGraph` | ✅ built, responsive (stacks) |
| B05 | `ReversalBidirectionalTest` | ✅ built, responsive (stacks) |
| B06 | `ClaudeCodeBeat` | ❌ **none — will be flagged** |
| BOUT | `HaiTitleOutro` | ❌ **none — will be flagged** |

The two new components read `useVideoConfig()` and re-lay out for portrait — the
document/graph pair and the two architecture columns go from side-by-side to stacked,
core artifact centred, exactly as the script's safe-zone note asks.

Three beats still need portrait variants before `./art vertical` produces a clean
companion. It will **flag** them, not silently centre-cut.

---

## Runtime

Measured narration: **~2:03** against a 2:30 target, with the script's VO used
near-verbatim. Kokoro reads faster than the script was timed for. Duration is an output,
not a target (`duration-planner`), so nothing was padded to hit 2:30. If the target is
firm, the natural places to add are B04 (one more sentence on what "conditionally
dependent" means in practice) and B06 (why rarer facts make a cleaner test).

---

## Next steps

```bash
# review cut (paperwork gate bypassed)
ART_FACTS=0 ./art run G:/Onkar/youtube/claude-stem-reversal-curse

# 9:16 companion — expect three flagged beats until their 916 variants exist
./art vertical G:/Onkar/youtube/claude-stem-reversal-curse

# 4K master (needs FACTCHECK.md / SHOTLIST.md / PROMPTS.md for a fully gated run)
./art final G:/Onkar/youtube/claude-stem-reversal-curse --out G:/Onkar/youtube/claude-stem-reversal-curse
```

Never publish. Output stays in this folder for human review.
