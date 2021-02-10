##n = 5
##print 'Hello'

##fhand = open('mbox.txt')
##print fhand

##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count + 1
##print "Line count",count

##fhand = open('mbox-short.txt')
##inp =fhand.read()
##print len(inp)

##fhand = open('mbox-short.txt')
##inp =fhand.read()
##print inp

##fhand = open('mbox-short.txt')
##count = 0
##for line in fhand:
##    if line.startswith('From'):
##        count = count + 1
##        print line
####        print count
##print 'Line Startswith',count

##fhand = open('mbox-short.txt')
##count = 0
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('From'):
##        count = count + 1
##        print line
####        print count
##print 'Line Startswith',count


##fhand = open('mbox-short.txt')
##count = 0
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('From:'):
##        continue
##    count = count + 1
##    print line
##print count

##fhand = open('mbox-short.txt')
##count = 0
##for line in fhand:
##    line = line.rstrip()
##    if line.find('@uct.ac.za') == -1:
##        continue
##    count = count + 1
##    print line
##print count

##fname = raw_input('Enter a filename:')
##fhand = open(fname)
##count = 0
##for line in fhand:
##    if line.startswith('Subject:'):
##        count = count + 1
##print 'There were',count, 'subject lines in',fname
##

##fname = raw_input('Enter a filename:')
##try:
##    fhand = open(fname)
##except:
##    print 'File cannot be opened:',fname
##    exit()
##
##count = 0
##for line in fhand:
##    if line.startswith('Subject:'):
##        count = count + 1
##print 'There were',count, 'subject lines in',fname

fout = open('output.txt')
print fout

















