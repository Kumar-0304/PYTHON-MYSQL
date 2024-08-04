import mysql.connector
print("hii")
mydb=mysql.connector.connect(host='localhost',user='root',password='kumar123',database='demo11')
print("connected")
mycursor=mydb.cursor()
#mycursor.execute("create database demo11")
#print("database created")
#mycursor.execute("create table s2(name varchar(20),lname varchar(20))")
#mycursor.execute("show tables")
#for x in mycursor:
 #   print(x)
#row="insert into s2 values(%s,%s)"
#values=("kumar","raja")
#mycursor.execute(row,values)
#mydb.commit()
mycursor.execute("select *from s2")
result=mycursor.fetchall()
for x in result:
    print(x)
   