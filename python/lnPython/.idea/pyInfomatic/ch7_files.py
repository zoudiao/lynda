#7.1 Persistence
#7.2 Opening files
fhand = open('mbox.txt')
print fhand

#fhand = open('stuff.txt')
#print fhand

#7.4 Reading files
fhand = open('mbox.txt')
count = 0
#for each line in the file represented by the file handle, add one to the count variable.
for line in fhand:
    count = count + 1
print 'Line Count:', count

fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)

#7.5 Searching through a file
# if the file is too large to read , put them into chunks
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print line


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print line


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:') :
        continue
    # Process our 'interesting' line
    print line

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 :
        continue
    print line


#7.6 Letting the user choose the file name
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
        print 'There were', count, 'subject lines in', fname

#7.7 Using try, except, and open
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print 'There were', count, 'subject lines in', fname


#7.8 Writing files
fout = open('output.txt', 'w')
print fout

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = 'the emblem of our land.\n'
fout.write(line2)

fout.close()



# Exercise 7.1 Write a program to read through a file and print the contents of the
# file (line by line) all in upper case. Executing the program will look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500
# You can download the file from www.py4inf.com/code/mbox-short.txt

# Exercise 7.2 Write a program to prompt for a file name, and then read through
# the file and look for lines of the form:
#     X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.


# Exercise 7.3 Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program (en.wikipedia.org/wiki/
#                                                  Easter_egg_(media)). Modify the program that prompts the user for the file
#     name so that it prints a funny message when the user types in the exact file name
# “na na boo boo”. The program should behave normally for all other files which
# exist and don’t exist. Here is a sample execution of the program:
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
# We are not encouraging you to put Easter Eggs in your programs—this is just an
# exercise.