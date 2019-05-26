from ..console_state import ConsoleState
from borrowing import Borrowing
from datetime import datetime

class BorrowConsoleState(ConsoleState):

    def __init__(self, display_text, utility, gc):
        super().__init__(display_text, '')
        self.utility = utility
        self.gc = gc

    def input(self):
        while True:
            try:
                response = int(input(
                    """Please enter ID of  
                    book that you wish to borrow: """))
                # Checks input against items returned in the search, returns the book the ID matches 
                # otherwise returns None
                result = next((x for x in self.utility.cur_results if x.book_id == response), None)
                if result is not None:
                    # Returns false if the requested book_id is available
                    if not self.utility.db.is_borrowed():
                        break
                    else:
                        print("The book is unavailable, please select another book to borrow.")
                else:
                    raise Exception
            except Exception:
                print("That's not a valid option, please try again.")
        
        return result
        
    def handle_input(self, input_string, context):
        # Stores book and calculates the dates relevant to the borrow
        requested_book = input_string
        bor_date, ret_date = self.calc_dates()
        
        # Creates the google calendar event and stores the returned event id
        event_id = self.gc.add_event(context.user.user_id, context.user.username, requested_book.title, requested_book.book_id) 
        
        # Creates a instance of borrowing and stores it with list of other currently loaned books
        bor_id = context.user.user_id + requested_book.book_id + ret_date
        bor = Borrowing(bor_id, requested_book, context.user, event_id, 'borrowed', bor_date, ret_date)
        context.db.add_borrow(bor)
        
        print(requested_book.id + ": " + requested_book.title + " successfully borrowed.")
        
        # If user wants to borrow another book
        if self.borrow_again():
            return ''
        else:
            return 'main'
    
    # Displays the results of the search
    def display(self):
        for count,items in enumerate(self.utility.cur_results,1):
            print(count,items.book_id + ": " + items.title)

    # Calculates the start/end dates of the borrow
    def calc_dates(self):
        bor_date = datetime.date.today()
        ret_date = bor_date + datetime.timedelta(days=7)
        return bor_date, ret_date

    def borrow_again(self): 
        while True:
            try:
                response = input("Do you want to borrow another booK? (Y/N): ") 
                if response.lower() is "y":
                    return True
                elif response.lower() is "n":
                    return False
                else:
                    raise Exception
            except Exception:
                print("That's not a valid option, please try again.")
        

