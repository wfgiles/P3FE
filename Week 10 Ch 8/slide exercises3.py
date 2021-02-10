##print [1, 1, 3]
##
##print ['red', 'yellow', 'blue']
##
##print ['red', 3, 98.6]
##
##print [1, [5, 6], 'red']
##
##print []
##
##for i in [5,4,3,2,1]:
##    print i
##print 'Blastoff!'
##
##friends = ['Bill', 'Mike', 'Tom']
##for friend in friends:
##    print 'Hello', friend
##print 'Done'
##
##friends = ['Bill', 'Mike', 'Tom']
##print friends [2]
##print friends [0]
##print friends [0:2]
##
##fruit = 'Banana'
####fruit [0] = 'b'
##
##x = fruit.lower()
##print x
##
##x = fruit.upper()
##print x

##lotto = [2, 4, 5, 12, 76, 45]
##print lotto
##
##lotto[3] = 2
##print lotto

##greet = 'Hello Bob'
##print len(greet)

##x = [1, 45, 6, 76, 8]
##print len(x)

##print range(6)

##friends = ['Joseph', 'Glenn']
##print len(friends)

##print range(len(friends))

##friends = ['Joesph', 'Glann', 'Sally']
##
##print len(friends)
##
##for friend in friends:
##    print 'Happy New Year:', friend

##for i in range(len(friends)):
##    friend = friends[i]
##    print i
##    print i, 'Happy New Year:', friend


##a = [1, 2, 3, 4, 5, 6]
##b = [7, 8, 9, 10, 11]
##c = a + b
##print c
##
##print a
##print b
##print c

##t = [9, 11, 65, 7, 11, 87, 823]
##print t
##print t[1:3]
##print t[5]
##print t[:5]
##print t[5:]

##stuff = list()
##print stuff
##stuff.append('book')
##print stuff
##stuff.append(99)
##print stuff
##stuff.append('cookie')
##print stuff

##t = [9, 11, 65, 7, 11, 87, 823]
##9 in t

##-------------------------
##slide 19
##EQUIVALENT SCRIPTS
##
##total = 0
##count = 0
##while True:
##    inp = raw_input('Enter a number:')
##    if inp == 'done': break
##    value = float(inp)
##    total = total + value
##    count = count + 1
##
##average = total / count
##print 'Average:', average
##
##----
##
##numlist = list()
##while True:
##    inp = raw_input('Enter a number:')
##    if inp == 'done': break
##    value = float(inp)
##    numlist.append(value)
##
##average = sum(numlist)/len(numlist)
##print 'Average:', average

##---------------------------------
##slide 20

##abc = 'With three words'
##stuff = abc.split()
##print stuff
##
##print len(stuff)
##
##print stuff[0]
##
##print stuff
##
##for r in stuff:
##    print r
##-------------------------
##slide 21

##line = 'A lot          of        spaces'
##etc = line.split()
##print etc
##
##
##line = 'A lot          of        spaces'
##etc = line.split(';')
##print etc
##
##------------

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('From '): continue
##    words = line.split()
##    print words[1]
##
##------------------
##THE DOUBLE SPLIT
##SLIDE 23 - 26
##
##fhand = open('mbox-short.txt')
##for line in fhand:
##    if not line.startswith('From ') : continue
##    line = line.rstrip()
-->##    words = line.split()
##    email = words[1]
####    print email
-->##    pieces = email.split('@')
##    print pieces[1]




































