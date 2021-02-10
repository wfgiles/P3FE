##--------------------------
##Exercise 5.1 - SEE VIDEO FOR WORKED PROBLEM
##
##count = 0
##total = 0
##
##while True:
##    inp = raw_input('Enter a number: ')
##    if inp == 'done': break
##    if len(inp) < 1 : break
##
##    try:
##        num = float(inp)    
##    except:
##        print 'Invalid Input'
##        continue
##    
##    count = count + 1
##    total = total + num
##    print num, total, count
##print 'Average:', total/count

nlis = [2,4,8,105,210,-3,47,8,33,1]  # average should by 41.5
rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4] # average is -9.215

def average(ytr):
    count = 0
    for num in ytr:
        count = count + num
        average = count/len(ytr)
    print(average)
