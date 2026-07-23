**Title:** Build Quantum Gates on the Bloch Sphere with Claude Code + Manim

The Hadamard gate moves the qubit from the north pole to the equator in a single matrix multiply — the simulation animates H then S on the Bloch sphere and verifies H·H = I by watching the state return to |0⟩.

**What you'll learn:** How to use Claude Code + Manim to build a working physics simulation — prompt → read the generated script → run → check → change. Each video in this series teaches the workflow; the physics is the running example.

**The physics:** H = (1/√2)[[1,1],[1,−1]] maps |0⟩ to |+⟩ = (|0⟩+|1⟩)/√2, moving the Bloch vector from the north pole (θ=0) to the equator (θ=π/2, φ=0). The S gate S = [[1,0],[0,i]] then rotates 90° about z, taking |+⟩ to |i⟩ = (|0⟩+i|1⟩)/√2 (equator, φ=π/2). The simulation verifies both rotations and confirms H·H = I — applying Hadamard twice returns the state to |0⟩ exactly.

**From:** Quantum Mechanics Vol. 4 · Chapter 4 — Quantum Gates and Circuits

---
Physics with Claude — building physics simulations with Claude Code + Manim.
Medhavy · AI-powered intelligent learning systems · @MedhavyAI · medhavy.com

#QuantumMechanics #PhysicsSimulation #ClaudeCode #Manim #QuantumGates #QuantumComputing
