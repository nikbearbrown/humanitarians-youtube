# Visual QC — `data-contract-simulation`

Frames sampled from the compiled masters (not from the beat renders), per the
VISUAL QC LAW: the mp4 probe is a file check, never QC.

Contact sheet: `_qc/qc-sheet.png` (B03 code · B07 payoff · B04 as-is · B08 summary).
Portrait spot-check: `_qc/916_B01_t13.png`.

| Check | 16:9 | 9:16 |
|---|---|---|
| True 4K | 3840×2160 ✅ | 2160×3840 ✅ |
| Duration matches audio clock | 126.32s ✅ | 126.32s ✅ |
| All 11 slots filled, zero slates | ✅ | ✅ |
| Per-beat video length == measured mp3 | ✅ 11/11 | ✅ 11/11 |
| SAFE / SAFE916 inset respected, no edge-bleed | ✅ | ✅ |
| Canvas fill (no timid type over dead space) | ✅ after the B01 fix | ✅ |
| Type legible at mobile scale | ✅ | ✅ portrait type is larger, as intended |
| One terracotta moment per beat | ✅ | ✅ |
| Handle wordmark on every beat | ✅ | ✅ |
| BLOCKER / MAJOR findings | 0 | 0 |

## Findings and dispositions

1. **B01 dead space (MINOR, fixed).** First render left the two top cards
   half-empty. Panel bodies now centre in their card; mono and headline sizes up
   ~15%. Re-rendered and re-checked.
2. **B05 duration mismatch (MAJOR, fixed).** An interrupted render left
   `media/B05.mp4` at the raw 30.06s composition length instead of its 13.14s beat,
   plus a corrupt `_ext_B05.mp4` temp. Caught by auditing every beat's video
   duration against `actual_duration_s` — *not* by the compile, which would have
   happily stretched it. Temp removed, beat re-rendered with `--force`, verified
   at 13.17s.
3. **`type-on` at 54% of beats (WARNING, accepted).** `compile.py` flags the ~40%
   motion-language cap. Accepted as structural rather than lazy: the cli-explainer
   spine mandates five composer beats and two code beats, and those genuinely type.
   The four illustration beats deliberately use four different languages —
   reveal / stagger / count / stack — so no two adjacent non-UI beats share a
   scheme (ILLUSTRATE LAW holds).
4. **`x0.01` renders as `X0.01`** in B07's right-hand column (uppercase transform
   on the scale chip). Cosmetic, legible, left as-is.
