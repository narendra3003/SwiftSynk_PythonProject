import pickle, os
from google_auth_oauthlib.flow import InstalledAppFlow
from connector.basic import *
from google.auth.transport.requests import Request

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
                client_secrets_file, ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_folder(service, folder_name="SwiftSynK"):
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=folder_metadata,
                                    fields='id').execute()
    print('Folder ID: ', folder.get('id'))
    return folder.get('id')

def grant_access(service, folder_id, email=app_email_id):
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
    request.execute()
