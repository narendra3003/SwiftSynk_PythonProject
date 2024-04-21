from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

def delete_folder_items(service, folder_id, indent=0):
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id, name, mimeType)",
    ).execute()
    
    items = results.get('files', [])
    for item in items:
        print('  ' * indent + f"{item['name']} (ID: {item['id']}, Type: {item['mimeType']})")
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            delete_folder_items(service, item['id'], indent + 1)

# Your Google Drive folder ID
folder_id = '1Rzq8giL1JMHK2COA64Qi7mCMdz4sy8Po'

credentials_file_path = "C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json"

# Load credentials from the service account key file
creds = service_account.Credentials.from_service_account_file(
    credentials_file_path,
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)


# Build the Drive API service
service = build('drive', 'v3', credentials=creds)

# Call the function to list files and folders recursively
delete_folder_items(service, folder_id)