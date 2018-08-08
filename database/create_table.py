import mysql.connector
mydn=mysql.connector.connect
host="localhost",
user="root",
passwd="",
database="myproject"
)
mycursor=mydn.cursor()
mycursor.execute("create table login(name_id integer auto_increment primary key,name VARCHAR(255), address VARCHAR(255),password varchar(255),user_name varchar(255))")