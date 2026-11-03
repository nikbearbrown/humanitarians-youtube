> Production status: Deepa explicitly approved this complete planning packet in the conversation. Original draft-state labels below describe the earlier planning stage. Audio listening remains pending; see AUDIO-REVIEW.md.

# Proposed Script and Visual Plan

HUMAN REVIEW PENDING. Editorial plan only; IDs are planning references, not an executable beat sheet. No shot or render is claimed complete. See FACTCHECK.md for claim IDs and PROMPTS.md for proposed requests.

## B00 — Opening

Visual: ClaudeComposerAsk opens directly. Greeting `Hi, Deepa`; footer `@HumanitariansAI`. Display Deepa Shenoy's credit and `AI narration: Liam for Deepa Shenoy`. Composer asks: “Why can 99% accuracy hide missed spam?” Proposed educational answer lines: “Count correct labels.” / “Check which emails were missed.” Label this as an illustrated explainer interface, not a recorded Claude session or a model benchmark.

Narration — Deepa's exact supplied wording:

> Hi, I am Deepa Shenoy, and this video is about why 99% accuracy can be misleading. This is Liam, narrating for Deepa.

## B01 — The Overview

Visual: BrutalistHesitantWriter writes “A high accuracy score tells the whole story.” and replaces “tells the whole story” with “can hide important mistakes”. Final text: “A high accuracy score can hide important mistakes.” Follow with “Check which examples were missed.” Use explicit HAI palette and deterministic seed 9901. A later beat sheet must include the required 0.8-second lead silence and satisfy the measured minimum overview window; no duration has been fabricated here.

Narration:

> A high accuracy score can hide important mistakes. Check which examples were missed. We'll count correct labels, then look at the spam the classifier failed to catch.

Claims: C1, C5. Small source credit: Google, Machine Learning Crash Course.

## B02 — The Counting Framework / Ask

Visual: composer shows the proposed request P1, already typed. Present the two evaluation questions as planned output: “Correct labels out of all emails?” and “Spam caught out of actual spam?” Introduce this framework before the worked example. Do not depict execution as completed until P1 has actually been implemented.

Narration:

> Build a labeled teaching example. We'll ask two questions: how many labels are correct overall, and how many actual spam emails are caught?

Claims: C1, C4. Source credit: scikit-learn metric definitions.

## B03 — Work Through the Example

Visual: P1 result. Native animated 10-by-10 tile graphic; one tile represents one email. Keep “Hypothetical teaching example” visible. Reveal 99 ordinary tiles and one outlined, explicitly labeled spam tile. Animate the rule “Always predict ordinary” assigning all 100 tiles the ordinary prediction. Keep true class distinct from predicted label. Count 99 matches and one miss. Show “99 correct out of 100 = 99% accuracy”.

Narration:

> Imagine one hundred emails: ninety-nine ordinary emails and one spam email. These are made-up teaching counts, not measurements of a real inbox. Our classifier always says “ordinary.” It labels the ninety-nine ordinary emails correctly and misses the spam. That's ninety-nine correct labels out of one hundred: ninety-nine percent accuracy.

Claims: C1–C3. Artifact: computed counts in FACTCHECK.md; attribution: “Constructed example; definitions: scikit-learn”.

## B04 — Ask About the Miss

Visual: brief composer micro-beat, already typed P2, immediately preceding its graphic. Its output announces the intended comparison, not a completed model experiment.

Narration:

> Now show the missed spam beside the overall score.

## B05 — Stress-Test the Score

Visual: P2 result. Keep the one spam tile visible and route it to “Predicted ordinary — missed”. Compare two large labeled counters: “Accuracy: 99% (99/100)” and “Spam recall: 0% (0/1)”. Hold the comparison long enough to read, at least two seconds after both are revealed. Preserve the hypothetical label. Show no unlabeled 0% and no zero-precision claim.

Narration:

> Of the one spam email, our rule catches zero. Spam recall asks what fraction of the actual spam was caught. Here, it's zero out of one, or zero percent. The high accuracy came from getting the common category right. It did not show that the rule could detect spam.

Claims: C3–C5. Artifact: computed counts. Source credit: scikit-learn, recall_score.

## B06 — Verdict

Visual: ClaudeVerdictArtifact candidate; explicitly set HAI brand label. Progressively reveal: “99% correct overall” / “0 of 1 spam caught” / “Ask which mistakes matter”. Use counts, not a text-only paragraph. No new numerical claims.

Narration:

> Accuracy is useful, but it isn't the whole evaluation. Ask how many examples belong to each category, which mistakes the system makes, and which mistakes matter for the task.

Claims: C5–C6; recap of worked example.

## B07 — Your Turn

Visual: ClaudeComposerAsk, greeting `Your turn.`, HAI footer, P3 typed verbatim. No fabricated answer. Display the checking rubric after the prompt; landscape side-by-side and portrait stacked. Narration reads the whole prompt and explains the check.

Narration:

> For ninety-nine ordinary emails and one spam email, predict ordinary every time. Calculate accuracy and spam recall, showing both denominators. Explain why the scores differ. Check the answer: one hundred emails overall, one actual spam email, ninety-nine percent accuracy, and zero percent spam recall.

P3 comprises the first three sentences; the last sentence is the spoken rubric. Claim: C7, independently checked.

## B08 — HAI Closing

Visual: HAI branded, title-restating closing card. Display title, `Deepa Shenoy`, `AI narration: Liam for Deepa`, `@HumanitariansAI`, full HAI mark. Adapt a suitable channel closing component after approval; do not use the hardcoded NikBearBrown title outro. Sources remain available in accompanying documentation/description. No subscribe pitch.

Narration:

> Why ninety-nine percent accuracy can be misleading. This is Liam, narrating for Deepa, for Humanitarians AI.

## Library-first inspection and implementation limits

Read-only searches executed with `--no-log`, before authoring this plan:

- `./art scenes "isotype grid percentage accuracy classification" --no-log --top 4`
- `./art scenes "Humanitarians outro verdict" --no-log --top 4`
- `./art scenes --check ClaudeComposerAsk ClaudeComposerAsk916 BrutalistHesitantWriter BrutalistHesitantWriter916 ClaudeVerdictArtifact OutroSeries OutroCTA`

The exact-name check found indexed compositions for all checked names. This establishes registry presence only, not successful rendering. Read scene props for composer, verdict and outro candidates. Composer accepts `folderLabel`; verdict accepts `brandLabel`. The writer has palette, replacement and seed props. `OutroSeries` accepts eyebrow/line but needs further work for this complete title/credit/HAI layout; `OutroCTA` is promotional and is not selected.

The broad grid search found mascot/catalog/chip previews, not a verified fit for this 100-item classification example. Proposed custom work: one data-driven email/counting illustration with native landscape and portrait layouts, plus any required HAI closing adaptation. No custom code is authorized or created at this gate. Resolve component coverage and inspect full schemas before an executable beat sheet; do not call these beats render-ready or ask Deepa to provide screenshots.

Teaching-arc intent: framework B02; worked example B03; failure-mode test B05; scaffolded task B07; opening/verdict/handoff/outro B00/B06/B07/B08. These are planned coverage, not passed implementation or visual-QC checks.
