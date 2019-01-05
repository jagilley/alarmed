from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from dateutil.parser import parse

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('/Users/jaspergilley/Code/alarmed/credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
events_result = service.events().list(calendarId='jaspergilley2021@u.northwestern.edu', timeMin=now,
                                    maxResults=10, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
today = datetime.datetime.today()
nextDays = (today + datetime.timedelta(days=2)).date()
tel = []
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    end = event['end'].get('dateTime', event['end'].get('date'))
    startdate = parse(start).replace(tzinfo=None)
    if startdate.date() == nextDays:
        tel.append(event)

toSpeak = "The following items are on your calendar today: "

for itc, ev in enumerate(tel):
    print(ev)
    if itc != len(tel) - 1:
        toSpeak = toSpeak + ev['summary'] + ", "
    else:
        toSpeak = toSpeak + "and " + ev['summary'] + "."