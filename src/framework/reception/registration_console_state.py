"""
registration_console_state.py
=============================
"""
import re
from ..console_state import ConsoleState
from .user import User


class RegistrationConsoleState(ConsoleState):
    """
    Allows a user to register themselves
    """
    def __init__(self):
        super().__init__('', '')

        self.attributes = ['Username',
                           'First name',
                           'Last name',
                           'Email',
                           'Password']
        self.reset()

    def reset(self):
        self.values = []

        self.current = 0

    def handle_input(self, input_string, context):
        if self.current == len(self.attributes):
            self.write_user(context.db)
            self.reset()
            return 'main'

        attribute = self.attributes[self.current]

        if not self.validate(input_string, attribute, context.db):
            return ''

        self.values.append(input_string)

        self.current += 1
        return ''

    def display(self):
        if self.current == len(self.attributes):
            print('Registration complete')
        elif self.current == 0:
            print('User registration')
        else:
            print()

    def input(self):
        if self.current < len(self.attributes):
            return input('Please enter your ' +
                         self.attributes[self.current] + ':')
        return ''

    def write_user(self, database):
        """Writes a new user to the DB"""
        user = User(username=self.values[0],
                    firstname=self.values[1],
                    lastname=self.values[2],
                    email=self.values[3],
                    password=self.values[4])
        database.write_user(user)

    def validate(self, input_string, attribute, database):
        """Validates user input"""
        if attribute == 'Username':
            if database.find_user(input_string) is not None:
                print('Username already used')
                return False
        elif attribute == 'Email':
            if not re.fullmatch(r'.+@.+', input_string):
                print('Not a valid email address')
                return False
        elif not input_string:
            print('Input is not valid')
            return False

        return True
