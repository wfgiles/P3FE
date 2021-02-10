##counts = dict()
##names = ['Bill', 'John', 'Bill', 'Mary', 'Alex', 'Jeb']
##for name in names:
##    if name not in counts:
##        counts[name] = 1
##    else:
##        counts[name] = counts[name] + 1
##print counts
##----------------
##counts = dict()
##names = ['Bill', 'John', 'Bill', 'Mary', 'Alex', 'Jeb']
##for name in names:
##    counts[name] = counts.get(name, 0) + 1
##print counts
##
##the line -
##counts[name] = counts.get(name, 0) + 1
##
##does the same thing as -
##if name not in counts:
##    counts[name] = 1
##else:
##    counts[name] = counts[name] + 1

##counts = {'chuck': 1, 'fred':42, 'jan':100}
##for key in counts:
##    print key, counts[key]


##jjj = {'chuck': 1, 'fred':42, 'jan':100}
##print list(jjj)
##print jjj.keys()
##print jjj.values()
##print jjj.items()

##jjj = {'chuck': 1, 'fred':42, 'jan':100}
##for key,value in jjj.items():
##    print key,value
##
##THIS PROGRAM FINDS THE MOST USED WORD IN  FILE

name = raw_input('Enter file name: ')
handle = open(name,'r')
text = handle.read()
words= text.split()

counts = dict()
for word in words:
    count[word] = counts.get(word,0) + 1

bigcount = 0
bigword = 0
for word,count in count.items():
    if bigcount is 0 or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount


























