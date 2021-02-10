


##eng2sp = dict()
##print eng2sp
##
##eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
##print eng2sp
##
##print eng2sp.values()


##word = 'brontosaurus':
##d = dict()
##for c in word:
##    if c not in d:
##        d[c] = 1
##    else:
##        d[c] = d[c] + 1
##print d
##
##-----------------
##Exercise 1
##
##fhand = open('words.txt')
##
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] = counts[word] + 1
##print counts
##
##----------------
##
##fhand = open('romeo.txt')
##
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1
##print counts

##-----------
##counts[word] = counts.get(word,0) + 1
##
##REPLACES
##
##if word not in counts:
##    counts[word] = 1
##else:
##    counts[word] += 1
##-----------


##fhand = open('romeo.txt')
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##print counts

##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    print key, counts[key]
    

##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    if counts[key] > 10:
##        print key, counts[key]
                
##--------------
##9.2 Dictionaries and files


##fname = raw_input('Enter a file name: ')
##try:
##    fhand = open(fname)
##except:
##    print 'File cannot be opened:',fname
##    exit()
##
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1
##print counts

##GET

##fname = raw_input('Enter a file name: ')
##try:
##    fhand = open(fname)
##except:
##    print 'File cannot be opened:',fname
##    exit()
##
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##
##print counts

##-------------------------
##
##9.3 Looping and Dictionaries

##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    print key, counts[key]
    
##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    if counts[key] > 10:
##        print key, counts[key]

##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##lst = counts.keys()
##print lst
##lst.sort()
##print lst
##for key in lst:
##    print key, counts[key]

##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    print key, counts[key]
    
##counts = {'chuck': 1, 'annie': 42, 'jan': 100}
##for key in counts:
##    if counts[key] > 10:        
##        print key, counts[key]

##---------------------------
##ELIMINATE PUNCTUATION AND LOWER CASE

import string
string.punctuation

fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()

counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
##New Code
    line = line.lower()
##New Code
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print counts











