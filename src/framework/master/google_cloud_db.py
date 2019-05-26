import MySQLdb
from .book import Book


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
        self.cursor = self.connection.cursor()

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
            if input_option == 1:
                self.cursor.execute("SELECT * FROM Book WHERE BookID = %(item)s")
                result_list = self.return_results(self.cursor.fetchall()) 
            elif input_option == 2:
                self.cursor.execute("SELECT * FROM Book WHERE Title LIKE %(item)s")
                result_list = self.return_results(self.cursor.fetchall())   
            elif input_option == 3:
                self.cursor.execute("SELECT * FROM Book WHERE Author LIKE %(item)s")
                result_list = self.return_results(self.cursor.fetchall())  
            elif input_option == 4:
                self.cursor.exceute("SELECT * FROM Book WHERE DatePublished LIKE %(item)s")
                result_list = self.return_results(self.cursor.fetchall())  
            else:
                print("Something has gone terribly wrong.")
        finally:
            self.connection.close()

        return result_list

    def add_borrow(self, borrowing):
        query = "INSERT INTO BookBorrowed (BorrrowID, BookID, UserID, EventID, Status, BorrowedDate, ReturnedDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (borrowing.borrow_id, borrowing.book.book_id, borrowing.user.user_id, borrowing.gc_event_id, 'borrowed', borrowing.bor_date, borrowing.ret_date)
        self.cursor.execute(query,val)
        self.connection.commit()
        print('Book borrowed, please return by: ' + borrowing.ret_date)
    
    def is_borrowed(self, book_id):
        self.cursor.execute("SELECT * FROM BookBorrowed WHERE BookID = %(book_id)s AND Status = 'borrowed'")
        results = self.cursor.fetchall()

        if not results: 
            return True
        else:
            return False

    def get_borrowed_books(self, user_id):
        result_dict = {}
        
        query = "SELECT * FROM BookBorrowed WHERE UserID = %s AND Status = %s"
        val = (user_id, 'borrowed')
       
        self.cursor.exceute(query,val) 
        results = self.cursor.fetchall()
        # Loops through fetched results and adds the book_id and event_id to a dictionary
        for row in results:
            result_dict[row[1]] = row[3]
        
        return result_dict
    
    def return_book(self, book_id, user_id):
        query = "UPDATE BorrowedBook SET Status = %s WHERE UserID = %s AND BookID = %s"
        val = ('returned', user_id, book_id)
        self.cursor.exceute(query,val)
        self.connection.commit()
        print(book_id + " returned.")

    def return_results(self, results):
        result_list = []
        for row in results:
            result_list.insert(Book(book_id=row[0],
                                    title=row[1],
                                    author=row[2],
                                    published_date=row[3]))

        return result_list



