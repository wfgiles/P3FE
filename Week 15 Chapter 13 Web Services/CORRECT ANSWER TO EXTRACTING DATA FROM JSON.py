##CORRECT ANSWER TO EXTRACTING DATA FROM JSON

import json
import urllib

sum = 0
url = 'http://python-data.dr-chuck.net/comments_168751.json'
uh = urllib.urlopen(url)
data = uh.read()

info = json.loads(data)

numlist = info['comments'][:]

for item in numlist:
    sum = sum + item['count']
print sum
##-------------------------   



##
##for items in comments:
##    print items




##    print[d['value'] for d in comments]




##for item in info:
##    print info['comments'][]['count']


##    print info['comments'][0]['count']

##for item in info:
##    print 'Name', item['name']
##    print 'Id', item['id']
##    print 'Attribute', item['x']

##    vals = item.values()
##    print value()
##    for item in info['comments']:
##        print value()
##---------------------------

##import json
##import urllib
##
##url = 'http://python-data.dr-chuck.net/comments_42.json'
##uh = urllib.urlopen(url)
##data = uh.read()
##print data
####lst = list()
##info = json.loads(data)

##print json.dumps(info, indent=4)

##for item in info:
##    print info['comments'][0]['count']
##----------------------

##    
##    vals = item.values()
##    print value()
##    for item in info['comments']:
##        print value()




    
##    
##    for item in item:
##        print(item[:])





              
##    for itm in item:
##        print 'next', itm[:]

##print info()['name']
##value = info[0]["count"]
##print value




##numlist = list()
##
##for item in info:
##    cou = info.value()
##
##    numlist.append(cou)
##    
##    print numlist
