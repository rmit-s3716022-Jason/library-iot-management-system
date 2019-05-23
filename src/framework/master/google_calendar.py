from __future__ import print_function
from datetime import datetime
from googleapiclient.discovery import build
from oauth2client import client, file, tools
from httplib2 import Http


class GoogleCalendar():

    def __init__(self):
        self.creds = self.get_credentials()
        self.http = self.creds.authorize(Http())
        self.service = build.build('calendar', 'v3', http=self.http)

    """
    Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    def get_credentials(self):
        scopes = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", scopes)
            creds = tools.run_flow(flow, store)

        return creds

    '''
    Calculates start/end time of event, and creates google calendar event with
    the given data identifying the user and the book being borrowed.

    Returns:
        The generated event id to be stored in the database

    '''
    def add_event(self, user_id, username, b_title, b_id):
        start_time = datetime.datetime.strptime(datetime.date(datetime.now()),
                                                "%d-%m-%Y")
        end_time = start_time + datetime.timedelta(weeks=1)

        event = {
            'summary': "New Borrowing Event",
            'description': user_id + " borrowing: " + b_id + "- " + b_title,
            'start': {'dateTime': start_time,
                      'timeZone': 'Australia/Melbourne'},
            'end': {'dateTime': end_time, 'timeZone': 'Australia/Melbourne'},
            "attendees": [{"id": user_id, "username": username}],
        }
        event = self.service.events().insert(calendarId='primary',
                                             body=event).execute()
        print("Event created: {}".format(event.get("htmlLink")))
        return event.get('id')

    '''
    Removes requested event with given event identifier.
    If successfully delete() returns a empty response body.
    '''
    def remove_event(self, e_id, c_id='primary'):
        event = self.service.events().delete(calendarId=c_id,
                                             eventId=e_id).execute()
        if not event:
            print("Event: {}".format(event['description'] + " deleted."))
        else:
            print("No such event.")

    '''
    Prints the start and description of the next 10 (unless specified
    otherwise) events on the user"s calendar.
    '''
    def display_events(self, m_results=10):
        now = datetime.utcnow().isoformat() + "Z"  # "Z" indicates UTC time.
        print("Getting upcoming events.")
        events_result = self.service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults=m_results,
            singleEvents=True,
            orderBy="startTime").execute()
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["description"])
