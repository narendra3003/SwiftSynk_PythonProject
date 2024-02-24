###Code to reupload on modified

from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.credentials import Credentials
from googleapiclient.errors import HttpError
import datetime
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

last_upload=datetime.datetime.now()
# print(type(last_upload))
# datetime_obj1 = datetime.datetime.strptime("24/02/23 16:40:01", '%y/%m/%d %H:%M:%S')
# datetime_obj2 = datetime.datetime.strptime("24/02/23 16:40:02", '%y/%m/%d %H:%M:%S')
# print(datetime_obj1)
# print(datetime_obj1<datetime_obj2)

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
filesToUpload=["C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt"]

#to delete files from drive
def delete_file_from_drive(file_name, drive_folder_id=drive_folder_id, credentials_file_path=credentials_file_path):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    drive_service = build('drive', 'v3', credentials=credentials)
    # file_name = os.path.basename(file_path)
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
    global last_upload
    last_upload=datetime.datetime.now()
    print("Modified at: ", last_upload)
    print(f"File uploaded successfully with file ID: {response['id']}")

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

#to get modified time
def get_last_modified_time(file_path):
    modified_timestamp = os.path.getmtime(file_path)
    modified_datetime = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified_datetime.strftime('%Y-%m-%d %H:%M:%S')

def reUpload(file_path, drive_folder_id, credentials_file_path):
    file_name=os.path.basename(file_path)
    if(get_file_id!=None):
        delete_file_from_drive(file_name, drive_folder_id, credentials_file_path)
    upload_file_to_drive(file_path, drive_folder_id, credentials_file_path)

def IsInternet():
    try:
        response=requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

while True:
    if(not IsInternet()):
        continue
    if(datetime.datetime.strptime(get_last_modified_time(file_path), '%Y-%m-%d %H:%M:%S')>last_upload):
        print(datetime.datetime.strptime(get_last_modified_time(file_path), '%Y-%m-%d %H:%M:%S'),last_upload)
        reUpload(file_path, drive_folder_id, credentials_file_path)
    time.sleep(1)