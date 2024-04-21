from connector.fileoprations import *


def upload_files_from_folder_to_drive(folder_path, drive_folder_id, credentials_path):
    for filename in os.listdir(folder_path):
        f = folder_path+"/"+ filename
        # checking if it is a file
        if os.path.isfile(f):
            upload_file_to_drive(f, drive_folder_id, credentials_path)
        elif(os.path.isdir(f)):
            upload_folder_to_drive(f, drive_folder_id, credentials_path)
        else:
            print("NONE")


def create_folder_in_parent_on_drive(folder_path="Second space", parent_folder_id=mainUser.base_drive_folder_id, credentials_path=credentials_file_path):
    drive_service=getDriveService()
    folder_name=folder_path.split("\\")[-1]

    # Set the file metadata
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]  # ID of the parent folder
    }
    print(file_metadata)
    # Create the folder
    folder = drive_service.files().create(body=file_metadata, fields='id').execute()

    print(f"Folder '{folder_name}' created successfully in folder with ID '{parent_folder_id}'.")
    return folder.get('id')

def upload_folder_to_drive(folder_path, parent_folder_id=mainUser.base_drive_folder_id, credentials_path=credentials_file_path):
    if(dbm.folder_isUploaded(folder_path)):
        return
    new_folder_id=create_folder_in_parent_on_drive(folder_path, parent_folder_id, credentials_path)
    dbm.insertFolder(new_folder_id,folder_path,mainUser.username)
    upload_files_from_folder_to_drive(folder_path, new_folder_id, credentials_path)

def delete_folder_from_drive(folder_name, drive_folder_id=mainUser.base_drive_folder_id, credentials_file_path=credentials_file_path):
    drive_service = getDriveService()
    query = f"name='{folder_name}' and '{drive_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
    response = drive_service.files().list(q=query, fields='files(id)').execute()
    folders = response.get('files', [])

    if not folders:
        print(f"Folder '{folder_name}' not found in parent folder with ID '{drive_folder_id}'.")
        return
    folder_id = folders[0]['id']

    results = drive_service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id, name, mimeType)",
    ).execute()
    
    items = results.get('files', [])
    for item in items:
        print( f"{item['name']} (ID: {item['id']}, Type: {item['mimeType']})")
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            delete_folder_from_drive(item['name'], folder_id)
        else:
            delete_file_from_drive(item['name'], drive_folder_id)
        
    drive_service.files().delete(fileId=folder_id).execute()
    dbm.deleteFolder(folder_id)
    print(f"Folder '{folder_name}' deleted successfully from Google Drive.")
    return folder_id

    # drive_service = getDriveService()
    # query = f"name='{folder_name}' and '{drive_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
    # response = drive_service.files().list(q=query, fields='files(id)').execute()
    # folders = response.get('files', [])

    # if not folders:
    #     print(f"Folder '{folder_name}' not found in parent folder with ID '{drive_folder_id}'.")
    #     return
    # folder_id = folders[0]['id']

    # files_query = f"'{folder_id}' in parents and trashed=false"
    # files_response = drive_service.files().list(q=files_query, fields='files(id)').execute()
    # files = files_response.get('files', [])

    # for file in files:
    #     file_id = file['id']
    #     drive_service.files().delete(fileId=file_id).execute()
    #     print(f"File with ID '{file_id}' deleted successfully.")
        
    # drive_service.files().delete(fileId=folder_id).execute()
    # print(f"Folder '{folder_name}' deleted successfully from Google Drive.")
    # return folder_id
