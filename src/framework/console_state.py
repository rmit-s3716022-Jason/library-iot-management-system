"""
console_state.py
================

Represents an activity within the CLI program
"""


class ConsoleState:
    """
    **display_text:** the text to display on the display part of the Console
    cycle

    **prompt_text:** the text to prompt user input on the input part of the
    Console cycle
    """
    def __init__(self, display_text, prompt_text):
        self.display_text = display_text
        self.prompt_text = prompt_text
        self.input_handlers = {}

    def handle_input(self, input_string, context):
        """Handles the input collected"""
        if input_string in self.input_handlers:
            result = self.input_handlers[input_string](context)
            return result
        return ''

    def add_handler(self, input_string, handler):
        """Adds a handler for a particluar input string"""
        self.input_handlers[input_string] = handler

    def display(self):
        """Displays the display text"""
        print(self.display_text)

    def input(self):
        """Collects input after displaying the prompt text"""
        return input(self.prompt_text)
