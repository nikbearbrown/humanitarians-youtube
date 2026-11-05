# PEDAGOGY.md — spinning-skater (Chapter 11.3, Conservation of Angular Momentum)

## Concept
With negligible external torque, a skater's angular momentum L = I omega is
conserved. Pulling her arms in lowers I, so omega rises by the factor I/I'.
Her rotational kinetic energy K = (1/2) I omega^2 = L^2 / (2I) therefore also
rises by I/I'; the extra energy is the work her muscles do pulling her hands
inward.

## Physics check (against 11-angular-momentum/3-conservation-of-angular-momentum.mdx)
- "The net torque on her is very close to zero because there is relatively little friction between her skates and the ice" -> narration "the ice exerts almost no torque on her".
- Fig. 11.15: "Her rate of spin increases greatly when she pulls in her arms, decreasing her moment of inertia. The work she does to pull in her arms results in an increase in rotational kinetic energy." -> B02/B03.
- Textbook: K'_Rot = K_Rot (I / I'). Narration: "the kinetic energy grows by the same factor" (same factor as omega). Correct, since omega'/omega = I/I' too.
- "the skater's arms do not move in a perfect circle — they spiral inward. This work causes an increase in the rotational kinetic energy" -> "Each hand tends to keep moving in a straight line, so she must pull it inward, and the work her muscles do is exactly the kinetic energy she gains." The inward pull has a component along the spiralling hand's velocity, so it does positive work.
- Model in script: I(r) = I_body + 2 m r^2 with I_body = 1, 2m = 1, r: 1.5 -> 0.5 (scene units), so I: 3.25 -> 1.25, ratio 2.6. omega(t) = L / I(r(t)) with L fixed; KE bar height proportional to 1/I(r(t)); I bar proportional to I; all driven by the same tracker r, so the bars and the arm length share one interpolator.
- Direction: spin is counterclockwise viewed from above, so L points up out of the page (right-hand rule), shown as a dot-in-circle symbol on the card.

## Audit against the bar
- **Single tension:** she speeds up with no external push; where does the energy come from?
- **Single resolution:** L is fixed, K = L^2/2I rises as I falls, and the energy is supplied by her muscle work.
- **One primary visual object:** the skater (top-down).
- **<=6 elements per scene:** skater, hand circle/radius arrow, equation card, I/omega bars (B02) or KE bar (B03), work arrows, one top label.
- **Self-contained:** needs only L = I omega and K = (1/2) I omega^2, both stated on screen.

## Exclusions honored
No derivation of I (only "grows with the square of the distance"), no
planetary/solar-system formation example.

## Style deviations from storyboard
Storyboard named a black/white/red/blue/yellow brutalist palette. Locked
medhavy style: white ground; radius arrow CRIMSON, spin-rate curl INK, KE bar
GOLD with ink outline, I bar SLATE, omega bar TEAL, skater with a teal dress
and skin-tone arms/head. Outro labels appear instantly (no fade) per the
storyboard's snap-in note.

## VERDICT: PASS
