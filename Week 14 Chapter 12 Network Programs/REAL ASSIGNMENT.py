import urllib
from BeautifulSoup import *


url = 'http://python-data.dr-chuck.net/known_by_Abar.html'
##raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t

url ="http://python-data.dr-chuck.net/known_by_Maaz.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t


url = "http://python-data.dr-chuck.net/known_by_Lennox.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t

url = 'http://python-data.dr-chuck.net/known_by_Aamna.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t

url = 'http://python-data.dr-chuck.net/known_by_Jessie.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t


url = 'http://python-data.dr-chuck.net/known_by_Rehan.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
##    print t

url = 'http://python-data.dr-chuck.net/known_by_Brett.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    t = tags[17]
    print t
##
##url = 'http://python-data.dr-chuck.net/known_by_Karleigh.html'
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
##tags = soup('a')
##for tag in tags:
##    t = tags[18]
####    print t
##
##url = 'http://python-data.dr-chuck.net/known_by_Tracey.html'
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
##tags = soup('a')
##for tag in tags:
##    t = tags[18]
##    print t
