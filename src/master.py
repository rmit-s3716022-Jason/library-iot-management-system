from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.sqlite_db_interface import SqliteDbInterface
from framework.utility import Utility
from framework.udp_socket import UdpSocket


def logout(context):
    # send logout message
    context.socket.send_message('logout', '{}', '127.0.0.1', 6000)
    return 'waiting'


class Master:
    def __init__(self, ip, port):
        db_interface = SqliteDbInterface()  # should be gcp database
        socket = UdpSocket(ip, port, True)
        socket.add_handler('login', self.login)
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)

        waiting_state = WaitingConsoleState('Waiting for login')
        
        main_menu = ConsoleState("""
            1. Search for a book
            2. Return a book
            3. Logout
            \n""",
                                 'Enter menu option: ')
        main_menu.add_handler("3", logout)

        self.console.add_state('waiting', waiting_state)
        self.console.add_state('main', main_menu)
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