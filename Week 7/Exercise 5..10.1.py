##number = raw_input('Enter number: ')
##num = int(number)
##print num
##
##Write a program which repeatedly reads numbers until the
##user enters "done". Once done is entered, print out the
##total, count and average of the numbers. If the user enters
##anything other than a number, detect the mistake usinf a try
##and except and print the error message and skip to the next
##number.
##
##Enter a number: 4
##Enter a number: 5
##Enter a number: bad data
##Invalid input
##Enter a number: 7
##Enter a number: done
##
##16 3 5.33333333333
##
##CORRECT CODE
##EXERCISE 5.10.1
##
##count = 0
##total = 0
##
##while True:
##    inp = raw_input('Enter a number: ')
##
##    ##Handle the edge cases
##    if inp == 'done':
##        print total, count, total/count
##        break
##    if len(inp) < 1 : break  #Check for empty line
##
##    try: 
##        num = float(inp)
##        count = count + 1
##        total = total + num
##    except:
##        print 'Invalid input'
##        continue
##
##EXERCISE 5.10.2
##
##while True:
##    inp = raw_input('Enter a number: ')
##
##    ##Handle the edge cases
##    if inp == 'done':
##        print "Maximum:", max(num)
##        print 'Minimum:', min(num)
##        break
##    if len(inp) < 1 : break  #Check for empty line
##
##    try: 
##        num = int(inp)
##
##    except:
##        print 'Invalid input'
##        continue
## 



















    

    


    
