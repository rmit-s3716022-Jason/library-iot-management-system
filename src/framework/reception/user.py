"""
user.py
=======
"""

import hashlib
import random
import string


class User:
    """
    The user data class

    If given a non hashed password, hashes the password before storing
    """
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', 0)
        self.username = kwargs.get('username', '')
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')
        self.email = kwargs.get('email', '')
        self.salt = kwargs.get('salt', ''.join(
            random.choice(string.ascii_letters) for i in range(3)))
        if 'password_hash' in kwargs:
            self.password_hash = kwargs['password_hash']
        elif 'password' in kwargs:
            self.password_hash = self.hash_password(kwargs['password'])

    def hash_password(self, password):
        """Hashes a password"""
        return hashlib.sha256(
            (password + self.salt).encode()).hexdigest()

    def check_password(self, password):
        """Checks a password against the stored hash"""
        hashed_password = self.hash_password(password)
        return hashed_password == self.password_hash
