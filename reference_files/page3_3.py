import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_file_to_drive(file_path, drive_folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Set the file metadata
    file_metadata = {
        'name': file_path.split("/")[-1],  # Extracting the file name from the path
        'parents': [drive_folder_id],  # ID of the folder in Google Drive to upload to
    }

    # Create a media file upload instance and upload the file
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

class MyHandler(FileSystemEventHandler):
    def __init__(self, folder_to_watch, credentials_file_path, drive_folder_id_to_upload_to):
        super().__init__()
        self.folder_to_watch = folder_to_watch
        self.credentials_file_path = credentials_file_path
        self.drive_folder_id_to_upload_to = drive_folder_id_to_upload_to

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified.')
        # Replace these with your specific values
        file_path_to_upload = event.src_path
        upload_file_to_drive(file_path_to_upload, self.drive_folder_id_to_upload_to, self.credentials_file_path)
        
        # Stop the current observer
        self.observer.stop()
        
        # Start a new observer
        self.observer = Observer()
        self.observer.schedule(self, path=self.folder_to_watch, recursive=True)
        self.observer.start()

if __name__ == "__main__":
    folder_to_watch = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files'  # Replace with the path to your folder
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files\\syncin-411107-949b882c5e98.json"
    drive_folder_id_to_upload_to = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n" #1Ov7bY55OAh-abKsfdksnsMkn

    event_handler = MyHandler(folder_to_watch, credentials_file_path, drive_folder_id_to_upload_to)
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    event_handler.observer = observer  # Store the observer reference in the event handler

    try:
        print(f'Watching folder: {folder_to_watch}')
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching folder.")
        observer.join()
