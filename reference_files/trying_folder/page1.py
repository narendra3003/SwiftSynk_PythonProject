### code for uploading folders and folders inside folders
# to install google drive client- pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
from google.oauth2 import service_account
import os
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
        'name': file_path.split("\\")[-1],  # Extracting the file name from the path
        'parents': [drive_folder_id],  # ID of the folder in Google Drive to upload to
    }
    print(file_metadata)
    # To get type of the file
    print(os.path.splitext(file_metadata.get('name')))

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

def upload_files_from_folder_to_drive(folder_path, drive_folder_id, credentials_path):
    for filename in os.listdir(folder_path):
        f = os.path.join(folder_path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            upload_file_to_drive(f, drive_folder_id, credentials_path)
        elif(os.path.isdir(f)):
            upload_folder_to_drive(f, drive_folder_id, credentials_path)
        else:
            print("NONE")

def create_folder_in_parent_on_drive(folder_path, parent_folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )
    
    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    folder_name=folder_path.split("\\")[-1]

    # Set the file metadata
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]  # ID of the parent folder
    }
    print(file_metadata)
    # Create the folder
    folder = drive_service.files().create(body=file_metadata, fields='id').execute()

    print(f"Folder '{folder_name}' created successfully in folder with ID '{parent_folder_id}'.")
    return folder.get('id')

def upload_folder_to_drive(folder_path, parent_folder_id, credentials_path):
    new_folder_id=create_folder_in_parent_on_drive(folder_path, parent_folder_id, credentials_path)
    upload_files_from_folder_to_drive(folder_path, new_folder_id, credentials_path)

if __name__ == "__main__":
    folder_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files"
    parent_folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files\\syncin-411107-949b882c5e98.json"

    new_folder_id=upload_folder_to_drive(folder_path, parent_folder_id, credentials_file_path)
    print(new_folder_id)
    