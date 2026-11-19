#!/bin/zsh
# Record the four Delta takes at 4K, seed 1. campaign1 starts from an empty save folder;
# campaign2 continues from it (Continue 07); defeat and extras use Select level.
# A take aborted by the draw-stall watchdog is retried; campaign2 is re-run after
# campaign1 if it has to be repeated, so the save is in the right state.
W="${0:A:h}"; U="$HOME/Library/Application Support/delta-filmcapture"
attempt() {  # $1 take
  for n in 1 2 3; do
    "$W/capture/harness/run_take.sh" "$1" "$W/takes/$1" 1; rc=$?
    stalled=$(grep -c draw_stalled "$W/takes/$1/inputs.jsonl")
    fails=$(grep -c '"pass":false' "$W/takes/$1/inputs.jsonl")
    echo "$1 attempt $n rc=$rc stalled=$stalled fails=$fails frames=$(cat $W/takes/$1/frames.count 2>/dev/null) $(date +%H:%M)"
    [[ $rc -eq 0 && $stalled -eq 0 && $fails -eq 0 ]] && return 0
    [[ $stalled -eq 0 ]] && return 1
    [[ $1 == campaign2 ]] && { rm -rf "$U"; "$W/capture/harness/run_take.sh" campaign1 "$W/takes/campaign1" 1; }
  done
  return 1
}
rm -rf "$U"
"$W/assemble.sh" || exit 9
attempt campaign1 || exit 1
attempt campaign2 || exit 2
attempt defeat || exit 3
attempt extras || exit 4
echo ALL DONE
