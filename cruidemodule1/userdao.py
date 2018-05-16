import MySQLdb
from view import *

class userdao:
	host="localhost"
	user="root"
	password="root"
	db="Student"


#*********************Connection method*********************************************
	
	@staticmethod
	def connection():

		print userdao.host
		print userdao.user
		print userdao.password
		print userdao.db
		print "*********************************"
		try:
			conn =MySQLdb.connect(userdao.host,userdao.user,userdao.password,userdao.db)
			cursor=conn.cursor()
			# print "val of conn : ",conn
			# print "val of cursor: ",cursor
			cursor.execute("Select version()")
			data=cursor.fetchone()
			print "Database version is % s"%data
			return conn
		except:
			print "unable to connect"
		

#***************************Select Methode*********************************************

	@staticmethod
	def viewall():
		conn=userdao.connection()
		cursor=conn.cursor()
		sql="select * from std "
		cursor.execute(sql)
		result = cursor.fetchall()
		if(len(result)>0):
			print "row insert successfully"
		else:
			"Unable to fetch record"
		print "------------------------------------------------------------------------------------"
		print "| Id   |\tName\t|\tAge\t|\tEmail\t\t\t\t   |"
		print "------------------------------------------------------------------------------------"
		for col in result:
			id="%s"%col[0]
			name="%s"%col[1]
			age="%s"%col[2]
			email="%s"%col[3]

			print "|"," ",id," "*(2-len(id)),"|","  ",name," "*(15-len(name)),"|","  ",age," "*(9-len(age)),"|","  ",email," "*(30-len(email)),"|"
			# print "\t%d\t|\t%s\t\t|\t%s\t|\t%s\t\t|"%(id,name,age,email)
			print "------------------------------------------------------------------------------------"
		conn.close()

#***************************************Insert Methode***************************************

	@staticmethod
	def insert(obj):
		print "*************start insert method ***************"
		print "I am in insert methode"
		
		conn=userdao.connection()
		cursor=conn.cursor()
		# print conn
		# print cursor
		# print obj.__dict__
		sql="INSERT INTO std (`name`, `age`, `email`) VALUES ('%s', '%s', '%s')"%(obj.name,obj.age,obj.email)
		
		cursor.execute(sql)
		conn.commit()
		
		conn.close()
		print "*************Data Insert Successfully ***************"

#*********************************Update Method*****************************************
	@staticmethod
	def update(obj):
		print "************Edit Data in database**************"
		print "I am in update method"
		print obj.name
		print obj.age
		print obj.email
		conn=userdao.connection()
		cursor=conn.cursor()
		sql="UPDATE std SET name='%s', age='%s', email='%s' WHERE email='%s'"%(obj.name, obj.age, obj.email, obj.email)
		cursor.execute(sql)
		conn.commit()
		conn.close()


#******************************Search By Mail**************************************

	@staticmethod
	def search(email):

		conn=userdao.connection()
		cursor=conn.cursor()
		u=user()
		print conn
		print cursor
		sql="select * from std where email='%s'"%(email)
		cursor.execute(sql)
		result = cursor.fetchall()
		if(len(result)>0):
			print "row insert successfully"
			print "------------------------------------------------------------------------------------"
			print "| Id   |\tName\t|\tAge\t|\tEmail\t\t\t\t   |"
			print "------------------------------------------------------------------------------------"
			for col in result:
			id="%s"%col[0]
			name="%s"%col[1]
			age="%s"%col[2]
			email="%s"%col[3]

			print "|"," ",id," "*(2-len(id)),"|","  ",name," "*(15-len(name)),"|","  ",age," "*(9-len(age)),"|","  ",email," "*(30-len(email)),"|"
			# print "\t%d\t|\t%s\t\t|\t%s\t|\t%s\t\t|"%(id,name,age,email)
			print "------------------------------------------------------------------------------------"
		
		else:
			print "Please Enter Valid details"
		conn.close()

		return u

#*******************************Delete methode*****************************************

	@staticmethod
	def delete(email):

		conn=userdao.connection()
		cursor=conn.cursor()

		sql="DELETE from std where email='%s'"%(email)
		cursor.execute(sql)
		conn.commit()
		conn.close()



#************************************End**************************************************
