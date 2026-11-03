"""Unit tests on pure logic: input in, output out, no mocks."""
import pytest

from bookstore.pricing import order_total


def test_plain_sum():
    assert order_total([1000, 2000]) == 3000


def test_three_items_cheapest_free():
    assert order_total([1000, 2000, 500]) == 3000


def test_two_items_no_free_item():
    assert order_total([1000, 500]) == 1500


def test_member_ten_percent():
    assert order_total([1000, 2000], member=True) == 2700


def test_member_rounds_down():
    assert order_total([999], member=True) == 899


def test_coupon_at_threshold():
    assert order_total([5000], coupon="SAVE5") == 4500


def test_coupon_below_threshold():
    assert order_total([4999], coupon="SAVE5") == 4999


def test_coupon_applies_after_member_discount():
    assert order_total([6000], member=True, coupon="SAVE5") == 5400 - 500


def test_member_discount_can_drop_below_coupon_threshold():
    assert order_total([5500], member=True, coupon="SAVE5") == 4950


def test_unknown_coupon_ignored():
    assert order_total([6000], coupon="SAVE50") == 6000


def test_empty_order():
    assert order_total([]) == 0


def test_negative_price_rejected():
    with pytest.raises(ValueError):
        order_total([100, -1])
