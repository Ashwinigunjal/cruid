# import db2

print "welcome to Student portal of AVCOE"

print "press \n 1. display individual record \n 2. display all record"
val=input("please enter your choice")

def information():

	print "1. Student Basic information\n2.Student info with certificate\n3. Student info with sport"
	choice1=input("Enter your choice")

	if choice1==1:
		print "welcome"
		db2.display_info()


	elif choice1==2:
		print "bye"

	elif choice1==3:
		print "heloo woow"



if(val==1):
	print "welcome to python"
	information()


elif(val==2):
	print "bye bye python"
	information()
 
		




