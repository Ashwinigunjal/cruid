import MySQLdb

print "*********welcome user***********"

db=MySQLdb.connect("localhost","root","password","Number")
cursor=db.cursor()

number=raw_input("Enter number: ")

while(1):

	sql="select word from num_list where number=%s"%(number)
	cursor.execute(sql)
	result=cursor.fetchone()
	print result

	# val=raw_input("Do you want to exit? press Y or y")



