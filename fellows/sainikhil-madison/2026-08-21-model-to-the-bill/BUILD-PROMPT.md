# BUILD-PROMPT — From The Model To The Bill

Paste-ready prompt to rebuild this reel end to end. Run every command from the
toolkit root (`/Users/nikhilkunapareddy/Documents/brutalist.art`).

Part 2 of 2 — part 1 is `weekly_updates/08-14(2)/`.

---

## The four commands

```bash
# STEP 1 — Sign GATE P (human). Open weekly_updates/08-20/PEDAGOGY.md, review
#          the narration end to end, and change the blank on the signature line
#          at the very bottom to the word PASS. Save.
#          Audio refuses to run until that line is signed.

# STEP 2 — Generate narration audio (the master clock). Free, local, ~30s.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/08-20

# STEP 3 — Render the ten beats. True 4K (1280x720 stages -> --scale=3).
.venv/bin/python runtime/scripts/remotion_scenes.py weekly_updates/08-20

# STEP 4 — Compile the 4K master + run visual QC.
ART_STRICT=0 ./art run weekly_updates/08-20
#   → claude-sai-model-to-the-bill.mp4        (clean 4K master)
#   → claude-sai-model-to-the-bill-slate.mp4  (labelled review cut)
#   → _qc/  (frame samples + REPORT.md — LOOK at these)
```

**Use `.venv/bin/python`, not `python3`.** The system interpreter does not have
Kokoro; `./art doctor` reports audio as blocked because of this, and it is
wrong about the cause.

**`ART_STRICT=0` is deliberate.** The airy Claude-style illustrations and the
centered title/verdict cards trip GATE V's `underfill` MAJOR every time. That
check is a known false positive for this brand. Run once without it first, read
`_qc/REPORT.md`, and satisfy yourself that every remaining defect is an
underfill — **a BLOCKER is never a false positive and must be fixed.**

To change pacing or wording: edit `narration_text`, delete `mp3/*.mp3`, then
re-run STEP 2 → STEP 3 (`--only B0X --force`) → STEP 4. **Never hand-edit
durations** — audio is the clock.

---

## What this reel needs that a stock weekly reel does not

Two Remotion compositions were written for it:

- `runtime/remotion/src/LlmDeployIllu.tsx` — `LlmInferenceKnobs` (B01) and
  `LlmLoraFactorization` (B04).
- `runtime/remotion/src/Root.tsx` — imports and registers both at 1280×720.

Verify they are live before rendering:

```bash
cd runtime/remotion && npx remotion compositions src/index.ts | grep -E "^Llm"
# expect LlmTokenSplit + LlmAttentionReach (part 1)
#        LlmInferenceKnobs + LlmLoraFactorization (this reel)
```

`remotion_scenes.py --only` takes **one** beat id per invocation. Loop it:

```bash
for b in B01 B04; do
  .venv/bin/python runtime/scripts/remotion_scenes.py weekly_updates/08-20 --only $b --force
done
```

---

## Shape

Ten beats, ~356 narration words, ~121s at the measured 176.7 wpm.

`ClaudeComposerAsk` → `LlmInferenceKnobs` → `ScaleComparison` → `BinaryBranch` →
`LlmLoraFactorization` → `DivergentFates` → `ClaudeScienceChipGrid` →
`ClaudeVerdictArtifact` → `ClaudeComposerAsk` → `ClaudeTitleOutro`

Host is **Sai** (not Liam-in-for-Bear — deliberate, see `PEDAGOGY.md`). Voice is
Kokoro `am_onyx`, free and local. No keys, no spend, at any step.

---

## Pitfalls

1. **Do not add an override prop for B04's parameter counts.** They are derived
   from `d`, `k`, `r` so the figures cannot contradict the drawn matrices.
2. **Do not widen B02's band to include INT8.** The blog's consumer-GPU claim is
   about the 4-bit case only.
3. **`./art run` refuses without `scenes.py`.** The empty guard file is here.
4. **Re-rendering skips finished beats.** Pass `--force`.
