### code for uploading file on 
# to install google drive client- pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
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

if __name__ == "__main__":
    file_path_to_upload = "C:\\Users\\tupti\\OneDrive\\Desktop\\curr\\HelloFool.txt"
    drive_folder_id_to_upload_to = "1Ov7bY55OAh-abKsfdKWFkR15HksnsMkn"
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\curr\\syncin-411107-949b882c5e98.json"

    upload_file_to_drive(file_path_to_upload, drive_folder_id_to_upload_to, credentials_file_path)