from lib.book import Book
from lib.book_repository import BookRepository

def test_all_records_returned(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    all_books = repo.all()
    assert all_books == [Book(1,'Nineteen Eighty-Four','George Orwell'), 
                        Book(2,'Mrs Dalloway', 'Virginia Woolf'), 
                        Book(3,'Emma', 'Jane Austen'), 
                        Book(4,'Dracula', 'Bram Stoker'), 
                        Book(5,'The Age of Innocence', 'Edith Wharton'),
                    ]
