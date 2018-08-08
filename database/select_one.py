import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject")

mycursor=mydb.cursor();
mycursor.execute("select count(name_id) from login where name_id=4")
result=mycursor.fetchall()
print(result);