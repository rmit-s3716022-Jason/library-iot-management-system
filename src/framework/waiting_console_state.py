"""
waiting_console_state.py
========================
A state that waits for a message on the socket
"""
from .console_state import ConsoleState


class WaitingConsoleState(ConsoleState):
    """ **display_text:** not used"""
    def __init__(self, display_text):
        super().__init__(display_text, '')

    def handle_input(self, input_string, context):
        """Waits for message on the socket"""
        context.socket.wait_for_message()
        return ''

    def input(self):
        """Does nothing"""
        return ''

    def display(self):
        """Does nothing"""
        return ''
