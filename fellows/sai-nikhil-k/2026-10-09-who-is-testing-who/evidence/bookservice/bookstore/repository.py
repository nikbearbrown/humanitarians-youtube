"""The repository the article's test mocks. Here it is real: SQLite (stdlib)."""
import sqlite3

from .models import Book

SCHEMA = "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)"


class BookRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def find_by_id(self, book_id):
        """Optional<Book> in the article: the Book, or None."""
        row = self.conn.execute(
            "SELECT id, title, author FROM books WHERE id = ?", (book_id,)).fetchone()
        return Book(*row) if row else None
