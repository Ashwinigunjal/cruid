import MySQLdb

print "*********welcome user***********"

db=MySQLdb.connect("localhost","root","password","Number")
cursor=db.cursor()

while(1):
	try:
		number=raw_input("Enter number: ")
		sql="select word from num_list where number='%s'"%(number)
		cursor.execute(sql)
		result=cursor.fetchone()
		print result[0]
	except :
		print "data not present"
	# val=raw_input("Do you want to exit? press Y or y")



