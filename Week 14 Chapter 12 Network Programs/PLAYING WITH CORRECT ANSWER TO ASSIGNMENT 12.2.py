import urllib
from BeautifulSoup import *

'''
Jamie Recommends- a simple loop x times

count = 4
for x in range (0, count):
print "Woohoo!"

'''

url ='http://python-data.dr-chuck.net/known_by_Fikret.html'
##raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


tags = soup('a')
for tag in tags:
    t = tags[2]

url ='http://python-data.dr-chuck.net/known_by_Fikret.htmlraw_input'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
##print t

url = 'http://python-data.dr-chuck.net/known_by_Montgomery.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[2]
##    print t

url = 'http://python-data.dr-chuck.net/known_by_Mhairade.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[2]
##    print t

url = 'http://python-data.dr-chuck.net/known_by_Butchi.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[2]
    print t
