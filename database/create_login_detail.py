import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)
sql="create table user_login_detail(id integer auto_increment primary key ,user_id integer,user_fname varchar(255),user_lname varchar(255),address varchar(255),pincode varchar(255),state varchar(255),city varchar(255))"
mycursor=mydb.cursor() 
mycursor.execute(sql) 
mydb.commit()