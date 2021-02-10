##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    if re.search('From:', line):
##        print line

##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    if line.find('From'):
##        print line
##-----------------

##import re
##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if re.search('^From:', line):
##        print line
##--------------------
##11.1

##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.strip()
##    if re.search('^F..m', line):
##        print line
##
##----------------------
##11.2 
##CHARACTER MATCHING

##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.strip()
##    if re.search('^From:.+@', line):
##        print line

##-------
##EXTRACTING DATA USING findall()

##import re
##s = 'Hello from csev@umch.edu to cwen@iupui.edu about the meeting @2PM'
##lst = re.findall('\S+@\S+', s)
##print lst

##import re
##count = 0
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.findall('\S+@\S+', line)
##    if len(x) > 0 :
##        print x

##import re
##count = 0
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
##    if len(x) > 0 :
##        print x

##------------------
##11.3 COMBINING SEARCHING AND EXTRACTING

##import re
##count = 0
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.search('^X-.*: [0-9.]+', line)
##    if len(x) > 0 :
##        print x


##import re
##count = 0
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.findall('^X\S*: ([0-9.]+)', line)
##    if len(x) > 0 :
##        print x

##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.findall('^Details:.*rev=([0-9]+)', line)
##    if len(x) > 0:
##        print x

##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.rstrip()
##    x = re.findall('^From .* ([0-9][0-9]):', line)
##    if len(x) > 0 : print x

##--------------------
##11.4

import re
x = 'We jus received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print y








        
