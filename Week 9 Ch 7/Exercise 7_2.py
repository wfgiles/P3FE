fname = raw_input('Enter a filename: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.lower()
    line = line.strip()
    if line.startswith('x-dspam-confidence:'):
        count = count + 1
        line = line[20:26]
        line = float(line)

        total = total + line

print ('Average spam confidence: ', total/count)




##PAGE 89 OF BOOK
##DONE!
