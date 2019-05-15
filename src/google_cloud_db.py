from .book import Book
from .user import User
#from .borrowing import Borrowing
import MySQLdb 


class GoogleCloudDB:
    """
    this is the google database class
    """

    HOST="localhost",
    USER="user",
    PASSWORD="123",
    DATABASE="dbcloud"
    

    def __init__(self):
        self.connection = MySQLdb.connect(GoogleCloudDB.HOST, GoogleCloudDB.USER,
            GoogleCloudDB.PASSWORD, GoogleCloudDB.DATABASE)
        self.books = []
        self.borrowings = []

    def load_users(self):
        """
        loads table books from google cloud database
        and places it into a list
        """

        try:
            with self.connection as cursor:
                sql = "SELECT * FROM 'LmsUser'"
                cursor.execute(sql)
                """
                (user_id, name, username) = cursor.fetchone()
                u1 = User(user_id, name, username)
                self.books.insert(u1)
                """

        finally:
            self.connection.close()

    def load_books(self):
        """
        loads table books from google cloud database
        and places it into a list
        """

        try:
            with self.connection as cursor:
                sql = "SELECT * FROM 'book'"
                cursor.execute(sql)
                (book_id, title, author, published_date) = cursor.fetchone()
                b1 = Book(book_id, title, author, published_date)
                self.books.insert(b1)

        finally:
            self.connection.close()

    def searh_books(self, input):
        """
        """

        try:
            with self.connection as cursor:
                if input == 1:
                    sql = "SELECT * FROM Book WHERE BookID LIKE %s"
                    cursor.execute(sql, input)
                elif input == 2:
                    sql = "SELECT * FROM Book WHERE Title LIKE %s"
                    cursor.execute(sql, input)
                elif input == 3: 
                    sql = "SELECT * FROM Book WHERE Author LIKE %s"
                    cursor.execute(sql, input)
                elif input == 4:
                    sql = "SELECT * FROM Book WHERE DatePublished LIKE %s"
                    cursor.execute(sql, input)
    
    def load_borrowings(self):
        pass

    def save_borrowing(self):
        pass
