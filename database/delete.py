import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)
mycursor=mydb.cursor()
mycursor.execute("Delete from login where name_id=4") 
mydb.commit()