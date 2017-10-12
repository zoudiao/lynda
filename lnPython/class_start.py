#basic class
class myClass():
    #self arguments refers to the object itself
    def method1(self):
        print "myClass method1"

    def method2(self, someString):
        print "myClass method2:" + someString

#inheriating myClass ????
class anotherClass(myClass):
    def method2(self):
        print "anotherClass method2"

    def method1(self):
        myClass.method1(self);
        print "anotherClass method1"

#exercise the class methods
def main():
    c = myClass()
    c.method1()
    c.method2("this is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()

if __name__ == '__main__':
    main()