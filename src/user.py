import hashlib


class User:
    def __init__(
            self, 
            user_id=0,
            name="",
            username="",
            password_hash="",
            salt="",
            google_id=""):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
        self.google_id = google_id

    def check_password(self, password):
        hashed_password = hashlib.sha256(
            (password + self.salt).encode()).hexdigest()
        return hashed_password == self.password_hash
