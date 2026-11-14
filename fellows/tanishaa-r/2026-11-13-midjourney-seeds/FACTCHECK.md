# Fact check — Why the Same Prompt Gives Four Different Images (script v1)

| Beat | Claim | Status | Source |
|---|---|---|---|
| B01 | One prompt gives four images | ✅ | Handbook §6.1, glossary |
| B02 | Every image starts as random noise, like TV static | ✅ | Midjourney Seeds page |
| B02 | The model cleans it up step by step | ✅ (simplified) | general diffusion; shown as schematic |
| B03 | The noise nudges the layout; the prompt says what it's about | ✅ (softened) | Seeds page: seeds "only influence the initial layout of noise" and "have the least impact on the final image" |
| B04 | Each of the four starts from different noise; no seed = new random every time | ✅ | Seeds page |
| B05 | Seed = any whole number 0–4,294,967,295; `--seed` at the end of the prompt | ✅ | Seeds page |
| B06 | Toy: seed twice → identical; four seeds → different; one word changed → same layout | ✅ measured | demo/seed_output.json (0 pixels different; ~21% of pixels differ between the four; layout identical after the word change) |
| B07 | Same seed + same prompt → almost the same image, "99% identical in V8" | ✅ | Seeds page |
| B07 | Find a seed: open → options → Copy → Seed | ✅ | Seeds page (web) |
| B08 | Use as a control when testing one change | ✅ | Seeds page |
| B08 | Can't carry a style/character across prompts; not reliable in Turbo | ✅ | Seeds page |
| B08 | For a consistent look: style references, moodboards, personalization | ✅ | Seeds page (style/omni references, personalization); Handbook §6.7 (moodboards) |
| topic note | "Reusing the seed is how you keep a consistent look across assets" | ❌ corrected | Seeds page "Not for Saving Styles"; Tanishaa chose the corrected ending |

**Caveats:** B06 is a toy (no AI model): its layout comes only from the noise and its colours only from the prompt word, which a real model mixes. The screen says "toy, not Midjourney".
