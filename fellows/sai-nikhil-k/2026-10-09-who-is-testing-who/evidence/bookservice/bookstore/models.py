from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    id: int
    title: str
    author: str


@dataclass(frozen=True)
class BookDto:
    id: int
    title: str
    author: str


class BookNotFoundError(Exception):
    pass


class Unauthorized(Exception):
    """The article's SecurityException("Unauthorized")."""
