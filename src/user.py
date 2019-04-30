from abc import ABC, abstractmethod


class AbstractUser(ABC):

    def __init__(self, first, last, username, password, email):
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.email = email

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def login(self):
        pass


class LibraryUser(AbstractUser):

    def logout(self):
        pass

    def login(self):
        pass

    def search_book(self, isbn, author_name, book_name):
        pass

    def borrow_book(self, isbn, author_name, book_name):
        pass

    def return_book(self, isbn, author_name, book_name):
        pass


class AdminUser(AbstractUser):
    
    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def login(self):
        pass

    def add_book(self, isbn, author_name, book_name):
        pass

    def remove_book(self, isbn, author_name, book_name):
        pass

    def generate_report(self):
        pass
