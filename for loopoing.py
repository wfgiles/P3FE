
fruit = 'banana'

fruit = 'banana'
for foot in fruit:  #foot could be any variable name
    print(foot)

fruit = 'banana'
if 'n' in fruit:   #IF STATEMENT WORKS! Prints 'thats 1'
    print('thats 1')

count = 0
fruit = 'banana'   #DOES NOT WORK
for 'n' in fruit:  #CAN NOT ASSIGN TO LITERAL!!
    count = count + 1
print("The number of letter 'n's' in fruit is", count)


"""
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

counta = 0
countn = 0
for letter in fruit:
    if letter == 'a':    #UNLIKE ABOVE FOR STATEMENT CAN USE IF
        counta = counta + 1
    if letter == 'n':
        countn = countn + 1
print("a's", counta)
print("n's", countn)

s = 'Monty Python'
print(s[0:4])

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

a = 'Hello'
b = 'There'
print(b + a)

c = a + ' ' + b
print(c)

fruit = 'banana'
if 'n' in fruit:
    print('thats 1')
    
fruit = 'banana'
for foot in fruit:  #foot could be any variable name
    print(foot)

count = 0
countn = 0
fruit = 'banana'
for 'n' in fruit:
    countn = countn + 1
print("The number of letter 'n's' in fruit is", countn)
"""
