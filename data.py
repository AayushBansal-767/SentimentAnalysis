import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="sentiment"
)

if mydb:
	print("yes")
mycursor = mydb.cursor()
sql="insert into review(name,review,result) values(%s,%s,%s)"

mycursor.execute(sql,("aa","ss","ss"))

mydb.commit()


'''

mycursor.execute("select * from review")
r=mycursor.fetchall()
for i in r:
	print(i)'''