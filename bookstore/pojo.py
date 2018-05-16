# import bookstore
from Dao import Dao
class A:
	def __init__(self):
		print "I am in constructor"
		

	def rule(self):
		print "welcome to python bookstore"
		print "1. add Book"
		print "2. delete book"

		val=input("enter your choice")

		if(val==1):
			print "i am in if block"

		elif(val==2):
			print "I am in else block"


		else:
			print "invalid choice"

		


a=A()

a.rule()

d=Dao()
d.connect_db()
