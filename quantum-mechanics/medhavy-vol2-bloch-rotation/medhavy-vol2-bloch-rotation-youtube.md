**Title:** Build a Bloch Sphere Sim with Claude Code + Manim

The parameterization uses θ/2, not θ — get that wrong and every state lands in the wrong place — the simulation places spin-up at the north pole and the |+⟩ state on the equator and checks both with probability calculations.

**What you'll learn:** How to use Claude Code + Manim to build a working physics simulation — prompt → read the generated script → run → check → change. Each video in this series teaches the workflow; the physics is the running example.

**The physics:** A qubit state is parameterized as |ψ⟩ = cos(θ/2)|↑⟩ + e^(iφ)sin(θ/2)|↓⟩, with Bloch vector (sin θ cos φ, sin θ sin φ, cos θ). The simulation verifies two predictions: |↑⟩ at θ = 0 (north pole) gives P(spin-up along z) = cos²(0) = 1, and the equatorial state |+⟩ at θ = π/2 gives ⟨Z⟩ = cos(π/2) = 0, confirming equal odds of spin-up and spin-down.

**From:** Quantum Mechanics Vol. 2 · Chapter 7 — Spin and the Bloch Sphere

---
Physics with Claude — building physics simulations with Claude Code + Manim.
Medhavy · AI-powered intelligent learning systems · @MedhavyAI · medhavy.com

#QuantumMechanics #PhysicsSimulation #ClaudeCode #Manim #BlochSphere #Qubit
