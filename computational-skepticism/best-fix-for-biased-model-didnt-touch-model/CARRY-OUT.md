# Carry-Out Law

## The Carry-Out Line
> "An intervention only removes what its causal path carries — and the highest-leverage path often bypasses the model entirely."

## Wrong Guess Defeated
The naive reflex that whenever a deployed AI system produces a biased disparity, the fix must live inside the model's weights, loss function, or training dataset.

## The Distinction That Matters
- **In-Model Intervention (Low Leverage)**: Rewriting the loss function or rebalancing training data only blocks the direct path through the model parameters, leaving proxy and deployment-context paths wide open.
- **Deployment-Context Intervention (High Leverage)**: Intervening on human review protocols and decision thresholds blocks the dominant causal path that carries bias around the model and amplifies it in the real world.
