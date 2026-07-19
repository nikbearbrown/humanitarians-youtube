# PEDAGOGY
Concept: DoWhy causal estimation — naive vs. backdoor-adjusted.
Problem: how much does confounding inflate the naive estimate?
Question on screen: why does conditioning on the confounder change the estimate?
Answer: the confounder creates a non-causal path T←Z→Y that inflates the raw association. Backdoor adjustment closes this path, recovering the true causal effect.
