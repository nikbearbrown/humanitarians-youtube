# FACTCHECK — How AI Draws Anime Frames

Checked against the Sources list in `SCRIPT.md`. Keya revised the B04 and B06 narration afterwards (claims 12, 13 and 24 updated).
Web pages were read through a fetch tool, so short quotes below are as that tool reported them.

**Verdicts:** ✅ confirmed · ⚠️ partly (the source supports less, or something different) · ❓ unverified · ✏️ editorial (opinion or illustration, not a factual claim)

**Tally:** 18 ✅ · 8 ⚠️ · 2 ❓ · 4 ✏️ (32 current claims; claim 13 removed). No claim was found to be contradicted by a source that was read.

## Sources

| Source | Read? | Notes |
|---|---|---|
| Anime Corner, May 19 2025 | Yes | Author Chike Nwaenie |
| Wikipedia, "Inbetweening" | Yes | General animation; the article body does not discuss anime |
| Li Siyao et al., AnimeInterp (arXiv 2104.02495) | Yes | Text read through part of §5.2, so the end of the paper is unchecked |
| Kreinin, 2024 | Yes | April 17 2024. No byline in the article; the site and footer point to Kreinin |
| RIFE, Huang et al. | Mostly | arXiv HTML; verbatim text stops partway, PDF too large to read |
| A.V. Club, Nov 5 2025 | Yes | Elijah Gonzalez |
| U-High Midway | Yes | Haley Maharry, March 23 2023, student opinion column |

## Claims

