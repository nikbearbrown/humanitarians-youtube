"""Unit tests for the dependencies that CAN be unit-tested without a mock — the article's
"combined with unit tests for the dependencies". The repository can't be: its behaviour
is a SQL query, and testing that needs a database ("not what most people would consider
a unit test")."""
import pytest

from bookstore.models import Book, BookDto
from bookstore.parts import BookMapper, BookValidator, MetricsService, SecurityService


@pytest.mark.parametrize("bad", [0, -1, None, "1"])
def test_validator_rejects(bad):
    with pytest.raises(ValueError):
        BookValidator().validate_id(bad)


def test_validator_accepts_positive():
    BookValidator().validate_id(1)


def test_mapper_copies_every_field():
    assert BookMapper().to_dto(Book(7, "T", "A")) == BookDto(7, "T", "A")


def test_security_reader_can_read():
    assert SecurityService(["reader"]).has_read_permission() is True


def test_security_others_cannot():
    assert SecurityService(["guest"]).has_read_permission() is False


def test_metrics_counts():
    m = MetricsService()
    m.increment_counter("x"); m.increment_counter("x")
    assert m.counters["x"] == 2
