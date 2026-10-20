WITH running AS (
  SELECT account_id, transaction_id, posted_at,
    SUM(amount) OVER (
      PARTITION BY account_id
      ORDER BY posted_at, transaction_id
      ROWS UNBOUNDED PRECEDING
    ) AS running_balance
  FROM transactions
  -- filters BEFORE the sum
  WHERE posted_at >= '2026-01-01'
    AND posted_at <  '2026-07-01'
),
last_posting_per_month AS (
  SELECT account_id,
    DATE_FORMAT(posted_at, '%Y-%m-01') AS month_start,
    running_balance,
    ROW_NUMBER() OVER (
      PARTITION BY account_id,
                   DATE_FORMAT(posted_at, '%Y-%m')
      ORDER BY posted_at DESC, transaction_id DESC
    ) AS rn
  FROM running
),
monthly_balances AS (
  SELECT account_id, month_start,
         running_balance AS eom_balance
  FROM   last_posting_per_month
  WHERE  rn = 1
)
SELECT account_id, month_start, eom_balance
FROM   monthly_balances
ORDER  BY account_id, month_start;
