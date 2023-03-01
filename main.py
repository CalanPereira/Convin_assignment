from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

scopes = ['https://www.googleapis.com/auth/calender']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json",scopes=scopes)

credientials = flow.run_local_server(host="localhost",bind_addr=None,port=3000)

pickle.dump(credientials,open("token.pkl","wb"))

credentials = pickle.load(open("token.pkl","rb"))

service = build("calendar","v3",credentials=credentials)

result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']
result = service.events().list(calendar_Id=calendar_id).execute()

result['item'][0]
