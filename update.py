import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="update  books set title='Data Structure' where book_id in (4,3,7)"
# tuple=(1,"Python3", 349.50)
cur.execute(s)
con.commit()