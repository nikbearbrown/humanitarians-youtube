# PEDAGOGY
Concept: structural audit of proposed confounders — separating true confounders from mediators and colliders.
Problem: Claude proposes 10 confounders — which ones must not be conditioned on?
Question on screen: how do you know which proposed confounders are actually mediators or colliders?
Answer: trace the arrows — a mediator sits on the causal path X→M→Y; a collider is caused by both X and Y. Conditioning on either creates bias.
