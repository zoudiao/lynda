#5.1 updating variables
#x = x+1

#5.2 while statement
n = 5
while n>0:
    print n
    n = n-1
print 'Blastoff!'

#5.3 infinite loops
#5.4 "infinite loops" and break
n = 10
#while True:
#    print n,
#    n = n-1
#print 'Done!'

while True:
    line = raw_input('>')
    if line == 'done':
        break
    print line
print 'Done!'

#5.5 finishing iterations with continue
while True:
    line = raw_input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print 'Done!'

#5.6 definite loop using for
friends = ['Joseph','Grem','Sally']
for friend in friends:
    print 'Happy New Year:',friend
print 'Done!'

#5.7 loop pattern
#5.7.1 Counting and summing loops
count = 0
total = 0
for itervar in [3,41,12,9,74,15]:
    count = count +1
    total = total + itervar
print 'Count:',count,',Total:',total

#5.7.2 Maximum and minimum loops
largest = None
print 'Before:', largest
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
print 'Loop:', itervar, largest
print 'Largest:', largest

smallest = None
print 'Before:', smallest
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
print 'Loop:', itervar, smallest
print 'Smallest:', smallest

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value:
            smallest = value
    return smallest

print min([1,3,5,79,20,100])