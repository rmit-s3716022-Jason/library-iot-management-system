"""
UDP client server class
"""
import socket
import json


class UdpSocket:
    """
    The UDP socket client/server class
    This manages the UDP socket and provides helper methods and message
    handling.
    """
    def __init__(self, ip, port, is_server):
        self.address = (ip, port)
        self.handlers = {}

        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_DGRAM)

        if is_server:
            self.socket.bind(self.address)

        self.buffer_size = 2048

    def send_message(self, type, data):
        """
        Sends a message to the external system
        Encodes as json
        """
        message_dict = {'type': type, 'data': data}
        message = json.dumps(message_dict)
        self.socket.sendto(message.encode(), self.address)

    def wait_for_message(self):
        """
        Waits for a message from the external system and tries
        to handle it when it is received
        """
        message_encoded = self.socket.recv(self.buffer_size)
        message_json = message_encoded.decode("utf-8")
        message = json.loads(message_json)
        if message['type'] in self.handlers:
            self.handlers[message['type']](message['data'])

    def add_handlers(self, message_type, handler):
        self.handlers[message_type] = handler

    def close(self):
        self.socket.close()
