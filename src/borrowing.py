from .google_calendar import GoogleCalendar
from .book import Book
from datetime import datetime
from enum import Enum


class Borrowing():

    def __init__(self, borrow_id, user_id, book_id, status, b_date, r_date, b_title):
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.book_id = book_id
        self.status = Enum('borrowed', 'returned')
        self.b_date = b_date
        self.r_date = r_date

    def return_book(self):
        # This should not be done in the borrowing it's completely breaking
        # encapsulation
        # gc = GoogleCalendar()
        # gc.remove_event()
        self.status = 'returned'
        self.r_date = datetime.strptime(datetime.date(datetime.now()),
                                        "%d-%m-%Y")

    ''' can be placed somewhere else'''
    def calc_ret_date(self):
        cur_date = datetime.strptime(datetime.date(datetime.now()), "%d-%m-%Y")
        bor_limit = datetime.timedelta(weeks=4)
        return cur_date + bor_limit

    def get_event_id(self):
        """
        Creates an event id for a borrowing
        """
        return self.b_date + self.user_id + str(self.book_id)
