from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try: 
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = "https://www.googleapis.com/auth/calendar"


class GoogleCalender():
    
    def create_event(self):
        store = file.Storage('storage.json')
        creds = store.get()

        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

        CAL = build('calendar', 'v3', http=creds.authorize(Http()))
        EVENT = {}
        e = CAL.events().insert(calendarId='primary', sendNotification=True, body=EVENT).execute()
        