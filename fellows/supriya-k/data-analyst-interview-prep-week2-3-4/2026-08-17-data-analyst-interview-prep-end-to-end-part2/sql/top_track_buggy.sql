WITH counts AS (
  SELECT user_id, track_id, COUNT(*) AS plays
  FROM   plays
  GROUP  BY user_id, track_id
),
ranked AS (
  SELECT user_id, track_id, plays,
         RANK() OVER (
           PARTITION BY user_id
           ORDER BY plays DESC
         ) AS rnk
  FROM   counts
)
SELECT user_id, track_id, plays
FROM   ranked
WHERE  rnk = 1;
