# PROMPTS - week9 (Nov 16)

No external generative image or video models are used. All approved visual beats render locally from Remotion scene props.

## B00 - cold-open question

> Can we move an adversarial patch out of the optimizer and into a real LIBERO scene without claiming an attack result yet?

## B01 - claim-boundary correction

> Correct "a random patch steers the robot" to "a random patch tests the geometry," and show the tempting claim beside the actual one.

## B02 - two-stage rendering

> Input: coaster world corners. Phases: camera calibration, Kornia warp, alpha reduction to 16x16 cells, native bake. Output: coverage mask plus a native MuJoCo coaster.

## B03 - scene terms

> Define three terms: the brown base box, the 90%-area patch face, and visual-only geoms that leave task physics unchanged.

## B04 - executed evidence

> Show 9/9 local smoke tests, a 0.90 projected area ratio, and a 0.03 mean chromaticity limit as measured rows, sourced from the smoke suite.

## B05 - result artifact

> Six LIBERO-Object episodes, two per task, all with finite actions and states and visible patch after resets. End on the boundary: no steering success claimed.

## B06 - viewer handoff

> Design a test that proves a textured prop survives every environment reset without changing task physics. Include a rendering check, a collision check, and a reset check.
