"""Pure logic, the kind the article says unit tests are for: "a pricing calculator that
applies discounts based on a set of rules". No I/O, no collaborators, nothing to mock."""


def order_total(prices, member=False, coupon=None):
    """Sum in cents. Rules: members get 10% off; 3+ items get the cheapest one free;
    coupon "SAVE5" takes 500 cents off orders of 5000 or more. Never below zero."""
    if any(p < 0 for p in prices):
        raise ValueError("prices can't be negative")
    total = sum(prices)
    if len(prices) >= 3:
        total -= min(prices)
    if member:
        total = total * 90 // 100
    if coupon == "SAVE5" and total >= 5000:
        total -= 500
    return max(total, 0)
