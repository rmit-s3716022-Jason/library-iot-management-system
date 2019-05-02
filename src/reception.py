from .console import Console
from .console_state import ConsoleState
from .sqlite_db_interface import SqliteDbInterface
from .utility import Utility
from .socket import Socket


class Reception:
    def __init__(self, socket_connection):
        db_interface = SqliteDbInterface()
        socket = Socket(socket_connection)
        utility = Utility(db_interface, socket)
        self.console = Console(utility)

        # add states

    def run(self):
        self.console.run()


if __name__ == '__main__':
    main = Reception('127.0.0.0:5000')
    main.run()
