"""
borrow_console_state.py
=======================
"""
from datetime import datetime,time, timedelta
from ..console_state import ConsoleState
from .borrowing import Borrowing
import pytz
# remove import later
from .master_user import MasterUser          


class BorrowConsoleState(ConsoleState):
    """
    Allows a user to borrow a book from the results of a book search

    Constructor
        :display_text: the text to display
        :utility: the shared utility class
        :google_calendar: a google calendar adapter
    """
    def __init__(self, display_text, utility, google_calendar):
        super().__init__(display_text, '')
        self.utility = utility
        self.gc = gc
        self.no_search = False

    def input(self):
        if not self.no_search:
            while True:
                try:
                    response = int(input("Please enter ID of book that you wish to borrow: "))
                    # Checks input against items returned in the search, returns the book the ID matches 
                    # otherwise returns None
                    result = next((x for x in self.utility.cur_results if x.book_id == response), None)
                    if result is not None:
                        # Returns false if the requested book_id is available
                        if not self.utility.db.is_borrowed(result.book_id):
                            break
                        else:
                            print("The book is unavailable, please select another book to borrow.")
                    else:
                        raise ValueError
                except ValueError:
                    print("That's not a valid option, please try again.")
            
            return result
        else:
            return ''
        
    def handle_input(self, input_string, context):
        if not self.no_search:
            # Stores book and calculates the dates relevant to the borrow
            requested_book = input_string
            bor_date, ret_date = self.calc_dates()
            
            # Creates the google calendar event and stores the returned event id
            event_id = self.gc.add_event(context.user.user_id, context.user.username, requested_book.title, requested_book.book_id, bor_date, ret_date) 
            
            # Creates a instance of borrowing and stores it with list of other currently loaned books
            bor_id = context.db.generate_id()
            
            bor = Borrowing(bor_id, requested_book, context.user, event_id, 'borrowed', bor_date, ret_date)
            context.db.add_borrow(bor)
            context.remove_result(requested_book)
            
            print("Title: " + requested_book.title + " BookID: " + str(requested_book.book_id) + " successfully borrowed.")
            # If user wants to borrow another book
            if not self.borrow_again():
                return 'main'
        else:
            self.no_search = False
        
        # returns searching if no_search is True OR borrow_again() returned TRUE
        return 'searching'
    
    # Displays the results of the search
    def display(self):
        print("\nBorrowing book.\nDisplaying search results.")
        if self.utility.cur_results:
            for items in self.utility.cur_results:
                print("Title: " + items.title + " BookID: " + str(items.book_id))
        else:
            print('You need to make a complete a search first')
            self.no_search = True

    
    '''
    Acknowledgement: https://stackoverflow.com/questions/373370/how-do-i-get-the-utc-time-of-midnight-for-a-given-timezone
    '''
    def calc_dates(self):
        # choose timezone
        tz = pytz.timezone("Australia/Melbourne")
        # get correct date for the midnight using given timezone.
        today = datetime.now(tz).date()

        #get midnight in the correct timezone (taking into account DST)
        #NOTE: tzinfo=None and tz.localize()
        # assert that there is no dst transition at midnight (`is_dst=None`)
        midnight = tz.localize(datetime.combine(today, time(0, 0)), is_dst=None)

        #convert to utc
        bor_date = midnight.astimezone(pytz.utc) 
        # calculate week later
        ret_date = bor_date+timedelta(days=7)
        return bor_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"), ret_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    def borrow_again(self): 
        while True:
            try:
                response = input("Do you want to borrow another booK? (Y/N): ")
                if response.lower() == "y":
                    return True
                if response.lower() == "n":
                    return False
                raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")
