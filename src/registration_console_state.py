from .console_state import ConsoleState
from .user import User


class RegistrationConsoleState(ConsoleState):
    def __init__(self):
        super().__init__('', '')

        self.attributes = ['Name', 'Username', 'Password']
        self.values = []

        self.current = 0

    def handle_input(self, input_string, context):
        if self.current == len(self.attributes):
            user = User(name=self.attributes[0],
                        username=self.attributes[1],
                        password=self.attributes[2])
            context.db.write_user(user)
            return 'done'

        self.values[self.current] = input_string
        if self.attributes[self.current] == 'Username':
            if context.db.find_user(input_string) is not None:
                print("Username already taken")
                return ""
        self.current += 1
        return ""

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

