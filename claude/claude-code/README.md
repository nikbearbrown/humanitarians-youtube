# Claude Code

Claude Code installation, commands, `CLAUDE.md`, subagents, coding workflows, MCP setup within Code, and unattended execution.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Claude Code

This folder organizes **227 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

## Projects in this folder

- [Agents That Remember Memory Store](./agents-that-remember-memory-store/)
- [Ai Creative Work Belongs To Nobody](./ai-creative-work-belongs-to-nobody/)
- [Boondoggle Score](./boondoggle-score/)
- [Build Chapter Mapping](./build-chapter-mapping/)
- [Ch06 Lecture](./ch06-lecture/)
- [Claude Lectures Ch04 Lecture](./claude--lectures--ch04-lecture/)
- [Claude Agentic Ai Lectures Ch04 Lecture](./claude-agentic-ai--lectures--ch04-lecture/)
- [Claude Code Action Natural Trigger Review Counting Check](./claude-code-action-natural-trigger-review-counting-check/)
- [Claude Code Base Action Turn Budget Stops Runaway Agent](./claude-code-base-action-turn-budget-stops-runaway-agent/)
- [Claude Code Coding Assistant Deliberately Refuses Write](./claude-code-coding-assistant-deliberately-refuses-write/)
- [Claude Code For Students Lectures Ch02 Lecture](./claude-code-for-students--lectures--ch02-lecture/)
- [Claude Code For Students Lectures Ch04 Lecture](./claude-code-for-students--lectures--ch04-lecture/)
- [Claude Code For Students Lectures Ch05 Lecture](./claude-code-for-students--lectures--ch05-lecture/)
- [Claude Code For Students Lectures Ch06 Lecture](./claude-code-for-students--lectures--ch06-lecture/)
- [Claude Code For Students Lectures Ch07 Lecture](./claude-code-for-students--lectures--ch07-lecture/)
- [Claude Code For Students Lectures Ch08 Lecture](./claude-code-for-students--lectures--ch08-lecture/)
- [Claude Code For Students Lectures Ch09 Lecture](./claude-code-for-students--lectures--ch09-lecture/)
- [Claude Code For Students Lectures Ch10 Lecture](./claude-code-for-students--lectures--ch10-lecture/)
- [Claude Code For Students Lectures Ch11 Lecture](./claude-code-for-students--lectures--ch11-lecture/)
- [Claude Code For Students Lectures Ch12 Lecture](./claude-code-for-students--lectures--ch12-lecture/)
- [Claude Code For Students Lectures Ch13 Lecture](./claude-code-for-students--lectures--ch13-lecture/)
- [Claude Code For Students Lectures Ch14 Lecture](./claude-code-for-students--lectures--ch14-lecture/)
- [Claude Code For Students Youtube Claude Liam Solve Verify Asymmetry](./claude-code-for-students--youtube--claude-liam-solve-verify-asymmetry/)
- [Claude Code For Teachers Lectures Ch01 Lecture](./claude-code-for-teachers--lectures--ch01-lecture/)
- [Claude Code For Teachers Lectures Ch02 Lecture](./claude-code-for-teachers--lectures--ch02-lecture/)
- [Claude Code For Teachers Lectures Ch04 Lecture](./claude-code-for-teachers--lectures--ch04-lecture/)
- [Claude Code For Teachers Lectures Ch05 Lecture](./claude-code-for-teachers--lectures--ch05-lecture/)
- [Claude Code For Teachers Lectures Ch06 Lecture](./claude-code-for-teachers--lectures--ch06-lecture/)
- [Claude Code For Teachers Lectures Ch08 Lecture](./claude-code-for-teachers--lectures--ch08-lecture/)
- [Claude Code For Teachers Lectures Ch09 Lecture](./claude-code-for-teachers--lectures--ch09-lecture/)
- [Claude Code For Teachers Lectures Ch10 Lecture](./claude-code-for-teachers--lectures--ch10-lecture/)
- [Claude Code For Teachers Lectures Ch11 Lecture](./claude-code-for-teachers--lectures--ch11-lecture/)
- [Claude Code For Teachers Lectures Ch13 Lecture](./claude-code-for-teachers--lectures--ch13-lecture/)
- [Claude Code For Teachers Lectures Ch15 Lecture](./claude-code-for-teachers--lectures--ch15-lecture/)
- [Claude Code For Teachers Lectures Ch16 Lecture](./claude-code-for-teachers--lectures--ch16-lecture/)
- [Claude Code Four Agents Scoring Same Bug](./claude-code-four-agents-scoring-same-bug/)
- [Claude Code Monitoring Guide Doubling Claude Code Session Time](./claude-code-monitoring-guide-doubling-claude-code-session-time/)
- [Claude Code Monitoring Guide Typing One Word Multiply Api](./claude-code-monitoring-guide-typing-one-word-multiply-api/)
- [Claude Code Security Review Same Eval Real Bug One](./claude-code-security-review-same-eval-real-bug-one/)
- [Ai Creative Work Belongs To Nobody](./claude-liam-ai-creative-work-belongs-to-nobody/)
- [Ai Speed Paradox](./claude-liam-ai-speed-paradox/)
- [Bcg Matrix Portfolio](./claude-liam-bcg-matrix-portfolio/)
- [Black Scholes Put Pricer](./claude-liam-black-scholes-put-pricer/)
- [Bond Duration Pricer](./claude-liam-bond-duration-pricer/)
- [Boondoggle Score](./claude-liam-boondoggle-score/)
- [Build Chapter Mapping](./claude-liam-build-chapter-mapping/)
- [Capm Alpha Calculator](./claude-liam-capm-alpha-calculator/)
- [Case Structuring Coach](./claude-liam-case-structuring-coach/)
- [Claude Liam Cli 00 Wave Packet Spreading](./claude-liam-claude-liam-cli-00-wave-packet-spreading/)
- [Claude Liam Cli 01 Uncertainty Minimizer](./claude-liam-claude-liam-cli-01-uncertainty-minimizer/)
- [Claude Liam Cli 02 Infinite Well Superposition](./claude-liam-claude-liam-cli-02-infinite-well-superposition/)
- [Claude Liam Cli 03 Coherent State Oscillator](./claude-liam-claude-liam-cli-03-coherent-state-oscillator/)
- [Claude Liam Cli 04 Uncertainty Ensemble](./claude-liam-claude-liam-cli-04-uncertainty-ensemble/)
- [Claude Liam Cli 05 Spherical Harmonics Cone](./claude-liam-claude-liam-cli-05-spherical-harmonics-cone/)
- [Claude Liam Cli 06 Stern Gerlach Sequential](./claude-liam-claude-liam-cli-06-stern-gerlach-sequential/)
- [Claude Liam Cli 07 Hydrogen Radial Density](./claude-liam-claude-liam-cli-07-hydrogen-radial-density/)
- [Claude Liam Cli 08 Helium Exchange Splitting](./claude-liam-claude-liam-cli-08-helium-exchange-splitting/)
- [Claude Liam Cli 08 Two Particle Symmetry](./claude-liam-claude-liam-cli-08-two-particle-symmetry/)
- [Claude Liam Cli 09 Asymptotic Perturbation](./claude-liam-claude-liam-cli-09-asymptotic-perturbation/)
- [Claude Liam Cli 09 Hydrogen Stark Effect](./claude-liam-claude-liam-cli-09-hydrogen-stark-effect/)
- [Claude Liam Cli 10 Rabi Vs Perturbation Theory](./claude-liam-claude-liam-cli-10-rabi-vs-perturbation-theory/)
- [Claude Liam Cli 11 Geiger Nuttall Alpha Decay](./claude-liam-claude-liam-cli-11-geiger-nuttall-alpha-decay/)
- [Claude Liam Cli 11 Tunneling Wave Packet](./claude-liam-claude-liam-cli-11-tunneling-wave-packet/)
- [Claude Liam Cli 11 Wkb Vs Exact Transmission](./claude-liam-claude-liam-cli-11-wkb-vs-exact-transmission/)
- [Claude Liam Cli 12 Chsh Bell Inequality](./claude-liam-claude-liam-cli-12-chsh-bell-inequality/)
- [Claude Liam Cli 13 Bloch Decoherence](./claude-liam-claude-liam-cli-13-bloch-decoherence/)
- [Claude Liam Cli 13 Nv Center Odmr](./claude-liam-claude-liam-cli-13-nv-center-odmr/)
- [Claude Liam Cli Em Faraday Cage](./claude-liam-claude-liam-cli-em-faraday-cage/)
- [Claude Unsupervised](./claude-liam-claude-unsupervised/)
- [Claudes C Compiler Ai Coding Limit](./claude-liam-claudes-c-compiler-ai-coding-limit/)
- [00 Wave Packet Spreading](./claude-liam-cli-00-wave-packet-spreading/)
- [01 Uncertainty Minimizer](./claude-liam-cli-01-uncertainty-minimizer/)
- [02 Infinite Well Superposition](./claude-liam-cli-02-infinite-well-superposition/)
- [03 Coherent State Oscillator](./claude-liam-cli-03-coherent-state-oscillator/)
- [04 Uncertainty Ensemble](./claude-liam-cli-04-uncertainty-ensemble/)
- [05 Spherical Harmonics Cone](./claude-liam-cli-05-spherical-harmonics-cone/)
- [06 Stern Gerlach Sequential](./claude-liam-cli-06-stern-gerlach-sequential/)
- [07 Hydrogen Radial Density](./claude-liam-cli-07-hydrogen-radial-density/)
- [08 Helium Exchange Splitting](./claude-liam-cli-08-helium-exchange-splitting/)
- [08 Two Particle Symmetry](./claude-liam-cli-08-two-particle-symmetry/)

<!-- END BRUTALIST REBUILD GUIDE -->
