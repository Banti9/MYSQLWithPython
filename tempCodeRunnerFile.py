import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="update  books set title='CPP' where book_id in (2,5)"
# tuple=(1,"Python3", 349.50)
cur.executemany(s)
con.commit()