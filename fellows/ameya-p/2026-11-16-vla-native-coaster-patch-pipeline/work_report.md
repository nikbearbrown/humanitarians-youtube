# Security & Exploitation in Physical AI: Native `MuJoCo` Coaster-Patch Pipeline and First Patched `LIBERO` Rollouts

---

Volunteer Name: Ameya Padwad  
Report Week: Nov 16 to Nov 22, 2026

## 1. Introduction

This week moved the **Security & Exploitation** exploration of stealthy trajectory steering in Vision–Language–Action (VLA) models from attention observability to the physical rendering path the attack actually needs. The prior week exposed `OpenVLA-7B`'s real `Llama-2` text-to-vision attention over the `16 x 16` visual-token grid. That measurement is only useful if an adversarial patch can be optimized in the same geometry that `LIBERO` renders during closed-loop evaluation, so this week built and validated that bridge: a differentiable `kornia` patch projector, a native `MuJoCo` coaster that carries the patch into the real scene, and a rollout recorder that keeps the coaster present across hard environment resets.

The week's completed work covered the following:

1. A shared differentiable projection module ([`common/patch_projection.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/patch_projection.py)) that maps a trainable patch onto a camera-space coaster quad and reports which `OpenVLA` visual-token cells it covers.
2. A native `MuJoCo` coaster injector ([`common/coaster.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/coaster.py)) that places a static, visual-only, 90%-area patch face on a dark-brown base without affecting task physics.
3. A single native coaster-patch rollout path in [`common/utils.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/utils.py) and [`hypothesis_1/record_trajectories.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/hypothesis_1/record_trajectories.py), used to record the first six `LIBERO-Object` episodes with the coaster and a fixed unoptimized patch visible after real resets.

The recorded episodes validate scene plumbing and asset survival, **not** attack success: the patch is a deterministic random baseline that has not been optimized, and no steering metric has been measured yet.

## 2. Differentiable Patch Projection onto the `OpenVLA` Token Grid

[`common/patch_projection.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/patch_projection.py) is the shared renderer that lets the training loop see the same patch geometry used during native evaluation. It is deliberately independent of `LIBERO`: callers supply the four image-space coaster corners obtained from camera calibration.

The module exposes three pieces:

- **`CameraCalibration`** — a `3 x 3` intrinsic matrix plus a `3 x 4` or `4 x 4` world-to-camera transform in the OpenCV axis convention (`+Z` forward, `+X` right, `+Y` down).
- **`project_world_points()`** — homogeneous projection of world points to pixel coordinates, rejecting any corner that falls behind or on the camera plane.
- **`render_patch(frame, patch, destination_corners_xy, grid_size=16)`** — composites the trainable patch into the frame and returns a **`PatchRender`** with the composited `image`, its `alpha_mask`, a `16 x 16` `grid_mask`, and flat `grid_indices`.

Compositing uses `kornia.geometry.transform.get_perspective_transform` followed by `warp_perspective` (bilinear, `align_corners=True`), so gradients from the rendered frame flow back to the patch tensor. The warped alpha mask is reduced into the native `OpenVLA` token grid, and a cell is marked covered when at least half of its area is occupied (`occupancy >= 0.5`), which suppresses the machine-scale residue that bilinear warping leaves outside the quad. The renderer validates malformed or non-finite inputs, rejects degenerate zero-area quads with the shoelace formula, rejects frame sizes not divisible by `grid_size`, rejects patches that cover no cell, and coerces corners to contiguous tensors for Kornia's linear solver.

## 3. Native `MuJoCo` Coaster Injection and Patch-Face Alignment

[`common/coaster.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/coaster.py) turns the projected patch into real scene geometry. `CoasterSpec` describes a square coaster by the world-space center of its bottom face, its `size_xy`, an optional texture, yaw, `thickness_m=0.01`, `patch_area_fraction=0.90`, and a dark-brown `base_color=(0.24, 0.12, 0.06, 1.0)`.

`add_coaster_to_arena(arena, spec)` appends the coaster to an uncompiled `robosuite` arena as:

