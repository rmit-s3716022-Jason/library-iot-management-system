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

    def __init__(self, db='reception.db', data_table='user'):
        self.db_name = db
        self.data_table_name = data_table

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
        query_string = "INSERT INTO {0} \
                        values((?), (?), (?), (?), (?))".format(
                            self.data_table_name)

        self.write_values(query_string,
                          (
                              user.name,
                              user.username,
                              user.password_hash,
                              user.salt,
                              user.google_id
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
                       password_hash,
                       salt,
                       google_id
                       FROM {0}
                       """.format(self.data_table_name)

        for row in self.read_values(query_string):
            [user_id, name, username, password_hash, salt, google_id] = row
            yield User(user_id=user_id,
                       name=name,
                       username=username,
                       password_hash=password_hash,
                       salt=salt,
                       google_id=google_id)

    def find_user(self, username):
        """
        Searches for a user that matches the username
        """
        query_string = """SELECT
                       id,
                       name,
                       username,
                       password_hash,
                       salt,
                       google_id
                       FROM {0}
                       WHERE username=(?)
                       """.format(self.data_table_name)

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            for row in cursor.execute(query_string, (username, )):
                [user_id, name, username, password_hash, salt, google_id] = row
                return User(user_id=user_id,
                            name=name,
                            username=username,
                            password_hash=password_hash,
                            salt=salt,
                            google_id=google_id)

        return None
