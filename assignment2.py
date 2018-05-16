# priblem1
s="Django"

print s[0]
print s[-1]
print "//////////////"
print s[:1]
print s[5:]
print s[0:4]
print s[1:4]
print s[4:]

print "/////////////"

print s[::-1]
#problem 2

ll=[3,7,[1,2,"hello"]]

print ll

ll[2][2]="Good Bye"

print ll


# ////problem 3

d1={"simple key":"hello"}
d2={'k1':{'k2':"hello"}}
d3={'k1':[{'nest_key':["this is deep","hello"]}]}

print d1["simple key"]
print d2['k1']['k2']
print d3['k1'][0]['nest_key'][1]
