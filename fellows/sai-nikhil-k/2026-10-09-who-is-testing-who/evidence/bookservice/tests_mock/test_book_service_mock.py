"""The mock-heavy suite. test_get_book_by_id_success is the article's BookServiceTest,
ported line for line (Mockito → unittest.mock). The article shows only that one test; the
other three give the mock style its strongest fair form — the same scenarios the
database suite covers, written the same way, each verifying what it should and
should not have called."""
from unittest.mock import Mock

import pytest

from bookstore.models import Book, BookDto, BookNotFoundError, Unauthorized
from bookstore.service import BookService


@pytest.fixture
def m():
    """@Mock × 5 and @InjectMocks."""
    mocks = {k: Mock() for k in ("book_repository", "book_validator", "book_mapper",
                                 "security_service", "metrics_service")}
    mocks["service"] = BookService(**mocks)
    return mocks


def test_get_book_by_id_success(m):
    # Arrange
    book_id = 1
    book = Book(book_id, "Book One", "Author One")
    book_dto = BookDto(book_id, "Book One", "Author One")
    m["book_validator"].validate_id.return_value = None            # doNothing()
    m["security_service"].has_read_permission.return_value = True
    m["book_repository"].find_by_id.return_value = book            # Optional.of(book)
    m["book_mapper"].to_dto.return_value = book_dto
    m["metrics_service"].increment_counter.return_value = None     # doNothing()

    # Act
    result = m["service"].get_book_by_id(book_id)

    # Assert
    assert result is not None
    assert result.title == "Book One"

    # Verify
    m["book_validator"].validate_id.assert_called_once_with(book_id)
    m["security_service"].has_read_permission.assert_called_once_with()
    m["book_repository"].find_by_id.assert_called_once_with(book_id)
    m["book_mapper"].to_dto.assert_called_once_with(book)
    m["metrics_service"].increment_counter.assert_called_once_with("book.fetch.success")


def test_get_book_by_id_not_found(m):
    m["security_service"].has_read_permission.return_value = True
    m["book_repository"].find_by_id.return_value = None            # Optional.empty()
    with pytest.raises(BookNotFoundError):
        m["service"].get_book_by_id(99)
    m["book_repository"].find_by_id.assert_called_once_with(99)
    m["metrics_service"].increment_counter.assert_not_called()      # verifyNoInteractions
    m["book_mapper"].to_dto.assert_not_called()


def test_get_book_by_id_unauthorized(m):
    m["security_service"].has_read_permission.return_value = False
    with pytest.raises(Unauthorized):
        m["service"].get_book_by_id(1)
    m["book_repository"].find_by_id.assert_not_called()
    m["metrics_service"].increment_counter.assert_not_called()


def test_get_book_by_id_invalid_id(m):
    m["book_validator"].validate_id.side_effect = ValueError("bad id")
    with pytest.raises(ValueError):
        m["service"].get_book_by_id(0)
    m["security_service"].has_read_permission.assert_not_called()
    m["book_repository"].find_by_id.assert_not_called()
