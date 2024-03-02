import pymysql as p

def connect():
    return p.connect(host="localhost", user="root", password='oracle',db="SwiftSynK", port=3306)

def checkLogin(email, password):
    con = connect()
    cur = con.cursor()
    print(email)
    try:
        cur.execute("SELECT password FROM user where username='{email}';".format(email=email))
        data=cur.fetchall()
        con.close()
        print("SELECT password FROM user where username='{email}';".format(email=email))
        print(data)
        if(len(data)==0):
            return 1
        elif(data[0][0]==password):
            return 0
        else:
            return 2
    except:
        con.close()
        return 3
    return 4

def is_folder_already_added(path):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM folder where folder_path='{folder_path}';".format(folder_path=path))
        data=cur.fetchall()
        con.close()
        print(data)
        if(len(data)==0):
            return False
        return True
    except:
        con.close()
        return False
    return False

def file_already_added(path):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM file where filepath='{filepath}';".format(filepath=path))
        data=cur.fetchall()
        con.close()
        print(data)
        if(len(data)==0):
            return False
        return True
    except:
        con.close()
        return False
    return False

def providePaths(base_folder_id, email):
    con=connect()
    cur=con.cursor()
    data=[[], []]
    try:
        cur.execute("select folder_path from folder where email='{email}'and folder_path not in ('Base');".format(email=email))
        data1=cur.fetchall()
        print(data1)
        con.close()
    except Exception as e:
        print(e)
        con.close()
        print("select folder_path from folder where email='{email}'and folder_path not in ('Base');".format(email=email))
        print("Error to get folders")
        return data
    
    con=connect()
    cur=con.cursor()
    try:
        cur.execute("select filepath from file where folder_id='{base_folder_id}';".format(base_folder_id=base_folder_id))
        data2=cur.fetchall()
        print(data2)
        con.close()
    except Exception as e:
        print(e)
        con.close()
        print("select filepath from file where folder_id='{base_folder_id}';".format(base_folder_id=base_folder_id))
        print("Error to get files")
        return data

    for i in data1:
        data[0].append(i[0])
    for i in data2:
        data[1].append(i[0])
    return data

def getFolders():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM folder;")
    data=cur.fetchall()
    con.commit()
    con.close()
    print(data)
    return data

def getFiles():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM file;")
    data=cur.fetchall()
    con.commit()
    con.close()
    print(data)
    return data

def getUsers():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM user;")
    data=cur.fetchall()
    con.commit()
    con.close()
    print(data)
    return data

def insertUser(email,password,username,folder_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into user (Email,password,Username,base_folder_id) values ('{email}','{password}','{username}','{folder_id}');".format(email=email, password=password, username=username, folder_id=folder_id))
    con.commit()
    con.close()
    return 1

def insertFolder(folder_id,folder_path,email):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into folder (folder_id,folder_path,Email) values ('{folder_id}','{folder_path}','{email}');".format(folder_id=folder_id, folder_path=folder_path, email=email))
    con.commit()
    con.close()
    return 1

def insertFile(file_id,filepath,upload_time,folder_id,status):
    con = connect()
    cur = con.cursor()
    cur.execute("Insert into file (file_id,filepath,upload_time,folder_id,Status) values ('{file_id}','{filepath}','{upload_time}','{folder_id}','{status}');".format(file_id=file_id, filepath=filepath, upload_time=upload_time, folder_id=folder_id, status=status))
    con.commit()
    con.close()
    return 1

def deleteUser(dEmail):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("Delete from User where Email = '{dEmail}';".format(dEmail=dEmail))
        con.commit()
    except:
        con.close()
        return 0
    con.close()
    return 1

def deleteFolder(dFolder_id):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("Delete from file where folder_id = '{dFolder_id}';".format(dFolder_id=dFolder_id))
        try:
            cur.execute("Delete from folder where folder_id = '{dFolder_id}';".format(dFolder_id=dFolder_id))
            con.commit()
            con.close()
            return 1
        except Exception as e:
            print("error occured")
            print(e)
            con.close()
            return 0
    except:
        print("error occured")
        print(e)
        con.close()
        return 0

def deleteFile(dFile_id):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute("Delete from file where file_id = '{dFile_id}';".format(dFile_id=dFile_id))
        con.commit()
        con.close()
        return 1
    except Exception as e:
        print(e)
        con.close()
        return 0

def modifyUser(mpassword,mUsername,memail):
    con = connect()
    cur = con.cursor()
    cur.execute("Update User set password ='{mpassword}', Username = '{mUsername}' where email = '{memail}';".format(mpassword=mpassword, mUsername=mUsername, memail=memail))
    con.commit()
    con.close()
    return 1

def modifyFolder(mfolder_path,mfolder_id):
    con = connect()
    cur = con.cursor()
    cur.execute("Update folder set folder_path = '{mfolder_path}' where folder_id = '{mfolder_id}';".format(mfolder_id=mfolder_id, mfolder_path=mfolder_path))
    con.commit()
    con.close()
    return 1

def modifyFile(mfilepath,mfile_id,mupload_time,mStatus):
    con = connect()
    cur = con.cursor()
    cur.execute("Update file set filepath = '{mfilepath}', upload_time = '{mupload_time}', Status = '{mStatus}' where file_id = '{mfile_id}';".format(mfilepath=mfilepath, mupload_time=mupload_time, mStatus=mStatus))
    con.commit()
    con.close()
    return 1