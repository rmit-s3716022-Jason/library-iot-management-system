"""
console.py
==========

This class provides the engine for the CLI programs

It runs the display->input loop and switches states when told to by the console
states that have been added to it
"""
from mock_state import MockState

class Console:
    """
    Params
        :utility: shared resources and state
    """
    def __init__(self, utility):
        self.states = {}
        self.current_state = None
        self.utility = utility

    def add_state(self, name, state):
        """Adds a state and associates it with a name"""
        self.states[name] = state

    def set_current_state(self, name):
        """Sets the state to a previously registered state"""
        self.current_state = self.states[name]

    def run(self):
        """Runs the display->input loop"""
        while True:
            self.display()
            new_state = self.input()
            if new_state in self.states:
                self.current_state = self.states[new_state]
            elif new_state == "exit":
                break

    def display(self):
        self.current_state.display()

    def input(self):
        input_result = self.current_state.input()
        return self.current_state.handle_input(input_result, self.utility)
