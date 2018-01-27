#4.1 function calls
print type(32)

#4.2 build-in functions
print max('Hello World')
print min('Hello World')
print len('Hello World')

#4.3 Type conversion functions
print int(3.99)
print int(-2.3)
print float('3.1324')
print str(32)

#4.4 random numbers
import random
for i in range(10):
    x = random.random()
    print x


#exe 4.1
print random
print random.randint(5,10)
t = [1,2,3]
print random.choice(t)


#4.5 math
import math
print math

degrees = 5
radians = degrees/ 360.0*2*math.pi
print math.sin(radians)
print math.sqrt(2)/2.0

#4.6 adding new functions
def print_lyrics():
    print "'I'm a lumberjack , and I'm ok'"
    print 'I sleep all night and I work all day.'

print print_lyrics
print type(print_lyrics)


#4.7 definitions and uses

def print_repeat_lyrics():
    print_lyrics()
    print_lyrics()



#4.9 parameters and arguments
def print_twice(bruce):
    print bruce
    print bruce


print_twice(21)

#4.10 frutiful functions and void functions
result = print_twice('hello')
print result #None

print math.cos(radians)


def addtwo(a,b):
    added = a+b
    return added

x = addtwo(3,5)
print x