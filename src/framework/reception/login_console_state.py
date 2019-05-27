"""
login_console_state.py
======================
"""
import json

from ..console_state import ConsoleState
from .sqlite_db_interface import SqliteDbInterface


class LoginConsoleState(ConsoleState):
    """
    Allows a user to login
    """
    def __init__(self, master_ip, master_port):
        super().__init__('', '')

        self.master_ip = master_ip
        self.master_port = master_port

        self.attributes = ['Username', 'Password']
        self.values = []
        self.reset()

    def reset(self):
        self.current = 0
        self.user = None

    def handle_input(self, input_string, context):
        self.current += 1

        if self.current == 1:
            self.user = context.db.find_user(input_string)
            if self.user is None:
                print("Username not found!")
                self.reset()
                return "main"
            return ""

        if(self.current == 1):
            self.values.append(input_string)
            self.current += 1

            db = SqliteDbInterface()

            user = db.find_user(self.values[0])
            if (user.check_password(self.values[1])): 
                
                print("You are logged in!")
                self.login(context)
                self.reset()
                return "waiting"

            print("Wrong password")

            self.reset()
            return "main"

        return "main"

    def display(self):
        if self.current == 0:
            print('User login')

    def input(self):
        if self.current < len(self.attributes):
            return input('Please enter your ' +
                         self.attributes[self.current] + ':')
        return ''

    def login(self, context):
        data = {}
        data['username'] = self.user.username
        data['firstname'] = self.user.firstname
        data['lastname'] = self.user.lastname
        data['user_id'] = self.user.user_id
        context.state.login()
        context.socket.send_message(
            'login', json.dumps(data), master_ip, master_port)
