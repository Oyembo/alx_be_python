class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)
    
class EBook(Book): 
    def __init__(self, file_size):
        super(). __init__(title, author)
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, page_count):
        super(). __init__(title, author)
        self.page_count = int(page_count)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        print(f"Added '{book.title}' to Library")
    
    def list_books(self):
        print(f"Books in {self.books}")
    
        


