from io import BytesIO
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def download_file_from_drive(file_id, destination_folder_path, credentials_path):
    try:
        # Load credentials from the service account key file
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )

        # Build the Google Drive API service
        drive_service = build('drive', 'v3', credentials=credentials)
        request = drive_service.files().get_media(fileId=file_id)

        # Retrieve file metadata
        file_metadata = drive_service.files().get(fileId=file_id).execute()

        # Get the file name from metadata
        file_name = file_metadata['name']

        # Create the destination file path
        destination_file_path = os.path.join(destination_folder_path, file_name)

        fh = BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print("Download Progress: {0}".format(int(status.progress() * 100))) 

    except Exception as e:
        print(f"Error occurred while downloading file: {e}")

def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download Progress: {0}".format(int(status.progress() * 100))) 

# Example usage:
file_id = '1B7WBda1i2E0lnupRI2RVzvK-12EBM1bh'
destination_folder_path = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang'
credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

download_file_from_drive(file_id, destination_folder_path, credentials_file_path)
