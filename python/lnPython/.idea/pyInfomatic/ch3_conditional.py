#3.1 boolean expressions
print (5==5)
print (5==6)
x = 5
y=6
#<,>,<=,>=,!=,is , is not
print (5 is 6)
print (5 is not 6)

#3.2 logical operators
#and , or , not
print (17 and True)
print (17 or false)
print not 17
print not True

#3.3 conditional execution
if x >0 :
    print 'x is positive'

#3.4 alternative execution
if x%2 ==0:
    print 'x is even'
else:
    print 'x is odd'

#3.5 chained conditionals
if x<y:
    print 'x is less than y'
elif x>y:
    print 'x is greater than y'
elif x==y:
    print 'x is equals y'

#nested conditionals
if x==y:
    print 'x and y are equal'
else:
    if x<y:
        print 'x is less than y'
    else:
        print 'x is greater than y'

#3.7 Catching exceptions using
inp = raw_input('Enter Fahrenheit Temperature:')
fahr = float(inp)
cel = (fahr - 32.0)*5.0/9.0
print cel

# if it goes wrong in try it will go to except
inp = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0)*5.0/9.0
    print cel
except:
    print 'Please enter a number'

#3.8 Short-circuit evaluation of logical expressions
x = 6
y = 2
print x>=2 and (x/y)>2