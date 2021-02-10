##Chapter 3

##x = 6
##y = 2
##x >= 2 and (x/y) > 2
##x >= 2 and y !=0 and (x/y) > 2


##import math
##signal_power = 9
##noise_power = 10
##ratio = signal_power / noise_power
##print (ratio)
##decibels = 10 * math.log10(ratio)
##print (decibels)
##--------------------
##Exercise 3.11.1
##
##inp = input('Enter hours ')
##hours = float(inp)
##
##inp = input('Enter rate ')
##rate = float(inp)
##
##print ('Hours ' + str(hours))
##print ('Rate ' + str(rate))
##
##if hours <= 40:
##    pay = hours * rate
##
##    print ('Pay ' + str(pay))
##
##else:
##    pay = (hours * rate) + (1.5(rate))
##    print (pay)
##
####print ('Pay ' + str(pay))
##else:
##pay = (40 * rate) + (hours - 40) * (rate * 1.5)
##print ('Pay ' + str(pay))

##CLEANED UP - 3.11.1
##
##inp = input('Enter hours ')
##hours = float(inp)
##inp = input('Enter rate ')
##rate = float(inp)
##print ('Hours ' + str(hours))
##print ('Rate ' + str(rate))
##if hours <= 40:
##    pay = hours * rate
##if hours > 40:
##    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
##print ('Pay ' + str(pay))
##--------------------------
##Exercise 3.11.2

##try:
##    inp = input('Enter hours ')
##    hours = float(inp)
##    inp = input('Enter rate ')
##    rate = float(inp)
##    print ('Hours ' + str(hours))
##    print ('Rate ' + str(rate))
##    if hours <= 40:
##        pay = hours * rate
##    if hours > 40:
##        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
##    print ('Pay ' + str(pay))
##except:
##    print ('Error, please enter numeric input')
##    quit()
##-----------------------------
##
##Exercise 3.11.3
##
inp = raw_input('Enter a score: ')
try:
    inp = float(inp)
    if inp >= 10.0:
        print('bad score')
    elif inp >= 0.9:
        print('A')
    elif inp >= 0.8:
        print ('B')
    elif inp >= 0.7:
        print ('C')
    elif inp >= 0.6:
        print ('D')
    elif inp < 0.6:
        print ('F')
except:
    print('Bad score')







