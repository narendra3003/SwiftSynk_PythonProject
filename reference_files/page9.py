###to get id of file given name
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_file_id(file_name, folder_id, credentials_path):
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
        return None

    # Return the ID of the first matching file
    return files[0]['id']
if __name__ == "__main__":
    file_name = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\test.txt"  # Replace with the name of the file you want to find
    folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"     # Replace with the ID of the folder containing the file
    credentials_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"  # Replace with the path to your service account credentials file
    file_id = get_file_id(file_name, folder_id, credentials_path)
    if file_id:
        print(f"File ID of '{file_name}' in folder '{folder_id}': {file_id}")