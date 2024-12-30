import mysql.connector
con=mysql.connector.connect(host="localhost",
     user="root",
    password="password" ,
     database="DB1")

cur=con.cursor()
s="insert into books(book_id,title, price) value(%s,%s,%s)"
# tuple=[(2,"Java", 899.50),(2,"Java", 899.50)]

# Create a cursor object
cur = con.cursor()

# SQL query for inserting data
s = "INSERT INTO books(book_id, title, price) VALUES (%s, %s, %s)"

# IT-related books data
data = [
    
    (21, "PHP", 599.75),
    (23, "Node.js", 699.80),
    (24, "React.js", 499.90),
    (25, "Web Development", 399.60),
    (26, "JavaScript", 549.99),
    (27, "Python", 899.99),
    (28, "PHP and MySQL", 749.99),
    (29, "Full Stack Development", 649.99),
    (30, "Java", 799.50),
]



# tuple= [(i, f"Book_{i}", 500.00 + i) for i in range(1, 21)]
cur.executemany(s,data)
con.commit()