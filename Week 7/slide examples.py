##n = 5
##while n > 0 :
##    print 'lather'
##    print 'rinse'
##print 'Dry off'

##n = 0
##while n > 0 :
##    print 'lather'
##    print 'rinse'
##print 'Dry off'

##while True:
##    line = raw_input('> ')
##    if line =='done':
##        break
##    print line
##print 'Done'
                
##while True:
##    line = raw_input('> ')
##    if line[0] == '#':
##        continue
##    if line =='done':
##        break
##    print line
##print 'Done'

##for i in [5, 4, 3, 2, 1]:
##    print i
##print 'Blastoff'

##friends = ['Frank', 'James', 'Tom']
##for friend in friends:
##    print 'Happy New Year',friend
##print 'Done'

##n = 5
##while n > 0:
##    print n
##    n = n - 1
##print 'Blastoff!'



##friends = ['Joseph', 'Glenn', 'Sally']
##for friend in friends:
##    print 'Happy New Year', friend
##print 'Done!'

##total = 0
##for intervar in [3, 65, 2, 768, 5, 986]:
##    total = total + intervar
##print total

##largest = None
##print 'Before:', largest
##for intervar in [3, 65, 2, 768, 5, 986]:
##    if largest is None or intervar > largest:
##        largest = intervar
##    print "Loop",intervar, largest
##print 'Largest', largest


##smallest = None
##print 'Before:', smallest
##for intervar in [3, 65, 2, 768, 5, 986]:
##    if smallest is None or intervar < smallest:
##        smallest = intervar
##    print "Loop",intervar, smallest
##print 'Smallest', smallest


##found = False
##print 'Before',found
##for value in [365, 65, 2, 768, 5, 3, 986]:
##    if value == 3:
##        found = True
##    print found, value
##print 'After',found

##largest_so_far = -1
##print 'Before', largest_so_far
##for the_num in [365, 65, 2, 768, 5, 3, 986]:
##    if the_num > largest_so_far:
##        largest_so_far = the_num
##    print largest_so_far, the_num
##
##print 'After', largest_so_far
        
##smallest_so_far = -1
##print 'Before', smallest_so_far
##for the_num in [365, 65, 2, 768, 5, 3, 986]:
##    if the_num < smallest_so_far:
##        smallest_so_far = the_num
##    print smallest_so_far, the_num
##
##print 'After', smallest_so_far


smallest = None
print 'Before',smallest
for value in [365, 65, 2, 768, 5, 3, 986]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print 'Smallest',smallest
print 'After',smallest

































