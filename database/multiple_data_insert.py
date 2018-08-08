import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)
mycursor=mydb.cursor()

sql="insert into login(name,address,password,user_name) value(%s,%s,%s,%s)"
val=[
	('ankit','a 38 sector 55','test123','ankit'),
	('kushal','a 38 sector 56','test1234','kushal'),
	('narendra','acc city','test123477','narendra'),
	]
	
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was insert")