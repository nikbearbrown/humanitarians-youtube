# PEDAGOGY.md — sonic-boom (Chapter 17, Shock Waves)

## Concept
As v_s -> v the moving-source Doppler formula diverges because every
wavefront arrives at a point ahead at the same instant. For v_s > v the
fronts are tangent to a cone of half angle sin(theta) = v/v_s = 1/M: the
shock wave. The cone travels with the plane; its ground intersection sweeps
along behind the plane, so each listener hears one boom after the plane
has passed, and the boom continues for the whole supersonic flight.

## Audit against the bar
- **Single tension:** the formula predicts an infinite pitch at Mach 1 -- what really happens?
- **Single resolution:** the waves stop arriving one after another and pile into a single shock front (cone) that sweeps the ground once per listener; the plane stays ahead of it.
- **One primary visual object:** the plane and its wavefront pattern, continuous from M = 0.5 to M = 1.5 (one unbroken acceleration).
- **<=6 elements per scene:** B00: plane, rings, formula, M readout, f_o readout. B01: + cone/wall (5-6). B02: formula and f_o readout fade; plane, rings, cone, M readout, sin(theta) block, theta arc = 6 (portrait drops the M readout). B03: block/arc/readout fade; plane, faint rings, cone, ground with listeners, boom bursts, below-plane marker = 6. B04: + summary (bursts and marker are part of the ground scene).
- **Self-contained:** recalls the Doppler formula on screen; defines M.

## Physics check (against 17-sound/8-shock-waves.mdx)
- f_o = f_s v/(v - v_s) for an approaching source; denominator -> 0 as v_s -> v, f_o -> infinity (section text). Readout f_o/f_s = 1/(1 - M) computed live from the drawn M; replaced by "-> infinity" at M >= 0.985.
- At M = 1 "each successive wave interferes with the previous one ... the observer gets them all at the same instant" (section) -- narrated as such; rings computed exactly (centre moves at v_s, radius grows at v) so at M = 1 all fronts touch the nose.
- M = v_s/v (Eq. 17.21). Cone half angle sin(theta) = v/v_s = 1/M (Eq. 17.22); at M = 1.5, theta = 41.8 deg, displayed "approximately 42 deg". Cone lines are drawn from the formula and are verifiably tangent to the simulated rings (distance from ring centre to line = M r sin(theta) = r).
- "The sonic boom occurs as the shock wave sweeps along the ground", not at the moment of breaking the barrier (section's misconception note) -- stated in B03. Listeners hear it after the plane has passed (section: observers "often do not see the aircraft ... because it has passed by before the shock wave reaches them"). Boom bursts are triggered exactly when the cone's lower edge reaches each listener.
- Storyboard said the pilot "has nothing to hear"; rephrased to the defensible claim that the plane's own boom never reaches it (the plane is at the cone's apex, ahead of all its fronts). Storyboard formula used "c" for sound speed; replaced by the textbook's v, v_s. "It's not a sound wave anymore" removed (a shock wave is a sound disturbance -- constructive interference).
- The section notes two shocks (nose and tail); only the nose shock is drawn, the mechanism being identical -- not claimed otherwise.
- Palette remap: teal wavefronts (storyboard cyan), gold cone with ink outline (storyboard yellow), crimson infinity and booms (storyboard red).

## Exclusions honored
No bow-wake derivation, no pressure calculations, no reentry physics.

## Style compliance
Formal narration; am_michael 0.85; plane-frame camera keeps the motion continuous without cuts; portrait question card from B00Q.

## VERDICT: PASS
