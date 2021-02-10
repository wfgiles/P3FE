##[10, 20, 30, 40]
##['crunchy frog', 'ram bladder', 'lark vomit']
##
##['spam', 2.0, 5, [10, 20]]
##
##cheeses = ['Chedder', 'Edam', 'Gouda']
##numbers = [17, 123]
##empty = []
##print cheeses, numbers, empty
##
##print cheeses[0]

##numbers = [17, 123]
##numbers[1] = 5
##print numbers

##cheeses = ['Chedder', 'Edam', 'Gouda']
####print 'Edam' in cheeses
####print 'Brie' in cheeses
##
##for cheese in cheeses:
##    print cheese


##numbers = [17, 123]
##
##for i in range(len(numbers)):
##    numbers[i] = numbers[i] * 2
##print numbers

##s = 'spam'
##t = list(s)
##print t


##s = 'spam-spam-spam'
##delimiter = '-'
##s.split(delimiter)
##print s

##t = ['pining', 'fot', 'the', 'fjords']
##delimiter = ' '
##delimiter.join(t)
##print t
##---------------
##Equivalent programs
##Summing and Counting
##
##total = 0
##count = 0
##while True:
##    inp = raw_input('Enter a number')
##    if inp == 'done': break
##    value = float(inp)
##    total = total + value
##    count = count + 1
##
##average = total / count
##print 'Average: ', average
##
##----------
##Create a list
##create list, append list, divide sum of list by len(count) of list
##USES 1 LINE INSTEAD OF 4 LINES
##
##numlist = list()
##while True:
##    inp = raw_input('Enter a number: ')
##    if inp == 'done': break
##    value = float(inp)
##    
##    numlist.append(value)
##
##average = sum(numlist) / len(numlist)
##print 'Average:', average
##
##-----------------------------

##s = 'spam'
##t = list(s)
##print t

##s = 'pining for the fjords'
##t = s.split()
##print t
##
##delimiter = ''
##delimiter.join(s)
##print s

##t = list(s)
##print t

##-------------
##8.10 Parsing Lines

##fhand = open('mbox-short.txt')
##for line in fhand:
##    line = line.rstrip()
##    if not line.startswith('From ') : continue
##    words = line.split()
##    print words[2]

##---------------
##8.11 Objects and values

##STRINGS
##a = 'banana'
##b = 'banana'
##
##print a == b
##print a is b

##-----

##LISTS
##
##a = [1, 2, 3]
##b = [1, 2, 3]
##
##print a == b
##print a is b

##-----------------------------
##8.13 List Arguments


##def delete_head(t):
##    del t[0]
##
##a = ['1', '2', '3']
##delete_head(a)
##print a

##------

##def tail(t):
##    return t[1:]
##
##a = ['1', '2', '3']
##rest = tail(a)
##print rest

##----------------------------

##Exercise 8.1
##Write a function called chop that takes a
##list and modifies it, removing the first
##and last elements, and returns None.

##def chop(t):
##    t = t[1:-1]
##    return t
## 
##a = ['1', '2', '3']
##a = chop(a)
##print a
##
##------

##Then write a function called middle that takes
##a list and returns a new list that contains
##all but the first and last elements.


##def middle(t):
##    s = t[1:-1]
##    return s
## 
##a = ['1', '2', '3']
##b = middle(a)
##print b
##print a

##--------------------------------
##DEBUGGING
##
##a = ['1', '2', '3']
##orig = a[:]
##print orig
##
##a.sort()
##print orig
##a.append('4')
##print a
##
##
##a.sort()
##print a
##
##a.sorted()
##print a
##
##---------------
##GUARDIAN CODE
##
##fhand = open('mbox-short.txt')
##for line in fhand:
##    words = line.split()
####    print 'Debug:',words
##    if len(words) == 0: continue
##    if words[0] != 'From': continue
##    print words[2]
##    
##--------------------------
##EXERCISE 8.2
##Figure out which line of the above program is
##still not properly guarded. See if
##you can construct a text file which causes
##the program to fail and then modify the
##program so that the line is properly guarded
##and test it to make sure it handles your new
##text file.































