# Explainer — Deep Sets in Multi-Agent RL — Order-Free Team Permutation Invariance

- **Week:** 26–31 Oct 2026
- **Type:** Topic explainer
- **Explainer video:** https://drive.google.com/file/d/1dYoiJJnA_AUAjisluJ1Ar8t3h_hcg1AO/view?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Beat sheet:** [beatsheet.md](beatsheet.md) · [beat_sheet.json](beat_sheet.json) · **Narration:** [script.md](script.md)

## What it covers

This report details the production and mathematical foundation of a dual-format explainer video (16:9 widescreen and 9:16 portrait) investigating **Deep Sets** (Zaheer et al., NeurIPS 2017) as an inductive bias for decentralized multi-agent reinforcement learning (MARL). 

When agents operate in teams, standard neural network architectures suffer from two fundamental design flaws:
1. **Roster-Order Sensitivity:** Standard feedforward or recurrent layers process inputs as ordered sequences. Swapping the arbitrary slot order of two identical teammates alters the network's intermediate representations and output actions, even though the physical world state is unchanged.
2. **Fixed-Dimension Input Constraints:** In an architecture relying on flat vector concatenation, training a policy with $N-1 = 2$ teammates fixes the observation input dimension. Deploying the same policy among $N-1 = 7$ teammates in a larger swarm leaves extra observation dimensions with nowhere to go, requiring structural redesign or retraining.

Deep Sets resolves both flaws by structuring teammate perception as an unordered set $X = \{x_1, x_2, \dots, x_{N-1}\}$ where each teammate's relative observation $x_j = (\Delta x_j, \Delta y_j, \Delta v_{x,j}, \Delta v_{y,j}) \in \mathbb{R}^4$ is projected through a shared feature extraction network $\phi: \mathbb{R}^4 \to \mathbb{R}^{32}$. The resulting embeddings are aggregated via an element-wise sum:
$$\mathbf{H} = \sum_{j=1}^{N-1} \phi(x_j)$$
Because addition is strictly associative and commutative, the team summary $\mathbf{H} \in \mathbb{R}^{32}$ is invariant under any permutation $\pi \in S_{N-1}$:
$$f(\pi(X)) = \rho\left(\sum_{j=1}^{N-1} \phi(x_{\pi(j)})\right) = \rho\left(\sum_{j=1}^{N-1} \phi(x_j)\right) = f(X)$$
Furthermore, $\mathbf{H}$ remains fixed at 32 dimensions whether an agent observes 1, 3, or 10 teammates, and naturally evaluates to the zero vector $\mathbf{H} = \mathbf{0}$ when no teammates are present ($N=1$). This architecture enables shared-parameter policies to train on small teams ($N \in [2, 4]$) and transfer zero-shot to large swarms ($N \in [8, 12]$) without structural retraining.

The explainer also rigorously examines the architectural trade-offs:
- **Pairwise Relational Information Loss:** Sum pooling operates element-wise in $O(N)$ time, discarding high-order relational interactions between pairs of teammates (which graph neural networks or self-attention capture at $O(N^2)$ computational complexity).
- **Sum Magnitude Scaling:** As team size scales from $N=2$ to $N=12$, the raw unnormalized sum grows proportionally, potentially causing activation drift unless paired with layer normalization or adaptive scaling.

Produced through human research direction and AI-assisted Remotion video generation voiced by Kokoro `am_onyx` (Liam in for Kriti).

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](FRICTIONAL.md).
- [Explainer video](https://drive.google.com/file/d/1dYoiJJnA_AUAjisluJ1Ar8t3h_hcg1AO/view?usp=drive_link).
- [Progress video](https://drive.google.com/file/d/12M1Yt1ivdba0GYSGlkWkJXk74UzJkaD3/view?usp=drive_link).

## Attribution and Contribution

Work by Kriti S.: technical mechanism structured into a 12-beat teardown (`claude-liam-deep-sets`), custom Remotion scenes constructed (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, mathematical equation layout, commutativity proofs), and narration script written, voiced via Kokoro `am_onyx` (Liam in for Kriti). Research and review by Kriti S.: mathematical specification of $\phi: \mathbb{R}^4 \to \mathbb{R}^{32}$, sum aggregator $\mathbf{H} = \sum \phi(x)$, permutation commutativity proofs, zero-teammate vector boundary validation, and approving the video review cut.
