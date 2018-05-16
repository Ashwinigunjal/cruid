import MySQLdb

from prettytable import PrettyTable

# def db_connect():
# 	db=MySQLdb.connect("localhost","root","password","test2")
# 	return db;

# def display_info():
# 	db1=db_connect()
# 	cursor=db1.cursor()
# 	sql="""select * from  std_info"""
# 	try:
# 		cursor.execute(sql)
# 		results=cursor.fetchall()
# 		for  row in results:
# 			idd=row[0]
# 			name=row[1]
# 			fname=row[2]
# 			lname=row[3]
# 			place=row[4]
# 			mobile_no=row[5]
# 			birthdate=row[6]
			

# 			print "%d,%s,%s,%s,%s,%s,%s"%\
# 			(idd,name,place,mobile_no,year,branch)
# 	except:
# 		print "unable to fetch data"

# 		db1.close()

# //////////////////////////////////////////////////////////
db=MySQLdb.connect("localhost","root","password","test2")

cursor=db.cursor()
sql="select id,name,fname,lname, place,mobile_no,birthdate from  std_info"
t = PrettyTable(['id', 'Name','FName','Lname','place','mobile'])
try:
	cursor.execute(sql)
	results=cursor.fetchall()

	for row in results:
		idd=row[0]
		name=row[1]
		fname=row[2]
		lname=row[3]
		place=row[4]
		mobile_no=row[5]
		
		
		t.add_row([idd, name,fname,lname,place,mobile_no])

		print "%d | %s | %s | %s | %s | %s"%\
		(idd,name,fname,lname,place,mobile_no)
except:
	print "unable to fetch data"

print t;
db.close()



