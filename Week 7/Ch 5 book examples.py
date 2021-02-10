##CHapter 5

##n = 50
##while n > 0:
##    print n
##    n = n - 1
##print 'Blastoff!'

##n = 10
##while True:
##    print n
##    n = n - 1
##print 'Done'

##while True:
##    line = raw_input('>')
##    if line == 'done':
##        break
##    print line
##print 'Done'

##while True:
##    line = raw_input ('>')
##    if line [0] == '#':
##        continue
##    if line == 'done':
##        break
##    print line
##print 'Done!'

##Counting in a loop
##zork = 0
##print 'Before', zork
##for thing in [9, 12, 5, 76, 4, 45, 99, 54]:
##    zork = zork + 1
##    print zork, thing
##print 'After', zork

##zork = 0
##print 'Before', zork
##for thing in [9, 12, 5, 76, 4, 45, 99, 54]:
##    zork = zork + thing
##    print zork, thing
##print 'After', zork

##count = 0
##sum = 0
##print 'Before', count, sum
##for value in [9, 12, 5, 76, 4, 45, 99, 54]:
##    count = count + 1
##    sum = sum + value
##    print count, sum, value
##print 'After', count, sum, sum/count

##print 'Before'
##for value in [9, 12, 5, 76, 4, 45, 99, 54]:
##    if value > 20:
##        print 'Large number:', value
##print 'After'

##found = False
##print 'Before', found
##for value in [9, 12, 5, 76, 4, 45, 99, 54]:
##    if value == 4:
##        found = True
##    print found, value
##print 'After', found   

##largest_so_far = -1
##print 'Before', largest_so_far
##for the_num in [9, 12, 5, 76, 4, 45, 99, 54]:
##    if the_num > largest_so_far:
##        largest_so_far = the_num
##    print largest_so_far, the_num
##print 'After', largest_so_far

##smallest_so_far = 1
##print 'Before', smallest_so_far
##for the_num in [9, 12, 5, 76, 4, 45, 99, 54]:
##    if the_num < smallest_so_far:
##        smallest_so_far = the_num
##    print smallest_so_far, the_num
##print 'After', smallest_so_far

##smallest = None
##print 'Before'
##for value in [9, 12, 5, 76, 4, 45, 99, 54]:
##    if smallest is None:
##        smallest = value
##    elif value < smallest:
##        smallest = value
##    print smallest, value
##    
##print 'After', smallest

##tot = 0
##for i in [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]:
##    tot = tot + 1
##print tot
##----------------------------------
##ASSIGNMENT 5.2
##Write a program that repeatedly prompts a user for integer numbers
##until the user enters 'done'. Once 'done' is entered, print out the
##largest and smallest of the numbers. If the user enters anything other
##than a valid number catch it with a try/except and put out an appropriate
##message and ignore the number. Enter the numbers from the book for
##problem 5.1 and Match the desired output as shown.

##Maximum = 0
##Minimum = None
##while True:
##    inp = raw_input('Enter a Number: ')  
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
##
##count = 0
##sum = 0
##print 'Before', count, sum
##for value in [9, 12, 5, 76, 4, 45, 99, 54]:
##    count = count + 1
##    sum = sum + value
##    print count, sum, value
##print 'After', count, sum, sum/count

##--------------------------
##Exercise 5.1 - SEE VIDEO FOR WORKED PROBLEM

numcount = 0
numsum = 0
while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done':
        break
    num = float(inp)
    numsum = numsum + num
    numcount = numcount + 1
print 'Total:', numsum
print 'Count:', numcount
print 'Average:', numsum/numcount 



=========================





































