import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)

sql= "UPDATE login SET name = 'manoj' WHERE name_id = '5'"
mycursor=mydb.cursor()
mycursor.execute(sql) 
mydb.commit()