from __future__ import print_function
from config import SCOPES
import bot

import os.path
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class MailWorker:

    def __init__(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'linker_sender/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        self.service = build('gmail', 'v1', credentials=creds)

    @property
    def get_message(self) -> str:

       result = self.service.users().messages().list(maxResults=1, userId='me', labelIds=['UNREAD', 'INBOX', 'CATEGORY_PERSONAL']).execute()
       
       message = result.get('messages')
       text = self.service.users().messages().get(userId='me', id=message[0]['id']).execute()
       try:
           payload = text['payload']
           headers = payload['headers']
           subject = None
           sender = None
           for d in headers:
               if d['name'] == 'Subject':
                   subject = d['value']
               if d['name'] == 'From':
                   sender = d['value']

           data = payload['body']['data']
           data = data.replace("-", "+").replace("_", "/")
           decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
           if subject and sender is not None:
                return 'Subject: ' + subject + '\nFrom: ' + sender + 'Message: ' + decoded_data
           else:
               return 'From: ' + sender + '\nMessage: ' + decoded_data

       except:
           pass
