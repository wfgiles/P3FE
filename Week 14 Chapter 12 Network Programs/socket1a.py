import socket

fhand = raw_input('Enter a filename - ')
fname = fhand.split('/')
##print fname

adr = fname[2]
##print adr

##bdr = fname[0-3]
##print bdr

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('adr', '80'))
mysock.send("GET" 'fhand', "HTTP/1.0\n\n")

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()
