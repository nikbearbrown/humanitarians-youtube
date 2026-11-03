# FACTCHECK — gps-how-it-works

| # | Claim | Verdict |
|---|---|---|
| 1 | GPS satellites continuously broadcast time and their position | TRUE — navigation message carries clock and orbital (ephemeris) data |
| 2 | The phone only receives; it sends nothing to the satellites | TRUE — GPS is receive-only |
| 3 | Signal delay × known speed gives distance | TRUE — pseudorange |
| 4 | One → circle, two → two points, three → one point | TRUE as the 2-D simplification shown; in 3-D these are spheres |
| 5 | A fourth satellite corrects the receiver's clock | TRUE — solves for the receiver clock bias |
| 6 | 1 µs timing error ≈ 300 m | COMPUTED: 299,792,458 m/s × 1e-6 s = 299.8 m |
| 7 | Buildings and tunnels block or bounce signals; accuracy varies | TRUE — obstruction and multipath |
