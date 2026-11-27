# FACTCHECK — Week 2: Learning the Physics Engine

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about learning how the physics simulations inside Medhavy's Physics Volume 1 textbook work. The voice you're hearing is Liam, an A I narrator, reading my script. Week two, I studied the physics simulations that live inside the textbook.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: I expected a game-style engine that simulates every frame. What I found draws the answer directly: it solves the motion equations once and plots the result. Knowing which kind you have changes everything.

## B02 · FRAMEWORK
- Source: physics-vol-1/USER_GUIDE.md; STAKEHOLDER_OVERVIEW.md
- Narration: Physics Volume One is its own app, seventeen chapters with simulations embedded in the pages. There are four kinds. The Projectile Explorer takes a launch angle, a speed and gravity, then draws the path and marks the peak and range. The others show circular motion vectors, plotted functions, and motion split into x and y.

## B03 · MECHANISM
- Source: physics-vol-1/ARCHITECTURE.md (directory reference)
- Narration: The architecture doc shows the split. The physics lives in a lib folder: kinematics for projectiles, circular motion, and a function plotting engine. The drawing lives in React components built with D3. That separation is the design choice I liked most. You can check the math without ever opening a browser.

## B04 · WORKED_EXAMPLE
- Source: my own script: week-2/code/projectile.py (run locally)
- Narration: To feel the difference, I wrote a tiny script of my own. Not Medhavy's code, my re-derivation. Same launch, two methods. The closed-form answer says forty point eight two metres. Stepping time forward lands at forty two with big steps, and forty one with small ones. Stepping only approaches the truth. The formula is just there.

## B05 · FALSIFIABILITY
- Source: physics-vol-1/ARCHITECTURE.md; USER_GUIDE.md; my projectile.py
- Narration: So which is better? Neither, in general. A game engine steps time because it has to handle collisions and messy forces. A textbook asks clean questions with exact answers, so solving once is faster and never drifts. The docs don't mention collisions or time steps at all. That absence told me which kind this is.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Week two, in short. Four simulation types, built with D3. Math and drawing kept apart. And the engine solves motion in closed form rather than stepping through time, which my own little test made obvious. Next week, I went from the docs into how the pieces connect.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude to compute a projectile's range two ways, the formula and a time-stepping loop, with three step sizes, and to explain when an engine must step time. Run the code yourself. Watch the error shrink as the step gets smaller, and ask why it never quite reaches zero.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Week 2: Learning the Physics Engine. Shubham L., for Humanitarians A I. Thanks for watching.

## Limits stated in the film
- Claims are limited to what the cited files say; opinions are labelled as proposals on screen.
