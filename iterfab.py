class fabonaci:

	def __init__(self,iLast=1,iSecondLast=0,iMax=50):
		self.iLast = iLast 
		self.iSecondLast = iSecondLast
		self.iMax = iMax  #cutoff


	def __iter__(self):
		return(self)

	def next(self):
		val = self.iLast + self.iSecondLast
		if self.iSecondLast >= self.iMax:
			raise StopIteration()

		self.iSecondLast = self.iLast
		self.iLast = val
		
		
		
		
		return val

def main():
	fb=fabonaci()
	print ("*******************")
	print fb.__dict__
	print ("*******************")

	for i in fb:
		print i
		print fb.__dict__


main()
	

