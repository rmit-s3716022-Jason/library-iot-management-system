"""
master.py
=========

The master library pi CLI program.

Allows the user to search for books, borrow books and return them.
The book and borrowing data is stored in the cloud.

Usage python3 master.py <reception_ip> <reception_port>

"""

import json
import sys
from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.utility import Utility
from framework.udp_socket import UdpSocket
from framework.master.google_cloud_db import GoogleCloudDb
from framework.master.google_calendar import GoogleCalendar
from framework.master.search_console_state import SearchConsoleState
from framework.master.borrow_console_state import BorrowConsoleState
from framework.master.return_console_state import ReturnConsoleState
from framework.master.master_user import MasterUser


class Master:
    """
    The class that runs the master pi library code

    Constructor

    Params
        :ip: IP address to listen on
        :port: port to listen on
        :reception_ip: reception pi IP address
        :reception_port: the port that the reception pi is listening on
    """
    def __init__(self, ip, port, reception_ip, reception_port):
        db_interface = GoogleCloudDb()
        gc = GoogleCalendar()
        socket = UdpSocket(ip, port, True)
        socket.add_handler('login', self.login)
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)

        self.reception_ip = reception_ip
        self.reception_port = reception_port

        waiting_state = WaitingConsoleState('Waiting for login')
        searching_state = SearchConsoleState('Searching for book')
        borrowing_state = BorrowConsoleState('Borrowing a book', self.utility, gc)
        returning_state = ReturnConsoleState('Returning a book', self.utility, gc)
        borrowing_state = BorrowConsoleState('Borrowing a book', self.utility, gc)

        main_menu = ConsoleState("""1. Search for a book\n2. Borrow a book\n3. Return a book\n4. Logout""", 'Enter menu option: ')
        main_menu.add_handler("1", lambda x: 'searching')
        main_menu.add_handler("2", lambda x: 'borrow')
        main_menu.add_handler("3", lambda x: 'return')
        main_menu.add_handler("4", self.logout)

        self.console.add_state('waiting', waiting_state)
        self.console.add_state('main', main_menu)
        self.console.add_state('searching', searching_state)
        self.console.add_state('borrow', borrowing_state)
        self.console.add_state('return', returning_state)
        self.console.set_current_state('waiting')

    def run(self):
        """Runs the main loop of the CLI program"""
        print("Master pi now running.")
        self.console.run()

    def login(self, data):
        login_data = json.loads(data)
        self.utility.user = MasterUser(login_data['username'],
                                       login_data['firstname'],
                                       login_data['lastname'],
                                       login_data['user_id'])
        
        self.console.set_current_state('main')

    def logout(self, context):
        # send logout message
        context.socket.send_message(
            'logout', '{}', self.reception_ip, self.reception_port)
        return 'waiting'


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main = Master(sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
        main.run()

    else:
        print('Usage python3 master.py <local_ip> <local_port> <reception_ip> <reception_port>')
