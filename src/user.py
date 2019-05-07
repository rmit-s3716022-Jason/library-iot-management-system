import hashlib

class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', 0)
        self.name = kwargs.get('name', '')
        self.username = kwargs.get('username', '')
        self.password_hash = kwargs.get('password_hash', '')
        self.salt = kwargs.get('salt', '')
        self.google_id = kwargs.get('google_id', '')

    def check_password(self, password):
        hashed_password = hashlib.sha256(
            (password + self.salt).encode()).hexdigest()
        return hashed_password == self.password_hash
