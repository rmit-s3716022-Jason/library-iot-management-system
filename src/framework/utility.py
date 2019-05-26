"""
utility.py
==========

Provides a collection of resources and data that is shared between console
states
"""


class Utility:
    """
    **db:** the db that this program is using

    **socket:** the socket instance to use
    """
    def __init__(self, db, socket):
        self.db = db
        self.socket = socket
        self.cur_results = []
        self.active_borrows = []

    def add_cur_results(self, results):
        self.cur_results.extend(results)

    def reset_results(self):
        self.cur_results.clear()

    def add_borrowing(self, borrow):
        self.active_borrows.append(borrow)

    def remove_borrowing(self, borrow):
        self.active_borrows.remove(borrow)
