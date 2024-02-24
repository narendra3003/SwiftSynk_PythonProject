import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class FileUploadHandler:
    def __init__(self, drive_folder_id, credentials_path):
        self.drive_folder_id = drive_folder_id
        self.credentials_path = credentials_path
        self.uploaded_files = set()

    def upload_file_to_drive(self, file_path):
        if file_path in self.uploaded_files:
            print(f"File {file_path} has already been uploaded.")
            return

        try:
            # Load credentials from the service account key file
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path,
                scopes=['https://www.googleapis.com/auth/drive.file']
            )

            # Build the Google Drive API service
            drive_service = build('drive', 'v3', credentials=credentials)

            # Set the file metadata
            file_metadata = {
                'name': os.path.basename(file_path),
                'parents': [self.drive_folder_id],
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
            self.uploaded_files.add(file_path)
        except Exception as e:
            print(f"Error uploading file: {e}")

class MyHandler(FileSystemEventHandler):
    def __init__(self, upload_handler):
        self.upload_handler = upload_handler

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified.')
        self.upload_handler.upload_file_to_drive(event.src_path)

if __name__ == "__main__":
    folder_to_watch = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files'  # Replace with the path to your folder
    drive_folder_id_to_upload_to = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

    upload_handler = FileUploadHandler(drive_folder_id_to_upload_to, credentials_file_path)
    event_handler = MyHandler(upload_handler)
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()

    try:
        print(f'Watching folder: {folder_to_watch}')
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching folder.")
        observer.join()

