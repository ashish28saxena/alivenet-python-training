import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)
mycursor=mydb.cursor()
sql = "insert into login(name,address,password,user_name) value(%s, %s,%s, %s)"
val  = ("ashish", "Highway 21",'12345','ashish saxena')

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")