matrix=[[1,2,3],[4,5,6],[7,8,9]]

print matrix[0]
print matrix[1]
print matrix[2]

print "I am printing single row in mattrix"
ll1=[row[0] for row in matrix]
ll2=[row[1] for row in matrix]
ll3=[row[2] for row in matrix]

for row in ll1:

	print row,

print "\n"
for row in ll2:

	print row,

print "\n"
for row in ll3:

	print row,

