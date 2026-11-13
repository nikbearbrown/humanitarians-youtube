-- pair strftime — strftime() on an indexed DATE column
-- wrapped (non-sargable) -> explain_a_non_sargable.txt
SELECT account_id, SUM(amount_cents) AS total_cents
FROM postings
WHERE strftime('%Y-%m', posted_at) = '2026-01'
GROUP BY account_id;

-- bare (sargable) -> explain_b_sargable.txt
SELECT account_id, SUM(amount_cents) AS total_cents
FROM postings
WHERE posted_at >= '2026-01-01' AND posted_at < '2026-02-01'
GROUP BY account_id;

-- pair CAST — CAST() on an indexed INTEGER column
-- wrapped (non-sargable) -> explain_c_non_sargable_cast.txt
SELECT COUNT(*) AS n, SUM(amount_cents) AS total_cents
FROM postings
WHERE CAST(branch_id AS TEXT) = '42';

-- bare (sargable) -> explain_d_sargable_cast.txt
SELECT COUNT(*) AS n, SUM(amount_cents) AS total_cents
FROM postings
WHERE branch_id = 42;

-- pair UPPER — UPPER() on an indexed TEXT column
-- wrapped (non-sargable) -> explain_e_non_sargable_upper.txt
SELECT COUNT(*) AS n, SUM(amount_cents) AS total_cents
FROM postings
WHERE UPPER(account_ref) = 'AC-04242';

-- bare (sargable) -> explain_f_sargable_upper.txt
SELECT COUNT(*) AS n, SUM(amount_cents) AS total_cents
FROM postings
WHERE account_ref = 'AC-04242';
