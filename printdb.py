import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="select  * from books"

cur.execute(s)
result=cur.fetchall()
for res in result:
    print(res)
# con.commit()