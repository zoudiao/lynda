#12.2 TheWorld's Simplest Web Browser
# import socket
# mysock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock1.connect(('www.py4inf.com',80))
# mysock1.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
#
#
# while True:
#     data = mysock1.recv(512)
#     if(len (data)<1):
#         print "break"
#         break
#     print data
#
# mysock1.close()


#12.3 Retrieving an image over HTTP
# mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock2.connect(('www.py4inf.com',80))
# mysock2.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
#
# count = 0
# picture = "";
# while True:
#     data = mysock2.recv(5120)
#     if(len(data)<1):break
#     count = count +len(data)
#     print len(data),count
#     picture = picture + data
#
# mysock2.close()

# Look for the end of the header (2 CRLF)
# pos = picture.find("\r\n\r\n");
# print 'Header length',pos
# print picture[:pos]

# Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg","wb")
# fhand.write(picture);
# fhand.close()

#12.4 Retrieving web pages with urllib
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()

counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print counts

#12.5 Parsing HTML and scraping the web

#12.6 Parsing HTML using regular expressions
