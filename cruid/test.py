import db

val=0

print "Welcome to AVCOE record book"
username=raw_input("Enter your username: ")
admin=raw_input("Enter you password: ")
db.db_connect()
if(username =="admin" and admin =="admin"):
	while(val !=7):
		print "***********************user choice **************************8"
		print "\t\t\t1.create new list \n\t\t\t2.add record \n\t\t\t3.display record \n\t\t\t4.search by id \n\t\t\t5.del data \n\t\t\t6.edit data \n\t\t\t7.exit"

		try:
			val=input("Enter your choice: ")
	 	except NameError:
	 		print "please enter only number input between 1-6"

	 	if(val>=7):
	 		print "please enter value 1-6"

	 	else:
	 		if(val==1):
	 			print "create table"
	 			table_name=raw_input("enter table name: ")
	 			db.create_table(table_name)

	 		elif(val==2):
	 			
	 			name=raw_input("Enter name: ")
	 			place=raw_input("Enter your place: ")
	 			mobile_no=raw_input("Enter mobile number: ")
	 			year=raw_input("Enter year: ")
	 			branch=raw_input("Enter your branch: ")
	 			db.insert_table(name,place,mobile_no,year,branch)
	 			print "add record"

	 		elif(val==3):
	 			print "display record"
	 			db.display_data()

	 		elif(val==4):
	 			print "search data"
	 			idd=input("Enter user id: ")
	 			db.search_by_id(idd)


	 		elif(val==5):
	 			print "del data by id"
	 			idd=input("Enter user id: ")
	 			db.delete_data(idd)

	 		elif(val==6):
	 			print "edit data"
	 		
	 		else:
	 			pass


else:
	print "***********wrong username and password*************88"
