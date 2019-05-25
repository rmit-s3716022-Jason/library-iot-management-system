class State():
    def __init__(self):
        self.state = 'logged_out'

    def login(self):
        self.state = 'logged_in'

    def logout(self):
        self.state = 'logged_out'

    def is_logged_in(self):
        return self.state == 'logged_in'
