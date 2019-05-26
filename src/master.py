import json
from IoTAssignment2.src.framework.console import Console
from IoTAssignment2.src.framework.console_state import ConsoleState
from IoTAssignment2.src.framework.waiting_console_state import WaitingConsoleState
from IoTAssignment2.src.framework.utility import Utility
from IoTAssignment2.src.framework.udp_socket import UdpSocket
from IoTAssignment2.src.framework.master.google_cloud_db import GoogleCloudDb
from IoTAssignment2.src.framework.master.google_calendar import GoogleCalendar
from IoTAssignment2.src.framework.master.search_console_state import SearchConsoleState
from IoTAssignment2.src.framework.master.borrow_console_state import BorrowConsoleState
from IoTAssignment2.src.framework.master.return_console_state import ReturnConsoleState
from IoTAssignment2.src.framework.master.master_user import MasterUser


def logout(context):
    # send logout message
    context.socket.send_message('logout', '{}', '127.0.0.1', 6000)
    return 'waiting'


class Master:
    def __init__(self, ip, port):
        db_interface = GoogleCloudDb()
        #self.gc?
        gc = GoogleCalendar()
        socket = UdpSocket(ip, port, True)
        socket.add_handler('login', self.login)
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)

        waiting_state = WaitingConsoleState('Waiting for login')
        searching_state = SearchConsoleState('Searching for book')
        borrowing_state = BorrowConsoleState('Borrowing a book', self.utility, gc)
        returning_state = ReturnConsoleState('Returning a book', self.utility, gc)

        main_menu = ConsoleState("""
            1. Search for a book
            2. Borrow a book
            3. Return a book
            4. Logout
            \n""", 'Enter menu option: ')
        main_menu.add_handler("4", logout)

        self.console.add_state('waiting', waiting_state)
        self.console.add_state('main', main_menu)
        self.console.add_state('searching', searching_state)
        self.console.add_state('borrow', borrowing_state)
        self.console.add_state('return', returning_state)
        self.console.set_current_state('waiting')

    def run(self):
        self.console.run()

    def login(self, data):
        login_data = json.loads(data)
        self.utility.user = MasterUser(login_data['username'],
                                       login_data['firstname'],
                                       login_data['lastname'],
                                       login_data['user_id'])
        
        self.console.set_current_state('main')


if __name__ == '__main__':
    main = Master('127.0.0.1', 5000)
    main.run()
