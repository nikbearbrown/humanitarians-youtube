# Sources — Why the Same Prompt Gives Four Different Images

Checked 2026-11-13.

1. Midjourney, "Seeds": https://docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds (seed as "the random noise you see on a TV screen"; 0–4294967295; new random seed every time if unset; "Seeds are 99% identical in V8.X"; use as a control when testing; "Not for Saving Styles"; recommends style references, omni references and personalization; not reliable in Turbo mode; may change across sessions; finding a seed: open image → options → Copy → Seed). Read in the browser; WebFetch was blocked (403).
2. Midjourney parameter list: https://docs.midjourney.com/parameter-list ("Using the same seed number and prompt will produce similar ending images", via search summary).
3. LL Fellows Handbook v1.0, §6.1 (one prompt → four images), §6.7 (style reference, image prompt, moodboard, personalize, Style Creator), glossary ("Job: one generation. It produces four images.").
4. Own experiment: `demo/seed_demo.py` → `demo/seed_output.json` (NumPy PCG64; a toy generator, not Midjourney).
