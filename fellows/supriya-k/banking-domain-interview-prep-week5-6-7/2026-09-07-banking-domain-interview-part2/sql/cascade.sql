-- Cascade Savings (the book's invented regional bank, Ch.8) — ledger fixture.
-- Schema verbatim from Ch.8 "Reading a banking schema fast". One account opened in 2025,
-- so the reporting window (2026 H1) has real history before it.
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
    account_id     INT PRIMARY KEY,
    customer_id    INT NOT NULL,
    opened_date    DATE NOT NULL,
    account_type   VARCHAR(20) NOT NULL,
    status         VARCHAR(10) NOT NULL
);
CREATE TABLE transactions (
    transaction_id   INT PRIMARY KEY,
    account_id       INT NOT NULL,
    posted_at        DATETIME NOT NULL,
    amount           DECIMAL(12,2) NOT NULL,
    transaction_type VARCHAR(12) NOT NULL,
    reversal_of      INT NULL
);
INSERT INTO accounts VALUES (50231, 7781, '2025-11-01', 'checking', 'open');
INSERT INTO transactions VALUES
  (1, 50231, '2025-11-03 10:15:00', 12400.00, 'deposit',    NULL),
  (2, 50231, '2026-01-08 14:02:00',  -300.00, 'withdrawal', NULL),
  (3, 50231, '2026-02-14 09:30:00',   150.00, 'deposit',    NULL),
  (4, 50231, '2026-03-01 16:45:00',   -75.00, 'withdrawal', NULL);
