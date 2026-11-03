SELECT treatment,
       SUM(patients) AS patients,
       ROUND(100.0 * SUM(successes)
             / SUM(patients), 1)
         AS success_pct
FROM kidney_stones
GROUP BY treatment
ORDER BY success_pct DESC;
