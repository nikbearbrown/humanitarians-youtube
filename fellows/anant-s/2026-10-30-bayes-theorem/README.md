# Bayes' Theorem: The Positive That's Usually Wrong

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainers · ai-explainer format
- **Channel:** @NikBearBrown · **Voice:** Kokoro `am_onyx` · **Greeting:** Hello, Liam
- **Long:** 3840×2160 · 3:43 · 15 beats — `tldr-bayes-theorem.mp4`
- **Last updated:** 2026-11-24

## Subject

What a positive result means when a test catches 99% of cases. The film sorts 10,000 people: 100 are sick and 99 of them test positive, but 495 of the 9,900 healthy test positive too, so only 99 of 594 positives are sick — one in six. Bayes' theorem is then built from those counts, and a sweep shows how much the answer depends on the base rate.

## Notes

- First built in the TL;DR format (greeting "Salaam, Liam"). On 2026-11-24 it was converted to the ai-explainer format: the new B00 cold open defines sensitivity and base rate; B01 corrects "means you're probably sick" to "can still be a false alarm". The body, Verdict, Your Turn and outro are unchanged.
- Four narration lines were changed after GATE P, for audibility and visual accuracy; whisper had heard "sick" after a number as "six". No facts changed, and I approved the edits.
- Every gate passed on the first final, but hand QC found B12 blank from about 45% to the end. Fixed with `set_z_index(1)`.
