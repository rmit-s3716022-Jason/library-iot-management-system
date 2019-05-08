from .book import Book
from .user import User
#from .borrowing import Borrowing
import MySQLdb 


class GoogleCloudDB:
    """
    this is the google database class
    """

    HOST="35.201.13.126",
    USER="root",
    PASSWORD="qoqOiGdo6yD2bmJv",
    DATABASE="dbcloud"
    

    def __init__(self):
        self.connection = MySQLdb.connect(GoogleCloudDB.HOST, GoogleCloudDB.USER,
            GoogleCloudDB.PASSWORD, GoogleCloudDB.DATABASE)
        self.books = []
        self.users = []
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

    def load_borrowings(self):
        """
        loads table book borrowing from google cloud database
        and places it into a list
        """

        try:
            with self.connection as cursor:
                sql = "SELECT * FROM 'BookBorrowed'"
                cursor.execute(sql)
                """
                #(book_borrowed_id, lms_user_id, book_id, status, borrowed_date, returned_date) = cursor.fetchone()
                #bo1 = Borrowing(book_borrowed_id, lms_user_id, book_id, status, borrowed_date, returned_date)
                #self.books.insert(bo1)
                """

        finally:
            self.connection.close()

    def save_borrowing(self):
        pass

    def save_user(self):
        pass
