##fhand = open('mbox.txt')
##print fhand

##stuff = 'Hello\nWorld'
##print stuff

##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count + 1
##print "Line count:", count

##fhand = open('mbox-short.txt')
##inp = fhand.read()
##print len (inp)
##print inp[:150]

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('From'):
##        print line

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    #skip uninteresting lines
##    if not line.startswith('From'):
##        continue
##    #process interesting line
##    print line

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    #skip uninteresting lines
##    if line.find('@uct.ac.za') == -1:
##        continue
##    #process interesting line
##    print line
##
##----------------
##FNAME = RAW_INPUT
##
##fname = raw_input('Enter a filename: ')
##fhand = open(fname)
##count = 0
##for line in fhand:
##    if line.startswith('Subject:'):
##        count = count + 1
##print 'There were', count, 'subject lines in', fname
##
##-------------------
##TRY/EXCEPT

##fname = raw_input('Enter a filename: ')
##try:
##    fhand = open(fname)
##except:
##    print 'File cannot be opened:', fname
##    exit()
##
##count = 0
##for line in fhand:
##    if line.startswith('Subject:'):
##        count = count + 1
##print 'There were', count, 'subject lines in', fname
##
##
##s = '1, 2\t 3\n 4'
##print s


s = '1, 2\t 3\n 4'
print repr(s)







