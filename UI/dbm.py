import pymysql as p

def connect():
    return p.connect(host="localhost", user="root", password='oracle',database="SwiftSynK", port=3306)

def getFolders():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM folder")
    data=cur.fetchall()
    con.close()
    print(data)
    return data

def syncFile(file_id, file_path, ):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM folder")
    data=cur.fetchall()
    con.close()
    print(data)
    return data
