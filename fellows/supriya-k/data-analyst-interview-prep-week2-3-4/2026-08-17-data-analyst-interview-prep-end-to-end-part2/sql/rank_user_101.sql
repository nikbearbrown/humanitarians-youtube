-- B02: what a window function keeps — user 101's per-track rows, each with its RANK.
WITH counts AS (
  SELECT user_id, track_id, COUNT(*) AS plays
  FROM   plays
  GROUP  BY user_id, track_id
)
SELECT user_id, track_id, plays,
       RANK() OVER (
         PARTITION BY user_id
         ORDER BY plays DESC
       ) AS rnk
FROM   counts
WHERE  user_id = 101
ORDER  BY rnk, track_id;
