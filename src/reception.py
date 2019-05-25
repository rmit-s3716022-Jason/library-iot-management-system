import json
import threading
from framework.console import Console
from framework.console_state import ConsoleState
from framework.waiting_console_state import WaitingConsoleState
from framework.utility import Utility
from framework.udp_socket import UdpSocket

from framework.reception.facial_recog import FacialRecog
from framework.reception.add_photo_console_state import AddPhotoConsoleState
from framework.reception.state import State
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
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)
        self.utility.state = State()

        main_menu = ConsoleState("""
            1. Login
            2. Register
            3. Add facial recognition to account


            """, "Enter menu option: ")
        main_menu.add_handler("1", lambda x: "login")
        main_menu.add_handler("2", lambda x: "register")
        main_menu.add_handler('3', lambda x: "add_photo")

        register = RegistrationConsoleState()
        register.add_handler('done', lambda x: 'main')

        login = LoginConsoleState()
        login.add_handler('done', lambda x: 'main')

        add_photo = AddPhoto()

        waiting_state = WaitingConsoleState('Waiting for logout')

        self.console.add_state('main', main_menu)
        self.console.add_state('login', login)
        self.console.add_state('register', register)
        self.console.add_state('waiting', waiting_state)
        self.console.add_state('add_photo', add_photo)
        self.console.set_current_state('main')

        self.facial_recog = FacialRecog()

        self.facial_recog_thread = threading.Thread(
            target=self.facial_recog.facial_recog_login,
            args=(self.utility.state, self.login))
        self.facial_recog_thread.start()

    def run(self):
        self.console.run()

    def logout(self, data):
        self.utility.state.logout()
        self.console.set_current_state('main')

    def login(self, username):
        user = self.utility.db.find_user(username)

        if not user:
            return

        self.utility.state.login()

        data = {}
        data['username'] = user.username
        data['name'] = user.name
        data['user_id'] = user.user_id
        self.utility.socket.send_message(
            'login', json.dumps(data), '127.0.0.1', 5000)


if __name__ == '__main__':
    main = Reception('127.0.0.1', 6000)
    main.run()
