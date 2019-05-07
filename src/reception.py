from .console import Console
from .console_state import ConsoleState
from .registration_console_state import RegistrationConsoleState
from .sqlite_db_interface import SqliteDbInterface
from .utility import Utility
from .udp_socket import UdpSocket


class Reception:
    def __init__(self, ip, port):
        db_interface = SqliteDbInterface()
        socket = UdpSocket(ip, port, False)
        utility = Utility(db_interface, socket)
        self.console = Console(utility)

        main_menu = ConsoleState("\n1. Login\n2. Register\n\n",
                                 "Enter menu option: ")
        main_menu.add_handler("2", lambda x: "register")

        register = RegistrationConsoleState("Registration",
                                            "Please enter your details")
        register.add_handler('done', lambda x: 'main')

        self.console.add_state('main', main_menu)
        self.console.add_state('register', register)

    def run(self):
        self.console.run()


if __name__ == '__main__':
    main = Reception('127.0.0.0', 5000)
    main.run()
