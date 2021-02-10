##fname = raw_input('Enter a filename: ')
##fhand = open(fname)
##if fhand == 'na na boo boo':
##    print "NA NA BOO BOO TO YOU - You have been punk'd!"
##else:
##    count = 0
##    total = 0
##    for line in fhand:
##        line = line.lower()
##        line = line.strip()
##        if line.startswith('x-dspam-confidence:'):
##            count = count + 1
##            line = line[20:26]
##            line = float(line)
##
##            total = total + line
##
##    print 'Average spam confidence: ', total/count


fname = raw_input('Enter the file name: ') 
if fname == ('na na boo boo'):
    print "NA NA BOO BOO TO YOU - you have been punk'd"
    exit()

try:
    fhand = open(fname)

except:
    print 'File can not be opened', fname
    exit()
    
count = 0
for line in fhand:
    count = count + 1
print count
