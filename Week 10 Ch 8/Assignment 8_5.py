# Assignment 8.5
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print (words[1])
count = count + 1
print ('Count:', count)
