##EXERCISE 12.1

## Change socket1.py so asks for URL

##import socket
##
##url = raw_input('Enter url: ')
##words = url.split('/')
##print words
##
##try:
##    host_url = words[2]
##    print host_url
##except:
##    print('Wrong url')
##    exit()
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

##---------------------


##EXERCISE 12.2
##Counts characters it receives
##Stops displaying characters after 3000
##Retrieve entire doc, display count of char at end

##
##import socket
##
##url = raw_input('Enter url: ')
##words = url.split('/')
##print words
##
##try:
##    host_url = words[2]
##    print host_url
##except:
##    print('Wrong url')
##    exit()
##    
##request = 'GET '+ url + ' HTTP/1.0\n\n'
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((host_url, 80))
##mysock.send(request)
##while True:
##    data = mysock.recv(512)
##    if ( len(data) > 3000 ) :
##        break
##    print data
##mysock.close()



















##import socket
##
####url = raw_input('Enter url: ')
##url = open('http://www.dr-chuck.com/page 1').read()
##words = url.split('/')
##print words
##
##try:
##    host_url = words[2]
##    print host_url
##except:
##    print('Wrong url')
##    exit()
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
##-------
##import urllib
##from BeautifulSoup import *
##
##
##url = ('http://www.dr-chuck.com')
##html = urllib.urlopen(url).read()
##
##soup = BeautifulSoup(html)
##
##
##
##
##
##print soup



























