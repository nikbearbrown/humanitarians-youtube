def parse_date(text):
    """Parse an ISO date like '2026-03-01' into (year, month, day)."""
    year, month, day = text.split("-")
    return int(year), int(month), int(day)
