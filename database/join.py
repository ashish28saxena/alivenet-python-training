import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="myproject"
)

mycursor = mydb.cursor()
sql = "SELECT \
  login.name_id AS user_id, \
  user_login_detail.user_fname AS user_fname \
  FROM login \
  INNER JOIN user_login_detail ON login.name_id = user_login_detail.user_id"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)
  