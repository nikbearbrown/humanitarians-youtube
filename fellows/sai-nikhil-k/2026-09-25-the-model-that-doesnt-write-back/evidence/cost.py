"""What TypeSafe's published Jev price means in dollars — arithmetic only.

Every input figure is TypeSafe's own, quoted from the launch post archived at
sources/typesafe-blog-introducing-jev.html (published Sep 15, 2026):
  * input  "$0.042 / MTok ($42 per billion tokens)"
  * output "FREE (too cheap to meter)"
  * latency "70ms-500ms" end-to-end, vs "3 to 329 seconds" for frontier LLMs
  * Doom demo "~$7/hour" at 10 queries per second

Nothing here calls Jev (that needs an account and spends money; this reel is
Fellow Tier). The ticket size is an ASSUMPTION, stated below, not a measurement.
"""
PRICE_PER_M_INPUT = 0.042        # USD per million input tokens (TypeSafe)
TICKETS = 1_000_000
TOKENS_PER_TICKET = 500          # assumption: a short support ticket plus the questions

tokens = TICKETS * TOKENS_PER_TICKET
cost = tokens / 1e6 * PRICE_PER_M_INPUT
print(f"published price          ${PRICE_PER_M_INPUT} per 1M input tokens; output free")
print(f"workload (assumed)       {TICKETS:,} tickets x {TOKENS_PER_TICKET} tokens = {tokens:,} tokens")
print(f"input cost               ${cost:,.2f}")
print(f"per ticket               ${cost / TICKETS:.6f}  ({cost / TICKETS * 100:.4f} cents)")

# Consistency check on TypeSafe's own Doom figure: what state size does "$7/hour
# at 10 queries/second" imply at this price?
q_per_hour = 10 * 3600
implied = 7 / q_per_hour / PRICE_PER_M_INPUT * 1e6
print(f"\nDoom demo check          ~$7/h at 10 q/s = {q_per_hour:,} queries/h")
print(f"implied input per query  {implied:,.0f} tokens (plausible for a JSON game state)")

# Latency range as stated
print(f"\nlatency (TypeSafe)       70-500 ms vs 3-329 s: ratio {3/0.5:.0f}x to {329/0.07:,.0f}x at the extremes")
