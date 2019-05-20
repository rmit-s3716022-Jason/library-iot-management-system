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
                sql = "SELECT * FROM Book WHERE BookID = %s"
                for row in cursor.execute(sql, (query, )):
                    row = row.fetchone()
                    return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 2:
                sql = "SELECT * FROM Book WHERE Title LIKE %s"
                for row in cursor.execute(sql, (query, )):
                    row = row.fetchone()
                    return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 3: 
                sql = "SELECT * FROM Book WHERE Author LIKE %s"
                for row in cursor.execute(sql, (query, )):
                    row = row.fetchone()
                    return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            elif input == 4:
                sql = "SELECT * FROM Book WHERE DatePublished LIKE %s"
                for row in cursor.execute(sql, (query, )):
                    row = row.fetchone()
                    return Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])
            else:
                print("Something has gone terribly wrong")
        finally:
            self.connection.close()