class A:
		total=20

		def show(self):
			data=30
			print "Total: ",self.total
			print "data: ",data
			print locals()
			print globals()


if __name__ == '__main__':
	obj=A()
	obj.show()
	print "----------------------"
	print locals()
	print globals()
	print "-----------------------"