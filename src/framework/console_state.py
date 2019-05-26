class ConsoleState:
    def __init__(self, display_text, prompt_text):
        self.display_text = display_text
        self.prompt_text = prompt_text
        self.input_handlers = {}

    def handle_input(self, input_string, context):
        if input_string in self.input_handlers:
            result = self.input_handlers[input_string](context)
            return result
        return ''

    def add_handler(self, input_string, handler):
        self.input_handlers[input_string] = handler

    def display(self):
        print("\nMain Menu")
        print(self.display_text)

    def input(self):
        return input(self.prompt_text)
