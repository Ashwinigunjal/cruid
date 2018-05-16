class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
        print "I am in Mammals class Constructor"
 
 
    def printMembers(self):
        print('Printing members of the Mammals class')
        for members in self.members:
        	print ('\t %s'%members)
        