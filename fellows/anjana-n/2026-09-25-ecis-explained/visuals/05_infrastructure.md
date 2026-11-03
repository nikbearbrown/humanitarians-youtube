# B05 — Infrastructure Upgrade

## Composition type
Remotion

## Layout
Dark stage. Migration animation from SQLite to PostgreSQL stack.

## Elements

### Left side: SQLite (old)
- A small single-box icon labeled "SQLite."
- Compact, simple, slightly dim.

### Migration arrow
- An animated flowing arrow from left to right.
- Particles travel along the arrow suggesting data migration.

### Right side: PostgreSQL stack (new)
- A larger box with three internal horizontal layers:
  - Top layer: "signals + outcomes" (blue, #4A90D9).
  - Middle layer: "TimescaleDB hypertable" with a small clock icon (teal, #1ABC9C).
  - Bottom layer: "materialized views" with a small cache/grid icon (green, #27AE60).

### Performance comparison
- Below the PostgreSQL box, a small before-and-after:
  - "query: 2.3s" in red, fading to "query: 0.1s" in green.

### Alembic bar
- A thin horizontal bar running along the bottom labeled "schema versioning (Alembic)."
- Small version markers along it: v1, v2, v3.

## Animation sequence
1. SQLite box appears on left (1s).
2. Migration arrow animates with flowing particles (2s).
3. PostgreSQL stack builds layer by layer on the right (3s).
4. Performance comparison fades in below: 2.3s crosses out, 0.1s appears (2s).
5. Alembic version bar slides in at the bottom (1s).

## Palette
- SQLite: #95A5A6 (muted grey)
- Migration arrow: #F1C40F (gold particles)
- Signals layer: #4A90D9 (blue)
- TimescaleDB layer: #1ABC9C (teal)
- Materialized views: #27AE60 (green)
- Old query time: #E74C3C (red)
- New query time: #27AE60 (green)
- Alembic bar: #7F8C8D (grey)
- Background: #1A1A2E
