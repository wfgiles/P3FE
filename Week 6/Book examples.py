##
##print len('Hello World')
##
##
##import random
##for i in range(10):
##	x = random.random()
##	print x
##
##	
##0.845726135169
##0.491848207369
##0.541276942169
##0.856676276833
##0.591766564224
##0.0502591389313
##0.950875965575
##0.66227981271
##0.65042526391
##0.494705002685

##random.randint(1, 49660)
##4290
##import random
##
##y = [1,2,3,4,5,6,7,8,9]
##print random.choice(y)
##
##
##
##import math
##
##ratio = .55
####ratio = signal_power / noise_power
##decibels = 10 * math.log10(ratio)
##
####ratio = .55
##print decibels



##
##
##
##
##
##
##
##
##
##import math
##
##radians = 0.7
##height = math.sin(radians)
##print height
##
##-------------------------
##
##import math
##print math.pi
##----------------------
##def print_lyrics():
##    print "I'm a lumberjack and I'm OK"
##    print "I sleep amm night and I work all day"
##
##def repeat_lyrics():
##    print_lyrics()
##    print_lyrics()
##
##print_lyrics()
##repeat_lyrics()
##-----------------------
##
##EXERCISE 2
##
##print_lyrics()
##repeat_lyrics()
##
##def print_lyrics():
##    print "I'm a lumberjack and I'm OK"
##    print "I sleep amm night and I work all day"
##
##def repeat_lyrics():
##    print_lyrics()
##    print_lyrics()
##
##EXERCISE 3
##def print_lyrics():
##    print "I'm a lumberjack and I'm OK"
##    print "I sleep amm night and I work all day"
##
##def repeat_lyrics():
##    print_lyrics()
##    print_lyrics()
##
##
##repeat_lyrics()
##print_lyrics()
##
##def print_twice(bruce):
##    print bruce
##    print bruce
##
##import math
##print_twice(math.pi)
##----------------------------------

##def print_twice(bruce):
##    print bruce
##    print bruce
##
##def addtwo(a, b):
##    added = a + b
##    return added
##
##x = addtwo(3, 5)
##print x
##
##
##EXERCISE 5
##
##ABC
##ZAP
##ABC
##
##CHECK ANSWER;
##def fred():
##    print "Zap"
##
##def jane():
##    print "ABC"
##
##jane()
##fred()
##jane()
##
##Yup, correct
##
##
##
##EXERCISE 6
##Rewrite your pay computation with time and a half for overtime
##and create a function called computepay which takes two
##parameters (hours and rate)
##
##Enter Hours: 45
##Enter Rate: 10
##Pay: 475
##
##hours = raw_input('Enter Hours: ')
##rate = raw_input('Enter Rate: ')
##hours = float(hours)
##rate = float(rate)
##print hours, rate
##
##
####ANSWER
####def computepay(hours, rate):
####    hours = float(hours)
####    rate = float(rate)
####    pay = (hours - 40) * (rate * 1.5) + (40  * rate)
####    print pay
####
####computepay(45, 10)
##
####------------------------------------------------
##
##EXERCISE 7
##
##Rewrite the grade program from the previous chapter using
##a function called computegrade that takes a score as its
##parameter and returns a grade as a string.
##
##score    Grade
##>0.9    A
##>0.8    B
##>0.7    C
##>0.6    D
##<=0.6   F
##
##Program Execution:
##Enter Score: 0.95
##A
##
##Enter score: perfect
##Bad Score
##
##Enter Score: 10.0
##Bad Score
##
##
##Enter Score: 0.75
##C
##
##Enter Score: 0.5
##F
##
##Run the program repeatedly to test the carious values for input
##
##---------------------------
##
##score = raw_input('Enter a score: ')

def computegrade(score):
    try:
        score = float(score)

        if score >1.0:
            print 'Bad Score'
        elif score >= 0.9:
            print 'Grade is A'   
        elif score >= 0.8:
            print 'Grade is B'
        elif score >= 0.7:
            print 'Grade is C'
        elif score >= 0.6:
            print 'Grade is D'
        elif score < 0.6:
            print 'Grade is F'

    except:
        print 'Bad Score'

computegrade(0.95)

computegrade(perfect)

computegrade(10)

computegrade(0.75)

computegrade(0.5)

    




















    




















