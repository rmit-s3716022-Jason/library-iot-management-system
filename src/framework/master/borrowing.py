from datetime import datetime
from enum import Enum

class Borrowing():
    
    def __init__(self, borrow_id, book, user, gc_event_id, status, bor_date, ret_date):
        self.borrow_id = borrow_id
        self.user = user
        self.book = book
        self.status = Enum('borrowed', 'returned')
        self.gc_event_id = gc_event_id
        self.bor_date = bor_date
        self.ret_date = ret_date
        
        
