###To get name of files on drive
# AIzaSyA_afFTiBXVexbjIiZxnTp9Op5NFkseRwI --API key
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_files_in_folder(folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # List all files in the specified folder
    query = f"'{folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(name)').execute()

    # Extract file names from the response
    files = response.get('files', [])
    file_names = [file['name'] for file in files]
    
    return file_names

def delete_file_from_drive(file_name, folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Search for the file in the specified folder
    query = f"name='{file_name}' and '{folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    
    # Check if the file exists in the folder
    files = response.get('files', [])
    if not files:
        print(f"File '{file_name}' not found in folder with ID '{folder_id}'.")
        return

    # Delete the file
    file_id = files[0]['id']
    drive_service.files().delete(fileId=file_id).execute()
    print(f"File '{file_name}' deleted successfully from Google Drive.")

if __name__ == "__main__":
    # file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files\\test.txt"
    drive_folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"
    credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\Sem4_project\\reference_files\\syncin-411107-949b882c5e98.json"
    file_names = get_files_in_folder(drive_folder_id, credentials_file_path)
    print("Files in folder:")
    for name in file_names:
        print(name)
        # delete_file_from_drive(name, drive_folder_id, credentials_file_path)