# PROMPTS — Automating the YouTube Review Pipeline

Beat-prefixed build prompts for every open slot. Paste one at a time into Claude
Code from the toolkit root. Each builds ONE component, then re-indexes.

## Standing preamble (applies to every prompt below)

    Build this as a Remotion component in runtime/remotion/src/scenes/,
    register it in Root.tsx at width 1920 height 1080 fps 30, and add it to the
    HAI Brutalist series group. Use the humanitarians palette tokens, not the
    Claude skin. Keep all essential text inside a 5% title-safe inset. Text
    boxes use maxWidth with wrap or auto-fit, never a fixed width. Fill the
    canvas - undersized content clustered in the top third is a defect.
    Animation is progress-based and duration-agnostic. When done, run
    ./art scene-index.

## B02 - HaiPipelineReviewLoop

    A five-stage horizontal rail: ARRIVES, UPLOAD, WAIT, CHECK 4K,
    KEEP / DELETE. A file token travels the rail. At ~80% the DELETE branch
    lights in terracotta and stays lit; everything upstream of it dims to about
    40% opacity, showing the wasted span. Props: stages (string array),
    wasteFrom (index), sparkLine.
    Closest existing component to model on: HaiBrutalistE01Pipeline.

## B03 - HaiPixelThreshold

    Two file cards side by side with blank dimension readouts. The readouts
    count up: left settles at 3840x2160, right stops at 2560x1440. A threshold
    line draws across both at 3840; left crosses it, right does not. Left
    stamps "4K", right stamps "not 4K". Props: left {w,h,verdict},
    right {w,h,verdict}, threshold, sparkLine.

## B04 - HaiSoftFourK

    A probe readout returns 3840x2160 with a green tick. The frame then peels
    back to reveal one piece underneath reading 1280x720. That piece stretches
    to fill the frame with visible edge softening. A stamp lands reading
    "no warning issued". Props: outer {w,h}, inner {w,h}, stamp, sparkLine.
    This beat must SHOW the softening, not label it.

## B05 - HaiRenderDefaultDrift

    A single line of code reads HEIGHT=1080. It rewrites itself to HEIGHT=2160.
    The trailing comment "# 4K-native master (was 1080)" fades up and holds.
    Two dated copies appear, one either side of the change. A small caveat chip
    reads "a likely explanation, not a finding" - the hedge is part of the
    design, keep it visible. Props: before, after, note, caveat, sparkLine.

## B06 - HaiStageOneSort

    Stage chip "STAGE 1 - check before uploading". A folder watcher pulses and
    a file lands. The file routes down one of two paths. A note card writes
    itself into the fail path reading "re-pull the toolkit, render again". A
    counter under the fail folder holds at "deleted: 0" - nothing is destroyed.
    Props: stage, title, note, deletedCount, sparkLine.

## B07 - HaiOutroMismatch

    A settings file opens with channel reading @HumanitariansAI. The outro
    resolves to the wrong component and its handle reads @NikBearBrown. A
    mismatch flag fires between the two. Cut to a documented precedent line.
    Props: declared, found, precedent, sparkLine.

## B08 - HaiStageTwoThree

    Stage 2 chip: the sort runs on the folder, hands-off. The frame slides left
    and a Stage 3 chip enters. The check visibly jumps upstream into the tool
    itself, and a failing render is refused before it finishes. Props:
    stageTwo {label,title}, stageThree {label,title}, sparkLine.

## B09 - HaiStageFourNeeds

    Stage chip "STAGE 4". Two need-cards land one at a time. Card one stamps
    LOCKED and is held longest: "An approved Google project / or one created
    before 28 July 2020". Card two: "The owner authorises, once / managers
    cannot, via the API" with delegation crossed out. A closing line reads
    "I show the procedure. I never hold the key." Props: stage, needs (array of
    {label,detail,stamp}), notMine, sparkLine.
    This beat holds longest in the reel - it is the credibility beat.

## Beats needing no prompt

B00, B01, B10 and B11 use components that already exist and are registered.
