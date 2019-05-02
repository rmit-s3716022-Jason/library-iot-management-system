from .console import Console
from .console_state import ConsoleState
from .sqlite_db_interface import SqliteDbInterface
from .utility import Utility


class Reception():
    def __init__(self):
        self.db_interface = SqliteDbInterface()
        self.utility = Utility(self.db_interface)
        self.console = Console(self.utility)

        # add states

    def run(self):
        self.console.run()


if __name__ == '__main__':
    main = Reception()
    main.run()
