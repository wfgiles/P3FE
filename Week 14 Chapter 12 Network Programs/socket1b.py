####import socket
####
####mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
####mysock.connect(('www.py4inf.com', 80))
####mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
####
####while True:
####    data = mysock.recv(512)
####    if ( len(data) < 1 ) :
####        break
####    print data
####
####mysock.close()
####-------------------------
####USING urlib - SAME INFORMATION BUT ONLY 4 LINES OF CODE
##
##import urllib
##fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
##
##for line in fhand:
##    print line.strip()


feature1 = 0.25
feature2 = 0.5

if (feature1 > feature2):
    println(feature1)

else:
    print (feature1 + feature2)
