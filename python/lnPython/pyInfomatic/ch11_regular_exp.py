import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()

    if re.search('^From:',line):
        print line

print "---1--"

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

print "---2--"
#11.1 Character matching in regular expressions
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:',line):
        print line

print "---3--"
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        print line


print "---4--"
#11.2 Extracting data using regular expressions
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
#using a two-character sequence that matches a non-whitespace character (\S).
lst = re.findall('\S+@\S+',s)
print lst

print "---5--"
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #x = re.findall('\S+@\S+',line)
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x)>0:
        print x


#
print "---6--"
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
   # x = re.findall('^X\S*: [0-9.]+',line)
    x = re.findall('^From .* ([0-9][0-9]):',line)
    if len(x)>0:
        print x
    #if re.search('^X\S*: [0-9.]+',line):
        #print line

print "---7--"
#11.4 Escape character
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print y


#Exercise 11.1 Write a simple program to simulate the operation of the grep command
# on Unix. Ask the user to enter a regular expression and count the number of
# lines that matched the regular expression:
# $ python grep.py
# Enter a regular expression: ˆAuthor
# mbox.txt had 1798 lines that matched ˆAuthor
# $ python grep.py
# Enter a regular expression: ˆXmbox.
# txt had 14368 lines that matched ˆX-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$
# Exercise 11.2 Write a program to look for lines of the form
# New Revision: 39772
# and extract the number from each of the lines using a regular expression and the
# findall() method. Compute the average of the numbers and print out the average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259