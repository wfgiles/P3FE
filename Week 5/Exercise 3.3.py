##Exercise 3.3  
##
##Write a program to prompt for a score between 0.0 and 1.0.
##If the score is out of range print an error. If the score is between
##0.0 and 1.0, print a grade using the following table:
##    Score   Grade
##    >= 0.9     A
##    >= 0.8     B
##    >= 0.7     C
##    >= 0.6     D
##    < 0.6      F
##
##Enter score: 0.95
##A
##
##Enter score: perfect
##Bad score
##
##Enter score: 10.0
##Bad score
##
##Enter score: 0.75
##C
##
##Enter score: 0.5
##F
##
##
##Exercise 3.3
x = raw_input('Enter a score between 0.0 and 1.0: ')
try:
    x = float(x)
    if 0 < x and x <= 1.0:
        if x >= 0.9:
            print 'A'
        elif x >= 0.8:
            print 'B'
        elif x >= 0.7:
            print 'C'
        elif x >= 0.6:
            print 'D'
        elif x < 0.6:
            print 'F'
    else:
        print 'Bad Score'
except:
    print 'Bad Score'
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
