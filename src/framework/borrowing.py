from .google_calendar import GoogleCalendar
from .book import Book
from datetime import datetime
from enum import Enum

class Borrowing():

    def __init__(self, book_id, book_title, user_id, bor_id, gc_event_id, status, bor_date, ret_date):
        self.book_id = book_id
        self.book_title = book_title
        self.user_id = user_id
        self.bor_id = bor_id
        self.gc_event_id = gc_event_id
        self.status = Enum('borrowed', 'returned')
        self.bor_date = bor_date
        self.ret_date = ret_date
        
    def return_book(self):
        self.status = self.status.returned
        print(self.book_title + " returned.")
        
