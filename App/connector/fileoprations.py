from connector.helpers import *
import dbm
from googleapiclient.http import MediaFileUpload


##To upload file on drive
def upload_file_to_drive(file_path, drive_folder_id=mainUser.base_drive_folder_id, credentials_file_path=credentials_file_path):
    drive_service=getDriveService(credentials_file_path)
    file_metadata = {
        'name': file_path.split("\\")[-1],
        'parents': [drive_folder_id],
    }
    print(file_metadata)
    print(os.path.splitext(file_metadata.get('name')))
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
    print(response['id']," ",file_path," ",get_current_time()," ",drive_folder_id," ","Synced")
    dbm.insertFile(response['id'],file_path,get_current_time(),drive_folder_id,"Synced")


#to delete files from drive
def delete_file_from_drive(file_name, drive_folder_id=mainUser.base_drive_folder_id, credentials_file_path=credentials_file_path, table="file"):
    drive_service = getDriveService()
    # file_name = os.path.basename(file_path)
    query = f"name='{file_name}' and '{drive_folder_id}' in parents and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    files = response.get('files', [])

    if not files:
        print(f"File '{file_name}' not found in folder with ID '{drive_folder_id}'.")
        return
    file_id = files[0]['id']
    drive_service.files().delete(fileId=file_id).execute()
    if(table=="version"):
        dbm.deleteVersion(file_id)
        return
    if(dbm.deleteFile(file_id)==1):
        print(f"File '{file_name}' deleted successfully from Google Drive. And DB", file_id)
    print(f"File '{file_name}' deleted successfully from Google Drive.")