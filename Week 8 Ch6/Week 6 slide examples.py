##INDEFINITE - WHILE STATEMENT
##
##fruit = 'banana'
##index = 0
##while index < len(fruit):
##    letter = fruit[index]
##    print index, letter
##    index = index + 1
##
##----------------------------
##DEFINITE - FOR STATEMENT
##
##fruit = 'banana'
##for letter in fruit:
##    print letter
##
##-------------------------------
##LOOPING AND COUNTING
##
##word = 'banana'
##count = 0
##for letter in word:
##    if letter == 'a':
##        count = count + 1
##print count
##
##------------------------------
##IN AS LOGICAL OPERATOR
##
##fruit = 'banana'
##'m' in fruit
##
##-----------------------------
##
##STRING COMPARUISON
##
##word = 'banana'
##word = 'airplane'
##word = 'zeplin'
##
##if word == 'banana':
##    print 'All right, bananas'
##
##if word < 'banana':
##    print 'Your word, ' + word + ', comes before banana.'
##elif word > 'banana':
##    print 'Your word, ' + word + ', comes after banana.'
##
##else:
##    print 'All right, bananas.'

##greet = 'Hello Bill'
##zap = greet.lower()
##
##print zap
##
##spiz = greet.upper()
## 
##print spiz
##
##fer = greet.title()
##
##print fer
##
##up = greet.capitalize()
##
##print up


##stuff = 'Hello World'
##type(stuff)
##-----------------------

##fruit = 'banana'
##pos = fruit.find('na')
##print pos

##greet = 'Hello Bob'
##print greet
##nstr = greet.replace('Bob', 'Jane')
##print nstr
##xstr = greet.replace('B', 'X')
##print xstr

##greet = '           Hello Bob               ' 
##print greet.lstrip()
##print greet.rstrip()
##print greet.strip()

##line = 'Please have a nice day'
##line.startswith('Please')
##--------------------------------------
##Parsing and Extracting
##
##data = 'From stephen.marguard@uct.ac.za Sat Jan  5 09:14:16 2008'
##atpos = data.find('@')
##print atpos
##
##sppos = data.find(' ',atpos)
##print sppos
##
##host = data[atpos+1 : sppos]
##print host


##str = '123'
##print str
##
##print int(str) + 1 

text = "X-DSPAM-Confidence:    0.8475";
nbr = text.find('0')
print nbr

trt = text.find('5')
print trt

tyt = text[23:29]
print tyt

tyt = float(tyt)
print tyt













































