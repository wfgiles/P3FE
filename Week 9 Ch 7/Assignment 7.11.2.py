fname = raw_input('Enter a filename:')
count = 0
total = 0
fhand = open(fname)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        num = line[20:]
        num = float(num)
        total = num + total
        count = count + 1
##print total
##print count
print total/count
