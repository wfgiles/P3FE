
##fhand = open('mbox-short.txt')
##inp = fhand.read()
##print len(inp)
##print inp[:21]


##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if line.startswith('From:'):
##        print line

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not'@uct.ac.za' in line:
##        continue
##    print line

##fname = raw_input('Enter a file name: ')
##fhand = open(fname)
##count = 0
##for line in fhand:
##    if line.startswith('Subject'):
##        count = count + 1
##print 'There were',count,'subject lines in',fname

fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print 'File can not be opened:',fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print 'There were',count,'subject lines in',fname
    













