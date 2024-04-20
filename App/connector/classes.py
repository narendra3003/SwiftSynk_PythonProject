
class User:
    def __init__(self, username, base_drive_folder_id, secondary_folder_id):
        self.username=username
        self.base_drive_folder_id=base_drive_folder_id
        self.secondary_folder_id=secondary_folder_id
        
    def modifyUser(self, Newusername, Newbase_drive_folder_id, Newsecondary_folder_id):
        self.username=Newusername
        self.base_drive_folder_id=Newbase_drive_folder_id
        self.secondary_folder_id=Newsecondary_folder_id