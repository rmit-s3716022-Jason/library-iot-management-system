"""
master_user.py
==============
"""


class MasterUser():
    """
    Caches user data from the reception pi
    """
    def __init__(self, username, firstname, lastname, user_id):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.userid = user_id
