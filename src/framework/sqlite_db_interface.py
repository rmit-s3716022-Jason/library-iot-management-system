"""
Contains the SQLite implementation of the db interface
Code also used in IoT assignment 1
"""
import sqlite3
from .user import User


class SqliteDbInterface():
    """
    The SQLite db interface implementation
    """

    def __init__(self, db='reception.db', data_table='users'):
        self.db_name = db
        self.data_table_name = data_table

        self.create_db()

    def create_db(self):
        """
        Creates the database table if it doesn't exist
        """
        connection = sqlite3.connect(self.db_name)
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE if not exists {0}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                salt TEXT NOT NULL
                )""".format(self.data_table_name))

    def write_values(self, query_string, values):
        """
        Worker function to insert data into a table
        """

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(query_string,
                           values)
            connection.commit()

    def write_user(self, user):
        """
        Writes a user to the table
        """
        query_string = "INSERT INTO {0} (name, username, password, salt)\
                        values((?), (?), (?), (?))".format(
                            self.data_table_name)

        self.write_values(query_string,
                          (
                              user.name,
                              user.username,
                              user.password_hash,
                              user.salt
                          ))

    def read_values(self, query_string):
        """
        Reads values from the DB returned by the given query
        """
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(query_string):
                yield row

    def read_all_users(self):
        """
        Enumerates all of the users in the database
        """

        query_string = """SELECT
                       id,
                       name,
                       username,
                       password,
                       salt
                       FROM {0}
                       """.format(self.data_table_name)

        for row in self.read_values(query_string):
            [user_id, name, username, password_hash, salt] = row
            yield User(user_id=user_id,
                       name=name,
                       username=username,
                       password_hash=password_hash,
                       salt=salt)

    def find_user(self, username):
        """
        Searches for a user that matches the username
        """
        query_string = """SELECT
                       id,
                       name,
                       username,
                       password,
                       salt
                       FROM {0}
                       WHERE username=(?)
                       """.format(self.data_table_name)

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(query_string, (username, )):
                [user_id, name, username, password_hash, salt] = row
                return User(user_id=user_id,
                            name=name,
                            username=username,
                            password_hash=password_hash,
                            salt=salt)

        return None
