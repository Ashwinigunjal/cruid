class roomtemp:

	def __init__(self,temp=0):
		self.__temp=temp
		print "I am in constructor"
		print type(self.__temp)

	def showtemp(self):
		print "Current room temperature : ",self.__temp

	def gettemp(self):
		print "I am in get methode"
		print self.__temp
		return self.__temp

	def settemp(self,temp):
		print "I am in set methode"
		self.__temp=temp


def main():
	rm=roomtemp()
	rm.settemp(22)

	rm.gettemp()
	rm.showtemp()
	print "#####################"
	print rm.__dict__

	print "#####################"

if __name__ == '__main__':
	main()

