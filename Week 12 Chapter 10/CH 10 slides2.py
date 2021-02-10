##counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
##lst = counts.keys()
##print lst
##lst.sort()
##for key in lst:
##    print key, counts[key]
##-------------
##d = {'a':10, 'b':1, 'c':22}
##print d.items()
##
##print sorted(d.items())
##--------------
##SORT BY VALUE
##d = {'a':10, 'b':1, 'c':22}
##
##print d.items()
##
##print sorted(d.items())
##
##for k, v in sorted(d.items()):
##    print k, v
##-------------------
##SORT BY VALUE INSTEAD OF KAY
##c = {'a':10, 'b':1, 'c':22}
##tmp = list()
##for k, v in c.items():
##    tmp.append((v, k))
##print tmp
##
##tmp = sorted(tmp,reverse=True)
##print tmp
##-------------

##*****KNOW THIS******

##TOP 10 COMMON WORDS IN A FILE

##fhand = open('romeo.txt')
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##
##lst = list()
##for key, val in counts.items():
##    newtup = (val, key)
##    lst.append(newtup)
##
##lst = sorted(lst, reverse=True)
##
##for val, key in lst[:10]:
##    print(key, val)
    













