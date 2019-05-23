from ..console_state import ConsoleState
from ..user import User
from ..sqlite_db_interface import SqliteDbInterface

class LoginConsoleState(ConsoleState):
    def __init__(self):
        super().__init__('', '')

        self.attributes = ['Username', 'Password']
        self.reset()

    def reset(self):
        self.values = []
        self.current = 0

    def handle_input(self, input_string, context):
        if(self.current == 0):
            self.values.append(input_string)
            self.current += 1

            db = SqliteDbInterface()

            user = db.find_user(self.values[0])
            if(user is None):
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
            else:
                print("Wrong password")

            self.reset()
            return "main"

        # if self.current == len(self.attributes):
        #     user = User(name=self.values[0],
        #                 username=self.values[1],
        #                 password=self.values[2])
        #     context.db.write_user(user)
        # return 'main'

        # self.values.append(input_string)
        # if self.attributes[self.current] == 'Username':
        #     if context.db.find_user(input_string) is not None:
        #         print("Username already taken")
        #         return ""
        # self.current += 1
        # return ""

        return "main"

    def display(self):
        # if self.current == len(self.attributes):
        #     print('Registration complete')
        # elif self.current == 0:
        #     print('User registration')
        # else:
        #     print()
        print('User login')

    def input(self):
        if self.current < len(self.attributes):
            return input('Please enter your ' +
                         self.attributes[self.current] + ':')
        return ''
