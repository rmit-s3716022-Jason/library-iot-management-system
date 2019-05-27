"""
google_calendar.py
==================
"""

from __future__ import print_function
from googleapiclient.discovery import build
from oauth2client import client, file, tools
from httplib2 import Http
import datetime
from googleapiclient.errors import HttpError

class GoogleCalendar():
    """
    Wraps all of the interactions with google calendar
    """
    def __init__(self):
        self.creds = self.get_credentials()
        self.http = self.creds.authorize(Http())
        self.service = build('calendar', 'v3', http=self.http)

    def get_credentials(self):
        """
        Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        scopes = "https://www.googleapis.com/auth/calendar"
        store = file.Storage('token.json')
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets('credentials.json', scopes)
            creds = tools.run_flow(flow, store)

        return creds

    def add_event(self, user_id, username, b_title, b_id, start_time, end_time):
        """
        Calculates start/end time of event, and creates google calendar event with
        the given data identifying the user and the book being borrowed.

        Returns:
            The generated event id to be stored in the database

        """
        event = {
            'summary': "New Borrowing Event",
            'description': str(user_id) + " borrowing: " + str(b_id) + "- " + str(b_title),
            'start': {'dateTime': str(start_time),
                      'timeZone': 'Australia/Melbourne'},
            'end': {'dateTime': str(end_time), 'timeZone': 'Australia/Melbourne'},
        }
        event = self.service.events().insert(calendarId='primary',body=event).execute()
        print("Event created: {}".format(event.get("htmlLink")))
        return event.get('id')

    def remove_event(self, e_id, c_id='primary'):
        try:
            self.service.events().delete(calendarId=c_id,eventId=e_id).execute()
            print("Event deleted.")
            return True
        except HttpError:
            print("Error: event not found")
            return False
