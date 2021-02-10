import urllib
from BeautifulSoup import *


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
##
##ANSWER - http://python-data.dr-chuck.net/known_by_Anayah.html
##
##OK GOT THE ANSWER - ON RIGHT TRACK!!!
##FU***** YAH!!!!!!
##NOW FIGURE HOW TO
##    COUNT 0 - 4
##    PRINT COUNT, POSITION, NAME

