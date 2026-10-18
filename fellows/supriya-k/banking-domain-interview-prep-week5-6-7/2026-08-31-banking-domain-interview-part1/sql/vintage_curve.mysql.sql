WITH cohort AS (
  SELECT account_id
  FROM   accounts
  WHERE  origination_month = '2025-01-01'
),
snap AS (
  SELECT s.account_id, s.dpd_bucket,
    PERIOD_DIFF(
      DATE_FORMAT(s.snapshot_month, '%Y%m'),
      DATE_FORMAT(a.origination_month, '%Y%m')
    ) AS months_on_book
  FROM monthly_snapshots s
  JOIN accounts a ON a.account_id = s.account_id
  JOIN cohort   c ON c.account_id = s.account_id
),
scoped AS (
  SELECT * FROM snap WHERE months_on_book IN (3, 6, 9)
),
bucketed AS (
  SELECT months_on_book, dpd_bucket,
    COUNT(*) AS accounts_in_bucket,
    SUM(COUNT(*)) OVER (
      PARTITION BY months_on_book
    ) AS cohort_total
  FROM scoped
  GROUP BY months_on_book, dpd_bucket
)
SELECT months_on_book, dpd_bucket, accounts_in_bucket,
  ROUND(100 * accounts_in_bucket / cohort_total, 1)
    AS pct_of_cohort
FROM bucketed
ORDER BY months_on_book,
  FIELD(dpd_bucket, 'current', '30', '60', '90+', 'charge_off');
