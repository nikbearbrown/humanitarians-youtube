# FACTCHECK — How GPS Knows Where You Are

| Beat | Claim | Verdict | Source / basis | Fix applied |
|---|---|---|---|---|
| B00 | Bella is an AI narrator; Claude drafted the script and Tanishaa approved it. | TRUE | Kokoro `af_bella`; script approved in chat 2026-11-08. | none |
| B01 | Phones never transmit to GPS satellites; they only listen and time the signals. | TRUE | GPS is a one-way broadcast system; receivers are passive. | none |
| B02 | About thirty satellites, about twenty thousand kilometers up. | TRUE | gps.gov: 24-slot baseline; a 2025 gps.gov ICWG deck lists 31 set healthy. Altitude about 20,200 km (Penn State GEOG 862; demo uses 26,560 km orbital radius → 20,189 km). | Says "about thirty", since gps.gov pages differ on the exact count. |
| B03 | Satellites broadcast position and time from onboard atomic clocks; delay × c = distance; ~0.07 s ≈ 21,000 km. | TRUE | GPS navigation message (ephemeris + time); demo: 70.59 ms → 21,162 km. | none |
| B04 | One range → a sphere, two → a circle, three → two points (one far off in space). | TRUE | Standard trilateration; the 2D circles are labeled as a flattened picture. | Caption "Flattened to circles. In 3D they're spheres." |
| B05 | 1 µs clock error = ~300 m per range; a fourth satellite solves the receiver clock. | TRUE | c × 1 µs = 299.8 m (demo); 4 unknowns (x, y, z, clock bias) need 4 ranges. | none |
| B06 | Ignoring the 1 µs clock error → 390 m off; solving for it → on the spot, finds 1.000000 µs. | TRUE (demo) | demo/gps_demo.py → gps_output.json (ignore: 390.2 m; solve: 7.4e-9 m, 1.000000 µs). Satellite positions are illustrative. | Footnote says the sky is an example and the solver is real. |
| B07 | Relativity: satellite clocks gain ~38 µs/day (gravity +45, speed −7); uncorrected ~11 km/day; clocks set slow before launch. | TRUE | Penn State GEOG 862 "The Satellite Clock"; Ohio State Astronomy 162 GPS notes; 38 µs × c = 11.4 km. | Says "about eleven kilometers" (computed), not the rounded "10 km" popular figure. |
| B08 | Open sky: within about 5 m; buildings bounce signals; indoors falls back on Wi-Fi/cell; satellites never know where you are. | TRUE | gps.gov GPS Accuracy: smartphones typically within 4.9 m under open sky, worse near buildings, bridges and trees. | none |
| B09 | Takeaway. | summary of B01–B08 | — | none |
| B10 | Your-turn prompt. | advice | — | none |
