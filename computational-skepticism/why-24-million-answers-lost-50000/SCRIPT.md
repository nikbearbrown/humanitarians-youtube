# Why 2.4 Million Answers Lost to 50,000 — Script

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Narrator**: Liam (in for Bear)
**Register**: Plain (Epistemic mechanism, then stop)
**Visual Object**: The Target / Estimator Space (True theta bullseye vs Off-center biased estimator)
**Manim Move**: accumulate

---

### [B00] Hesitant Writer Cold Open (Remotion)
*(Visual: Hesitant writer types naive question, hesitates on 'eliminate sampling bias', corrects to 'amplify an error')*
**Liam**: If you collect millions of responses, you might assume massive dataset size eliminates sampling error. It doesn't. In fact, more data often just makes the wrong answer mathematically certain. Let's see why.

### [B01] 1 Stakes: The 1936 Literary Digest Poll (Manim)
*(Visual: Archive card for 1936 Literary Digest poll: 10M mailed ballots, 2.4M returned responses, predicting 57% Landon landslide)*
**Liam**: In 1936, the Literary Digest mailed ten million postcard ballots and gathered 2.4 million responses. It was the largest poll in history, and it predicted a crushing landslide for Alf Landon.

### [B02] 1 Stakes: The 50,000 Gallup Result (Manim)
*(Visual: Comparison card showing actual election outcome: Roosevelt 60.8% landslide vs George Gallup's 50,000 sample calling it right)*
**Liam**: Franklin Roosevelt won with sixty point eight percent of the vote — carrying forty-six states. A young pollster named George Gallup surveyed fifty thousand people — fifty times fewer — and called the race right.

### [B03] 4 ANCHOR PLANTED: The Target (Manim)
*(Visual: THE ANCHOR — Target showing true parameter theta at the bullseye and biased expected value E[theta_hat] off-center)*
**Liam**: To see why, look at estimation as shooting at a target. The bullseye is the true population parameter, theta. The center of your aim is the expected value of your estimator.

### [B04] 2 Wrong Guess: The Big Data Reflex (Manim)
*(Visual: Naive diagram showing massive sample size N collapsing uncertainty directly into the bullseye, labeled 'The Volume Reflex')*
**Liam**: The intuitive reflex is that sample size cures all defects. We assume that if sample volume grows large enough, random errors cancel out and the estimate must land on the truth.

### [B05] 2 BREAK IT: High Volume Does Not Move the Aim (Manim)
*(Visual: Falsifying breakdown: 2.4M points tightly clustered far away from the bullseye, showing razor-sharp precision around a 16-point error)*
**Liam**: That reflex breaks against the math. The Literary Digest didn't suffer from noisy scatter. Their variance was near zero — and their estimate was sixteen percentage points off target.

### [B06] 3 Mechanism: Definition of Bias (Manim)
*(Visual: Mathematical formulation: Bias(theta_hat) = E[theta_hat] - theta, highlighting that bias is a property of the estimator)*
**Liam**: In statistics, bias is a property of the estimator: the systematic difference between what your sampling procedure expects to measure and the true value. Bias equals E of theta-hat minus theta.

### [B07] 3 Mechanism: The Skewed Sampling Frame (Manim)
*(Visual: Diagram showing 1936 sampling frame: Telephone books, car registrations, and club rosters during the Great Depression)*
**Liam**: The Digest drew its addresses from telephone directories, automobile registries, and subscriber lists — luxury assets in the depths of the Depression. Their sampling frame excluded the working-class majority deciding the election.

### [B08] 4 ANCHOR PAYOFF: MANIM MOVE accumulate (Manim)
*(Visual: Kinetic demonstration: Points rapidly accumulate on the target, collapsing variance into a dense cluster around the biased offset)*
**Liam**: Watch what happens as data accumulates. A small sample scatters widely around the biased center. But as millions of responses flood in, the scatter collapses. The estimator converges with absolute confidence to the wrong value.

### [B09] 4 ANCHOR PAYOFF: Gallup's Representative Sample (Manim)
*(Visual: Gallup's 50,000 sample: wider scatter but centered directly on the true bullseye E[theta_hat] = theta)*
**Liam**: Gallup's sample was fifty times smaller, so its individual scatter was wider. But his quota frame was representative — his aim was centered on the true population mean.

### [B10] 3 ONE FLAG: Unobserved Selection Cannot Be Scaled Away (Manim)
*(Visual: The One Flag banner: Correcting sampling bias requires knowing selection probabilities; unobserved exclusions cannot be solved by data scale)*
**Liam**: One flag — you can only correct a skewed sample if you know who was excluded; when selection bias is unobserved in your training pipeline, no amount of scaling will fix it.

### [B11] 5 DIRECTION A: Volume Does Not Prove Accuracy (Manim)
*(Visual: Direction A: Massive Sample Volume ≠ Ground Truth Accuracy struck through with heavy terracotta bar)*
**Liam**: So in one direction, massive data volume and tight confidence intervals do not prove an estimate is accurate. If the collection frame is skewed, big data only measures the skew with extreme precision.

### [B12] 5 DIRECTION B: Small Samples Can Be Unbiased (Manim)
*(Visual: Direction B: Small Sample Size ≠ Systematic Inaccuracy. Representative small samples beat massive skewed datasets)*
**Liam**: And in the other direction, a smaller dataset does not mean an estimate is untrustworthy. A well-framed small sample will always defeat millions of biased observations.

### [BCRY] 6 CARRY-OUT: The Single Sentence (Remotion)
*(Visual: Remotion WantQuote with the carry-out sentence in elegant serif typography)*
**Liam**: More data only narrows the scatter around the wrong answer — when your sampling frame is biased, volume gives you convergence to an error with absolute confidence.

### [BHTF] Your Turn Handoff (Remotion)
*(Visual: Remotion ClaudeComposerAsk displaying paste-ready prompt for Claude)*
**Liam**: Your turn. Here's the prompt — read it with me. Audit a dataset or training pipeline in your organization. Identify the sampling frame: what systematic exclusion is present, and does collecting more data fix the bias or just make the error more confident? Liam, in for Bear.

### [BOUT] Outro (Remotion)
*(Visual: Remotion OutroCTA with Humanitarians AI branding and title restatement)*
**Liam**: Why 2.4 Million Answers Lost to 50,000. Liam, in for Bear.
