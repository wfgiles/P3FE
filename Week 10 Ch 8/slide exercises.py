##friends = ['Joseph', 'Glenn', 'Sally',]
####print friends[0:]
##
##for friend in friends:
##    print friend
##
##
##lotto = [2, 5, 1, 8, 45,9]
##print lotto
##
##lotto[4] = 5
##
##print lotto


##print range(5)


##friends = ['Joseph', 'Glenn', 'Sally',]
##
##for friend in friends:
##    print 'Happy New Year:', friend
##
##THESE ARE EQUIVELANT STATEMENTS - YIELD SAME RESULTS
##
##for i in range(len(friends)):
##    print range(len(friends))
##    
##    friend = friends[i]
##    print 'Happy New Year:', friend

##t = [9, 41, 12, 5, 75]
##print t[1:3]
##
##stuff = list()
##stuff.append('book')
##stuff.append(99)
##print stuff

##t = [9, 41, 12, 5, 75]
####t.sort()
####print t
####print t[2]
##
##print 'length t:', len(t)
##
##print 'max in t:', max(t)
##
##print min(t)
##
##print sum(t)
##
##print sum(t)/len(t)

##total = 0
##count = 0
##while True:
##    inp = raw_input('Enter a number:')
##    if inp == 'done': break
##    value = float(inp)
##    total = total + value
##    count = count + 1
##
##print 'Average:', total/count
##
##
##THIS CODE YIELDS SAME RESULT, JUST AS A LIST
##USES MORE MEMORY AS IT STORES DATA IN LIST

##numlist = list()
##while True:
##    inp = raw_input('Enter a number:')
##    if inp == 'done': break
##    value = float(inp)
##    numlist.append(value)
##
##average = sum(numlist)/len(numlist)
##print 'Average;', average


##abc = 'With three words'
##stuff = abc.split()
##print stuff
##
##print len(stuff)
##
##print stuff[0]
##
##for w in stuff:
##    print "hello", w

##numbers = [4, 23, 6, 78, 375]
##for i in range(len(numbers)):
##    numbers[i] = numbers[i] * 2

##    ##-------------------    
##REBOOT REBOOT
##SEP 2, 2016

##print range(4)
##
##friends = ['Kken', 'Fred', 'bill',]
##print len(friends)
##
##print range(len(friends))
##
##for friend in friends:
##    print 'Happy', friend

##a = [1,2,3]
##b = [4,5,6]
##c = b + a
##print c

##t = [4, 4, 2, 65, 76, 6, 32]
##t.sort()
##print t

##total = 0
##count = 0
##while True:
##    inp = raw_input('Enter a number')
##    if inp == 'done': break
##    value = float(inp)
##    total = total + value
##    count = count + 1
##
##average = total/count
##print 'Average', average


##numlist = list()
##while True:
##    inp = raw_input('Enter a number')
##    if inp == 'done': break
##    value = float(inp)
##    numlist.append(value)
##
##average = sum(numlist)/len(numlist)
##print sum(numlist)
##print len(numlist)
##print 'Average', average

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print pieces[1]
    
    
##    words = line.split()
##    print words[2]





















































