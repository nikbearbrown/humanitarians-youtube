"""The same four scenarios, through the real pieces and a real database (SQLite, in
memory — the stand-in here for the article's Testcontainers / DataJpaTest). No mocks.
Asserts what a caller sees: the returned book, the error raised, the counter recorded."""
import sqlite3

import pytest

from bookstore.models import BookDto, BookNotFoundError, Unauthorized
from bookstore.parts import BookMapper, BookValidator, MetricsService, SecurityService
from bookstore.repository import SCHEMA, BookRepository
from bookstore.service import BookService


def make(roles=("reader",)):
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO books VALUES (?, ?, ?)",
                     [(1, "Book One", "Author One"), (2, "The Loon", "A. Birder")])
    metrics = MetricsService()
    service = BookService(BookRepository(conn), BookValidator(), BookMapper(),
                          SecurityService(roles), metrics)
    return service, metrics


def test_returns_the_stored_book():
    service, metrics = make()
    assert service.get_book_by_id(2) == BookDto(2, "The Loon", "A. Birder")
    assert metrics.counters == {"book.fetch.success": 1}


def test_missing_book_is_not_found_and_not_counted():
    service, metrics = make()
    with pytest.raises(BookNotFoundError):
        service.get_book_by_id(99)
    assert metrics.counters == {}


def test_without_permission_is_refused():
    service, metrics = make(roles=("guest",))
    with pytest.raises(Unauthorized):
        service.get_book_by_id(1)
    assert metrics.counters == {}


def test_invalid_id_is_rejected():
    service, _ = make()
    with pytest.raises(ValueError):
        service.get_book_by_id(0)
