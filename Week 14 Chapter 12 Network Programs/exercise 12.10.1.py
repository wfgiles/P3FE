

##socket1.py
##import socket
##
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect(('www.py4inf.com', 80))
##mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
##
##while True:
##    data = mysock.recv(512)
##    if ( len(data) < 1 ) :
##        break
##    print data
##
##mysock.close()

##----------------------------
##MY ANSWER TO EXERCISE 12.10.1
##RUNS THE PROGRAM CORRECTLT

## Change socket1.py so asks for URL

##import socket
##
##url = raw_input('Enter url: ')
##words = url.split('/')
##
##try:
##    host_url = words[2]
##
##except:
##    print('Wrong url')
##    
##request = 'GET '+ url + ' HTTP/1.0\n\n'
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((host_url, 80))
##mysock.send(request)
##while True:
##    data = mysock.recv(512)
##    if ( len(data) < 1 ) :
##        break
##    print data
##mysock.close()

##At the end of episode five, it turns out that
##>! he's actually his father.
##
##------------------------------------

##Exercise 12.2

##import socket
##
##url = raw_input('Enter url: ')
##words = url.split('/')
##
##try:
##    host_url = words[2]
##
##except:
##    print('Wrong url')
##    
##request = 'GET '+ url + ' HTTP/1.0\n\n'
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((host_url, 80))
##mysock.send(request)
##
##while True:
##    data = mysock.recv(512)
##    if ( len(data) < 1 ) :
##        break
##    print data[:3000]
##mysock.close()

##info = len(soup)
##print info


##    
##fhand = open(url, 'w')
##count = 0
##
##while True:
##    info = url.read

##import socket
import urllib


url = raw_input('Enter a url: ')
fhand = urllib.urlopen(url)

##print url

for line in fhand:
    print line.strip()



























