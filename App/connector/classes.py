
class User:
    def _init_(self, username=None, base_drive_folder_id="", secondary_folder_id=""):
        self.username=username
        self.base_drive_folder_id=base_drive_folder_id
        self.secondary_folder_id=secondary_folder_id
        
    def modifyUser(self, Newusername, Newbase_drive_folder_id, Newsecondary_folder_id):
        self.username=Newusername
        self.base_drive_folder_id=Newbase_drive_folder_id
        self.secondary_folder_id=Newsecondary_folder_id
    
    def delUser(self):
        self.username=None
        self.base_drive_folder_id=None
        self.secondary_folder_id=None
