##count = 0
##total = 0
##
##inp = raw_input('Enter a number: ')
##try: 
##    num = int(inp)
##except:
##    print 'Invalid input'
##    continue
##
##    count = count + 1
##    total = total + num
##-------------

count = 0
total = 0

while True:
    inp = raw_input('Enter a number: ')

    if inp == 'done': break
    if len(inp) < 1 : break  #Check for empty line

    try:
        num = float(inp)
    except:
        print 'Invalid input'
        continue
