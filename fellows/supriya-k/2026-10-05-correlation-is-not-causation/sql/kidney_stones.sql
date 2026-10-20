-- Charig et al., BMJ 1986;292:879-82, Table II (counts); Table I (patients per group).
CREATE TABLE kidney_stones (
  treatment  TEXT,     -- 'open surgery' | 'keyhole (PCNL)'
  stone_size TEXT,     -- 'small' (<2 cm) | 'large' (>=2 cm or multiple stones)
  patients   INTEGER,
  successes  INTEGER
);
INSERT INTO kidney_stones VALUES
  ('open surgery',   'small',  87,  81),
  ('open surgery',   'large', 263, 192),
  ('keyhole (PCNL)', 'small', 270, 234),
  ('keyhole (PCNL)', 'large',  80,  55);
