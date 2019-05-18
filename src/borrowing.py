from .google_calendar import GoogleCalendar
from .book import Book
from datetime import datetime
from enum import Enum

class Borrowing():

    def __init__(self, borrow_id, user_id, status, b_date, r_date, b_title, gc_id):
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.status = Enum('borrowed', 'returned')
        self.b_date = b_date
        self.r_date = r_date
        self.gc_id = gc_id

    def return_book(self):
        gc = GoogleCalendar() 
        # will need to determine what the generated event id is to pass
        # if we set it ourselves it could be easier to
        gc.remove_event('eventId') 

    ''' can be placed somewhere else'''
    def calc_ret_date(self):
        cur_date = datetime.datetime.strptime(datetime.date(datetime.now()),"%d-%m-%Y")
        bor_limit = datetime.timedelta(weeks=4)
        return cur_date + bor_limit
