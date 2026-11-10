import unittest

from dates import parse_date


class ParseDateTest(unittest.TestCase):
    def test_year(self):
        self.assertEqual(parse_date("2026-03-01")[0], 2026)

    def test_same_day_and_month(self):
        self.assertEqual(parse_date("2026-07-07"), (2026, 7, 7))

    def test_month_and_day(self):
        self.assertEqual(parse_date("2026-03-01"), (2026, 3, 1))


if __name__ == "__main__":
    unittest.main()
