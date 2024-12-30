import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="password")


# cursor is method use to return cursor object
cur=con.cursor() 
cur.execute("create database DB1")