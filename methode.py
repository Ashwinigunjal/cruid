from module import *

class Test:
	count=0
	__val=10
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print "I am in constructor"
		print Test.count

		Test.count = Test.count +1pip install MySQL-python
		print "after increment"
		print Test.count

	


	@classmethod
	def cls(cls):
		print "I am in cltass methode"
		# print "count : %s"%(count)
		cls.count=10

	def method(self):
		print "I am in class methode"
		print "general methode get end"

		print "value : %s"%(Test.count)
		print "@@@@@@@@@@@@@@@@@@@@"
		print self.name
		print "@@@@@@@@@@@@@@@@@@@@@"
		

def main():

	print module.__dict__
	print "**********start *************"
	m=module()
	print m
	# print "general method in python other package"
	# m.details()
	print "*********Eastablish data connection *******"
	conn=module.connection()
	print conn



if __name__ == '__main__':
	main()