###to verify permissions
from google.oauth2 import service_account
from googleapiclient.discovery import build

def check_folder_permissions(folder_id, credentials_path):
    # Load credentials from the service account key file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Retrieve permissions for the specified folder
    permissions = drive_service.permissions().list(fileId=folder_id).execute()

    # Check if the service account email address is listed with the necessary permissions
    service_account_email = "pythonproject-syncin@syncin-411107.iam.gserviceaccount.com"
    for permission in permissions.get('permissions', []):
        if permission['email'] == service_account_email:
            print(f"Service account has the following permissions: {permission['role']}")

if __name__ == "__main__":
    folder_id = "1gvh-akOM4JlkCljrtpxAGfX4dXdbfJ2n"  # Replace with the ID of the folder you want to check permissions for
    credentials_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"  # Replace with the path to your service account credentials file
    check_folder_permissions(folder_id, credentials_path)
