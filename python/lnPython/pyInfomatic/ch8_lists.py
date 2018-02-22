#8.1 A list is a sequence
print [10,20,30,40]
print ['crunchy frog','ram blandder','lark vomit']
print ['spam',2.0,5,[10,20]]


#8.2 Lists are mutable
numbers = [17,23]
numbers[1] = 5
print numbers

cheeses = ['Cheddar', 'Edam', 'Gouda']
print 'Edam' in cheeses
print 'Brif' in cheeses

#8.3 Traversing a list
for cheese in cheeses:
    print cheese

for i in range(len(numbers)):
    numbers[i] = numbers[i] *2
    print numbers[i]

j=0
if j < len(numbers):
    numbers[j] = numbers[j] *3
    j=j+1
    print numbers[j]


#8.4 List operations
a = [1,2,3]
b = [4,5,6]
print a+b

print [1]*3
print ['a','b','c'] *3

#8.5 List slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[1:3] #[b,c]
print t[:4]#['a', 'b', 'c', 'd']
print t[3:]#['d', 'e', 'f']
print t[:]

#replace
t[1:3] = ['x', 'y']
print t

#8.6 List methods
t.append('g')
print t

t2= ['h','i']
t.extend(t2)
print t

t.sort()

print t

#8.7 Deleting elements
x = t.pop(4)
print x
print t

del t[2]
print t

t.remove('y')
print t

del t[1:3]
print t

#8.8 Lists and functions
nums = [3, 41, 12, 9, 74, 15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)



total = 0
count = 0
while ( True ) :
    inp = raw_input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
    print 'Average:', average


numlist = list()
while ( True ) :
    inp = raw_input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    average = sum(numlist) / len(numlist)
    print 'Average:', average


#8.9 Lists and strings
s = 'spam'
t = list(s)
print t

s = 'pining for the fjords'
t = s.split()
print t

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
print s

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)
print t

#8.10 Parsing lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print words[2]

#8.11 Objects and values
a = 'banana'
b = 'banana'
print a is b #a and b is identical

a = [1,2,3]
b = [1,2,3]
print a is b # a and b is equivalent

#8.12 Aliasing
a = [1,2,3]
b = a
print b is a

#8.13 List arguments
def delete_head(t):
    del t[0]

letters = ['a','b','c']
delete_head(letters)
print letters


