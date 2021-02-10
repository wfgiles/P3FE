##import random
##
##for i in range(10):
##    x = random.random()
##    print x


##def hello():
##    print 'hello'
##    print 'bye'
##
##hello()
##hello()


##def greet():
##    return 'Hello'
##
##print greet()
##
##print greet(), 'Glenn'
##print greet(), 'Mark'


##def greet(lang):
##    if lang == 'es':
##        return 'Hola'
##    elif lang == 'fr':
##        return 'Bonjour'
##    else:
##        return 'Hello'
##print greet('en'), 'Glenn'
##print greet('fr'), 'Marcel'


##def addtwo(a,b):
##    added = a + b
##    return added
##
##x = addtwo(4, 5)
##print x


##def print_lyrics():
##    print ("I'm a lumberjack")
##
##def repeat_lyrics():
##    print_lyrics()
##    print_lyrics()
##    
##repeat_lyrics()


##EXERCISE 4.2 AND 4.3
##def print_lyrics():
##    print ("I'm a lumberjack")
##
##def repeat_lyrics():
##    print_lyrics()
##    print_lyrics()
##    
##repeat_lyrics()


##import math
##
##x = math.sin(50)
##print x

##import math
##x = math.cos(radians)
##golden = (math.sqrt(5) + 1)/2
##
##def addtwo(a, b):
##    added = a + b
##    return added
##
##x = addtwo(3, 5)
##print x

##--------------------------
##Exercise 4.6
##
##def computepay(hours, rate):
##    hours = float(hours)
##    rate = float(rate)
##    print ('Hours ' + str(hours))
##    print ('Rate ' + str(rate))
##    if hours <= 40:
##        pay = hours * rate
##    if hours > 40:
##        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
##    return pay
##
##pay = computepay (45, 10)
##print pay
##----------------------------
##
##Exercise 4.7
####
##def computegrade(score):
##    try:
##        x = float(score)
##        if 0 < x and x <= 1.0:
##            if x > 0.9:
##                print ('A')
##            elif x > 0.8:
##                print ('B')
##            elif x > 0.7:
##                print ('C')
##            elif x > 0.6:
##                print ('D')
##            elif x <= 0.6:
##                print ('F')
##        else:
##            print('Bsd Score')
##    except:
##        print('Bad Score')
##    
##        
##grade = computegrade (.95)

##grade = computegrade (perfect)
##EVERYTHING WORKS EXCEPT - PERFECT!!!!
##
##grade = computegrade (10.0)
##
##grade = computegrade (.75)
##
##grade = computegrade (.5)


##def stuff():
##    print 'Hello'
##    return
##    print 'World'
##
##stuff()

##
##def addtwo(a, b):
##    added = a + b
##    return a
##
##x = addtwo(2, 7)
##print x
##

def computepay(hrs, rte):
    pay = hrs * rte
    return pay
inp = input('Enter Hours: ')
hrs = float(inp)
inp + input('Enter Rate: ')
rte = float(inp)
if hrs <= 40:
    pay = hrs * rte
elif hrs > 40:
    pay = ((hrs - 40) * (1.5 * rte)) + (40 * rte)
    return(pay)

x =  computepay(45, 10.50)
print(x)

