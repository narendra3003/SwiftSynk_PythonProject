### code for uploading file on 
# to install google drive client- pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def delete_file_from_drive(file_path, drive_folder_id, credentials_file_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Extract the file name from the file path
    file_name = str(file_path)
    # file_name = os.path.basename(file_path.split("\\")[-1])

    # Search for the file in the specified folder
    query = f"name='{file_name}' and '{drive_folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    
    # Check if the file exists in the folder
    files = response.get('files', [])
    if not files:
        print(f"File '{file_name}' not found in folder with ID '{drive_folder_id}'.")
        return

    # Delete the file
    file_id = files[0]['id']
    drive_service.files().delete(fileId=file_id).execute()
    print(f"File '{file_name}' deleted successfully from Google Drive.")

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

if __name__ == "__main__":
    file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt"
    drive_folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

    # upload_file_to_drive(file_path, drive_folder_id, credentials_file_path)
    delete_file_from_drive(file_path, drive_folder_id, credentials_file_path)