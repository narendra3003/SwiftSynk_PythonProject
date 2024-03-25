from google.oauth2 import service_account
from googleapiclient.discovery import build

def copy_file(file_id, destination_folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Retrieve the metadata of the file to be copied
    file_metadata = drive_service.files().get(fileId=file_id, fields='name').execute()

    # Create a copy of the file in the destination folder
    copied_file = drive_service.files().copy(
        fileId=file_id,
        body={'parents': [destination_folder_id]},
        fields='id'
    ).execute()

    print(f"File '{file_metadata['name']}' copied to destination folder with ID '{destination_folder_id}'.")

if __name__ == "__main__":
    file_id = "1dpsFMCwPhVI8k9i9pGJcTbjPqCfMT0-N"  # Replace with the ID of the file you want to copy
    destination_folder_id = "16OGxSt74hhmluHekVRs6RRfvoJ1XZdxS"  # Replace with the ID of the destination folder
    credentials_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"  # Replace with the path to your service account credentials file

    copy_file(file_id, destination_folder_id, credentials_path)
