import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)

mycursor=mydb.cursor()
mycursor.execute("select * from login order by name_id desc")
result=mycursor.fetchall()
print(result);