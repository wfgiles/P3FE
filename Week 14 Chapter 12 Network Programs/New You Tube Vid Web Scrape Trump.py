import urllib
##import urllib.request
from bs4 import BeautifulSoup

theurl = "http://twitter.com/realDonaldTrump"
thepage = urllib.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
##print(soup.findAll('a')[0])
##SAME AS
print(soup.find('a'))


"""
for link in soup.findAll('a'):
    print (link.get('href'))
    print(link.text)

"""

print (soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)

i = 1
for tweets in soup.findAll('div',{"class":"content"}):
    print (i)
    print (tweets.find('p').text)
    i = i + 1

























