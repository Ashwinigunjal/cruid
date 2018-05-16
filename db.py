import MySQLdb
db=MySQLdb.connect("localhost","root","","Student")


cursor=db.cursor()


sql="select * from std4"

try:
	cursor.execute(sql)
	

	# print "Total row",cursor.rowcount

	result=cursor.fetchall()

	for row in result:
		idd=row[0]
		name=row[1]
		print "id=%d,name=%s" %(idd,name)



except:
	print db.rollback()

db.close()