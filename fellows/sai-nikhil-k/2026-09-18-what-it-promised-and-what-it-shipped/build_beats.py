#!/usr/bin/env python3
"""build_beats.py — emit beat_sheet.json for 09-18-1.

The math rows on B04 are OUTLINED SVG produced by runtime/scripts/typeset_math.py
(matplotlib mathtext -> path-outlined SVG, no LaTeX process, no text fallback),
so they are regenerated here rather than pasted as base64 into a hand-edited
file. Re-run this script after changing any expression, then re-render B04.

Run:  python3 build_beats.py          # writes beat_sheet.json
      python3 build_beats.py --check  # verify algebra + string budgets only
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "runtime" / "scripts"))
from typeset_math import typeset  # noqa: E402

# ---------------------------------------------------------------- the figures
# Every number below is read verbatim out of the model card that ships inside
# Gavia.app: Contents/Resources/gavia-backend/_internal/models/loon_v1.json
P = 0.92957      # metrics.precision
R = 0.80012      # metrics.recall
MAP50 = 0.89423  # metrics.mAP50
MAP5095 = 0.61357  # metrics["mAP50-95"]
F1 = 2 * P * R / (P + R)   # DERIVED HERE. Not on the card. Labelled as ours.

MATH_ROWS = [
    (r"P = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FP}} = 0.930", 0.0),
    (r"R = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}} = 0.800", 5.2),
    (r"F_1 = \frac{2PR}{P + R} = 0.860", 11.0),
]


def check():
    """Algebra and typography budgets are verified separately (MATH-TYPESETTING)."""
    assert abs(F1 - 0.860) < 5e-4, F1
    assert min(P, R) <= F1 <= max(P, R), "harmonic mean must lie between P and R"
    assert abs(round(P, 3) - 0.930) < 1e-9 and abs(round(R, 3) - 0.800) < 1e-9
    assert abs(1 / (1 - R) - 5.0) < 0.01, "miss rate must be exactly one in five"
    for expr, _ in MATH_ROWS:
        assert "$" not in expr
        typeset(expr)  # raises if mathtext cannot set it
    print(f"algebra OK   P={P} R={R} F1={F1:.6f} -> 0.860   1/(1-R)={1/(1-R):.3f}")
    print(f"mAP50={MAP50} mAP50-95={MAP5095}")
    # deck-pattern strings do not reflow: fixed-x SVG text, ~42 char budget
    for s in DECK_STRINGS:
        flag = "OK " if len(s) <= 42 else "LONG"
        print(f"  {flag} {len(s):>2}  {s}")
    assert all(len(s) <= 42 for s in DECK_STRINGS), "deck string over budget"


DECK_STRINGS = [
    "RECALL 0.800 · ONE LOON IN FIVE UNSEEN",
    "Lower the threshold, or leave it at 0.25?",
    "Drop below 0.25",
    "more birds found, more reeds boxed",
    "recall up, precision down",
    "Hold at 0.25",
    "keep the 93% it already earns",
    "one in five stays unreported",
    "The field decides, not the F-score",
]

TITLE = "What It Promised, And What It Shipped"
SLUG = "claude-sai-what-it-promised-and-what-it-shipped"
TOPIC = "Computational Skepticism"
CHIP = "@HumanitariansAI"


def beats():
    math_rows = []
    for expr, at in MATH_ROWS:
        row = typeset(expr)
        row["at"] = at
        math_rows.append(row)

    return [
        # ------------------------------------------------------------- B00 ASK
        {
            "beat_id": "B00", "act": "ASK",
            "narration_text":
                "Last week I told you the real numbers would come from the model itself, "
                "before the meeting. They did. And they are printed on a card inside an "
                "application that now runs on a laptop, with no server and no account. "
                "This is Sai. Here is what it promised, and here is what it shipped.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.15, "event": "the ask types in — last week's promise, quoted back"},
                    {"at": 0.55, "event": "three result lines land: the app, the detector inside it, the two numbers"},
                    {"at": 0.9, "event": "the last line is the promise being kept, in figures"},
                ],
                "remotion": {
                    "pattern": "ClaudeComposerAsk",
                    "props": {
                        "greeting": "Hello, Sai",
                        "topic": TOPIC,
                        "segment": TITLE,
                        "command":
                            "Last week there was a prediction sheet and a promise — precision and "
                            "recall from the model itself, before the meeting. This week there is an "
                            "application. Open the bundle, read the model card it ships with, and tell "
                            "me whether the promise was kept or only moved.",
                        "runningText": "reading the model card out of the bundle…",
                        "folderLabel": CHIP,
                        "output": [
                            "Gavia 0.1.0 · ai.humanitarians.gavia · arm64",
                            "the detector ships inside — loon_v1.onnx, 36 MB",
                            "precision 0.930 · recall 0.800",
                        ],
                    },
                    "rendered": {"out": "media/B00.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 18.0,
        },
        # ------------------------------------------------------ B01 THE BUNDLE
        {
            "beat_id": "B01", "act": "THE BUNDLE",
            "narration_text":
                "So what is it? A desktop application. Eighty-four megabytes to download, a "
                "hundred and seventy-six once it is installed. Apple silicon, macOS ten "
                "fifteen and up. Inside there is a Rust shell, a Python service, the onnx "
                "runtime, and the detector itself — thirty-six megabytes of weights. "
                "Nothing in that list reaches for a server.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.1, "event": "version and download size land first — it is a thing you can install"},
                    {"at": 0.45, "event": "the runtime layers fill in: shell, service, onnx runtime"},
                    {"at": 0.8, "event": "the weights and the local database close the grid"},
                ],
                "remotion": {
                    "pattern": "ClaudeScienceChipGrid",
                    "props": {
                        "sparkLine": "WHAT SHIPPED · INSIDE THE BUNDLE",
                        "items": [
                            "Gavia 0.1.0",
                            "84 MB download",
                            "176 MB installed",
                            "arm64 · macOS 10.15+",
                            "Rust desktop shell",
                            "Python 3.11 service",
                            "onnxruntime · CPU",
                            "loon_v1.onnx · 36 MB",
                            "SQLite, on your disk",
                        ],
                        "cols": 3,
                        "caption": "Read from Info.plist and the bundle tree of Gavia_0.1.0_aarch64-1.dmg",
                    },
                    "rendered": {"out": "media/B01.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 18.5,
        },
        # --------------------------------------------------------- B02 THE APP
        {
            "beat_id": "B02", "act": "THE APP",
            "narration_text":
                "And it behaves the way a field tool should. One image in. A box drawn where "
                "the bird is, eighty-two percent on that box, and a line underneath saying "
                "highlighted areas show where a loon was found. Not a score on its own — a "
                "place. The history page keeps the earlier checks, on your own disk.",
            "shot": {
                "type": "STILL", "source": "own", "treatment": "none", "motion": "hold",
                "show": [
                    {"at": 0.0, "event": "the result screen holds — no pan, no zoom; the layout is the argument"},
                    {"at": 0.45, "event": "the eye goes to the box on the bird, then to the confidence beside it"},
                    {"at": 0.85, "event": "the prototype footer stays legible for the whole beat"},
                ],
                "remotion": None,
                "still": {
                    "src": "media/B02.png",
                    "still_916": "pantry/B02-916.png",
                    "composed_from":
                        "author's own screen capture of Gavia 0.1.0 returning a detection "
                        "(data/WhatsApp Image 2026-09-17 at 13.43.38.jpeg, staged to "
                        "images/B02-source-detect.jpg at 1600x1371), composed to 3840x2160 by "
                        "make_plates.py with the history and about screens as thumbnails",
                    "note":
                    "The author's own screen capture of Gavia 0.1.0 — an irreplaceable source "
                    "artifact under EXECUTABLE-EVIDENCE.md (the still IS the evidence that the "
                    "application exists and runs). Composed onto the reel's cream by "
                    "make_plates.py, never retouched: no box, label, percentage or footer was "
                    "redrawn or repositioned. HOLD, not Ken Burns — compile.py's zoompan would "
                    "push the prototype footer and the confidence panel off frame. The portrait "
                    "plate is RE-COMPOSED (banner / boxed bird / confidence block stacked), not "
                    "centre-cut, which would discard the whole right-hand details panel.",
                },
            },
            "estimated_duration_s": 18.0,
        },
        # ------------------------------------------------ B03 THE PROMISE KEPT
        {
            "beat_id": "B03", "act": "THE PROMISE KEPT",
            "narration_text":
                "Here is the card the promise was about. Precision, ninety-three percent — "
                "when it calls something a loon, it is almost always right. Recall, eighty. "
                "Mean average precision at fifty, eighty-nine. And the strict one, fifty "
                "through ninety-five, sixty-one. Four numbers, off the checkpoint itself. "
                "Not a hand count this time.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.12, "event": "precision fills first and nearly reaches the end of the bar"},
                    {"at": 0.38, "event": "recall stops visibly short of it — the gap is the beat"},
                    {"at": 0.62, "event": "mAP50 fills back up past recall, closing the row of bars"},
                ],
                "remotion": {
                    "pattern": "ExecutedData",
                    "props": {
                        "title": "loon_v1 — the numbers last week promised",
                        "mode": "probability",
                        # THREE bars, not four. Four probability rows overflow
                        # this component at 2160: GATE V flagged edge-bleed at
                        # 50% and 85% (2026-09-18), the note disappeared and the
                        # 0%/100% axis labels were clipped off the bottom.
                        # Shortening the note did not help — the ROWS are what
                        # overflow. The strict mAP50-95 moves into the note so
                        # all four card figures still appear on screen, and the
                        # precision/recall gap stays visible as bar length.
                        "rows": [
                            {"label": "precision", "value": P, "at": 2.0},
                            {"label": "recall", "value": R, "at": 6.0},
                            {"label": "mAP50", "value": MAP50, "at": 9.5},
                        ],
                        # ONE LINE ONLY. Four probability rows + a 3-line note
                        # overflowed the component at 2160 (GATE V edge-bleed,
                        # 2026-09-18): the note vanished and the 0%/100% axis
                        # labels were clipped at the bottom edge. Provenance
                        # that used to live here is spoken on B03 and printed
                        # on B06 instead.
                        "note": "Recorded output — the model card inside the app.  ·  strict mAP50-95 = 0.614",
                    },
                    "rendered": {"out": "media/B03.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 17.0,
        },
        # -------------------------------------------------- B04 THE ARITHMETIC
        {
            "beat_id": "B04", "act": "THE ARITHMETIC",
            "narration_text":
                "Two of those four are a trade, and the trade has a shape. Precision divides "
                "the true finds by everything it called a loon. Recall divides the same true "
                "finds by every loon that was really there. One number balances them — the "
                "harmonic mean, eighty-six. The card does not print it. I computed it from "
                "the two it does.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.05, "event": "precision sets first — the false positive sits in the denominator"},
                    {"at": 0.35, "event": "recall sets beneath it; only the denominator changed, FP becomes FN"},
                    {"at": 0.72, "event": "F-one resolves the pair into a single figure, 0.860"},
                ],
                "remotion": {
                    "pattern": "TypesetMath",
                    "props": {
                        "title": "Two definitions that differ by one term",
                        "rows": math_rows,
                        "note": "F₁ is the harmonic mean of precision and recall — ours, not the card's.",
                        "conditions":
                            "P, R verbatim from the shipped model card · F₁ computed and "
                            "re-checked in FACTCHECK.md · TP+FP > 0, TP+FN > 0",
                    },
                    "rendered": {"out": "media/B04.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 18.5,
        },
        # -------------------------------------------------------- B05 THE FORK
        {
            "beat_id": "B05", "act": "THE FORK",
            "narration_text":
                "But eighty percent recall has a plain meaning. One loon in five, the model "
                "says nothing about. And there is a dial for it in the card — confidence "
                "threshold, zero point two five. Drop it and you find more birds and more "
                "reed beds. Hold it and the misses stay. That is a decision to make, not a "
                "bug to fix.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.15, "event": "the question sets — one dial, two directions"},
                    {"at": 0.45, "event": "both branches carry a cost; neither is the safe one"},
                    {"at": 0.85, "event": "the resolver puts the choice back in the field, not in the metric"},
                ],
                "remotion": {
                    "pattern": "BinaryBranch",
                    "props": {
                        "data": {
                            "slideMeta": "RECALL 0.800 · ONE LOON IN FIVE UNSEEN",
                            "question": "Lower the threshold, or leave it at 0.25?",
                            "branches": [
                                {
                                    "label": "Drop below 0.25",
                                    "detail": "more birds found, more reeds boxed",
                                    "fix": "recall up, precision down",
                                    "tone": "warn",
                                },
                                {
                                    "label": "Hold at 0.25",
                                    "detail": "keep the 93% it already earns",
                                    "fix": "one in five stays unreported",
                                    "tone": "good",
                                },
                            ],
                            "resolver": {
                                "label": "The field decides, not the F-score",
                                "detail":
                                    "a missed loon is a gap in a survey; a boxed reed bed is one "
                                    "click to dismiss — and the app already asks a researcher to "
                                    "review every result, so the two costs are not equal",
                            },
                            "ghostText": "0.25 is the shipped default, not a finding",
                        },
                        "typeScale": 1.4,
                    },
                    "rendered": {"out": "media/B05.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 19.0,
        },
        # ----------------------------------------------------- B06 THE VERDICT
        {
            "beat_id": "B06", "act": "VERDICT",
            "narration_text":
                "So: one page. The promise is kept — four numbers, from the checkpoint, "
                "inside the app. The detector left the notebook and runs on a laptop. It "
                "calls itself a prototype on every screen. And one loon in five is still "
                "unreported. That is next week.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.12, "event": "the page opens on the promise and the four figures"},
                    {"at": 0.4, "event": "the architecture line lands — the model is inside the bundle"},
                    {"at": 0.68, "event": "the prototype disclosure, in the app's own words"},
                    {"at": 0.9, "event": "the open number closes the page and is not a footnote"},
                ],
                "remotion": {
                    "pattern": "ClaudeVerdictArtifact",
                    "props": {
                        "artifactTitle": TITLE,
                        "artifactHeading": "Gavia 0.1.0 · one page",
                        "artifactLines": [
                            "Last week's promise is kept. precision 0.930, recall 0.800, mAP50 0.894, "
                            "mAP50-95 0.614 — read off the model card shipped inside the application, "
                            "not counted by hand off a sheet.",
                            "The detector left the notebook. loon_v1.onnx and the onnx runtime are in "
                            "the bundle, inference ran on CPU in about an eighth of a second, and the "
                            "backend's own help text says it is not a network service.",
                            "It is version 0.1.0 and says so on every page — a prototype for "
                            "conservation research, carrying its own note that AI results contain "
                            "errors and should be reviewed by someone who knows the bird.",
                            "One number is not on the card: recall 0.800 means roughly one loon in "
                            "five is still unreported. The 0.25 confidence threshold is one lever on "
                            "that, and it is not the only one.",
                        ],
                    },
                    "rendered": {"out": "media/B06.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 16.0,
        },
        # ---------------------------------------------------------- B07 HANDOFF
        {
            "beat_id": "B07", "act": "HANDOFF",
            "narration_text":
                "Your turn. If you have a model that only works in a notebook, try this "
                "before you demo it again. Put it in something a colleague can open with no "
                "terminal and no account. Then make the build write the model's own numbers "
                "into the bundle. If you cannot state recall on the way out the door, it is "
                "not shipped yet.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.2, "event": "the handoff prompt types in, ready to paste"},
                    {"at": 0.6, "event": "the emphasis lands on the card travelling WITH the weights"},
                    {"at": 0.9, "event": "the ask ends on the field you cannot fill in yet"},
                ],
                "remotion": {
                    "pattern": "ClaudeComposerAsk",
                    "props": {
                        "greeting": "Your turn.",
                        "topic": TOPIC,
                        "segment": "Ship The Card With The Model",
                        "command":
                            "Take a model that currently only runs in my notebook. Package it so a "
                            "colleague opens it like any other application — no terminal, no account, "
                            "no server. Then make the build write a model card into the bundle: "
                            "architecture, training run, precision, recall, thresholds, licence. Tell "
                            "me which of those fields I cannot honestly fill in yet.",
                        "runningText": "packaging the model with its own numbers…",
                        "folderLabel": CHIP,
                    },
                    "rendered": {"out": "media/B07.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 19.0,
        },
        # ------------------------------------------------------------ B08 OUTRO
        {
            "beat_id": "B08", "act": "OUTRO",
            "narration_text": "What it promised, and what it shipped. Sai.",
            "shot": {
                "type": "GRAPHIC", "source": "remotion", "motion": "illustrate",
                "show": [
                    {"at": 0.15, "event": "the humanitarians mark springs in on the cream ground"},
                    {"at": 0.6, "event": "the handle settles beneath it"},
                    {"at": 0.9, "event": "the mark holds, then the card closes"},
                ],
                "remotion": {
                    "pattern": "LogoOutro",
                    "props": {
                        "svgFile": "logo-outro/humanitarians/humanitarians-logo-1.svg",
                        "animation": "springEntrance",
                        "durationS": 4,
                        "aspectRatio": 0.845,
                        "bg": "#FAF9F5",
                        "accent": "#D97757",
                        "handle": CHIP,
                        "_contract_note":
                            "LogoOutro, NOT ClaudeTitleOutro — ClaudeTitleOutro's handle is "
                            "hardcoded to @NikBearBrown and cannot carry this series' "
                            "@HumanitariansAI. TIMING TRAP: the composition is 120 frames @30fps "
                            "= 4.0s and fades to opacity 0 over its last 12 frames, while "
                            "remotion_scenes.py freeze-extends a short render with "
                            "tpad=stop_mode=clone — which would clone the FADED frame into "
                            "seconds of black. Narration is held to 8 words (~2.5s) so it "
                            "finishes inside the card. `./art run` will print a SKIN LINT line "
                            "wanting ClaudeTitleOutro; it is wrong for this channel and expected.",
                    },
                    "rendered": {"out": "media/B08.mp4", "at": ""},
                },
            },
            "estimated_duration_s": 3.7,
            "qc": {
                "sparse": True,
                "sparse_reason": "brand card — centred logo / handle only; negative space is the design",
            },
        },
    ]


NOTE = (
    "WEEKLY PROGRESS REEL for the loon-detector project, week of 2026-09-18. "
    "THE WEEK, as reported by the author: the first version of the application is "
    "built and packaged — Gavia 0.1.0, supplied as Gavia_0.1.0_aarch64-1.dmg with "
    "three screen captures (check-an-image result, previous checks, about). "
    "NO TEAMMATE IS NAMED ANYWHERE, carried forward from 09-11-1: collaborators "
    "appear as 'we' and 'the team', never by name, in narration, on-screen text, "
    "SOURCES.md and PEDAGOGY.md alike. "
    "THROUGH-LINE: 09-11-1 ended on a promise — 'real precision and recall come "
    "from the model, before the meeting'. This week those four numbers exist AND "
    "travel inside the artifact that uses them. The reel is the promise being "
    "checked, which is why the title pairs promised against shipped. "
    "FIGURES — READ THIS BEFORE CHANGING ANY NUMBER ON SCREEN. Everything "
    "quantitative is read out of the supplied DMG, not from the author's prose and "
    "not from git. Verbatim from Contents/Resources/gavia-backend/_internal/models/"
    "loon_v1.json: precision 0.92957, recall 0.80012, mAP50 0.89423, mAP50-95 "
    "0.61357, architecture YOLO11s, 100 epochs, 640 px, conf threshold 0.25, IoU "
    "0.45, max 300 detections, onnx opset 17, exported by ultralytics 8.4.138 from "
    "pytorch 2.14.0, trained 2026-09-02, exported 2026-09-09, onnx 37,927,878 "
    "bytes. Verbatim from Info.plist: CFBundleShortVersionString 0.1.0, "
    "CFBundleIdentifier ai.humanitarians.gavia, LSMinimumSystemVersion 10.15. "
    "Measured locally: 84 MB dmg (ls -lh), 176 MB installed (du -sh), arm64 (lipo "
    "-info). OBSERVED BY RUNNING THE SHIPPED BACKEND: model warm-up 0.128 s, "
    "provider CPUExecutionProvider, tiling false, steady-state /api/detect "
    "processingTime 0.124–0.143 s over five calls (first call 0.231 s, cold), local "
    "store is a SQLite gavia.db with tables results + detections. Read off the "
    "author's screen captures: '1 loon detected', 82% on the boxed bird, 89% and "
    "82% highest-confidence in the history list, both dated September 15 2026. "
    "DERIVED, AND LABELLED AS DERIVED ON SCREEN: F1 = 2PR/(P+R) = 0.860, and "
    "'one loon in five' from 1/(1-0.80012) = 5.00. "
    "THE ONE CONFLATION TO NEVER MAKE: the 82% and 89% in the screen captures are "
    "PER-IMAGE detection confidences. They are NOT model metrics, and mAP50 is "
    "0.894 by coincidence only. B02 speaks about 82% strictly as the score on one "
    "box in one photograph; B03 is the only beat that speaks about the card. "
    "AGPL: the model card carries \\\"spdx\\\": \\\"AGPL-3.0-only\\\", inherited from "
    "Ultralytics YOLO11. On the author's explicit instruction this is kept OUT of "
    "the reel entirely — no beat, no on-screen text, no narration, and not in "
    "DESCRIPTION.md. It is logged in SOURCES.md as an item for him to settle. "
    "Do not reinstate it without asking him again. "
    "A CLAIM DELIBERATELY NOT MADE: a crop of the loon out of the author's own "
    "screen capture was fed to the shipped backend and returned zero detections. "
    "That is an artifact of re-compressing an already-displayed image, NOT a miss "
    "by the model, and it appears nowhere in the reel. The original photograph was "
    "not supplied. Logged in SOURCES.md. "
    "ILLUSTRATE LAW: Claude UI at B00, B07 and the verdict only. Body beats run "
    "ChipGrid -> STILL -> ExecutedData -> TypesetMath -> BinaryBranch; no two "
    "consecutive beats share a pattern. "
    "MATH: B04 is the required typeset-math beat. Rows are outlined SVG from "
    "runtime/scripts/typeset_math.py (matplotlib mathtext, svg.fonttype=path) — "
    "real fraction bars, upright \\\\mathrm TP/FP/FN, italic variables, F_1 "
    "subscript. No text-card fallback exists for this beat; if the typesetter "
    "fails, B04 is BLOCKED, not downgraded. Algebra is checked independently by "
    "`python3 build_beats.py --check` and recorded in FACTCHECK.md. "
    "SHORTS / 9:16: every Remotion pattern used here has a registered 916 sibling "
    "(ClaudeComposerAsk916, ClaudeScienceChipGrid916, ExecutedData916, "
    "TypesetMath916, BinaryBranch916, ClaudeVerdictArtifact916, LogoOutro916), so "
    "shorts.py rewires with no new TSX. ClaudeScienceLayerStack and "
    "ClaudeScienceSourceFlow — the WEEKLY-VIDEO-GUIDE default B01/B02 patterns — "
    "have NO 916 sibling and are avoided for that reason alone. B02 is user media "
    "and would otherwise be centre-cut; it carries a hand-composed "
    "pantry/B02-916.png and HOLDS rather than pans. "
    "NARRATION CARRIES NO POSITIONAL REFERENCE ('top right', 'the panel beside "
    "it') because the same mp3 plays over both the landscape and the re-composed "
    "portrait plate and the block order differs between them. "
    "typeScale 1.4 on BinaryBranch, which was authored against a 1280x720 stage; "
    "its 916 sibling takes {data} only and ignores it harmlessly. Deck-pattern "
    "label and detail strings are kept under ~42 characters — fixed-x SVG text "
    "does not reflow, so a long string overprints silently and Remotion still "
    "exits 0. Budgets are asserted by --check. "
    "OUTRO: LogoOutro, not ClaudeTitleOutro, whose handle is hardcoded to "
    "@NikBearBrown. B08 narration is 8 words so it finishes inside the 4.0s card "
    "before its fade — see the _contract_note on that beat. `./art run` will print "
    "a SKIN LINT line asking for ClaudeTitleOutro; it is wrong for this channel "
    "and is expected."
)

METADATA = {
    "title": TITLE,
    "slug": SLUG,
    "topic": TOPIC,
    "register": "Teardown",
    "audience": "Claude",
    "brand": "claude",
    "channel": "claude-liam",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "palette": "claude",
    "style_preset": "claude",
    "ground": "#FAF9F5",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "greeting": "Hello, Sai",
    "greeting_note":
        "ATTRIBUTION OVERRIDE (established 2026-07-31, carried forward from 09-04-01, "
        "09-04-02, 09-11-1 and 09-11-2): hosted by Sai in his own name, not by "
        "Liam-in-for-Bear. Voice stays Kokoro am_onyx. B00 says 'This is Sai'; B08 "
        "signs off 'Sai.' The IN-FOR-BEAR LAW of WEEKLY-VIDEO-GUIDE.md is "
        "deliberately suspended for this series.",
    "folder_chip": CHIP,
    "note": NOTE,
    "voice_note":
        "metadata.voice (legacy) is deliberately ABSENT. build_safety.default_voice "
        "treats it as an alias for the Kokoro voice id and refuses the build when it "
        "disagrees with voice_kokoro — and this series used to set "
        "voice='NikBearBrown', a persona name, not a voice id. The persona is carried "
        "by channel, folder_chip and greeting_note instead.",
    "tags": [
        "loon detection", "Gavia", "LoonNet", "National Loon Center", "conservation AI",
        "wildlife detection", "object detection", "YOLO", "YOLO11", "computer vision",
        "ONNX", "onnxruntime", "edge inference", "on-device AI", "offline AI",
        "desktop application", "Tauri", "model card", "precision and recall",
        "mean average precision", "confidence threshold", "model evaluation",
        "model packaging", "MLOps", "Humanitarians AI", "weekly progress",
    ],
}


# Fields the pipeline measures or stamps. Regenerating this file must NEVER
# silently discard them: on 2026-09-18 a note edit wiped every
# actual_duration_s, and the next --force render retimed B03 against the
# ESTIMATE (17.0s) instead of its measured audio (16.34s) — a straight
# audio-first violation that the render log reports as success.
MEASURED = ("actual_duration_s", "audio_file", "render_duration_s", "build", "qc")


def carry_measurements(out, doc):
    """Carry measured/stamped fields from the sheet on disk into the new one.

    Keyed on narration_text: if the words changed, the old mp3 and its duration
    are stale and are deliberately NOT carried, so the audio step re-measures.
    """
    if not out.is_file():
        return
    prev = {b["beat_id"]: b for b in json.loads(out.read_text()).get("beats", [])}
    kept, dropped = [], []
    for b in doc["beats"]:
        old_b = prev.get(b["beat_id"])
        if not old_b:
            continue
        if old_b.get("narration_text") != b.get("narration_text"):
            dropped.append(b["beat_id"])
            continue
        for k in MEASURED:
            if k in old_b and k not in b:
                b[k] = old_b[k]
        # keep render provenance so an unchanged beat is not re-rendered
        old_r = ((old_b.get("shot") or {}).get("remotion") or {}).get("rendered") or {}
        new_r = ((b.get("shot") or {}).get("remotion") or {}).get("rendered")
        if new_r is not None and old_r.get("at"):
            new_r["at"] = old_r["at"]
        if "actual_duration_s" in b:
            kept.append(b["beat_id"])
    if kept:
        print(f"carried measured durations for {len(kept)} beat(s): {' '.join(kept)}")
    if dropped:
        print(f"narration CHANGED — audio must be regenerated for: {' '.join(dropped)}")


def main():
    if "--check" in sys.argv:
        check()
        return
    check()
    doc = {"metadata": METADATA, "beats": beats()}
    out = HERE / "beat_sheet.json"
    carry_measurements(out, doc)
    out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    words = sum(len(b["narration_text"].split()) for b in doc["beats"])
    est = sum(b["estimated_duration_s"] for b in doc["beats"])
    print(f"wrote {out.relative_to(ROOT)}  {len(doc['beats'])} beats")
    print(f"narration {words} words → ~{words/3.25:.0f}s at am_onyx 195 wpm "
          f"(estimated {est:.0f}s)")
    for b in doc["beats"]:
        n = len(b["narration_text"].split())
        pat = (b["shot"].get("remotion") or {}).get("pattern", b["shot"]["type"])
        print(f"  {b['beat_id']}  {n:>3}w  ~{n/3.25:>4.1f}s  {pat}")


if __name__ == "__main__":
    main()
