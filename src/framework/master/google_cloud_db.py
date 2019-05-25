import MySQLdb
from book import Book

class GoogleCloudDb():
    
    '''
    This is a class that provides GCP capabilities in the form of a search function that allows users to search a book by whatever attribute they input
    '''
    
    HOST = '35.201.13.126'
    USER = 'root'
    PASSWORD = 'qoqOiGdo6yD2bmJv'
    DATABASE = 'dbcloud'

    def __init__(self):
        self.connection = MySQLdb.connect(self.HOST,
                                          self.USER,
                                          self.PASSWORD,
                                          self.DATABASE)

    '''
    params:
        input<Integer>: Value will determine the type of search requested
        item<String>: Book item/identifier that the user is querying
        
        Method will create a connection the mysqldb and
        return a result_list containing all results of books from the requested
        query.
    '''
    def search(self, input_option, item):
        result_list = []
        try:
            cursor = self.connection.cursor()
            if input_option == 1:
                cursor.execute("SELECT * FROM Book WHERE BookID = %(item)s")
                result_list = self.return_results(cursor.fetchall()) 
            elif input_option == 2:
                cursor.execute("SELECT * FROM Book WHERE Title LIKE %(item)s")
                result_list = self.return_results(cursor.fetchall())   
            elif input_option == 3:
                cursor.execute("SELECT * FROM Book WHERE Author LIKE %(item)s")
                result_list = self.return_results(cursor.fetchall())  
            elif input_option == 4:
                cursor.exceute("SELECT * FROM Book WHERE DatePublished LIKE %(item)s")
                result_list = self.return_results(cursor.fetchall())  
            else:
                print("Something has gone terribly wrong.")
        finally:
            self.connection.close()

        return result_list
    
    def return_results(self, results):
        result_list = []
        for row in results:
            result_list.insert(Book(book_id=row[0],
                                    title=row[1],
                                    author=row[2],
                                    published_date=row[3]))

        return result_list