1. A `_base` box geom with only an `rgba`, so the plain brown coaster is the untextured Clean+Coaster baseline.
2. Optional `_patch` box geom whose half-extents are scaled by `sqrt(patch_area_fraction)`, raised by `PATCH_OFFSET_M = 0.0002` m to avoid z-fighting, carrying a `<texture>` and a `<material texrepeat="1 1" specular="0" shininess="0">`.

Both geoms are visual-only (`group="1"`, `contype="0"`, `conaffinity="0"`), so the coaster changes rendered observations without changing task collision dynamics. Body, texture, and material names are namespaced with an `h1_coaster_` prefix and de-duplicated, so the coaster can be re-added on every model rebuild without collisions.

Three rendering findings drove the final implementation:

- **Orientation must be a quaternion, not degree Euler angles.** `robosuite`'s robot `models/assets/base.xml` sets `<compiler angle="radian">`, so an arena `euler="6.875 0 0"` was reinterpreted as 6.875 radians (about `33.9°`, roughly a fivefold yaw error). Emitting a `quat` makes the coaster orientation independent of the compiler's angle unit.
- **`texuniform` must be omitted.** In `MuJoCo 3.1.6`, `texuniform` multiplies the texture scale by the geom half-size, so only a small central window of the patch PNG was visible. With `texrepeat="1 1"` and no `texuniform`, the full patch spans the face.
- **Box UV order is fixed by the engine, not by a corner reorder.** PNG column 0 maps to local `-X` (`u = (x/hx + 1)/2`) and PNG row 0 to local `+Y` (`v = (1 - y/hy)/2`); `lodepng` rows are uploaded without flipping. `CoasterSpec.patch_corners_world()` therefore returns TL, TR, BR, BL already in patch-PNG order, and the earlier `[1, 0, 3, 2]` corner permutation was removed after the yaw bug was fixed.

## 4. Shared Native Coaster-Patch Rollout Path and First Recorded Episodes

The coaster is now part of the shared closed-loop engine rather than a test-only fixture. [`common/utils.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/common/utils.py) adds an optional `coaster_texture_path` argument to `run_closed_loop_rollout()`. When supplied, it:

- Resolves and validates the PNG, then reads the task's BDDL problem class from `TASK_MAPPING`.
- Temporarily wraps that class's `_load_fixtures_in_arena` so every hard `reset()` reconstructs the model with the same native textured coaster.
- Derives the support height from `mujoco_arena.table_top_abs` when present, otherwise from `floor_body`, and places the coaster at `(0.30, -0.14)` m on a `0.12 x 0.12` m face with `0.12` rad yaw.
- Restores the original loader in a `finally` block, so clean rollouts and other tasks are unaffected.

This design addresses a concrete `LIBERO` behavior: `ControlEnv.reset()` uses `hard_reset=True`, which re-runs `_load_model()` and therefore `_load_fixtures_in_arena`. A coaster appended only once at construction would disappear before the first recorded step.

[`hypothesis_1/record_trajectories.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/hypothesis_1/record_trajectories.py) (renamed from the clean-only recorder while preserving its clean defaults) now accepts `--patch [PNG]`. Without an explicit path it uses the deterministic `224 x 224` baseline at [`hypothesis_1/patches/attention_magnet/unoptimized.png`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/hypothesis_1/patches/attention_magnet/unoptimized.png): a fixed-seed `16 x 16` random color grid expanded with nearest-neighbor sampling so the pattern survives texture filtering. Patch mode records task IDs 0–2, targets 2 successful episodes per task, caps retries at 5 attempts per task, writes under `hypothesis_1/outputs/<suite>/clean_with_coaster_patch/`, and stores the resolved patch path and SHA-256 in `collection_summary.json`.

The reference documents were also tidied in this week's restructuring commit: `docs/clean_trajectory_results.md` and `docs/weekly_execution_plan_hypothesis_1.md` now sit under [`docs/`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/docs), and the README's module inventory reflects the new projection, coaster, and recorder surfaces.

## 5. Validation Results

