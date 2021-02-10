##txt = 'but soft what light in yonder window breaks'
##words = txt.split()
##print words
##
##t = list()
##print t
##
##for word in words:
##    t.append((len(word), word))
##    
##t.sort(reverse = True)
##
##res = list()
##for length, word in t:
##    res.append(word)
##
##print res

##m = ['have', 'fun']
##x, y = m
##print x

##t = tuple('lupins')
##print t

##t = ('a',)
##b = ('b', 'c', 'd')
##print t[0]
##
##print t + b
##
##print b[1:2]
##
##print b[-1]

##t[1] = 'A'

##b = ('A',) + b[1:]
##print b

##(0,1,2,3) < (0,3,4)

##m = ['have', 'fun']
##(x,y) = m
##print x
##print y

##addr = 'monty@python.org'
##uname, domain = addr.split('@')
##print uname

##d = {'a':10, 'b':1, 'c':22}
##t = d.items()
##print t
##t.sort()
##print t

##for ham, eggs in d.items():
##    print eggs, ham


##d = {'a':10, 'b':1, 'c':22}
##l = list()
##for key, val in d.items():
##    l.append((val, key))
##    print l

##l.sort(reverse=True)
##print l

##import string
##fhand = open('romeo-full.txt')
##
##counts = dict()
##for line in fhand:
##    line = line.translate(None, string.punctuation)
##    line.lower()
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1
##
###Sort the distionary by value
##
##lst = list()
##for key, val in counts.items():
##    lst.append ((val, key))
##
##lst.sort(reverse=True)
##
##for key, val in lst[:10]:
##    print key, val


directory[last, first] = number
for last, first in directroy:
    print first, last, directory[last, first]
                        

























     
    


