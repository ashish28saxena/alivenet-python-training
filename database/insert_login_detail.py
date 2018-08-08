import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject")
sql="insert into user_login_detail(user_id,user_fname,user_lname,address,pincode,state,city) value(%s,%s,%s,%s,%s,%s,%s)"
val=[
	('5','manoj','kumar','a 36 sector 55','25001','up','meerut'),
	('7','ashish','saxena','a 36 sector 55','25001','up','meerut'),
	('8','ashish','kumar','a 36 sector 55','25001','up','meerut'),
	('9','sachin','kumar','a 36 sector 55','25001','up','meerut'),
	('10','mohit','saxena','a 36 sector 55','25001','up','meerut'),
	('11','ankit','soni','a 36 sector 55','25001','up','meerut'),
	('12','kushal','kumar','a 36 sector 55','25001','up','meerut'),
	('13','narendra','kumar','a 36 sector 55','25001','up','meerut'),
	]
mycursor=mydb.cursor()	
mycursor.executemany(sql,val)
mydb.commit()	