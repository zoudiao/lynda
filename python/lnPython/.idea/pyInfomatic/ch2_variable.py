##2.1 values and types
type('Hello World!')
type(17)
type(3.2)
#python interprets 1,000,000 as a comma-seperated sequence of integers
#print 1,000,000 ##not support in Python 3

##2.2 variables
message = 'and now for'
n = 17
pi = 3.1415926
print (message)
print (n)
print (pi)
type(message)
type(n)
type(pi)

##2.3 variable names and keywords

##2.4 statements : print and assignment
print (1)
x = 2
print (x)

##2.5 operators and operands
minute = 60
print (59/minute) ## in Python 3 is fload division

##2.6 expressions : combinition of values , variables , operators
5
x = 5
print x+5

##2.7 order of operators
##Parentheses (), Exponentiation ** , Multiplication * , Division /, Addition +, Substraction -

##2.8 modulus operator
quotient = 7/3
print quotient
remainder = 7%3
print remainder

##2.9 string operations : concatenation
first =10
second =15
print first + second
first ='100'
second ='200'
print first+second

##2.10 asking the user for input
#input = raw_input()
#print input
# name = raw_input('what is your name?\n')
# print name

# prompt = 'What..is the airspeed velocity of an unladen swallow?\n'
# speed = raw_input(prompt)
# print int(speed)
# print int(speed)+5

##2.11 comments
##2.12 choosing mnemonic variable name (memory aid)
##2.13 debugging
##2.14 glossary
##2.15 exercises
# exe 2.2
#prompt = 'Enter your name: \n'
#name = raw_input(prompt)
#print 'Hello ' + name


#exe 2.3
# promt_hours = 'Enter Hours: \n'
# promt_rate = 'Enter Rate: \n'
# hours = raw_input(promt_hours)
# rate = raw_input(promt_rate)
# pay = int(hours) * float(rate)
# print 'Pay: ' +str(pay)pay

#exe 2.4
width = 17
height = 12.0
print width/2
print width/2.0
print height/3
print 1+2*5

#exe 2.5 convert Celsius temperature to Fahrenheit C= (F-32)/1.8, F=1.8*C +32
promt = 'What is current Celsius? \n'
celsius = raw_input(promt)
fahrenheit = 1.8*int(celsius) +32
print 'The Fahrenheit is :' +str(fahrenheit)
