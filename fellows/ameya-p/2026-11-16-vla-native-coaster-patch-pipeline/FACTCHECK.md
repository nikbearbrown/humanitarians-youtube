# FACTCHECK - week9 (Nov 16)

## Primary source

`D:/Ameya/Career/Humanitarians AI/humanitarians-youtube/fellows/ameya-p/2026-11-16-vla-native-coaster-patch-pipeline/work_report.md`

## Supporting implementation evidence

- `common/patch_projection.py`: `CameraCalibration`, `project_world_points()`, and `render_patch()` warp a trainable patch with `kornia` and reduce the alpha mask to the `16 x 16` `OpenVLA` token grid.
- `common/coaster.py`: `CoasterSpec` and `add_coaster_to_arena()` create a brown base plus an optional 90%-area textured patch face as visual-only (`contype="0"`, `conaffinity="0"`) geoms.
- `common/utils.py`: `run_closed_loop_rollout(..., coaster_texture_path=...)` temporarily overrides `_load_fixtures_in_arena` so every hard reset rebuilds the coaster.
- `hypothesis_1/record_trajectories.py`: `--patch [PNG]` records under `clean_with_coaster_patch/` and stores the patch SHA-256 in `collection_summary.json`.
- `smoke_tests/patch_and_coaster_tests.py`: 9 tests, including the native three-environment projection test.
- `hypothesis_1/outputs/libero-object/clean_with_coaster_patch/collection_summary.json`: `all_tasks_complete: true`, 2 successful episodes per task, patch SHA-256 `58152f0dc4b6aecd1ebe23aabba48b9f513875e623f84ff22bd1e0fe3ec0b26f`.

## Claims used in the beat sheet

| Claim | Evidence | Status |
|---|---|---|
| The patch is projected with the same geometry used for native evaluation. | Work report section 2; `patch_projection.py`; `render_patch()` returns `grid_mask`/`grid_indices`. | Supported |
| The coaster is visual-only and does not change task physics. | Work report section 3; `coaster.py` uses `group="1"`, `contype="0"`, `conaffinity="0"`. | Supported |
| The patch face covers 90% of the top surface. | Work report section 3; `CoasterSpec.patch_area_fraction=0.90`, `patch_linear_scale = sqrt(0.90)`. | Supported |
| The coaster survives hard environment resets. | Work report section 4; `common/utils.py` fixture-loader override; six recorded episodes show the patch after resets. | Supported |
| 9 of 9 patch-and-coaster tests pass. | Work report section 5.1; `smoke_tests/patch_and_coaster_tests.py` `run_all_tests()`. | Supported |
| Projected area ratio is 0.90 and chromaticity difference is below 0.03. | Work report section 5.1; integration-test assertions `abs(area_ratio - 0.90) < 0.02` and `mean_diff < 0.03`. | Supported |
| Six `LIBERO-Object` episodes were recorded, two per task. | Work report section 5.2; `collection_summary.json`; six `trajectory.npz` + six `video.mp4` files verified. | Supported |
| A successful trajectory-steering attack has occurred. | Not claimed by the report; the patch is unoptimized and no steering metric was computed. | Excluded explicitly |
| The patch improves task success, smoothness, or decoy selection. | Not measured this week. | Excluded explicitly |

## Editorial correction

The beat sheet says the patch "tests the geometry," not that it "steers the robot." The report's completed outcome is a rendering and recording pipeline; the recorded episodes use a deterministic random patch and demonstrate asset survival, not adversarial effect.
