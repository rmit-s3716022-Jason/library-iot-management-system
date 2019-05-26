"""
borrowing.py
============
"""
from enum import Enum


class Borrowing():
    """
    Represents a book being borrowed

    Constructor
        :borrow_id: the id of this borrowing
        :user: user id who is doing the borrowing
        :book: book id that is being borrowed
        :gc_event_id: the id of the google calendar event
        :status: the status of the borrowing
        :bor_date: the date the borrowing happened
        :ret_date: the date the book was returned
    """
    def __init__(self, borrow_id, book, user, gc_event_id, status, bor_date, ret_date):
        self.borrow_id = borrow_id
        self.user = user
        self.book = book
        self.status = Enum('borrowed', 'returned')
        self.gc_event_id = gc_event_id
        self.bor_date = bor_date
        self.ret_date = ret_date
