import MySQLdb


class Dao:

	def connect_db(self):
		db=MySQLdb.connect("localhost","root","password","book")
		cursor=db.cursor()
		cursor.execute("SELECT VERSION()")
		data=cursor.fetchone()
		print "version: ",data




