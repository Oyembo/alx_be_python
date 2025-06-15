class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = Date 
class Library:
    def __init__(self):
        self._book = []
    def add_book(self, book):
        """Adds a book to library collection"""
        library.add_book(Book("title", "author"))
    def check_out_book(self, title):
        """Check out book by title"""
        library.check_out_book("title")
        print("Available books after check out: ")
    def return_book(self, title):
        """Return book to library by title"""
        print("Available book after return: ")
    def list_available_books(self):
        """Lists all book currently available in library"""
        available_books = [book for book in self._books if not book._is_checked_out]
        library.list_available_books()




