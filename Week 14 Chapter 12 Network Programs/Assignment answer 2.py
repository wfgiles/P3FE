import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen(raw_input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")

print soup

spans = soup('span')

print spans

numbers = []

for span in spans:
    numbers.append(int(span.string))

print sum(numbers)


##http://www.python-data.dr-chuck.net/comments_44.html
