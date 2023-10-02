from lib.book import Book

def test_book_construct():
    book = Book(1, "Book Title", "Author Name")
    assert book.id == 1
    assert book.title == "Book Title"
    assert book.author_name == "Author Name"

def test_books_are_equal():
    book1 = Book(1, "Book Title", "Author Name")
    book2 = Book(1, "Book Title", "Author Name")
    assert book1 == book2 

def test_book_print():
    book1 = Book(1, "Book Title", "Author Name")
    assert str(book1) == "ID: 1, Title: Book Title, Author: Author Name"