import Student as std

def main():
	
	u=std.user()
	
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
			std.userdao.insert(u)
		
		elif(choice ==2):#upadate according to email

			email=raw_input("Please Enter your Mail Id")
			u.email=email
			u=std.userdao.search(u.email)	
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

			print "******************************"
			print u.name, u.age, u.email
			print "*******************************"

			std.userdao.update(u,email)
			

		elif(choice == 3):
			std.userdao.viewall()
			
		elif(choice ==4):
			u.email=raw_input("Enter email id: ")
			std.userdao.search(u.email)
			
		elif(choice ==5):
			u.email=raw_input("Enter email id: ")
			std.userdao.delete(u.email)

		else:
			print "please enter the valid choice"

		val =raw_input("Do you want to continue? press 'Y' else press 'N': ")


if __name__ == '__main__':
	
	main()