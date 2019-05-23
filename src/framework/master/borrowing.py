from datetime import datetime
from .book import Book


class Borrowing():
    def __init__(self, book_id, book_title, user_id, bor_id, gc_event_id,
                 status, bor_date, ret_date):
        self.book_id = book_id
        self.book_title = book_title
        self.user_id = user_id
        self.bor_id = bor_id
        self.gc_event_id = gc_event_id
        self.status = status
        self.bor_date = bor_date
        self.ret_date = ret_date

    def return_book(self):
        self.status = self.status.returned
        print(self.book_title + " returned.")
