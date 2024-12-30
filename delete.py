import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s=" delete from  books  where book_id in (10,11,12,13,14,15,16,17)"
cur.execute(s)
con.commit()