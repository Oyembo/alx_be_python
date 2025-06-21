class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the Book object.
        """
        return f"{self.title} by {self.author}"
class EBook(Book): 
    def __init__(self, file_size):
        super(). __init__(title, author)
        self.file_size = int(file_size)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the EBook object,
        including its file size.
        """
        return f"{self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, page_count):
        super(). __init__(title, author)
        self.page_count = int(page_count)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the PrintBook object,
        including its page count.
        """
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        print(f"Added '{book.title}' to Library")
    
    def list_books(self):
        print(f"Books in {self.books}")
    
        


