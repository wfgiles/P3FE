##5.2 Write a program that repeatedly prompts a user for integer
##numbers until the user enters 'done'. Once 'done' is entered,
##print out the largest and smallest of the numbers. If the user
##enters anything other than a valid number catch it with a
##try/except and put out an appropriate message and ignore the
##number.
##
##Enter the numbers from the book for problem 5.1 and Match the
##desired output as shown.
##

##largest = None
##smallest = None
##
##inp = raw_input('Enter a number:')
##inp = int(inp)
##
##try: 
##    num = int(inp)
##     if num is None or 
##
##
##
##except:
##    print 'Invalid input'

##ANSWER TO ASSIGNMANT 5.2 ON AUTOGRADER

Maximum = 0
Minimum = None
while True:
    inp = raw_input('Enter a Number: ')  
    #Check for empty line
    if len(inp) < 1:
        break
    
    #Handle the edge cases
    if inp == 'done':
        print 'Maximum is', Maximum
        print 'Minimum is', Minimum
        break

    #Do the work
    try :
        num = int(inp)
    except :
        print 'Invalid input'
        continue

    #Get max
    if Maximum < num:
        Maximum = num

    #Get min
    if Minimum is None or num < Minimum:
        Minimum = num


