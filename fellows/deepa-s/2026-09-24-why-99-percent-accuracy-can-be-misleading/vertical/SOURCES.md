> Production status: Deepa explicitly approved this complete planning packet in the conversation. Original draft-state labels below describe the earlier planning stage. Audio listening remains pending; see AUDIO-REVIEW.md.

# Sources and Provenance

Sources accessed 2026-09-24. Paraphrase definitions; do not present invented quotations. No source images, logos from the web, or source footage downloaded.

## S1 — Google Machine Learning Crash Course

Title: Classification: Accuracy, recall, precision, and related metrics.
URL: https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
Publisher: Google for Developers.
Relevant sections: Accuracy; Recall; Choosing a metric.
Use: explanation of the limits of aggregate accuracy and selection of metrics based on task, class balance and error costs. This is educational guidance, not evidence of any particular deployed spam filter's performance.

## S2 — scikit-learn accuracy_score documentation

URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
Publisher: scikit-learn project.
Relevant sections: normalize parameter; Returns.
Use: independent definition of unweighted classification accuracy as the fraction of matching true/predicted labels.

## S3 — scikit-learn recall_score documentation

URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
Publisher: scikit-learn project.
Relevant section: definition, TP / (TP + FN), binary positive-class convention.
Use: define spam as the positive class and verify the spam-recall denominator. This video does not use macro or weighted recall.

## D1 — Constructed teaching example

Origin: the proposed and human-approved brief in this conversation. Exactly 99 ordinary emails and one spam email, with an always-ordinary prediction rule. No collected emails, public dataset, training, evaluation benchmark or observed model output is claimed. The prevalence is deliberately chosen to illustrate the arithmetic, not asserted as a real-world statistic. The classifier is a baseline rule, not a demonstrated trained AI model.

The exact deterministic calculation, interpreter version, input hash and observed output are preserved in FACTCHECK.md. No random seed is required; no randomness is used. Visual requests P1/P2 are proposed generation instructions, not receipts of an already-completed build.

## Editorial corrections and boundaries

- Say “in this example” when giving 99% accuracy or 0% spam recall.
- Say “can be misleading”, not “accuracy is always misleading”.
- Do not claim a one-email positive class estimates real-world detection ability reliably.
- Do not claim the score is fraudulent; the arithmetic is correct but incomplete for this task.
- Do not replace accuracy with recall as a universal single-score solution. False alarms also matter; choosing metrics depends on the task.
- Do not report precision as 0% here: the mathematical denominator is zero because no email is predicted spam. Precision is outside this video's scope.
- No personal accomplishments, affiliations beyond Deepa's supplied volunteer identity, or public profile links have been invented.
