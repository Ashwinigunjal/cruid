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

#//***********************************************************************

def main():
	
	u=user()
	
	val='Y'
	while (val =='Y'):
		print "*****Enter Your Choice******\n\t1. Insert Data \n\t 2. Upadate Data \n\t 3. Show Details \n\t 4. Search Data \n\t 5. Delete"
		choice = input("Enter your choice: ")
		if(choice ==1):

			name=raw_input("Enter User Name: ")
			age=raw_input("Enter User Age: ")
			email=raw_input("Enter User Mail Id: ")
			u.name=name
			u.age=age
			u.email=email
			userdao.insert(u)
		
		elif(choice ==2):#upadate according to email

			email=raw_input("Please Enter your Mail Id")
			u.email=email
			u=userdao.search(u.email)	
			print "This is You Deails User, Please select what do you want edit"
			data=raw_input("Enter what you want to update: ")
			if(data == 'name'):
				u.name=raw_input("Name : ")

			elif(data =='age'):
				u.age=raw_input("Age: ")

			elif(data =='email'):
				u.email=raw_input("Email: ")

			else:
				print "Invalid data"

			userdao.update(u)
			

		elif(choice == 3):
			userdao.viewall()
			
		elif(choice ==4):
			u.email=raw_input("Enter email id: ")
			userdao.search(u.email)
			
		elif(choice ==5):
			u.email=raw_input("Enter email id: ")
			userdao.delete(u.email)

		else:
			print "please enter the valid choice"

		val =raw_input("Do you want to continue? press 'Y' else press 'N': ")


if __name__ == '__main__':
	main()