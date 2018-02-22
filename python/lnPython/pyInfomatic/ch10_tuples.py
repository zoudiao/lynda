#10.1 Tuples are immutable
t = ('a', 'b', 'c', 'd', 'e')
print type(t)

t1=('a')
print type(t1)

t2=tuple()
print type(t2)

t3=()
print type(t3)

print t[0]

print t[1:3]

t = ('A',) + t[1:]
print t

#10.2 Comparing tuples
print (0,1,2) < (0,3,4)

txt = 'but soft what light in yonder window breaks'
words = txt.split()
print words

t = list()
for word in words:
    t.append((len(word),word))

t.sort(reverse=True)

res=list()
for length,word in t:
    res.append(word)

print res

#10.3 Tuple assignment
m = [ 'have', 'fun' ]
x, y =m
print x
print y

x=m[0]
y=m[1]
print x
print y

addr = 'monty@python.org'
uname,domain = addr.split('@')
print uname
print domain

#10.4 Dictionaries and tuples
d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t
t.sort()
print t

#10.5 Multiple assignment with dictionaries
for key,val in d.items():
    print val,key

#10.6 The most common words
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
    lst.sort(reverse=True)

for key, val in lst[:10] :
    print key, val

#10.7 Using tuples as keys in dictionaries
d = {'a':10, 'b':1, 'c':22}
for key, val in d.items:
    print key ,val 