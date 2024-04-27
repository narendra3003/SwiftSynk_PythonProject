import os, dbm

def getlogdata():
    data = dbm.logtable()
    modified_data = []
    for row in data:
        modified_row = []
        timestamp = row[3]
        modified_row.append(timestamp)
        act = row[1]
        path_email = row[2]
        ty = row[0]
        if ty == 'User':
            if act == 'insert':
                desc = 'User account: '+path_email+' was added.'
                modified_row.append(desc)
            elif act == 'update':
                desc = 'User account: '+path_email+' was updated.'
                modified_row.append(desc)
            elif act == 'delete':
                desc = 'User account: '+path_email+' was removed.'
                modified_row.append(desc)
        elif ty == 'File' or 'Folder':
            if act == 'insert':
                desc = ty+': '+os.path.basename(path_email)+' was synced. '+ty+' path: '+path_email
                modified_row.append(desc)
                print("modified_row: ",modified_row)
            elif act == 'update':
                desc = ty+': '+os.path.basename(path_email)+'   was updated. '+ty+' path: '+path_email
                modified_row.append(desc)
            elif act == 'delete':
                desc = ty+': '+os.path.basename(path_email)+' was unsynced. '+ty+' path: '+path_email
                modified_row.append(desc)
        modified_data.append(tuple(modified_row))
    return modified_data

