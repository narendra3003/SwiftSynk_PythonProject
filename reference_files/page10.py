from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
# from __future__ import print_function
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.credentials import Credentials
from googleapiclient.errors import HttpError
import datetime

####Basic things needed
file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt"
drive_folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"
credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"
####Code common to all functions
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
# Load credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(
    credentials_file_path,
    scopes=SCOPES
)
# Build the Google Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

#to get modified time
def get_last_modified_time(file_path):
    modified_timestamp = os.path.getmtime(file_path)
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified_datetime

#to get size of the file
def get_file_size(file_path):
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file_path)
    return file_size_bytes

##to get id of the file on drive
def get_file_id(file_name, folder_id, credentials_path):

    # Search for the file in the specified folder
    query = f"name='{file_name}' and '{folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    
    # Check if the file exists in the folder
    files = response.get('files', [])
    if not files:
        print(f"File '{file_name}' not found in folder with ID '{folder_id}'.")
        return None

    # Return the ID of the first matching file
    return files[0]['id']

def delete_by_Id(id):
    drive_service.files().delete(fileId=id).execute()

#to delete files from drive
def delete_file_from_drive(file_path, drive_folder_id, credentials_file_path):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    drive_service = build('drive', 'v3', credentials=credentials)
    file_name = os.path.basename(file_path)
    query = f"name='{file_name}' and '{drive_folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    files = response.get('files', [])

    if not files:
        print(f"File '{file_name}' not found in folder with ID '{drive_folder_id}'.")
        return
    file_id = files[0]['id']
    drive_service.files().delete(fileId=file_id).execute()
    print(f"File '{file_name}' deleted successfully from Google Drive.")

##To upload file on drive
def upload_file_to_drive(file_path, drive_folder_id, credentials_path):
    file_metadata = {
        'name': file_path.split("\\")[-1],
        'parents': [drive_folder_id],
    }
    print(file_metadata)
    print(os.path.splitext(file_metadata.get('name')))
    media = MediaFileUpload(file_path, resumable=True)
    request = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    )
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")
    print(f"File uploaded successfully with file ID: {response['id']}")

##authenticate the user
def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

## to create folder on drive
def create_folder(service, folder_name):
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service.files().create(body=folder_metadata,
                                    fields='id').execute()
    print('Folder ID: ', folder.get('id'))
    return folder.get('id')

##to grant access to python to edit drive
def grant_access(service, folder_id, email):
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

# to get all files in the folder
def get_files_in_folder(folder_id, credentials_path):
    # List all files in the specified folder
    query = f"'{folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(name)').execute()

    # Extract file names from the response
    files = response.get('files', [])
    file_names = [file['name'] for file in files]
    
    return file_names

if __name__ == "__main__":
    ###Giving the main call
    upload_file_to_drive(file_path, drive_folder_id, credentials_file_path)
    # delete_file_from_drive(file_path, drive_folder_id, credentials_file_path)
    print(get_file_id("test.txt", drive_folder_id, credentials_file_path))