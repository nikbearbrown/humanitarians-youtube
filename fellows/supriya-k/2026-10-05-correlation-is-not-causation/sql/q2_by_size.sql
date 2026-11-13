SELECT stone_size,
       treatment,
       SUM(patients) AS patients,
       ROUND(100.0 * SUM(successes)
             / SUM(patients), 1)
         AS success_pct
FROM kidney_stones
GROUP BY stone_size, treatment
ORDER BY stone_size DESC,
         success_pct DESC;
