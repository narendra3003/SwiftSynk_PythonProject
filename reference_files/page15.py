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

        # Retrieve file metadata
        file_metadata = drive_service.files().get(fileId=file_id).execute()

        # Get the file name from metadata
        file_name = file_metadata['name']

        # Create the destination file path
        destination_file_path = os.path.join(destination_folder_path, file_name)

        # Download the file
        request = drive_service.files().get_media(fileId=file_id)
        with open(destination_file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()

        print(f"File '{file_name}' downloaded successfully to '{destination_folder_path}'")

    except Exception as e:
        print(f"Error occurred while downloading file: {e}")

# Example usage:
file_id = '1fiD9dABGk6suX_QPSe9ucCTSBp-wZBYf'
destination_folder_path = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject'
credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

download_file_from_drive(file_id, destination_folder_path, credentials_file_path)
