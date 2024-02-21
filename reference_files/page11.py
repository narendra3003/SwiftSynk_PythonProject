#####Database connection

import pymysql as p

def connect():
    return p.connect(host="localhost", user="root", password='oracle',database="exp_tracker", port=3306)

      # name of the data base
con = connect()
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = con.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM user")

# print all the first cell of all the rows
for row in cur.fetchall():
    for col in range(len(row)):
        print(row[col])

con.close()



