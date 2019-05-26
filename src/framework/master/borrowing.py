"""
borrowing.py
============
"""


class Borrowing():
    """
    Represents a book being borrowed

    Constructor
        :user: user id who is doing the borrowing
        :book: book id that is being borrowed
        :bor_date: the date the borrowing happened
        :ret_date: the date the book was returned
    """
    def __init__(self, user, book, gc_event_id, bor_date, ret_date):
        self.user = user
        self.book = book
        self.gc_event_id = gc_event_id
        self.bor_date = bor_date
        self.ret_date = ret_date
        self.borrowed = True

    def return_book(self):
        """Returns a borrowed book"""
        if self.borrowed is True:
            self.borrowed = False
            print("Thank you " + self.user.firstname + ", " + self.book.title + " has been returned.")
        else:
            print("Unable to return unborrowed book.")

