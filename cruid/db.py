import MySQLdb
db=""
sql=""
cursor=""
table="student"
def db_connect():
	db=MySQLdb.connect("localhost","root","","Student")
	return db;
	

def create_table(table_name):
	db1=db_connect()
	cursor=db1.cursor()

	sql="""create table (id int(10) auto_increment,
							  name varchar(30),
							  place varchar(30),
							  mobile_no varchar(12),
							  year varchar(5),
							  branch varchar(20),
							  primary key(id))"""

	cursor.execute(sql)
	print "table create successfully"
	db1.close()


def insert_table(name,place,mobile_no,year,branch):
	db1=db_connect()
	cursor=db1.cursor()
	# sql="""insert into student5(name,place,mobile_no,year,branch)
	# 		values("ashu","sangamner","99999999","2015","electronics")"""
	sql="insert into student5(name,place,mobile_no,year,branch)\
	 	   values('%s','%s','%s','%s','%s')"%(name,place,mobile_no,year,branch)

	cursor.execute(sql)
	db1.commit()
	print "insert record successfully"
	db1.close()

def update_table(place,mobile_no,year,branch):
	one=place
	two=mobile_no
	three=year
	four=branch
	db1=db_connect()
	cursor=db1.cursor()
	sql="""update student5 set mobile_no="9423386825" where id=1"""
	cursor.execute(sql)
	db1.commit()
	db1.close()


def delete_data(idd):
	db1=db_connect()
	cursor=db1.cursor()
	sql="delete from student5 where id=%s"%(idd)
	cursor.execute(sql)
	db1.commit()
	db1.close()

def search_by_id(idd):
	db1=db_connect()
	cursor=db1.cursor()
	sql="select * from student5 where id=%s"%(idd)
	cursor.execute(sql)
	data=cursor.fetchone()
	print data
	db1.commit()
	db1.close()

def display_data():
	db1=db_connect()
	cursor=db1.cursor()
	sql="""select * from  student5"""
	try:
		cursor.execute(sql)
		results=cursor.fetchall()
		for  row in results:
			idd=row[0]
			name=row[1]
			place=row[2]
			mobile_no=row[3]
			year=row[4]
			branch=row[5]

			print "%d,%s,%s,%s,%s,%s"%\
			(idd,name,place,mobile_no,year,branch)
	except:
		print "unable to fetch data"

		db1.close()


