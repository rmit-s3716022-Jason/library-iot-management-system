from ..console_state import ConsoleState
import facial_recog


class AddPhotoConsoleState(ConsoleState):
    def __init__(self):
        super().__init__('', '')

        self.reset()

    def reset(self):
        self.user = None

    def handle_input(self, input_string, context):
        if not self.user:
            self.user = context.db.find_user(input_string)
            if self.user is None:
                print('Username not found!')
                self.reset()
                return 'main'

        if not self.user.check_password(input_string):
            print('Password incorrect')
            return 'main'

        facial_recog.capture_photo(self.user.username)
        facial_recog.encode()

        self.reset()

        return 'main'

    def display(self):
        if not self.user:
            print('Add facial recognition login')
            print('')

    def input(self):
        if not self.user:
            return input('Enter your username: ')

        return input('Enter your password: ')
