from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

calendar = googleapiclient.discovery.build(
      'calendar', 'v3', credentials=credentials)


    # Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = calendar.events().list(calendarId='ma2shcfl1bmfjrstv9bu732bn4@group.calendar.google.com', timeMin=now,
                            maxResults=10, singleEvents=True,
                            orderBy='startTime').execute()
events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()




#https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar&access_type=offline&include_granted_scopes=true&state=state_parameter_passthrough_value&redirect_uri=https://localhost:9000%2Foauthcallback&response_type=code&client_id=828543267006-scihaocr3lbiq8pg9d0tsvjshccv8emc.apps.googleusercontent.com
def oauthcallback(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],)

    flow.redirect_uri = 'https://localhost:9000/oauthcallback'
    authorization_response = request.get_raw_uri()
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    print(str({
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}))

    #{'token': 'ya29.GltOBvriNoRcOGgILK5zbno3f-NxZvcqaSRQzSTEI1MFR_0olb0BCX66ysHDxjwd_iT5d_YzJ2LbVi1ogdIsMMQ5C7ftzM9QP8RByWO7HxgF1f3bx0yzo6EaDvqI', 'refresh_token': '1/_x4Yv7RM-IlVNrZjmH0dG7wVzEA15-UtTdyLQlhlAFlDJ1f38w7RHoYuXeCKSQIu', 'token_uri': 'https://www.googleapis.com/oauth2/v3/token', 'client_id': '828543267006-scihaocr3lbiq8pg9d0tsvjshccv8emc.apps.googleusercontent.com', 'client_secret': 'bJkZRIkr72sdUFsh3hD7hTif', 'scopes': ['https://www.googleapis.com/auth/calendar']}

    return ''
