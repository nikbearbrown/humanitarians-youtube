# Video 11: Measuring the Classifier — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya from the Mycroft team.
This video covers how I started measuring the Claims Agent's classifier: an evaluation harness, a real BigQuery pull, and one finding that changed the plan.

## B00 — Cold open
In an earlier spot check, every result came back narrow and defensive. That could be true of the patents we picked. Or the prompt could be giving the same answer every time. Reading a few outputs by hand can't tell those two apart.

## B01 — The evaluation harness
Method: the harness runs the classifier on claims a human has labeled, then compares its answers with the labels. Accuracy alone isn't enough. It also reports Cohen's kappa, the score you'd get by always guessing the most common label, and a collapse check that flags any single answer covering eighty percent of the output. Kappa measures how much the classifier agrees with the labels beyond what chance alone would give, so a classifier that always gives the same answer scores zero, however good its accuracy looks. I tested it offline with a fake classifier that always says narrow and defensive. Both collapse warnings fired, and kappa came out at zero.

## B02 — One query, not sixteen
The patents table isn't partitioned, so BigQuery charges for every byte of each column a query touches, no matter how many patents it returns. Looking up one patent costs about seventy-three cents. Looking up one hundred sixty costs about the same. So instead of sixteen separate lookups, one per patent in the final set, the script pulls a pool of one hundred sixty candidate patents in a single query, then picks the final sixteen on my own machine for free. A free dry run predicted the size first. The real query scanned about one hundred sixty-two gigabytes: ninety-two cents at list price.

## B03 — The real finding
The plan assumed about five independent claims per patent: fifty claims from eight to ten patents. The real data disagreed. Of the one hundred sixty candidate patents, one hundred forty-seven had only one to three independent claims. Just thirteen had four or more. So instead of leaning on a few unusual patents, I took fifty claims from sixteen patents. The candidates were US patents granted from 2020 to 2024, twenty from each of the eight CPC sections, picked by a hash of the patent number rather than by hand. Patents with fewer than three independent claims were skipped. The script then took two patents from each section, and at most four claims from any one patent.

## B04 — What's not done yet
Phase two, labeling those fifty claims by hand, is deliberately paused until the project lead can review the set. That means there is no accuracy number yet. The harness works, and the data is real, but whether the classifier really is stuck on narrow and defensive is still an open question.

## B05 — Handoff
Your turn. Before you build an evaluation set, count what your real data actually contains. Check one assumption, like how many items each record has, against a real sample before you size the set around it.

## B06 — Outro
Measuring the Classifier. Built with Claude, for Humanitarians AI.
