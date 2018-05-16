class OurClass:

    def __init__(self, a):
        self.OurAtt = a
        print "I am in constructor"

    @property
    def OurAtt(self):
    	print "I am in getter method"
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
    	print "I am in setter method"
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)