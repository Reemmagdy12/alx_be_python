class Book:
    def __init__(self, title, author):
        self.title = title
        self.author =author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author) 
        self.page_count = page_count

class Library:
    def __init__(self):
        self._books = [] 
    def add_book(self, book):
        self._books.append(book)
    def list_books(self):
        if self._books:
            for book in self._books:
                print(book)
        else:
            print("No books available")
