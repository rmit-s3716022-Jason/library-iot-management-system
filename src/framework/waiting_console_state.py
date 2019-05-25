from .console_state import ConsoleState

class WaitingConsoleState(ConsoleState):
   
    def __init__(self, display_text):
        super().__init__(display_text, '')

    def handle_input(self, input_string, context):
        context.socket.wait_for_message()
        return ''

    def input(self):
        return ''
    
    def display(self):
        return ''
