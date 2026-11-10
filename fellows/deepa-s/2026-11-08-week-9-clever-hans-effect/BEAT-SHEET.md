# Beat Sheet — The Clever Hans Effect: When AI Gets the Right Answer for the Wrong Reason

Unchanged measured narration clock: **183.875000 seconds / 4413 frames at 24 fps** in both formats. Deepa approved the illustrated visual direction; final redesigned video review remains separate. Source: [Root.tsx](src/Root.tsx) and [Worlds.tsx](src/redesign/Worlds.tsx).

Original narration, caption boundaries and citations are preserved. Target editorial scene windows were adjusted to the actual recorded narration; the exact contiguous windows below govern the export. Citation IDs resolve in [SOURCES.md](SOURCES.md).

## B00 — Right answer. Wrong pattern?

- Start / end: 0.000000 / 20.125000 s
- Duration: 20.125000 s (483 frames)
- Narration: What if an AI predicts correctly, but learns the wrong pattern? A confident answer can hide a fragile shortcut. The model may recognize something in the background instead of the object we care about. This is Liam, narrating for Deepa, with Humanitarians AI. Let's look beyond the score.
- On-screen text: Right answer. Wrong pattern?; What feature did it use?; Illustrative classifier; Background changes; The animal stays the same.. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Layered outdoor illustration with one dog, changing snowy/grass background and classifier scan.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: G

## B01 — The horse that appeared to count

- Start / end: 20.125000 / 46.416667 s
- Duration: 26.291667 s (631 frames)
- Narration: Clever Hans was a horse that appeared able to answer arithmetic questions by tapping a hoof. Psychologist Oskar Pfungst investigated the performance. His experiments showed that subtle, unintentional movements from people supplied cues for the horse's responses. The apparent success depended on information outside the supposed mathematical task. The lesson is about testing what supports an answer.
- On-screen text: The horse that appeared to count; Clever Hans / a closer look; SUBTLE HUMAN CUES; Original illustration • Pfungst, 1911; The cue changes the answer.; A hoof tap is observable.; Arithmetic is not established.; Pfungst / 1911. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Original sepia horse/observer illustration, animated hoof taps and cue line, credited to Pfungst.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: P

## B02 — An easy pattern is not always useful

- Start / end: 46.416667 / 72.708333 s
- Duration: 26.291667 s (631 frames)
- Narration: Machine learning can produce a similar surprise. Shortcut learning happens when a model uses an easy predictive pattern that fails under different conditions. A spurious correlation is an association that does not reliably represent the intended relationship. Generalization means performing well beyond the examples used to develop the model. A shortcut may work locally while failing that broader test.
- On-screen text: An easy pattern is not always useful; A useful cue—or a fragile shortcut?; BACKGROUND; PREDICTED LABEL; NEW SETTING; An easy feature can fail.; Shortcut learning; Spurious correlation; Generalization. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Illustrated background/predicted-label/new-setting pathway with moving signals.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: G

## B03 — Wolves, dogs—and the background

- Start / end: 72.708333 / 100.458333 s
- Duration: 27.750000 s (666 frames)
- Narration: Consider this illustrative classification example. Suppose many wolf photos in training have snow, while dog photos usually do not. A model could learn snow as a shortcut for wolf. Now place a dog in snow: the model may call it a wolf. Change the background while keeping the animal the same, and the prediction might flip. This animation illustrates the mechanism; its predictions are not measured experimental results.
- On-screen text: Wolves, dogs—and the background; ILLUSTRATION / PREDICTION: DOG; SHORTCUT PREDICTION: WOLF. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Same dog in grass and snow: side-by-side landscape, stacked portrait; illustrative predictions DOG and WOLF.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: R

## B04 — Familiar tests can hide the shortcut

- Start / end: 100.458333 / 126.625000 s
- Duration: 26.166667 s (628 frames)
- Narration: A familiar test set can preserve the same background pattern as training, making the model look reliable. New environments can break that pattern and expose the weakness. This differs from data leakage, our earlier topic. Leakage involves information crossing a boundary it should not cross. Shortcut learning can happen even with properly separated datasets, when the same misleading association appears in both.
- On-screen text: Familiar tests can hide the shortcut; Separate data can share a shortcut.; Familiar tests can preserve a cue.; New settings can break it.; This differs from data leakage.. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Background changes around the same dog; familiar-test shortcuts are distinguished from data leakage.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: G, L

## B05 — Change what should not matter

- Start / end: 126.625000 / 154.458333 s
- Duration: 27.833333 s (668 frames)
- Narration: To investigate, compare counterfactual examples: keep the intended subject fixed while changing a feature that should not determine the answer. Replace a background, vary a setting, or evaluate relevant subgroups separately. Test data from outside the familiar distribution. These checks can reveal dependence on unintended features. They do not prove that every shortcut is gone, and a changed prediction still needs careful interpretation.
- On-screen text: Change what should not matter; ILLUSTRATION / PREDICTION: DOG; SHORTCUT PREDICTION: WOLF. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Counterfactual pair preserves the dog while changing background; same horizontal/stacked adaptations.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: G, L

## B06 — Reliability needs more than a score

- Start / end: 154.458333 / 173.625000 s
- Duration: 19.166667 s (460 frames)
- Narration: The issue matters in computer vision, medical AI, and automated classification. An image source or background may correlate with a label without representing the intended concept. Reliability depends on testing across meaningful conditions, not only reporting one overall accuracy number.
- On-screen text: Reliability needs more than a score; TEST RELIABILITY ACROSS CONDITIONS; Changing inputs; Separate evaluation; Human review; Original conceptual diagram • no experimental metrics; Reliability needs context.; Computer vision; Medical AI; Automated classification. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Illustrated independent-evaluation workstation contextualizes computer vision, medical AI and classification.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: L

## B07 — Ask what supports the answer

- Start / end: 173.625000 / 183.875000 s
- Duration: 10.250000 s (246 frames)
- Narration: Getting the right answer doesn't prove that AI learned the right reasoning. Test the pattern, not just the prediction. Humanitarians AI.
- On-screen text: Ask what supports the answer; Test the pattern.; Right answer ≠ right reasoning.; Check meaningful conditions.. Full sentence captions, Humanitarians AI branding, @HumanitariansAI and “Liam, narrating for Deepa.” remain present.
- Composition: Layered landscape and classifier scan hold through the closing message to test the pattern, not just the prediction.
- Animation: Deterministic frame-driven SVG motion in src/redesign/Worlds.tsx; 0.32-second eased entrance, 0.20-second exit, subtle 1.8% camera push. Final scene holds through the last frame.
- Transition: 0.32-second eased scene fade-in and 0.20-second fade-out; final scene does not fade away.
- Landscape: Native 1920×1080 composition: illustration left, contextual text right; comparison environments side by side; dedicated caption and source bands.
- Portrait: Native 1080×1920 composition: illustration above contextual text; comparison environments stacked vertically; dedicated caption and source bands. No landscape crop.
- Citations: G
