"""The four collaborators the article's BookService takes besides the repository."""
from collections import Counter

from .models import Book, BookDto


class BookValidator:
    def validate_id(self, book_id):
        if not isinstance(book_id, int) or book_id <= 0:
            raise ValueError("book id must be a positive integer")


class BookMapper:
    def to_dto(self, book: Book) -> BookDto:
        return BookDto(id=book.id, title=book.title, author=book.author)


class SecurityService:
    def __init__(self, roles):
        self.roles = set(roles)

    def has_read_permission(self) -> bool:
        return "reader" in self.roles


class MetricsService:
    def __init__(self):
        self.counters = Counter()

    def increment_counter(self, name: str) -> None:
        self.counters[name] += 1
