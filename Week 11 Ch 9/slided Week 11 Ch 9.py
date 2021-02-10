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

##name = raw_input('Enter file:')
##handle = open(name)
##text = handle.read()
##words = text.split()
##
##counts = dict()
##for word in words:
##   counts[word] = counts.get(word,0) + 1
##
##bigcount = None
##bigword = None
##for word,count in counts.items():
##    if bigcount is None or count > bigcount:
##        bigword = word
##        bigcount = count
##
##print bigword, bigcount
























