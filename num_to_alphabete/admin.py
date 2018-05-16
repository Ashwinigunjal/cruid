import MySQLdb

val=0
print "********Login*************"
name=raw_input("Enter password: ")
password=raw_input("Enter password: ")

db= MySQLdb.connect("localhost","root","password","Number")
cursor=db.cursor()


if(name =='admin' and password =='admin'):


	while(1):

		number=input("Enter number: ")
		word=raw_input("Enter alphabet: ")

		# sql="insert into num_list(number,word)values(%d,%s)"% (number,word)
		sql="insert into num_list(number,word)values('%d','%s')"%(number,word)
		cursor.execute(sql)

		db.commit()

		# val=raw_input("Do you want to exit? press Y or y else press n")

else:
	print "invalid password"








