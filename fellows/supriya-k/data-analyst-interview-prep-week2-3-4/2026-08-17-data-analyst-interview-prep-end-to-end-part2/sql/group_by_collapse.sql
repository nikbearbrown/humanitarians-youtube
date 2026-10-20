SELECT user_id, COUNT(*) AS plays
FROM   plays
GROUP  BY user_id;
