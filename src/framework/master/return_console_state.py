"""
return_console_state.py
=======================
"""
from ..console_state import ConsoleState
from .google_calendar import GoogleCalendar


class ReturnConsoleState(ConsoleState):
    """
    Allows a user to return a borrowed book
    """
    def __init__(self, display_text, utility, gc):
        super().__init__(display_text, '')
        self.utility = utility
        self.gc = gc

    def input(self):
        while True:
            try:
                response = int(input(
                    """Please enter ID of  
                    book that you wish to return: """))

                # Returns the first item in the list with a matching book_id that you have borrrowed
                # otherwise returns None
                result = next((x for x in self.utility.active_borrows if x.book.book_id == response 
                            and x.user.user_id == self.utility.user.user_id), None)
                if result is not None:
                    break
                else:
                    raise Exception
            except Exception:
                print("That's not a valid option, please try again.")
        
        return result
        
    def handle_input(self, input_string, context):
        borrowing = input_string
        event_id = borrowing.gc_event_id
        # Removes google calendar event and borrowing from active borrowings list
        self.gc.remove(event_id)
        context.remove_borrowing(borrowing)
        
        print(borrowing.book.title + " has been successfully returned.")
        
        # Checks with user if they want to return any more books.
        if self.return_again():
            return ''
        else: 
            return 'main'

    
    def display(self):
        if any(x.user.user_id == self.utility.user.user_id for x in self.utility.active_borrows):
            print("Displaying list of books you currently have on loan.")
            for count,items in enumerate(self.utility.active_borrows,1):
                print(count,items.book.id + ": " + items.book.title)
        else:
            print("You currently don't have any borrowed books.")
            # need to change here to skip running input/handle_input

    def return_again(self):
        while True:
            try:
                response = input("Do you want to return another booK? (Y/N): ") 
                if response.lower() is "y":
                    return True
                elif response.lower() is "n":
                    return False
                else:
                    raise Exception
            except Exception:
                print("That's not a valid option, please try again.")
        

