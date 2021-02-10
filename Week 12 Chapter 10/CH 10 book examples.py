
##t = tuple()
##print t


####t = tuple('lupins')
####print t
##
##t = ('a', 'b', 'c', 'd', 'e')
####print t[0]
##
####t[0] = 'A'
##
##t = ('A',) + t[1:]
##print t

##(0, 1, 2) < (0, 3, 4)
##------------
##txt = 'but soft what light in yonder window breaks'
##words = txt.split()
##t = list()
##for word in words:
##    t.append((len(word), word))
##
##t.sort(reverse=True)
##
##res = list()
##for length, word in t:
##    res.append(word)
##
##print res
##------------

##m = [ 'have', 'fun']
##x, y = m
##print x
##print m

##tuple of variables = tuple of expressions

##addr = 'monty@python.org'
##uname, domain = addr.split('@')
##print uname, domain
##
##-------------

##d = {'a': 10, 'b':1, 'c':22}
####t = d.items()
##
##for key, val in d.items():
##    print val, key
##--------------

##d = {'a': 10, 'b':1, 'c':22}
##l = list()
##
##for key, val in d.items():
##    l.append(( val, key))
##
##print l
##
##l.sort(reverse=True)
##
##print l
##-------------------

##import string
##fhand = open('romeo-full.txt')
##counts = dict()
##for line in fhand:
##    line = line.translate(None, string.punctuation)
##    line = line.lower()
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1
##
##lst = list()
##for key, val in counts.items():
##    lst.append((val, key))
##
##lst.sort(reverse=True)
##
##for key, val in lst[:10]:
##    print val, key

##----------------

for last, first in directory:
    print first, last, directory[last,first]























































