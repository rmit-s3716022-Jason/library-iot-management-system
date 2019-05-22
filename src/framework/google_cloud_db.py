from .book import Book
import MySQLdb

class GoogleCloudDb():
    HOST='35.201.13.126'
    USER='root'
    PASSWORD='qoqOiGdo6yD2bmJv'
    DATABASE='dbcloud'

    def __init__(self):
        self.connection = MySQLdb.connect(GoogleCloudDb.HOST, GoogleCloudDb.USER, GoogleCloudDb.PASSWORD, GoogleCloudDb.DATABASE)
    
    '''
    params:
        input<Integer>: Value will determine the type of search requested
        item<String>: Book item/identifier that the user is querying  

        Method will create a connection the mysqldb and 
        return a list containing all results of books from the requested query.
    '''
    def search_(self, input, item):
        list=[]V
        try:
            cursor = self.connection.cursor()
            if input == 1:
                cursor.execute("SELECT * FROM Book WHERE BookID = %(item)s")
                results = cursor.fetchall()
                for row in results:
                    list.insert(Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3]))
            elif input == 2:
                cursor.execute("SELECT * FROM Book WHERE Title LIKE %(item)s")
                results = cursor.fetchall()
                for row in results:
                    list.insert(Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3]))
            elif input == 3: 
                cursor.execute("SELECT * FROM Book WHERE Author LIKE %(item)s")
                results = cursor.fetchall()
                for row in results:
                    list.insert(Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])) 
            elif input == 4:
                cursor.exceute("SELECT * FROM Book WHERE DatePublished LIKE %(item)s")
                results = cursor.fetchall()
                for row in results:
                    list.insert(Book(book_id=row[0],title=row[1],author=row[2],published_date=row[3])) 
            else:
                print("Something has gone terribly wrong")
        finally:
            self.connection.close()
        
        return list

