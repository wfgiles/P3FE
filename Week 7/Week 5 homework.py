##Homework Exercises 5.1

##count = 0
##total = 0
##while True:
##    inp = raw_input('Enter a Number: ')
##
##    #Handle the edge cases
##    if inp == 'done':
##        break
##    
##    #Check for empty line
##    if len(inp) < 1:
##        break
##    
##    #Do the work
##    try :
##        num = float(inp)
##    except :
##        print 'Invalid Entry'
##        continue
##    count = count + 1
##    total = total + num
##    print num, total, count 
##
##print 'Average:', total / count

##Homework Exercise 5.2
##THIS "CODE" IS CORRECT BUT THE FORMAT IS WRONG.
##NEEDED CAPS AND "IS" TO MATCH REQUIRED OUTPUT
##maximum = 0
##minimum = None
##while True:
##    inp = raw_input('Enter a Number: ')
##   
##    #Check for empty line
##    if len(inp) < 1:
##        break
##    
##    #Handle the edge cases
##    if inp == 'done':
##        print 'maximum', maximum
##        print 'minimum', minimum
##        break
##
##    #Do the work
##    try :
##        num = int(inp)
##    except :
##        print 'Invalid Input'
##        continue
##
##    #Get max
##    if maximum < num:
##        maximum = num
##
##    #Get min
##    if minimum is None or num < minimum:
##        minimum = num
##
##
##CORRECT FORMAT 
##Maximum = 0
##Minimum = None
##while True:
##    inp = raw_input('Enter a Number: ')
##   
##    #Check for empty line
##    if len(inp) < 1:
##        break
##    
##    #Handle the edge cases
##    if inp == 'done':
##        print 'Maximum is', Maximum
##        print 'Minimum is', Minimum
##        break
##
##    #Do the work
##    try :
##        num = int(inp)
##    except :
##        print 'Invalid input'
##        continue
##
##    #Get max
##    if Maximum < num:
##        Maximum = num
##
##    #Get min
##    if Minimum is None or num < Minimum:
##        Minimum = num
