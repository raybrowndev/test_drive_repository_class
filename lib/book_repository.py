from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        book_list = []
        for book in rows:
            i = Book(book["id"], book["title"], book["author_name"])
            book_list.append(i)
        return book_list 

