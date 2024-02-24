###Code to create a folder inside a folder on gdrive
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_folder_in_folder(parent_folder_id, folder_name, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Create file metadata for the new folder
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]  # ID of the parent folder
    }

    # Create the folder
    folder = drive_service.files().create(body=file_metadata, fields='id').execute()

    print(f"Folder '{folder_name}' created successfully in folder with ID '{parent_folder_id}'.")
    return folder.get('id')

if __name__ == "__main__":
    parent_folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"  # Replace with the ID of the parent folder
    folder_name = "Hii" 
    credentials_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

    new_folder_id = create_folder_in_folder(parent_folder_id, folder_name, credentials_path)
    print(new_folder_id)
