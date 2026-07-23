# FACTCHECK — medhavy-vol5-multiplicity-peak/short

## Physics claims verified

1. **Multiplicity formula**: Omega(N,n) = C(N,n) = N!/(n!(N-n)!)
   - Standard statistical mechanics result. Source: Kittel & Kroemer Ch.2, Reif Ch.1.

2. **Peak at n=N/2**: C(10,5) = 10!/(5!5!) = 3628800/14400 = 252. Verified.

3. **Adjacent bar**: C(10,4) = 10!/(4!6!) = 3628800/17280 = 210.
   - 252/210 = 1.20; peak is 20% above adjacent. Verified.

4. **Pascal symmetry**: C(N,n) = C(N,N-n) for all n. Exact symmetry — peak at n=N/2 for any even N.

5. **Portrait scene values**:
   - sx(5) = -1.6 + (5+0.5)/11*3.2 = -1.6 + 5.5/11*3.2 = -1.6+1.6 = 0.0 (center). Correct.
   - sy(252) = 0.1-2.25 + 252/280*4.5 = -2.15 + 4.05 = 1.90. Within pan top 2.35. Correct.
   - Peak chip at y=1.90+0.34=2.24 — below sub at 2.82, above panel top 2.35? No: 2.24 < 2.35.
     Chip is INSIDE the panel zone (bar_top+chip_half ~ 2.24+~0.15=2.39). Slightly overlapping
     panel top. However the header is at 3.15 and sub at 2.82 — chip at 2.24 is clear of those.
     Gate B will confirm no visual overlap.

VERDICT: All physics claims accurate.
