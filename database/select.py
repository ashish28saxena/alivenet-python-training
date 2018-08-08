import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)
mycursor=mydb.cursor()
mycursor.execute("select * from login")
result=mycursor.fetchall()
for x in result:
  print(x)