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
        self.no_borrows = False
        self.borrowed_books = {}

    def input(self):
         # If the user has books to return
        if not self.no_borrows:
            while True:
                try:
                    response = int(input("Please enter ID of book that you wish to return: "))

                    # Checks if the input book_id exists as a key in the dictionary
                    if response in self.borrowed_books:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("That's not a valid option, please try again.")
            
            return response
        
        return ''
        
    def handle_input(self, input_string, context):
        # If the user has books to return
        if not self.no_borrows:
            event_id = self.borrowed_books.get(input_string)
            # Removes google calendar event and updates status of book in database
            self.gc.remove_event(event_id)
            context.db.return_book(input_string, self.utility.user.user_id)
           
            # Checks with user if they want to return any more books.
            if self.return_again():
                self.borrowed_books.clear()
                return ''
        # Reset no borrows state
        else:
            self.no_borrows = False

        return 'main'

    
    def display(self):
        print("\nReturning book.")
        # Returns dictionary containing the book_id and event_id of all books currently borrowed by the user
        self.borrowed_books = self.utility.db.get_borrowed_books(self.utility.user.user_id)
        # Check if the dictionay is empty i.e. no borrowed books
        if any(self.borrowed_books.values()):
            print("Displaying list of books you currently have on loan.")
            for key in self.borrowed_books:
                print("BookID: " + str(key))
        else:
            print("You currently don't have any borrowed books.")
            self.no_borrows = True

    def return_again(self):
        while True:
            try:
                response = input("Do you want to return another book? (Y/N): ") 
                if response.lower() == "y":
                    return True
                elif response.lower() == "n":
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")
        