| # | Beat | Claim | Verdict | Evidence or problem |
|---|---|---|---|---|
| 1 | B00 | The voice is an AI voice reading Keya's script | ✅ | Project fact: Kokoro `af_bella`, narration taken verbatim from `SCRIPT.md` |
| 2 | B01 | Fans often say AI-smoothed anime looks unnatural | ❓ | The tagged source (Anime Corner) does not mention smoothing. No source read quotes fans or shows how often. Closest: critic and student columnists calling such edits bad |
| 3 | B01 | In 2025, Toei said it expects to use AI to draw in-between frames | ✅ | Anime Corner: in-between animation is among areas "where AI is expected to improve work efficiency in the future". Same note: "at present, we are not using AI" for it. The narration is accurate but leaves out the denial of current use |
| 4 | B01 | Toei is the studio behind One Piece | ✅ | Anime Corner: "known for One Piece" |
| 5 | B03 | Anime is hand-drawn animation | ❓ | Wikipedia does not discuss anime. AnimeInterp only says "2D animations" and "drawing" |
| 6 | B03 | Every scene starts with key frames; a key animator draws the most important poses | ⚠️ | Wikipedia confirms this for traditional animation: "draws key frames to define movement". Anime-specific support and "every scene" are unconfirmed |
| 7 | B03 | Rock Lee launching his kick at Gaara, and it landing, as an example | ✏️ | Illustration; `SCRIPT.md` says these are not claims about how the scene was animated. Not in any listed source |
| 8 | B03 | In-between artists draw the connecting frames | ✅ | Wikipedia: "a specialized inbetweener artist fills in the gaps between the key drawings" |
| 9 | B03 | In-betweens are the drawings AI is being asked to make | ✅ | Anime Corner: "AI-generated in-between frames"; AnimeInterp |
| 10 | B04 | Video plays at 24 frames a second | ⚠️ | Wikipedia says 24 frames for one second of **film**. "Video" is broader, and no source read says all video is 24 |
| 11 | B04 | Anime rarely draws all 24 | ✅ | AnimeInterp: producers "replicate one drawing two or three times to reduce the cost" |
| 12 | B04 | Most anime is drawn on twos or threes: each drawing is held for two or three frames, so twelve or eight drawings a second | ✅ | AnimeInterp: producers "usually replicate one drawing two or three times to reduce the cost". 24 ÷ 2 = 12; 24 ÷ 3 = 8 |
| 13 | B04 | ~~Slow moments go on threes~~ | Removed | No longer in the narration |
| 14 | B04 | Fast action, like a punch, can be on ones | ✅ | Wikipedia: "very fast movements". The punch is an illustration |
| 15 | B04 | Holds are a choice about budget and feel | ✅ | Budget: AnimeInterp, "to reduce the cost". Feel: Wikipedia, "an artistic choice" |
| 16 | B05 | Optical flow is a map of arrows showing where each pixel moved | ✅ | RIFE: "estimate the per-pixel motion". Arrows are a fair simplification |
| 17 | B05 | AI calculates flow, follows it halfway and draws the middle frame | ⚠️ | Fair for the common method. RIFE, the tagged source, warps at t=0.5 and blends, but predicts intermediate flows directly and says optical flow models "can not be directly used" |
| 18 | B05 | On live-action video this works surprisingly well | ⚠️ | RIFE reports "state-of-the-art" benchmark results, but also calls real-world video challenging. "Surprisingly well" is a judgment no source states |
| 19 | B06 | A flat color gives AI too little texture to tell which pixel went where | ✅ | AnimeInterp: "insufficient textures to match the corresponding pixels". Kreinin: "large flat-color regions" |
| 20 | B06 | Between two drawings, a fist can fly halfway across the screen along a curve | ⚠️ | AnimeInterp confirms "non-linear and extremely large motions". The fist and distance are illustrative; Kreinin does not mention arcs |
| 21 | B06 | Naruto and Sasuke's final fight, as an example | ✏️ | Illustration, as in claim 7. Not in any listed source |
| 22 | B06 | A hidden hand has nothing to match | ✅ | Kreinin: "I can't track something that isn't there." AnimeInterp uses occlusion only to rate difficulty |
| 23 | B06 | The result is ghosting and extra limbs | ✅ | Kreinin: "'ghosting' of details"; "3-4 arms and legs and 2 heads" |
| 24 | B06 | The result is blur | ✅ | A.V. Club: "a blurry 60 frames per second (FPS) nightmare". Kreinin: "AnimeInbet doesn't blur lines", contrasting it with methods that do |
| 25 | B07 | Many fans and animators dislike 60 fps AI edits | ⚠️ | U-High Midway: "Animators are enraged", unattributed. A.V. Club quotes no fans or animators. "Many" is unmeasured |
| 26 | B07 | Smoothing every frame wipes out the animator's timing | ✅ | A.V. Club: "no sense of impact or timing". U-High Midway: "ruins the timing" |
| 27 | B07 | One critic called the result lifeless (on screen: "a critic in The A.V. Club") | ✅ | Gonzalez: "smoothed out into a steady, lifeless tedium" |
| 28 | B07 | Keya's view: a little AI is fine, a whole anime looks unnatural | ✏️ | First-person opinion |
| 29 | B08 | A 2021 project, AnimeInterp, built a dataset of 12,000 sets of anime frames | ✅ | arXiv: "AnimeInterp"; "Accepted by CVPR21"; "ATD-12K ... 12,000 frame triplets selected from 30 animation movies" |
| 30 | B08 | Its model matches flat color shapes before guessing the motion | ✅ | Paper: color piece matching, then flow generated from the matches, then refined |
| 31 | B08 | Such tools could take repetitive in-betweens off a desk, with the animator checking every frame | ⚠️ | Kreinin: useful for "small movements", "easier to edit"; output "not quite usable as is". He tests AnimeInbet (2023), not AnimeInterp. "Repetitive" and "every frame" are not his words |
| 32 | BVDT | AI can draw in-betweens but struggles with flat colors, big movement and hidden parts | ⚠️ | Follows from claims 19, 20 and 22, so it carries the limit on claim 20 |
| 33 | BVDT | AI can't choose the timing; that's where the feeling lives; AI should be a helping hand | ✏️ | The film's argument, not a sourced fact |

## Open before final

**Kept knowingly (Keya's decision).** The wording of these stays as is, with their verdicts unchanged:

- **Claim 2 (❓):** "Fans often say AI-smoothed anime looks unnatural."
- **Claim 5 (❓):** "Anime is hand-drawn animation."
- **Claim 6 (⚠️):** "every scene starts with key frames"; a key animator draws the most important poses.

Gate F only checks that this file exists. It does not read these verdicts, so a pass does not mean the claims hold.
