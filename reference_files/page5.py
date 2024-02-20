### compare files
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
class MyHandler(FileSystemEventHandler):  
    def compare_files(self, local_file_path, drive_file_id):
        # Load credentials from the service account key file
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file_path,
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )

        # Build the Google Drive API service
        drive_service = build('drive', 'v3', credentials=credentials)

        # Download the file from Google Drive
        request = drive_service.files().get_media(fileId=drive_file_id)
        drive_file_contents = request.execute()

        # Read the local file contents
        with open(local_file_path, 'rb') as local_file:
            local_file_contents = local_file.read()

        # Compare file contents
        if local_file_contents == drive_file_contents:
            print(f"File {local_file_path} is identical to the file on Google Drive.")
        else:
            print(f"File {local_file_path} is different from the file on Google Drive. Uploading...")
            self.upload_file_to_drive(local_file_path)