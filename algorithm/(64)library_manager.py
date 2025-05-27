# این برنامه با استفاده از کلاس ها کار مدیریت کتابخانه رو انجام میده



class Book:
    def __init__(self, title, author, publication_year, ISBN):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"ISBN: {self.ISBN}")
        print("-------------------------")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()


library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-3-16-148410-0")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0-06-112008-4")
book3 = Book("1984", "George Orwell", 1949, "978-0-452-28423-4")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
