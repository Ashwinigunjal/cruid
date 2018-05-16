#////////////Problem 1
# count add and even number
even=0
odd=0
l1=[]
l2=[]
ll=[11,22,33,44,55,66,77,88,99]

for i in ll:
	if i%2==0:
		print i
		
		l1.append(i)
		
		# print  "{} is even number" . format(i)
		even = even + 1 

	else:
		print i
		l2.append(i)
		
		# print  "{} is even number".format(i)
		odd = odd + 1

print "total even number: ",even
print "total odd number: ",odd

print l1

print l2


# problem 2 print double char in string

name ="hellobye"

result=""

for char in name:
	result += char*2

print result

#problem 3

str1="ashuaaa"
str2="gunaaa"

if(str1.endswith(str2) or str2.endswith(str1)):
	
	print "welcome"








