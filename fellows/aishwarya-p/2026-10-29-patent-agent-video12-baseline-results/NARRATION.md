# Progress Video 12: What the Baseline Found — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya from the Mycroft team.
This video covers the first real evaluation of our patent claim classifier: fifty hand-labeled claims, one baseline run, and a result that went the opposite way from what we expected.

## B00 — Cold open
For weeks, the classifier's readings looked narrow and defensive, and we suspected it was stuck on one answer. When we finally measured it against human labels, it wasn't stuck there. It was leaning the other way.

## B01 — The setup
Last week I built the evaluation harness and pulled the test set: one BigQuery query, ninety-two cents, one hundred sixty patents. From those I selected fifty independent claims across sixteen patents, two from each of the eight patent classification sections. This week I labeled all fifty by hand, breadth and posture, with a note on each explaining why.

## B02 — The baseline run
Then I ran the classifier on all fifty, for at most thirty-two cents. Breadth accuracy was 0.66, posture accuracy 0.60. Accuracy alone is misleading here. Forty-six of my fifty labels are narrow, so a model that always says narrow would score ninety-two percent. Cohen's kappa corrects for that: 0.08 on breadth and 0.00 on posture, which is barely better than chance.

## B03 — The finding
The surprise is the direction. The classifier called eleven claims broad and offensive, and I had labeled ten of those eleven narrow. Its reasoning kept treating functional wording, like "configured to" or "a protrusion", as broad, while I read the named parts and specific limits as narrow. One caveat: every one of my labels is defensive, so this test set can't measure posture agreement well. That needs offensive and broad examples.

## B04 — The refusal bug
Three claims on one patent, a cryogenic grinding process, kept failing. Raising the token limit didn't help. One diagnostic call showed why: the model was refusing partway through its answer, leaving half a JSON reply that the parser couldn't read. The code only handled empty refusals. I fixed it to treat any refusal as declined, and all fifty claims now score. The prompt fix comes next.

## B05 — Handoff
Your turn. Before you trust any classifier's accuracy, score a fake model that always gives the most common answer. If your real model can't beat it, accuracy is telling you about your data, not your model.

## B06 — Outro
What the Baseline Found. Built with Claude, for Humanitarians AI.
