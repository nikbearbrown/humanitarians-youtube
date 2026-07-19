# PROMPTS — yield-curve-bootstrap

## B01 — PROBLEM slate
Visual: coupon bond cash flows, then stripped zero-coupon bonds
Caption: "Coupon bonds in. Zero rates out. Bootstrapping."

## B06 — SUMMARY slate
Two curves: original z5=5.42% vs repriced z5=7.21%
z10 also shifts: 6.28% -> 7.05%
Caption: "Each bond is a lever. Reprice one, move all longer rates."

## B07 — NEXT STEPS slate
Nelson-Siegel: f(t) = beta0 + beta1*(1-exp(-t/tau))/(t/tau) + beta2*(...)
4 parameters: level, slope, curvature, decay

## B08 — NEXT STEPS 2 slate
Swap rate = fixed rate where fixed PV = floating PV
floating leg PV = 1 - disc_factor(T)
fixed leg PV = swap_rate * sum(disc_factors)
