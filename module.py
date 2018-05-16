import  MySQLdb
class module:
	host="localhost"
	user="root"
	password="root"
	db="Student"

	@staticmethod
	def connection():

		# print module.host
		# print module.user
		# print module.password
		# print module.db
		conn =MySQLdb.connect(module.host,module.user,module.password,module.db)
		cursor=conn.cursor()
		print "val of conn : ",conn
		print "val of cursor: ",cursor
		cursor.execute("Select version()")
		data=cursor.fetchone()
		# print "Database version is % s"%data
		cursor.close()
		


	@staticmethod
	def static():
		print "I am in static method"
		
		return 1
	
		
	def details(self):
		print "I am in Ashwini Gunjal. I always belive on think position , make positive !!!!!I"