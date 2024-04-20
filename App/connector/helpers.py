from connector.basic import *
import os, datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

def getDriveService(credentials_file_path=credentials_file_path):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file_path,
        scopes=SCOPES
    )
    
    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service

##to get id of the file on drive
def get_file_id(file_name, folder_id=mainUser.base_drive_folder_id, credentials_path=credentials_file_path):
    drive_service=getDriveService()
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

#to get modified time
def get_last_modified_time(file_path):
    modified_timestamp = os.path.getatime(file_path)
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified_datetime.strftime('%Y-%m-%d %H:%M:%S')

#to get current time
def get_current_time():
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    return now

#to compare 2 string times (true if 1 is after 2)
def compare_time(time1, time2):
    time1_obj=datetime.datetime.strptime(time1[2:], '%y-%m-%d %H:%M:%S')
    time2_obj=datetime.datetime.strptime(time2[2:], '%y-%m-%d %H:%M:%S')
    return time1_obj>time2_obj
