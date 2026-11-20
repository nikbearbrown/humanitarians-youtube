# Friction Log: Week 9 — Security & Exploitation in Physical AI: Native `MuJoCo` Coaster-Patch Pipeline and First Patched `LIBERO` Rollouts

**Project:** Security & Exploitation in Physical AI (VLA Adversarial Robustness)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Nov 16 to Nov 22, 2026

---

## 1. Focus of the week

- Building the rendering bridge between the differentiable attack loop and native `LIBERO` evaluation: a `kornia` patch projector that reports `OpenVLA`'s `16 x 16` token coverage.
- Injecting the patch as a real, visual-only `MuJoCo` coaster with a 90%-area textured face on a dark-brown base.
- Making the coaster survive `LIBERO`'s hard resets by integrating it into `run_closed_loop_rollout()` rather than a test-only fixture.
- Extending the trajectory recorder with `--patch [PNG]` and recording the first six `LIBERO-Object` episodes with the coaster and a fixed unoptimized patch.
- Keeping the claim boundary explicit: these recordings validate scene plumbing and asset survival, not an adversarial steering result.

## 2. What was tried, and what was expected

- **Project the coaster corners with `CoasterSpec.corners_world()` and composite the patch with `render_patch()`.** Expectation: the projected quad would align with the native `MuJoCo` render and the same PNG would occupy the same pixels in both paths.
- **Orient the coaster with a degree Euler yaw in the arena XML.** Expectation: `euler="6.875 0 0"` would produce the intended `6.875°` rotation, matching the hand-authored test fixtures.
- **Map a 2D PNG onto the box face with `texuniform="true"` and `texrepeat="1 1"`.** Expectation: the full patch image would span the top face.
- **Compare the `kornia` composite and the native texture by raw RGB.** Expectation: if the geometry was correct, the two images would match pixel-for-pixel.
- **Append the coaster once at environment construction.** Expectation: the coaster would remain present for every episode in the rollout batch.
- **Record two successful patched episodes per task with the unoptimized PNG.** Expectation: the six episodes would show the textured coaster in the initial frames after the resets between tasks.

## 3. Points of resistance, and next steps taken

### The coaster yaw was five times too large
- **Resistance:** the rendered coaster appeared rotated far more than the specified `0.12` rad. `robosuite`'s robot `models/assets/base.xml` sets `<compiler angle="radian">`, so the arena's degree `euler` value was reinterpreted in radians (`6.875` became about `33.9°`). The earlier `[1, 0, 3, 2]` corner reorder was a downstream artifact of this error, not a real UV rule.
- **Next step:** emit a `quat` for the coaster body so orientation is independent of the compiler's angle unit, and remove the corner permutation so projected TL, TR, BR, BL corners are used directly after the horizontal image mirror.

### `texuniform` showed only a fragment of the patch
- **Resistance:** with `texuniform="true"`, only a small central window of the patch PNG was visible and it appeared rotated. In `MuJoCo 3.1.6`, `settexture` multiplies the texture scale by the geom half-size when `texuniform` is set.
- **Next step:** omit `texuniform` from the material; with `texrepeat="1 1"` the full PNG now spans the patch face.

### Composite and native rendering could not be compared by absolute RGB
- **Resistance:** the offline `kornia` composite inserts patch pixels without `MuJoCo` shading, while the native texture is lit. Raw RGB differed even when geometry and orientation were correct (for example, native cyan rendered near `(0.12, 0.92, 0.79)`).
- **Next step:** validate geometry and orientation with chromaticity instead of absolute color. The integration test now requires a mean per-pixel chromaticity difference below `0.03` inside an eroded patch mask, while still checking the projected `0.90` area ratio and `sqrt(0.9)` side ratio.

