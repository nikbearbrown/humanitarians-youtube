#!/bin/zsh
# Record day, night and defeat at 4K. A take aborted by the draw-stall watchdog is retried
# from the save it depends on (backed up after the take that wrote it).
W="$1"; U="$2"
attempt() {  # $1 take, $2 setup
  for n in 1 2 3; do
    eval "$2"
    "$W/capture/harness/run_take.sh" "$1" "$W/takes/$1"; rc=$?
    stalled=$(grep -c draw_stalled "$W/takes/$1/inputs.jsonl")
    fails=$(grep -c '"pass":false' "$W/takes/$1/inputs.jsonl")
    echo "$1 attempt $n rc=$rc stalled=$stalled fails=$fails frames=$(cat $W/takes/$1/frames.count 2>/dev/null)"
    [[ $rc -eq 0 && $stalled -eq 0 && $fails -eq 0 ]] && return 0
  done
  return 1
}
attempt day 'rm -rf "$U"' || exit 1
cp "$U/savegame.json" "$W/save_after_day.json"
attempt night 'cp "$W/save_after_day.json" "$U/savegame.json"' || exit 2
cp "$U/savegame.json" "$W/save_after_night.json"
attempt defeat 'cp "$W/save_after_night.json" "$U/savegame.json"' || exit 3
echo ALL DONE
