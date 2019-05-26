"""
state.py
========
"""


class State():
    """The login state of the reception pi"""
    def __init__(self):
        self.state = 'logged_out'

    def login(self):
        """Change state to logged in"""
        self.state = 'logged_in'

    def logout(self):
        """Change state to logged_out"""
        self.state = 'logged_out'

    def is_logged_in(self):
        """Check whether the reception pi is logged in"""
        return self.state == 'logged_in'
