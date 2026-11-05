# PEDAGOGY.md — resonance (Chapter 15, 15.6 Forced Oscillations)

## Concept
A driven, lightly damped oscillator responds weakly when the driving
frequency is far from its natural frequency f_0, and its amplitude grows
cycle after cycle — up to a damping-limited maximum — when driven at f_0.
A small-amplitude drive can then produce a large-amplitude response.

## Audit against the bar
- **Single tension:** small footsteps, large bridge sway.
- **Single resolution:** timing, not force size: driving at the natural frequency (resonance).
- **One visual object:** the spring-mass oscillator and its position trace (B01-B04); the bridge is the hook/callback only and is gone before the rig appears.
- **<=6 elements per scene:** support/drive bar, spring, mass, chart trace, frequency label, summary.
- **Self-contained:** needs only the idea of a natural frequency.

## Physics check against 15.6
- Natural frequency defined as in the text: "the frequency at which a system would oscillate if there were no driving and no damping force."
- Motion is simulated, not hand-drawn: Eq. 15.27, -kx - b dx/dt + F_0 sin(ωt) = m d²x/dt², with the drive supplied by moving the top of the spring (F = k s(t), as with the paddle ball held by a moving finger, Fig. 15.30). Light damping (γ = b/m = 0.25 s⁻¹) with ω_0 = 2π/1.6 s.
- Off resonance (ω = 1.7 ω_0) the steady amplitude is small (Eq. 15.29 denominator large); at ω = ω_0 "the ball's oscillations increase in amplitude with each oscillation for as long as you drive it", saturating at the damping-limited maximum (A_max = F_0/(bω)). Drive amplitude is identical in B02 and B03 — "a small-amplitude driving force can produce a large-amplitude response".
- "Energy is transferred ... less efficiently" off resonance and "efficiency of energy transfer ... is best at resonance" (15.6) — narration's "some add energy, others take it away" is the qualitative version.
- Hook: the textbook's own example (Fig. 15.34): London Millennium Footbridge, "People continuing to cross reinforced the oscillation's amplitude", closed for about two years. Storyboard's soldiers-breaking-step hook is not in the textbook and was replaced. The sway is drawn lateral (top view), as it was.

## Exclusions honored
No Q-factor math, no Laplace/Fourier, no over/underdamped cases. Storyboard's doodle cold-open and logo replaced by the locked clean, unbranded medhavy style.

## Bug patterns checked
- Drive phase is accumulated (φ += ω dt), so switching frequency never jumps the support.
- Chart trace is aligned with the mass's height so the response reads directly; trace clipped to the chart window.
- Every mobject stored on self; bridge group faded out before the rig appears.
- Portrait: rig left, narrow chart right, labels above, nothing in the caption band.

VERDICT: PASS
