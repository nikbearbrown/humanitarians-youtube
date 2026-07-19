# FACTCHECK — medhavy-companion-tunneling/short

## Physics claims verified

1. **T = exp(-2*kappa*d)**: WKB approximation for rectangular barrier.
   Source: Griffiths "Introduction to Quantum Mechanics" Ch.8.

2. **kappa = sqrt(2*m*(V0-E))/hbar**: V0=1 eV, E=0.5 eV.
   dV = 0.5 eV = 8.01e-20 J.
   kappa = sqrt(2*9.109e-31*8.01e-20) / 1.0546e-34 = sqrt(1.46e-49) / 1.0546e-34
         = 1.208e-25 / 1.0546e-34 = 1.146e9 m^-1 = 1.146 nm^-1. CORRECT.

3. **slope = -2*kappa = -2.292 per nm**: From ln(T) = -2*kappa*d.
   Rounded to -2.29 in display. CORRECT.

4. **T=1 at d=0**: exp(-2*kappa*0) = exp(0) = 1. Exact. CORRECT.

5. **At d=1 nm**: ln(T) = -2*1.146*1 = -2.292. T = exp(-2.292) = 0.101. CORRECT.
6. **At d=2 nm**: ln(T) = -4.584. T = exp(-4.584) = 0.010. CORRECT.

7. **Portrait layout verification**:
   - sy(0) = 0.0 - 2.4 + (0+5)/5.5*4.8 = -2.4 + 4.364 = 1.964. x-axis in scene at y=1.964.
   - sy(-2.29) = -2.4 + (2.71/5.5)*4.8 = -2.4 + 2.367 = -0.033. At sx(1)=0.0.
   - Panel bottom at cy_pan-pan_h/2 = -2.4. Chips at -2.78 and -3.20 between -2.4 and -3.4. CORRECT.
   - t1_lbl at (-0.65, sy(0)+0.38) = (-0.65, 2.34). Panel top = 2.4. Inside. CORRECT.

VERDICT: All physics claims accurate.
