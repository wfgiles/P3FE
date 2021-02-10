##Write a program to read through a file and print the contents
##of the file (line by line) all in upper case.
##file = www.py4inf.com/code/mbox-short.txt


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print line
