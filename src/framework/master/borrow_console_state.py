"""
borrow_console_state.py
=======================
"""
from datetime import datetime
from ..console_state import ConsoleState
from .borrowing import Borrowing


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
        self.google_calendar = google_calendar

    def input(self):
        while True:
            try:
                response = int(input(
                    """Please enter ID of
                    book that you wish to borrow: """))
                result = next((x for x in self.utility.cur_results if x.book_id == response), None)
                if result is not None:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")

        return result

    def handle_input(self, input_string, context):
        # Stores book and calculates the dates relevant to the borrow
        requested_book = input_string
        bor_date, ret_date = self.calc_dates()

        # Creates the google calendar event and stores the returned event id
        event_id = self.google_calendar.add_event(context.user.user_id, context.user.username, requested_book.title, requested_book.book_id)

        # Creates a instance of borrowing and stores it with list of other currently loaned books
        bor = Borrowing(context.user, requested_book, event_id, bor_date, ret_date)
        context.add_borrowing(bor)

        print(requested_book.title + " successfully borrowed.")

        if self.borrow_again():
            return ''

        # Resets the most recent search results list and returns to the main menu
        context.reset_results()
        return 'main'

    def display(self):
        print('Book borrowing.')

    def calc_dates(self):
        bor_date = datetime.date.today()
        ret_date = bor_date + datetime.timedelta(days=7)
        return bor_date, ret_date

    def borrow_again(self):
        while True:
            try:
                response = input("Do you want to borrow another booK? (Y/N): ")
                if response.lower() == "y":
                    return True
                if response.lower() == "n":
                    return False
                raise Exception
            except Exception:
                print("That's not a valid option, please try again.")
