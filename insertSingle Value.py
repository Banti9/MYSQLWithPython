import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="insert into books(book_id,title, price) value(%s,%s,%s)"
tuple=(1,"Python3", 349.50)
cur.execute(s,tuple)
con.commit()