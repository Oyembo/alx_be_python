class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

class EBook(Book): 
    def __init__(self, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Invalid item. Only Book instances can be added to the library.")  
    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
Library = Book()

    
        


