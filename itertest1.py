class A:
	str="ashwini"

	tt=iter(str)
	print next(tt)
	print next(tt)
	print next(tt)
	print next(tt)


class B:
	def __init__(self,name):
		self.name=name
		print next(self.name)


	def __iter__():
		return self

	def next(self):
		len=length(self.name)
		if(self.index > len -1 ):
			raise StopIteration
		else:
			return self.name[self.index]

def main():
	b =B(12)


if __name__ == '__main__':
	main()