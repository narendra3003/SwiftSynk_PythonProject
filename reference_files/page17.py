from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from io import BytesIO

file_name = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang\\Sem4\\SwiftSynk_PythonProject\\reference_files\\syncin-411107-949b882c5e98.json'  # Replace with the desired file name

SCOPES = ['https://www.googleapis.com/auth/drive']

def create_service():
    flow = InstalledAppFlow.from_client_secrets_file(file_name, SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def download_file(service, file_id):
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download Progress: {0}".format(int(status.progress() * 100))) 

service = create_service()
file_id = 'C:\\Users\\tupti\\OneDrive\\Desktop\\new Lang'  # Replace with the actual file ID
download_file(service, file_id)