### 5.1 Patch and coaster smoke suite

The consolidated suite [`smoke_tests/patch_and_coaster_tests.py`](../../../../team-work/projects/security-and-exploitation/adversarial-attacks-on-VLA-model/smoke_tests/patch_and_coaster_tests.py) covers projection math, patch compositing, gradient flow, input rejection, coaster geometry, MJCF compilation, repeated insertion, and a real `LIBERO-Object` Task 0 pipeline. **All 9 tests pass** under the `vla-adv` environment:

- `test_project_world_points` and behind-camera rejection.
- `test_render_patch_shape_composite_and_grid` and `test_render_patch_preserves_gradients`.
- `test_render_patch_rejects_invalid_input`.
- `test_coaster_spec_corners_and_validation`.
- `test_add_coaster_xml_and_mujoco_compilation`.
- `test_add_coaster_names_do_not_collide`.
- `test_add_coaster_to_robosuite_arena`.
- `test_native_libero_brown_and_patch_textured_coasters`.

The integration test builds three Task 0 environments (base, plain brown, and native patch-textured), injects the coaster through a patched `Libero_Floor_Manipulation._load_fixtures_in_arena`, calibrates the `agentview` pinhole camera from `sim.data.cam_xpos` / `sim.data.cam_xmat` and `sim.model.cam_fovy`, projects the coaster corners, and composites the same patch with `render_patch`. It asserts:

- Projected patch-to-base area ratio `0.90` within `0.02`, and side ratio `sqrt(0.9)` within `0.02`.
- Native-render quadrant colors match cyan, yellow, pink, and blue at the projected TL, TR, BR, BL points.
- The `kornia` composite and the native lit patch agree to a mean per-pixel chromaticity difference below `0.03` inside an eroded patch mask.

Saved frames under `smoke_tests/outputs/coaster_and_patch_projection/` show the base scene, the brown coaster, the brown coaster with the projected patch, and the native patch-textured coaster at the same pose.

### 5.2 First native coaster-patch rollouts

`collection_summary.json` for `hypothesis_1/outputs/libero-object/clean_with_coaster_patch/` reports `all_tasks_complete: true` for task IDs 0–2, with **2 successful episodes per task (6 total)**. The fixed patch SHA-256 is `58152f0dc4b6aecd1ebe23aabba48b9f513875e623f84ff22bd1e0fe3ec0b26f`.

All six `trajectory.npz` files contain finite 7-DoF actions and finite `MuJoCo` states, and all six `video.mp4` files are nonempty. Episode lengths were 192 and 129 steps (alphabet soup), 132 and 141 steps (cream cheese), and 133 and 146 steps (salad dressing). The two salad-dressing attempts recorded this run had mean step RTTs of `1024.76 ms` and `1004.67 ms`. Initial frames show the colored native patch coaster visible in all six episodes, including after the hard resets between tasks.

**Claim boundary:** these are unoptimized-patch baseline rollouts under the benign task instructions. They demonstrate that the coaster, patch, and hard-reset path survive real closed-loop recording; they do not demonstrate attention hijacking, decoy selection, or a successful adversarial attack. No steering, smoothness, or success-rate comparison has been computed.

## 6. Next Steps

- **Wire the projector into the Way 1 Attention Magnet loop:** render the plain brown coaster natively, project `patch_corners_world()` per episode, and overlay the current trainable patch with `render_patch()` before the attention/loss computation.
- **Compute clean per-task attention baselines** and verify that the optimizer can concentrate `Llama-2` text-to-vision attention on the covered `16 x 16` cells under changing closed-loop viewpoints.
- **Add the `SigLIP + DINOv2` post-projector token path** required by the Way 2 Auto-Feature Copy method.
- **Extend the patched baseline to `LIBERO-Spatial`** and, after optimization, evaluate the final PNG with `record_trajectories.py --libero-object --patch <optimized.png>` against the same 2-success / 5-attempt protocol.
- **Decide whether to model native shading** by multiplying the composite patch with the brown coaster's top-face shading, closing the remaining train/eval appearance gap before optimization begins.
