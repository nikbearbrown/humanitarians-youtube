# SHOTLIST — medhavy-vol1-packet-spread

## Beat Histogram
B00: GRAPHIC remotion (MedhavyOpen)
B01: GRAPHIC remotion (MedhavyTerminalAsk)
B02: GRAPHIC remotion (MedhavyCodeBlock)
B03: GRAPHIC manim (B03_PacketRun)
B04: GRAPHIC remotion (MedhavyTerminalAsk)
B05: GRAPHIC remotion (MedhavyOutro)

## Act Map
B00: MEDHAVY INTRO
B01: PACKET SPREAD — PROMPT
B02: PACKET SPREAD — SCRIPT
B03: PACKET SPREAD — RUN (Manim: Gaussian spreading + σ(t) curve)
B04: PACKET SPREAD — CHANGE
B05: MEDHAVY OUTRO

## Color Law
TEAL: Gaussian envelope at t=0, σ(t) curve
CRIMSON: packet at t=τ (broadened), doubling annotation
INK: all Text()

## Exclusions
No Fourier transform derivation on screen, no momentum-space
panel, no complex wave function oscillations, no full WKB.

## Slot: B03 — Manim RUN scene
Source: own (vox_scenes.py)
Visual: Two panels side by side.
  Left panel: σ(t) vs t curve (TEAL) showing growth from σ₀ to σ₀√2 at t=τ.
    Dot on curve at t=τ (CRIMSON). Dotted horizontal at σ₀√2.
  Right panel: Gaussian |Ψ|² at t=0 (TEAL) and t=τ (CRIMSON).
    Both normalized. Shows broadening visually.
  Header: "Wave Packet Spreading  τ = 17.3 fs"
  Chips: "v_g = ℏk₀/m" (TEAL), "σ(τ) = √2·σ₀" (CRIMSON)
