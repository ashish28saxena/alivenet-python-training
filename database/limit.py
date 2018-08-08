import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject")
sql="select * from login  LIMIT 5 OFFSET 0"
mycursor=mydb.cursor()
mycursor.execute(sql)
result=mycursor.fetchall()
print(result)