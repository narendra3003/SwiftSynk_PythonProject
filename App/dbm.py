import pymysql as p

def connect():
    return p.connect(host="localhost", user="root", password='oracle',db="SwiftSynK", port=3306)

def getFolders():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM folder;")
    data=cur.fetchall()
    con.close()
    print(data)
    return data

def getFiles():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM file;")
    data=cur.fetchall()
    con.close()
    print(data)
    return data

def getUsers():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM user;")
    data=cur.fetchall()
    con.close()
    print(data)
    return data

def insertUser(email,password,username,folder_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into user (Email,password,Username,base_folder_id) values ('{email}','{password}','{username}','{folder_id}');")
    con.commit()
    con.close()
    return 1

def insertFolder(folder_id,folder_path,email):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into folder (folder_id,folder_path,Email) values ('{folder_id}','{folder_path}','{email}');")
    con.commit()
    con.close()
    return 1

def insertFile(file_id,filepath,upload_time,folder_id,status):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into file (file_id,filepath,upload_time,folder_id,Status) values ('{file_id}','{filepath}','{upload_time}','{folder_id}','{status}');")
    con.commit()
    con.close()
    return 1

def deleteUser(dEmail):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("Delete from User where Email = '{dEmail}';")
        con.commit()
    except:
        con.close()
        return 0
    con.close()
    return 1

def deleteFolder(dFolder_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Delete from folder where folder_id = '{dFolder_id}';")
    con.commit()
    con.close()
    return 1

def deleteFile(dFile_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Delete from file where file_id = '{dFile_id}';")
    con.commit()
    con.close()
    return 1

def modifyUser(mpassword,mUsername,memail):
    con = connect()
    cur = con.cursor()
    cur.execute("Update User set password ='{mpassword}', Username = '{mUsername}' where email = '{memail}';")
    con.commit()
    con.close()
    return 1

def modifyFolder(mfolder_path,mfolder_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Update folder set folder_path = '{mfolder_path}' where folder_id = '{mfolder_id}';")
    con.commit()
    con.close()
    return 1

def modifyFile(mfilepath,mfile_id,mupload_time,mStatus):
    con = connect()
    cur = con.cursor()
    cur.execute("Update file set filepath = '{mfilepath}', upload_time = '{mupload_time}', Status = '{mStatus}' where file_id = '{mfile_id}';")
    con.commit()
    con.close()
    return 1