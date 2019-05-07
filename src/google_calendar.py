from __future__ import print_function
from googleapiclient.discovery import build
from oauth2client import client, tools
from oauth2client.file import Storage
from httplib2 import Http
from datetime import datetime
import os

try: 
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = "https://www.googleapis.com/auth/calendar.readonly"
CLIENT_SECRET_FILE = ""
APPLICATION_NAME = ""
BOR_LIMIT = datetime.timedelta(weeks=4)

class GoogleCalendar():

    # constructor to login to google calendar?
    def __init__(self):
        self.start_time = datetime.datetime.strptime(datetime.date(datetime.now()),"%d-%m-%Y")
        self.end_time = self.start_time + BOR_LIMIT

    """
    Gets valid user credentials from storage.
    
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """ 
    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')
    
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            print('Storing credentials to ' + credential_path)
        return credentials
        
    def add_event(self, title, b_title, r_date, hidden = False):
        creds = self.get_credentials()
        http = creds.authorize(Http())
        service = build.build('calendar', 'v3', http=http)

        # Unsure what else to add in
        # https://developers.google.com/calendar/create-events
        body = {
            'summary': title,
            'description': b_title,
            'start': {'dateTime': self.start_time, 'timeZone': 'Australia/Melbourne'}, 
            'end': {'dateTime': self.end_time, 'timeZone': 'Australia/Melbourne'},
        }
        service.events().insert(calendarID='primary',body=body).execute()

    def remove_event(self):
        pass

    