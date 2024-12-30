import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="create table books(book_id integer(10),title varchar(25), price float(5,2))"
cur.execute(s)
