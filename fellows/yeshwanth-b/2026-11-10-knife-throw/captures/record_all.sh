#!/bin/zsh
# Record campaign, defeat and extras at 4K, each with a fixed RNG seed. The campaign
# starts from an empty save folder. A take aborted by the draw-stall watchdog is retried.
W="${0:A:h}"; U="$HOME/Library/Application Support/knife-throw-filmcapture"
attempt() {  # $1 take, $2 seed
  for n in 1 2 3; do
    "$W/capture/harness/run_take.sh" "$1" "$W/takes/$1" "$2"; rc=$?
    stalled=$(grep -c draw_stalled "$W/takes/$1/inputs.jsonl")
    fails=$(grep -c '"pass":false' "$W/takes/$1/inputs.jsonl")
    echo "$1 attempt $n rc=$rc stalled=$stalled fails=$fails frames=$(cat $W/takes/$1/frames.count 2>/dev/null)"
    [[ $rc -eq 0 && $stalled -eq 0 && $fails -eq 0 ]] && return 0
    [[ $stalled -eq 0 ]] && return 1
  done
  return 1
}
rm -rf "$U"
attempt campaign 1 || exit 1
attempt defeat 1 || exit 2
attempt extras 1 || exit 3
echo ALL DONE
