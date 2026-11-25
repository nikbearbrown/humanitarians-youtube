#!/bin/zsh
# Record the three Night Yard takes at 4K, seed 1, in this order, sharing one save folder
# (emptied before campaign). A take aborted by the draw-stall watchdog is retried; if
# campaign has to be repeated the save is emptied first.
W="${0:A:h}"; U="$HOME/Library/Application Support/nightyard-filmcapture"
attempt() {  # $1 take
  for n in 1 2 3; do
    [[ $1 == campaign ]] && rm -rf "$U"
    "$W/capture/harness/run_take.sh" "$1" "$W/takes/$1" 1; rc=$?
    stalled=$(grep -c draw_stalled "$W/takes/$1/inputs.jsonl")
    fails=$(grep -c '"pass":false' "$W/takes/$1/inputs.jsonl")
    echo "$1 attempt $n rc=$rc stalled=$stalled fails=$fails frames=$(cat $W/takes/$1/frames.count 2>/dev/null) $(date +%H:%M)"
    [[ $rc -eq 0 && $stalled -eq 0 && $fails -eq 0 ]] && return 0
    [[ $stalled -eq 0 ]] && return 1
  done
  return 1
}
cd "$W" && cat core.gd takes.gd > capture_driver.gd && cp capture_driver.gd run_take.sh capture/harness/ || exit 9
attempt campaign || exit 1
attempt defeat || exit 2
attempt extras || exit 3
echo ALL DONE
