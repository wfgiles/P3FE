

fhand = open('romeo.txt')
lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
        else:
            continue

lst.sort
print(lst)
