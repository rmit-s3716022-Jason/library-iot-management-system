from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.utility import Utility
from framework.udp_socket import UdpSocket

from framework.reception.registration_console_state import (
    RegistrationConsoleState
)
from framework.reception.login_console_state import (
    LoginConsoleState
)
from framework.reception.sqlite_db_interface import SqliteDbInterface


class Reception:
    def __init__(self, ip, port):
        db_interface = SqliteDbInterface()
        socket = UdpSocket(ip, port, True)
        socket.add_handler('logout', self.logout)
        utility = Utility(db_interface, socket)
        self.console = Console(utility)

        main_menu = ConsoleState("\n1. Login\n2. Register\n\n",
                                 "Enter menu option: ")
        main_menu.add_handler("1", lambda x: "login")
        main_menu.add_handler("2", lambda x: "register")

        register = RegistrationConsoleState()
        register.add_handler('done', lambda x: 'main')

        login = LoginConsoleState()
        login.add_handler('done', lambda x: 'main')

        waiting_state = WaitingConsoleState('Waiting for logout')

        self.console.add_state('main', main_menu)
        self.console.add_state('login', login)
        self.console.add_state('register', register)
        self.console.add_state('waiting', waiting_state)
        self.console.set_current_state('main')

    def run(self):
        self.console.run()

    def logout(self, data):
        self.console.set_current_state('main')


if __name__ == '__main__':
    main = Reception('127.0.0.1', 6000)
    main.run()
