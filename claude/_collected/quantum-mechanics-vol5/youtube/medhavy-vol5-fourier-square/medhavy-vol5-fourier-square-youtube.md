**Title:** Build a Fourier Square Wave with Claude Code + Manim

The Gibbs overshoot at a discontinuity stubbornly stays at 9% no matter how many harmonics you add — the simulation builds the square wave term by term and shows the overshoot is a fundamental property, not a bug.

**What you'll learn:** How to use Claude Code + Manim to build a working physics simulation — prompt → read the generated script → run → check → change. Each video in this series teaches the workflow; the physics is the running example.

**The physics:** A square wave decomposes as f(x) = Σ (4/nπ) sin(nπx/L) summed over odd n. The Fourier coefficient 4/nπ is the entire physics. The simulation verifies two results: at the discontinuity edge the N = 9 partial sum overshoots the true value by ≈ 9% (converging to 1.089, not 1.000), and at x = L/2 the partial sum converges to exactly 1.000 — the Leibniz series for π/4.

**From:** Quantum Mechanics Vol. 5 · Chapter 5 — Fourier Series and the Wave Equation

---
Physics with Claude — building physics simulations with Claude Code + Manim.
Medhavy · AI-powered intelligent learning systems · @MedhavyAI · medhavy.com

#QuantumMechanics #PhysicsSimulation #ClaudeCode #Manim #FourierSeries #GibbsPhenomenon