### A coaster added at construction disappeared on reset
- **Resistance:** `ControlEnv.reset()` uses `hard_reset=True`, re-running `_load_model()` and `_load_fixtures_in_arena`; a coaster appended once at construction was dropped before the first recorded step, and projected corners computed before `set_init_state` did not match the reset pose.
- **Next step:** move coaster injection into `run_closed_loop_rollout()` as a temporary `_load_fixtures_in_arena` override, restored in a `finally` block, and derive the coaster support height per problem (`table_top_abs` for tabletop tasks, `floor_body` for `LIBERO_Floor_Manipulation`). The recorder then recomputes coverage from each rendered frame rather than caching construction-time corners.

### Small surface mismatches kept breaking the contract
- **Resistance:** `sim.model` is `robosuite`'s binding wrapper, so `mujoco.mj_name2id` is not usable; `LIBERO-Object` Task 0 compiles `EmptyArena` and has no `table_top_abs`; and repeated insertion required namespaced, de-duplicated body/texture/material names to avoid XML collisions.
- **Next step:** use `sim.model.camera_name2id(...)`, branch on the available support surface, and namespace every generated element with an `h1_coaster_` prefix plus a de-duplication suffix. All four insertion tests now compile the generated MJCF before asserting placement.

## 4. AI and other contributions: accepted, changed, rejected

### Dev (Peer Review)
- **Accepted:** no new peer review landed this week. Dev's standing coordinate-free constraint from the Week 6 review still shaped the work: `render_patch()` only reports coverage of the patch's own cells, so no target or decoy object coordinates enter the projection API.
- **Changed:** none this week; there was no new review to revise against.
- **Rejected:** none.

### AI Research Assistant
- **Accepted:** AI assistance was used for documentation and consistency checks across `README.md`, `WORK_PROGRESS.md`, `work_report.md`, this friction log, and `HOURS.md`, and for reviewing the `kornia`/`MuJoCo` coordinate conventions.
- **Changed:** a first degree-Euler coaster orientation was replaced with a quaternion after the radian `<compiler>` behavior was identified; the absolute-RGB comparison was replaced with a lighting-invariant chromaticity check.
- **Rejected:** caching projected corners at environment construction, because hard resets rebuild the model and invalidate both the coaster pose and any cached quad.

## 5. Understood now, and still unresolved

### Understood
- **Two-stage rendering is now concrete:** the training loop can warp a trainable patch through `kornia` and report the exact `16 x 16` `OpenVLA` cells it covers, while native evaluation uses the same PNG on a real coaster face.
- **Native coaster orientation must be unit-safe:** `robosuite`'s radian compiler makes Euler yaw fragile across task and robot XML; a quaternion removes the ambiguity.
- **Texture mapping depends on engine defaults:** `texuniform` changes scale in `MuJoCo 3.1.6`, and box UV order is fixed by the engine (`u = (x/hx + 1)/2`, `v = (1 - y/hy)/2`), so no corner permutation is needed once yaw is correct.
- **Hard resets require hook-based injection:** the coaster must be re-added by `_load_fixtures_in_arena` on every model rebuild, and the recorded frames already show it surviving the resets between tasks.
- **Appearance must be compared in chromaticity:** offline compositing and native lighting differ in absolute RGB, but geometry and quadrant orientation can still be validated robustly.

### Unresolved (To Be Tested in Weeks 10–12)
- **Differentiable-to-native transfer under optimization:** whether a patch optimized through the `kornia` warp retains its effect when baked onto the native lit coaster in closed-loop evaluation.
- **Attention concentration under changing viewpoints:** whether the Way 1 objective can keep `Llama-2` text-to-vision mass on the patch's cells as the camera moves during a rollout.
- **The Way 2 `SigLIP + DINOv2` token path:** the post-projector hook for Auto-Feature Copy is still unspecified in code.
- **`LIBERO-Spatial` patched rollouts:** only the `LIBERO-Object` patched condition has been recorded.
- **Whether native shading must be modeled:** the chromaticity gap is controlled in tests, but closing it in training may matter once the patch is optimized rather than random.
- **Any attack claim:** no steering, smoothness, or success-rate metric exists yet; the six episodes used an unoptimized patch under benign instructions.
