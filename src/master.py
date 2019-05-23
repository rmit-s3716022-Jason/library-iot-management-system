import json
from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.utility import Utility
from framework.udp_socket import UdpSocket
from framework.master.google_cloud_db import GoogleCloudDb
from framework.master.search_console_state import SearchConsoleState


def logout(context):
    # send logout message
    context.socket.send_message('logout', '{}', '127.0.0.1', 6000)
    return 'waiting'


class Master:
    def __init__(self, ip, port):
        #db_interface = GoogleCloudDb()
        db_interface = None
        socket = UdpSocket(ip, port, True)
        socket.add_handler('login', self.login)
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)

        waiting_state = WaitingConsoleState('Waiting for login')
        searching_state = SearchConsoleState('Searching for book')

        main_menu = ConsoleState("""
            1. Search for a book
            2. Return a book
            3. Logout
            \n""", 'Enter menu option: ')
        main_menu.add_handler("3", logout)

        self.console.add_state('waiting', waiting_state)
        self.console.add_state('main', main_menu)
        self.console.add_state('searching', searching_state)
        self.console.set_current_state('waiting')

    def run(self):
        self.console.run()

    def login(self, data):
        login_data = json.loads(data)
        self.utility.username = login_data['username']
        self.utility.name = login_data['name']
        self.utility.user_id = login_data['user_id']

        self.console.set_current_state('main')


if __name__ == '__main__':
    main = Master('127.0.0.1', 5000)
    main.run()