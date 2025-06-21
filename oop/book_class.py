class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year =int(year)
    
    def ___str__(self):
        return f"Title {self.title}, by Author:{self.author}, Year:{self.year}"
        my_book = Book("Title", "Author", "Year")
        print("my_book")

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
        my_book = Book("title", "author", "year")
        print("my_book")

    def __del__(self):
        my_book = Book("Title", "Author", "Year")
        del my_book
        print(f"Deleting {self.title}")
    


   

    