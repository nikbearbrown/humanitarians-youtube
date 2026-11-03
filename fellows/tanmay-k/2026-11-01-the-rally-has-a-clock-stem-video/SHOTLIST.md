# SHOTLIST — Pong (long film 16:9 and Short 9:16)

Every picture is our own drawing and simulation: no third-party footage, images or marks. Slates are drawn with Pillow (EB Garamond + Inter, open licences); every figure on a slate is computed by `sim_model.py` and asserted against the signed narration before a pixel is drawn.

## Long film

| Beat | Start | Length | Picture | Stages (cue times) |
|---|---|---|---|---|
| B00 Shot Six | 0:00.0 | 14.3 s | Our rectangles on black. Shot counter 1 to 6. The two framework bars (paddle can travel / paddle must travel, with the line) sit in a corner from frame one, unnarrated. Paddle slides; ball passes on shot six; hold on the gap. 'Our model' tag stays in a corner all film. | rally_start 0.0s, paddles_play 1.0s, counter_1 2.6s, counter_2 3.2s, counter_3 3.9s, counter_4 4.5s ... |
| B01 The Claim | 0:14.3 | 12.9 s | The two phrases as chips, source line: 'from an essay in the Humanitarians AI repo' (author credited in README and description, not on screen). | chip_no_perfect_defense 0.0s, chip_game_to_eleven 3.1s, question_line 8.1s |
| B02 The Stage | 0:27.2 | 20.3 s | Field drawn once with labels fading in. Settings chip stays on screen from here: field 858 by 525, paddle 60, ball starts at 6 per tick, plus 5 percent per shot. | field 0.0s, paddle_arrows 2.6s, bounce_note 4.5s, steering_card 6.8s, name_chip 10.9s, constants_card_lit 14.0s |
| B03 What The Defender Knows | 0:47.4 | 18.6 s | Ball launched, dotted path with wall bounces unfolded into a straight line; timer bar for one crossing. The two corner bars are highlighted and labelled 'can travel' and 'must travel'. | ball_launch_path 0.0s, defender_sees 2.8s, timer_bar 7.1s, bars_highlight 10.9s, can_bar_pulse 13.1s, must_bar_pulse 15.9s |
| B04 The Worst Shot | 1:06.0 | 16.2 s | Fan of paths from the attacker's paddle; landing points marked along the far wall; defender parked at center; the two extreme landings lit; 'must travel' bar grows to match. | attacker 0.0s, fan_all_aims 3.1s, defender_waits_middle 7.6s, extremes_lit 11.6s, half_field_card 14.5s |
| B05 The Line | 1:22.2 | 20.0 s | Two bars large, threshold line, ratio 0.27 appears once; the form as a one-line card: 'reach in one flight vs half the free height'. | bars_large 0.0s, compare 2.7s, exists 7.5s, none_exists 9.6s, ratio_0_27 10.7s, form_card 14.0s |
| B06 Turn The Dial | 1:42.3 | 19.2 s | Three lanes side by side, same rally, three dial settings; counters stop at 1, 6 and 14; each held at least two seconds. | rows_appear 0.0s, row1_break_1 3.7s, row2_fill_to_6 6.4s, row3_fill_to_14 9.6s, same_rules 12.7s, one_number 14.3s |
| B07 The Clock | 2:01.5 | 17.1 s | The two bars stepping down shot by shot with the counter; line crossed on the break shot. | chart_axes 0.3s, ball_speeds_up 1.8s, curves_draw 3.4s, bars_sink 8.4s, in_my_model 10.5s, clock_line 13.1s |
| B08 Predicted, Then Found | 2:18.5 | 19.7 s | Table filling in: predicted 4.24 -> sixth; found sixth. Predicted 12.56 -> fourteenth; found fourteenth. Side by side, held two seconds. | header 0.0s, row1_arithmetic 3.0s, row1_found 8.0s, row2_arith_and_found 11.1s, fourteenth_found 15.8s |
| B09 The Second Dial | 2:38.3 | 20.2 s | Fan narrows to a thin wedge; line drops from 0.271 to 0.215 on the bar. Predicted breaks appear as ticks on the shot counter first, then the count runs and lands on each tick; a closing two-line tally puts old breaks (sixth, fourteenth) beside new (tenth, nineteenth), held two seconds. No table until the end. | second_dial 0.0s, aim_anywhere 0.9s, wedge_narrows 3.0s, line_drops 7.9s, tick_tenth 11.3s, tick_nineteenth 12.9s ... |
| B10 A Different Field | 2:58.5 | 19.5 s | Lead with the new field redrawn at the same scale beside the old one; settings chip updated (1200 by 500, paddle 50); line bar drops to 0.188; then a small predicted-vs-found table for all three speeds (1.5, 2.5, 4.0), held two seconds. Speech names two; the table shows the third (eighteenth) silently. | new_field 0.0s, size_chip 1.2s, line_0_1875 5.2s, two_speeds 6.9s, predicted_col 9.2s, found_col 11.9s ... |
| B11 Which Rule | 3:18.0 | 21.8 s | The two dials lit; a third lane, fast paddle and no speed-up, counter running past the frame. | question 0.0s, dial_one 5.8s, dial_two 7.3s, conditional 8.6s, no_speedup_card 10.7s, speeding_up_line 16.9s |
| B12 What This Does Not Claim | 3:39.8 | 17.1 s | Plain slate listing what is left out. | header 0.0s, model_line 3.0s, item_spin 4.2s, item_reaction 5.3s, item_paddle_edges 6.8s, item_real_machine 8.4s ... |
| B13 Your Turn | 3:56.9 | 30.5 s | Card: line = (height - paddle) / (2 x width). The numbers 1000, 500, 50 appear; answer withheld for a five second hold, then 0.225 appears with the 0.25 and 0.2 comparison. Then the dial, still, counter at zero; fade. | your_turn 0.0s, case_numbers 0.6s, line_formula 4.3s, hold_start 8.9s, answer_0_225 13.9s, verdict_cards 14.8s ... |

## Short (one continuous scene)

| Line | Start | End | Picture |
|---|---|---|---|
| S01 The Bet | 0.3 s | 6.9 s | Hook on frame one: the field fills the safe area, the rally already moving; big counter at the top. |
| S02 The Context | 7.7 s | 19.8 s | Same scene, the ball easing between the paddles; a settings chip in the safe area (858 by 525, paddle 60, plus five percent per shot); the two essay phrases as small captions. |
| S03 The Count | 20.6 s | 27.9 s | Counter 1 to 6 in step with the words; the ball's path to the top edge each shot; on six the paddle stops 8.4 px short. |
| S04 The Time | 28.7 s | 35.9 s | A timer bar for one crossing shrinks with each shot; the ball's speed number steps up. |
| S05 The Two Bars | 36.7 s | 48.6 s | The two bars grow into view over the field (can travel 286 px at shot one; must travel 232.5 px), the line between them. |
| S06 The Clock | 49.4 s | 63.1 s | The first bar sinks shot by shot (286 to 224 px); on six it crosses the line; the gap lit; two ticks land on shot six. |
| S07 The Limit | 63.9 s | 72.2 s | MODEL, NOT A MACHINE in the safe area; the no-speed-up row runs past the frame edge. |
| S08 The Film | 73.0 s | 78.4 s | The title in the safe area; the scene settles back to the first frame (loop-friendly). |

Full change schedule and the phone contract (safe band, type sizes, headline per phase) are in `SHORT-SCRIPT.md`.
