##fhand = open('mbox.txt')
##print fhand

##fhand = open('mbox.txt', 'r')
##print fhand

##stuff = 'Hello\n\nWorld'
##print stuff

##xfile = open('mbox.txt')
##for hghf in xfile:
##    print hghf

##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count + 1
##print 'Line count:', count

##fhand = open('mbox-short.txt')
##inp = fhand.read()
##print len(inp)

##fhand = open('mbox-short.txt')
##inp = fhand.read()
##print inp

##fhand= open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('From:') :
##        print line


##fhand= open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('From: ') :
##        continue
##    print line

##fhand= open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('From: cwen') :
##        continue
##    print line

##----------------------

##THIS IS THE SAME AS-
##...NOT IN LINE...


##fhand= open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not '@uct.ac.za' in line:
##        continue
##    print line


##THIS
##...IN LINE....

##fhand= open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if '@uct.ac.za' in line:
##        print line


##------------------------

fname = raw_input('Enter a filename:')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print 'There were',count,'Subject lines in',fname



































