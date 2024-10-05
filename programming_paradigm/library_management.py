class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and  self._is_checked_out==False:
                book.check_out()
                self._books.remove(book)
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not self._is_checked_out==True:
                book.return_book()
                self.add_book(book)
                return True
        return False

    def list_available_books(self):
        if self._books:
            for book in self._books:
                print(book)
        else:
            print("No books available.")
        
