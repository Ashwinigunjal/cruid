from userdao import *
class user:
	# name, age , email
	def __init__(self,name="null",age=0,email=0):
		self.name=name
		self.age = age
		self.email=email
		print "I am in constructor"

	@property
	def name(self):
		print "I am in get methode"
		return self.__name

	@name.setter
	def name(self,name):
		print "I am in set method"
		self.__name=name


	@property
	def age(self):
		print "I am in get methode"
		return self.__age

	@age.setter
	def age(self,age):
		print "I am in set method"
		self.__age=age


	@property
	def email(self):
		print "I am in get methode"
		return self.__email

	@name.setter
	def email(self,email):
		print "I am in set method"
		self.__email=email

	@staticmethod
	def display():
		print "This display method in  user"

#//***********************************************************************

