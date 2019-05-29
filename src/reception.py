"""
reception.py
============

The reception main program

Handles the user management and login of the users. Supports
facial recognition for login.

Usage: python3 reception.py master_ip master_port
"""
import json
import threading
import sys
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
    """
    This is the class that sets up and runs the cli program that
    handles library login.

    Params
        :ip: the IP address to listen on
        :port: the port to listen on
        :master_ip: the master IP address to connect to
        :master_port: the master port to connect to

    """
    def __init__(self, ip, port, master_ip, master_port):
        db_interface = SqliteDbInterface()
        socket = UdpSocket(ip, port, True)
        socket.add_handler('logout', self.logout)
        self.utility = Utility(db_interface, socket)
        self.console = Console(self.utility)
        self.utility.state = State()
        self.master_ip = master_ip
        self.master_port = int(master_port)

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

        login = LoginConsoleState(self.master_ip, self.master_port)
        login.add_handler('done', lambda x: 'main')

        add_photo = AddPhotoConsoleState()

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
        """
        Starts the main loop of the cli program

        """
        self.console.run()

    def logout(self, data):
        self.utility.state.logout()
        self.console.set_current_state('main')

    def login(self, username):
        user = self.utility.db.find_user(username)

        if not user:
            return

        self.utility.state.login()

        print(user.username + " has logged in")

        data = {}
        data['username'] = user.username
        data['firstname'] = user.firstname
        data['lastname'] = user.lastname
        data['user_id'] = user.user_id
        self.utility.socket.send_message(
            'login', json.dumps(data), self.master_ip, self.master_port)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main = Reception('127.0.0.1', 6000, '10.132.113.27', 5500)
        main.run()
    else:
        print('Usage python3 reception.py <master_ip> <master_port>')
