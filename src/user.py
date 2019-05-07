import hashlib


class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', 0)
        self.name = kwargs.get('name', '')
        self.username = kwargs.get('username', '')
        if 'password_hash' in kwargs:
            self.password_hash = kwargs['password_hash']
        elif 'password' in kwargs:
            self.password_hash = self.hash_password(kwargs['password'])
        self.salt = kwargs.get('salt', '')

    def hash_password(self, password):
        return hashlib.sha256(
            (password + self.salt).encode()).hexdigest()

    def check_password(self, password):
        hashed_password = self.hash_password(password)
        return hashed_password == self.password_hash
