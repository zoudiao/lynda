eng2sp = dict()
print eng2sp

eng2sp['one'] = 'uno'
print eng2sp

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print eng2sp['two']

print len(eng2sp)
vals = eng2sp.values()
print 'uno' in vals

#9.1 Dictionary as a set of counters
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print d

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print counts.get('jan', 0)
print counts.get('tim', 0)


for c in word:
    d[c] = d.get(c,0) + 1 #if key c has value return default value otherwise 0
print d

#9.2 Dictionaries and files
#fname = raw_input('Enter the file name: ')
try:
    fhand = open('remeo.txt')
except:
    print 'File cannot be opened:', fname
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts

#9.3 Looping and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = counts.keys()
print lst
lst.sort()
for key in lst:
    print key, counts[key]

#9.4 Advanced text parsing
import string
#print string.punctuation

counts=dict()
fhand = open('romeo-full.txt')
for line in fhand:
    #print line
    line = line.translate(None,string.punctuation)
    line = line.lower()
    print line
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
print counts
