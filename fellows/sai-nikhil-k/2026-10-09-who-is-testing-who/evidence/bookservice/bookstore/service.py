"""BookService.getBookById, line for line from the article."""
from .models import BookNotFoundError, Unauthorized


class BookService:
    def __init__(self, book_repository, book_validator, book_mapper, security_service,
                 metrics_service):
        self.book_repository = book_repository
        self.book_validator = book_validator
        self.book_mapper = book_mapper
        self.security_service = security_service
        self.metrics_service = metrics_service

    def get_book_by_id(self, book_id):
        self.book_validator.validate_id(book_id)

        if not self.security_service.has_read_permission():
            raise Unauthorized("Unauthorized")

        book = self.book_repository.find_by_id(book_id)
        if book is None:
            raise BookNotFoundError("Book not found")

        self.metrics_service.increment_counter("book.fetch.success")

        return self.book_mapper.to_dto(book)
