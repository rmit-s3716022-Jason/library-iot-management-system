"""
upd_socket.py
=============

UDP client server class
"""
import socket
import json


class UdpSocket:
    """
    The UDP socket client/server class
    This manages the UDP socket and provides helper methods and message
    handling.

    Params
        :ip: the IP address to use
        :port: the port to use
        :is_server:
    """
    def __init__(self, ip, port, is_server):
        self.address = (ip, port)
        self.handlers = {}

        self.socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

        if is_server:
            self.socket.bind(self.address)

        self.buffer_size = 2048

    def send_message(self, message_type, data, ip_address, port):
        """
        Sends a message to the external system
        Encodes as json

        Params
            :message_type: the type of message being sent
            :data: the message data
            :ip_address: the ip_address to send to
            :port: the port to send to
        """
        sending_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        message_dict = {'type': message_type, 'data': data}
        message = json.dumps(message_dict)

        sending_socket.sendto(message.encode(), (ip_address, port))
        sending_socket.close()

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

    def add_handler(self, message_type, handler):
        """
        Adds a handler for a message type

        Params
            :message_type: the type of message this handler handles
            :handler: the handler to handle the message
        """
        self.handlers[message_type] = handler

    def close(self):
        """Closes the connection"""
        self.socket.close()
