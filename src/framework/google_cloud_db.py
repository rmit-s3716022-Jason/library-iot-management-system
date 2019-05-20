from .book import Book
import MySQLdb

class GoogleCloudDb():
    """
    """
    HOST='35.201.13.126'
    USER='root'
    PASSWORD='qoqOiGdo6yD2bmJv'
    DATABASE='dbcloud'

    def __init__(self):
        self.connection = MySQLdb.connect(GoogleCloudDb.HOST, GoogleCloudDb.USER, GoogleCloudDb.PASSWORD, GoogleCloudDb.DATABASE)

    #def connect_(self):
     #   try:
      #       cursor = self.connection.cursor()
       # finally:
        #    self.connection.close()

    def search_(self, input, query):
        try:
            cursor = self.connection.cursor()
            if input == 1:
                cursor.execute("SELECT * FROM Book WHERE BookID = %(query)s")
                row = cursor.fetchall()
                return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 2:
                cursor.execute("SELECT * FROM Book WHERE Title LIKE %(query)s")
                return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 3: 
                cursor.execute("SELECT * FROM Book WHERE Author LIKE %(query)s")
                row = cursor.fetchall()
                return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 4:
                cursor.exceute("SELECT * FROM Book WHERE DatePublished LIKE %(query)s")
                row = cursor.fetchall()
                return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            else:
                print("Something has gone terribly wrong")
        finally:
            self.connection.close()
