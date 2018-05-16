import MySQLdb


def connect_db():

	db=MySQLdb.connect("localhost","root","password","test2")

	cursor=db.cursor()

	cursor.execute("Select version()");
	data = cursor.fetchone()
	db.close()
