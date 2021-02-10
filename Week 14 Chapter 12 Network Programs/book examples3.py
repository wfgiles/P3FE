##import socket
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect(('www.py4inf.com', 80))
##mysock.send('GET http://www.py4inf/code/romeo.txt HTTP/1.1\n\n')
##
##while True:
##    data = mysock.recv(4096)
##    if (len(data) < 1) : break
##    print data

##--------------------
##SECTION 12.3

##import socket
##import time
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect(('www.py4inf.com', 80))
##mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
##
##count = 0
##picture = ""
##while True:
##    data = mysock.recv(5120)
##    if (len(data) < 1): break
####    time.sleep(0.25)
##    count = count + len(data)
##    print len(data), count
##    picture = picture + data
##
##mysock.close()
##
##
###Look for the end of the header (2 CRLF)
##pos = picture.find("\r\n\r\n");
##print'Header length',pos
##print picture[:pos]
##
###Skip past the header and save the picture data
##picture = picture[pos+4:]
##fhand = open("stuff.jpg","wb")
##fhand.write(picture);
##fhand.close()

##-----------------------
##SECTION 12.4

##import urllib
##
##fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
##for line in fhand:
##    print line.strip()


##import urllib
##
##counts = dict()
##fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
##for line in fhand:
##    words = line.split()
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##print counts

##--------------------------
##SECTION 12.6

##import urllib
##
##fhand = urllib.urlopen('http://www.dr-chuck.com/page2.htm')
##for line in fhand:
##    print line.strip()

##import urllib
##import re
##
##url = raw_input('Enter- ')
##html = urllib.urlopen(url).read()
##links = re.findall('href="(http://.+?)"', html)
##for link in links:
##    print link

##-----------------------------
##SECTION 12.7

##import urllib
##from BeautifulSoup import *
##
##url = raw_input('Enter- ')
##html = urllib.urlopen(url).read()
##
##soup = BeautifulSoup(html)
##print soup
##
####Retrieve all anchot tags
##tags = soup('a')
##for tag in tags:
##    print tag.get('href', None)

##import urllib
##from BeautifulSoup import *
##
##
##url = raw_input('Enter: ')
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
###Retrieve all anchor tags
##tags = soup('a')
##for tag in tags:
##    #Look at the parts of the tag
##    print 'TAG:',tag
##    print'URL:',tag.get('href', None)
##    print 'Contents:',tag.contents[0]
##    print 'Attrs:',tag.attrs

##-------------------------
##SECTION 12.8

##import urllib
##
##img = urllib.urlopen('http://www.py4inf.com/cover.jpg').read()
##fhand = open('cover.jpg', 'w')
##fhand.write(img)
##fhand.close()


##import urllib
##
##img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
##fhand = open('cover.jpg', 'w')
##size = 0
##while True:
##    info = img.read(100000)
##    if len(info) < 1 : break
##    size = size +len(info)
##    fhand.write(info)
##
##print size,'characters copied.'
##fhand.close()
##------------------

##EXERCISE 12.1

## Change socket1.py so asks for URL

import socket

url = raw_input('Enter url: ')
words = url.split('/')
print words

try:
    host_url = words[2]
    print host_url
except:
    print('Wrong url')
    exit()
    
request = 'GET '+ url + ' HTTP/1.0\n\n'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_url, 80))
mysock.send(request)
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()






























   
