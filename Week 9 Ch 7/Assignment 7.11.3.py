fname = raw_input('Enter a file name:')
if fname == 'na na boo boo':
    print 'NA NA BOO BOO TO YOU -\n', "You have been punk'd!"
    exit()
try:
    fhand = open(fname)
    total = 0
    for line in fhand:
        if line.startswith('Subject'):
            total = total + 1
    print "There were",total, "subject lines in",fname
except:
    print"File cannot be opened:",fname
    exit()

