WITH counts AS (
  SELECT user_id, track_id, COUNT(*) AS plays
  FROM   plays
  GROUP  BY user_id, track_id
),
ranked AS (
  SELECT user_id, track_id, plays,
         ROW_NUMBER() OVER (
           PARTITION BY user_id
           ORDER BY plays DESC, track_id ASC
         ) AS rn
  FROM   counts
)
SELECT user_id, track_id, plays
FROM   ranked
WHERE  rn = 1;
