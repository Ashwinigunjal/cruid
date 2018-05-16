import re

def A(x=10):
	print "I am function A"
	def B():
		print "I am in function B"
		print x
		print B
		
		return x*2
		print B.__dict__
	return B


def fun1(x,**kwargs):
	
	print "This is kwargs"
	print x
	for k,v in kwargs.items():
		print k,v	


fun1(1,a=1, b=2)
print "*********************************"

# print (re.split(r"[^\S.*]","This is Ashwini gunjal, Now I become a python exper yahuuuuuuu"))

# str="2123 moral of life is simple 2345 if you treat me good then i definately"
# print re.findall(r"(^[0-9]{4})([^0-9])+.*",str)


# fun=A(1)
# fun()


# example of regex flag re.MULTILINE


ss = """abc
def
ghi"""

r1 = re.findall(r"^\w+", ss)
r2 = re.findall(r"^\w+", ss, flags = re.MULTILINE)

print r1                        # ['a']
print r2  


