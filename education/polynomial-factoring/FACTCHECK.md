# FACTCHECK — polynomial-factoring

**Topic**: Polynomial Factoring Decision Tree

## Claims verified

1. **GCF first** — Correct. Standard first step in all factoring algorithms; extracting the greatest common factor simplifies subsequent steps.

2. **Difference of squares: a² − b² = (a+b)(a−b)** — Standard algebraic identity, correct. Only applies to differences, not sums (a²+b² does not factor over ℝ).

3. **Trinomial strategy: find p, q where p·q = c and p+q = b** — Correct for monic trinomials x² + bx + c. This is the standard "product-sum" method.

4. **Worked example: x² + 5x + 6**
   - GCF: none (coefficients are 1, 5, 6; GCF = 1). Correct.
   - 3 terms → trinomial strategy. Correct.
   - a = 1, need p·q = 6 and p+q = 5. Correct.
   - Pairs: 1×6 = 6, sum = 7 ✗. Correct.
   - Pairs: 2×3 = 6, sum = 5 ✓. Correct.
   - Answer: (x+2)(x+3). Correct.
   - Check: (x+2)(x+3) = x²+3x+2x+6 = x²+5x+6. Correct ✓

5. **Grouping strategy for 4-term polynomials** — Correct. Factor pairs of terms, extract common binomial factor.

## No issues found. All factoring claims and the worked example are correct.
