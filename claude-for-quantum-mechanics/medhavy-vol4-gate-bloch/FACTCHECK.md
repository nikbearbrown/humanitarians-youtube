# FACTCHECK — medhavy-vol4-gate-bloch

## Formula: Hadamard gate H
  Source: Nielsen & Chuang "Quantum Computation and Quantum Information" §1.3
  H = (1/sqrt(2)) * [[1,1],[1,-1]]
  H|0> = |+> = (|0>+|1>)/sqrt(2) (north pole to equator on Bloch sphere)
  H|1> = |-> = (|0>-|1>)/sqrt(2)
  H*H = I (Hadamard is its own inverse) ✓

## Formula: Phase gate S
  Source: Nielsen & Chuang §1.3, p. 18
  S = [[1,0],[0,i]] = [[1,0],[0,e^(i*pi/2)]]
  S|+> = (|0>+i|1>)/sqrt(2) = |i> (rotation by pi/2 about z-axis on Bloch sphere)
  Bloch sphere: equatorial rotation by 90 degrees (phi: 0 -> pi/2) ✓

## Numbers:
  - |0> at north pole: theta=0, phi=0 (Bloch vector = [0,0,1])
  - H applied: |+> at equator: theta=pi/2, phi=0 (Bloch vector = [1,0,0])
  - S applied to |+>: |i>=(|0>+i|1>)/sqrt(2): theta=pi/2, phi=pi/2 (Bloch vector=[0,1,0])
  - H*H=I: |+> -> H -> |0> -> confirmed ✓

## Two testable predictions:
  P1: H*H = I: applying Hadamard twice returns to |0> (north pole) ✓
  P2: S gate rotates equatorial state by exactly pi/2 (90 degrees) about z-axis:
      |+> -> |i>, phi shifts from 0 to pi/2 ✓

VERDICT: PASS
