#@@@@@@@@@@Encapsulation@@@@@@@@@@@@@@@@@22


class A:

	def __init__(self):
		self.A="ashu"
		self.__B="gunjal"

	def display(self):
		print self.A ,self.__B


    	

a=A()
print"@@@@@@@@@@@"

class B:

	def method1(self):
		print "you can see me"

	def __method2(self):
		print "you can not see me"


b=B()

b.method1()
b.__method2()