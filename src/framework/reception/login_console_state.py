import json

from ..console_state import ConsoleState


class LoginConsoleState(ConsoleState):
    def __init__(self):
        super().__init__('', '')

        self.attributes = ['Username', 'Password']
        self.reset()

    def reset(self):
        self.current = 0
        self.user = None

    def handle_input(self, input_string, context):
        self.current += 1

        if self.current == 0:
            self.user = context.db.find_user(input_string)
            if self.user is None:
                print("Username not found!")
                self.reset()
                return "main"
            return ""

        if self.current == 1:
            if self.user.check_password(input_string):
                print("You are logged in!")
                self.login(context.socket)
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

    def login(self, socket):
        data = {}
        data.username = self.user.username
        data.name = self.user.name
        data.user_id = self.user.id
        socket.send_message('login', json.dumps(data), '127.0.0.1', 6000)
