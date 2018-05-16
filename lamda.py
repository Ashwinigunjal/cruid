f=lambda x,y: x+y
f1=lambda x,y: x-y

f2=lambda x,y: x*y
f3=lambda x,y: x%y



print (f(2,4))
print (f1(2,4))
print (f2(2,4))
print (f3(2,4))


print "************map******************"

t=[1,2,3,4,5,6,7,8,9]
def fune(l):
	l1=[]
	if l%2==0:

		l1.append(l)

	return l1


list=map(fune,t)

print list


print "**************filter*************"

result=filter(lambda x: x%2,range(1,12))
print result

res=reduce(lambda x,y : x+y,result)
print res