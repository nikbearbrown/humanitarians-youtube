A model can pass every test on launch day and, a year later, do barely better than guessing. Nobody has to change a line of code for that to happen.

This week's second reel is a general one: MLOps, and the part of it that catches this, which is monitoring. Chip Huyen's MLOps guide defines the "ops": "To operationalize something means to bring it into production, which includes deploying, monitoring, and maintaining it."

To see it happen, we trained a model on the first year of ELEC2, half-hourly data from Australia's New South Wales electricity market from 1996 to 1998. The model predicts whether the price goes up or down. We froze it and scored it every four weeks after that. It started at 0.838. Four weeks later it was at 0.629. By weeks 45–48 it was at 0.548, while always guessing "down" scores 0.544. Nothing in the model changed. The prices did: the KS distance between training-year prices and live prices rose from 0.22 to 0.92.

Huyen's names for this: covariate shift is when P(X) changes but P(Y|X) stays the same, and concept drift is when P(Y|X) changes but P(X) stays the same. In most products, the right answers arrive late, if they arrive at all. So we also watched something available immediately: the model's own scores. We compared each block's scores with the training year's using the two-sample Kolmogorov–Smirnov statistic. That label-free gap rose as accuracy fell and fell as accuracy came back (r = −0.85 over 20 blocks).

Two honest footnotes. On this dataset the label arrives 30 minutes later, so simply copying the last half-hour's answer averages 0.86, ahead of both models in 19 of 20 blocks. Most systems are not that lucky. And retraining every four weeks helped in 12 of 20 blocks but lost 7. That included the stretch a year on, when prices returned to normal and the untouched model recovered on its own to 0.849.

Try it yourself: for any model in production, list which of its right answers you won't see for weeks. Then list what you can monitor today without them, such as input distributions and the model's own scores against training. For each alarm, decide in advance whether you would retrain, roll back, or wait.

Chapters:
0:00 Why is an untouched model wrong a year later?
0:18 The ops in MLOps
0:37 A real model, frozen: 0.838 to 0.548
0:54 Covariate shift, concept drift, and the KS gap
1:10 Labels arrive late: watch the scores
1:29 Retrain it? It helps, and it costs
1:47 Verdict
2:01 Your turn: monitor what you have today
2:16 Outro

Sources:
Chip Huyen, MLOps guide — https://huyenchip.com/mlops/
Chip Huyen, "Data Distribution Shifts and Monitoring" (2022) — https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html
ELEC2 electricity dataset — M. Harries (1999), normalised by A. Bifet; OpenML dataset 151 — https://www.openml.org/d/151

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics built with Remotion. The equations are typeset locally as outlined SVG. Every number on screen comes from a script run for this video on the public ELEC2 file, which was checked against OpenML's checksum. The script uses scikit-learn's HistGradientBoostingClassifier with a fixed seed and SciPy's KS test, checked by hand. The model uses only the New South Wales columns, because the Victoria columns are empty for the training year. A version with all columns, reported alongside, shows the same decay. Quotations from Chip Huyen were checked verbatim against her pages. No image was generated. No human-performed audio or video in this production.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: MLOps, machine learning in production, model monitoring, data drift, covariate shift, concept drift, distribution shift, Kolmogorov-Smirnov test, retraining, feedback loop, ELEC2, electricity market, Chip Huyen, Humanitarians AI, Computational Skepticism, weekly

#MLOps #MachineLearning #DataDrift #ModelMonitoring #AI #DataScience #HumanitariansAI #ComputationalSkepticism
