#6.1 A string is a sequence
fruit = 'banana'
letter = fruit[1]
print letter
index = 0
length = len(fruit)

#6.2 Getting the length of a string using len
#6.3 Traversal through a string with a loop
while index < length:
    letter = fruit[index]
    index = index +1
    print letter


for char in fruit:
    print char
#Exercise 6.1 Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on
#a separate line, except backwards.
index = length
while index > 0:
    letter = fruit[index-1]
    index = index -1
    print 'index:',index,',letter:',letter

#6.4 String slices
print 'letter of fruit 3-5:',fruit[3:5]
print 'letter of fruit 0-3:',fruit[:3]
print 'letter of fruit 3-:',fruit[3:]
print 'letter of fruit 3-3:',fruit[3:3]
#Exercise 6.2 Given that fruit is a string, what does fruit[:] mean?
print 'what does it mean:', fruit[:]

#6.5 Strings are immutable
greeting = 'Hellow,World'
#greeting[0] = 'J'

#TypeError: 'str' object does not support item assignment
new_greeting = 'J' + greeting[1:]
print new_greeting


#6.6 Looping and counting
count = 0
word = 'banana'
for letter in word:
    if letter is 'a':
        count = count+1
print count

#Exercise 6.3 Encapsulate this code in a function named count, and generalize it
#so that it accepts the string and the letter as arguments.

def count(letter,word):
    count = 0
    for l in word:
        if l is letter:
            count = count +1
    return count

print count('n','banana')

#6.7 The in operator
print 'a' in 'banana'
print 'seed' in 'banana'


#6.8 String comparison
word = 'Pineapple'
if word == 'banana':
    print 'All right, bananas.'
if word < 'banana':
    print 'Your word,' + word + ', comes before banana.'
elif word > 'banana':
    print 'Your word,' + word + ', comes after banana.'
else:
    print 'All right, bananas.'

#6.9 string methods
stuff = 'Hello world'
print type(stuff)
#print dir(stuff)
print stuff.upper()
index = stuff.find('e')
print index

line = ' Here We Go   '
print line.strip()

#Exercise 6.4 There is a string method called count that is similar to the function
#in the previous exercise. Read the documentation of this method at https://
#docs.python.org/2/library/stdtypes.html#string-methods and write an
#invocation that counts the number of times the letter a occurs in 'banana'.

#6.10 Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1:sppos]
print host

#6.11 Format operator
camels = 42
print 'I have spotted %d camels.' % camels
print 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

#print '%d %d %d' % (1, 2) #TypeError: not enough arguments for format string

#Exercise 6.5 Take the following Python code that stores a string:‘
#str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string after the colon
#character and then use the float function to convert the extracted string into a
#floating point number.


#Exercise 6.6 Read the documentation of the string methods at https://docs.
#python.org/2/library/stdtypes.html#string-methods. You might want
#to experiment with some of them to make sure you understand how they work.
#strip and replace are particularly useful.