
import MySQLdb

val=0
print "********Login*************"
name=raw_input("Enter password")
password=raw_input("Enter password")

connect=new MySQLdb("localhost","root","password","Number")
cursor=new cursor()


if(name == 'admin' and password == 'admin' ):


	while(val==('y' or 'Y' )):

		number=raw_input("Enter number")
		word=raw_input("Enter alphabet")

		sql="insert into num_list(number,word)values(%d,%s)"% number,word
		cursor.execute(sql)

		val=raw_input("Do you want to exit? press Y or y")










