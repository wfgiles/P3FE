

##FINDING THE TOP 10 MOST USED WORDS IN A FILE
##**KNOW EVERY LINE**

##fhand = open('romeo.txt')
##counts = dict()
##for line in fhand:
##    words = line.split()
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##
##lst = list()
##for key, val in counts.items():
##    lst.append((val, key))
##
##lst.sort(reverse=True)
##
##for val, key in lst[:10]:
##    print key, val
##-------------------------

##ASSIGNMENT 10.2
##fname = open('mbox-short.txt')
##counts = dict()
##for line in fname:
##    words = line.split()
##    if len(words) == 0 : continue
##    if words[0] != 'From' : continue
##    time = words[5]
##    hour = time[:2]
##    if hour not in counts:
##        counts[hour] = 1
##    else:
##        counts[hour] +=1
##
##clok = list()
##for kie, vaal in counts.items():
##    newtup = (kie, vaal)
##    clok.append(newtup)
##
##clok.sort()
##
##for kie, vaal in clok:
##    print kie, vaal

##----------------
##WORKED EXERCISES CH 10

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        wrd = word.lower()
        counts[wrd] = counts.get(wrd,0) + 1

flipped = list()
for kie, vaal in counts.items():
    newtup = (vaal,kie)
    flipped.append(newtup)

##print flipped
flipped.sort(reverse=True)

for kay, vall in flipped[:5]:
    print 'Winner',kay, vall














