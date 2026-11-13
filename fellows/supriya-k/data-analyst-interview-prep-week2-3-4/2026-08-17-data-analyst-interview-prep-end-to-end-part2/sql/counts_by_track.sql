SELECT user_id, track_id, COUNT(*) AS plays
FROM   plays
GROUP  BY user_id, track_id
ORDER  BY user_id, plays DESC, track_id;
