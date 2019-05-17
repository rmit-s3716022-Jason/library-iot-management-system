from .book import Book
import MySQLdb


class GoogleCloudDb():
    """
    """
    HOST='localhost'
    USER='root'
    PASSWORD='omitted'
    DATABASE='dbcloud'

    def __init__(self):
        self.connection = MySQLdb.connect(GoogleCloudDb.HOST, GoogleCloudDb.USER, GoogleCloudDb.PASSWORD, GoogleCloudDb.DATABASE)

    #def connect_(self):
     #   try:
      #       cursor = self.connection.cursor()
       # finally:
        #    self.connection.close()

    def search_(self, input, value):
        try:
            cursor = self.connection.cursor()
            if input == 1:
                sql = "SELECT * FROM Book WHERE BookID = %s"
                for row in cursor.execute(sql, (value, )):
                    (book_id, title, author, published_date) = row
                    return Book(book_id=book_id,title=title,author=author,published_date=published_date)
            elif input == 2:
                sql = "SELECT * FROM Book WHERE Title LIKE %s"
                for row in cursor.execute(sql, (value, )):
                    (book_id, title, author, published_date) = row
                    return Book(book_id=book_id,title=title,author=author,published_date=published_date)
            elif input == 3: 
                sql = "SELECT * FROM Book WHERE Author LIKE %s"
                for row in cursor.execute(sql, (value, )):
                    (book_id, title, author, published_date) = row
                    return Book(book_id=book_id,title=title,author=author,published_date=published_date)
            elif input == 4:
                sql = "SELECT * FROM Book WHERE DatePublished LIKE %s"
                for row in cursor.execute(sql, (value, )):
                    (book_id, title, author, published_date) = row
                    return Book(book_id=book_id,title=title,author=author,published_date=published_date)
            else:
                print("Something has gone terribly wrong")
        finally:
            self.connection.close()
