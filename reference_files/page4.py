from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_folder(service, folder_name):
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=folder_metadata,
                                    fields='id').execute()
    print('Folder ID: ', folder.get('id'))
    return folder.get('id')

def grant_access(service, folder_id, email):
    batch = service.new_batch_http_request(callback=callback)
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email
    }
    request = service.permissions().create(
        fileId=folder_id,
        body=user_permission,
        fields='id',
    )
    batch.add(request)
    batch.execute()

def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    folder_name = input("Enter the name of the folder: ")
    folder_id = create_folder(service, folder_name)

    email = input("Enter the email address to grant access: ")
    grant_access(service, folder_id, email)

if __name__ == '__main__':
    main()
