from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.utility import Utility
from framework.udp_socket import UdpSocket
from framework.master.google_cloud_db import GoogleCloudDb
from framework.master.google_calendar impot GoogleCalendar
from framework.master.search_console_state import SearchConsoleState
from framework.master.result_console_state import ResultConsoleState


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
        result_state = ResultConsoleState('Displaying search results', self.utility, gc)

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
        self.console.add_state('result', result_state)
        self.console.set_current_state('waiting')

    def run(self):
        self.console.run()

    def login(self, data):
        self.utility.username = data.username
        self.utility.name = data.name
        self.utility.user_id = data.user_id

        self.console.set_current_state('main')


if __name__ == '__main__':
    main = Master('127.0.0.1', 5000)
    main.run()