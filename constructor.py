class Test:

	def __init__(self,x,y):
		self.a=x+y


	def show(self):
		print "A value is",self.a

t=Test(2,3)

t.show()

print t.x