import re

# str= "123 12345 12345 12345"
# p=re.compile('\s')
# ll=p.split(str)

# print ll

# for i in ll:
# 	l1=re.findall('\d',i)
# 	print "*******************"
# 	print l1
# 	for j in l1:
# 		l2=re.findall('[2-3]',j)
# 		if(l2):
# 			print "find 2 ,3"
# 		

# pattern="[\w._%+-]{5,10}@[\w.]{2,20}com"
# str="ashwiniz@gmail.com"

# ll=re.findall(pattern,str)

# print ll

# str="@ hello python developer do you know how"

# regex=re.compile(r"[^@\s]+.")

# ll=re.findall(regex,str)

# for i in ll:

# data="this is ashwini@gmail.com mail personal and official is gunjal@1gmail.com"

# p=re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+',data)

# for i in p:
# 	print i
# phone="99-212-60-414"

# regex=re.compile(r"([\d]{2})-([\d]{3}-[\d]{2}-[\d]{3})")

# data=re.sub(regex,r"(\1)\2",phone)


# print data


# str="1234 1234-3456 2345-5678 3456"

# p=re.compile(r"(\d{4}-\d{4}|\d{4})+")

# s=re.findall(p,str)

# print s


str="ashwini@gmail.com ashwini@gmail.com ashwini@gmail.com"

p=re.compile(r'^[a-zA-Z0-9-+.!]\w+@[a-zA-Z0-9-+.!]\w+\.[a-zA-Z0-9]\w+.+')

q=re.findall(p,str)
print q
