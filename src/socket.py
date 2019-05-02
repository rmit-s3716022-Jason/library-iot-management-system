class Socket:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.handlers = {}

    def send_message(self, message):
        pass

    def add_handlers(self, message_type, handler):
        self.handlers[message_type] = handler
