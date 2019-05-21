from book import Book
import MySQLdb

class GoogleCloudDb():
    """
    This is a class that provides GCP capabilities in the form of a search function that allows users to search a book by whatever attribute they input
    """
    
    HOST='removed'
    USER='removed'
    PASSWORD='removed'
    DATABASE='removed'

    def init(self):
        pass
    
    """
    Constructor method
    """

    def search(self, input, query):
    """
    Returns a list of database results 

    """
    
    """
    params:
        input<Integer>: Value will determine the type of search requested
        item<String>: Book item/identifier that the user is querying  
        Method will create a connection the mysqldb and 
        return a list containing all results of books from the requested query.
    """
        self.connection = MySQLdb.connect(GoogleCloudDb.HOST, GoogleCloudDb.USER, GoogleCloudDb.PASSWORD, GoogleCloudDb.DATABASE)
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
        
        self.connection.close()

        return list

