class iterator:
	
	def __init__(self,name):
		print "start constructor"
		self.name=name
		self.index=-1
		print "ending of constructor"

	def __iter__(self):
		print "I am in __iter__ function"
		print self
		return self

	def next(self):
		print "I am in next() method"
		if (self.index >= len(self.name)-1) :

			raise StopIteration

		self.index +=1
		return self.name[self.index]

def main():

	print "*****main start***"
	it=iterator("ashwini")
	for i in it:
		print i
	# print "*****main end***"
	# val=iter("ashhu")
	# print "val is1 ", next(val)
	# # print "iii"
	# print "val is2 ", next(val)
	# print "val is3 ", next(val)
	# print "val is4 ", next(val)
	# print "val is5 ", next(val)




main()

