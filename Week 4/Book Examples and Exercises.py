##
##inp = raw_input('Enter a number: ')
##x = int(inp)

##inp = raw_input('Enter a number: ')
##y = int(inp)

##if x%2 == 0:
##    print 'even'
##else:
##    print 'odd'
        

##if x < y:
##    print 'x is less than y'
##elif x > y:
##    print 'x is greater than y'
##else:
##    print 'x and y are equal'
    
##if 0 < x and x < 10:
##    print 'x is a positive single digit number'
##
##location 844 in Book

##inp = raw_input('Enter Farenheit Temperature: ')
##try:
##    fahr = float(inp)
##    cel = (fahr - 32.0) * 5.0/9.0
##    print round(cel, 2)
##except:
##    print 'Enter an Number Fool!'

##x = 1   
##x >= 2 and (x/y) > 2

##import math
##
##signal_power = 9.0
##noise_power = 10
##ratio = signal_power/noise_power
##decibels = 10 * math.log10(ratio)
##print round(decibels, 4)


##EXERCISE 3.1

##Enter Hours: 45
##Enter Pay: 10
##Pay: 475.0

##inp = raw_input('Enter Hours: ')
##hrs = float(inp)
####print hrs
##
##inp = raw_input('Enter Rate: ')
##rate = float(inp)
####print rate
##
##pay = (hrs - 40)*(rate * 1.5) + (40 * rate)
##print 'Pay: ',pay


##EXERCISE 3.2

inp = raw_input('Enter Hours: ')
try:
    hrs = float(inp)
    print 'Hours: ',hrs
except:
    print 'please enter numeric input'

inp = raw_input('Enter Rate: ')
try:
    rate = float(inp)
    print 'Rate: ',rate
except:
    print 'please enter numeric input'

pay = (hrs - 40)*(rate * 1.5) + (40 * rate)
print 'Pay: ',pay


####EXERCISE 3.3
##
##inp = raw_input('Enter a score between 0.0 and 1.0: ')
##try:
##    x = float(inp)
##except:
##    x = -1
##    
##if x > 0 and x <= 1.0:
##    if x >= 0.9:
##        print 'A'
##    elif x >= 0.8:
##        print 'B'
##    elif x >= 0.7:
##        print 'C'
##    elif x >= 0.6:
##        print 'D'
##    elif x < 0.6:
##        print 'F'
##else:
##    print'bad score'























































