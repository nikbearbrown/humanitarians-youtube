# FACTCHECK — "Claude, Ringed."

| Claim (beat) | Verdict | Source / derivation |
|---|---|---|
| Servers and keys hashed onto the same circular space (B02) | ✓ | Karger et al., 1997, "Consistent Hashing and Random Trees" — the ring is the algorithm's defining structure |
| A key's owner is the next server clockwise (B03) | ✓ | Same source — the lookup rule |
| Adding a node only remaps the arc between it and its counter-clockwise neighbor (B04) | ✓ | Direct consequence of the ring + "next clockwise" rule |
| Plain consistent hashing gives uneven load at small N (B05) | ✓ | Well-known limitation; motivation for virtual nodes in DynamoDB (2007) and Cassandra |
| Virtual nodes reduce load variance (B05) | ✓ | Same sources — the documented reason virtual nodes exist in production |

## Corrections applied

None needed.

## Numbers on screen

None invented. "~1/N keys move" is a structural property (N servers evenly
dividing the ring implies ~1/N per server), not a benchmark.
