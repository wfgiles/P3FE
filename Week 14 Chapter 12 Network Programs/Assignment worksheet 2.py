##import urllib
##from BeautifulSoup import *

##import re
##
##url = 'http://python-data.dr-chuck.net/comments_44.html' ##http://python-data.dr-chuck.net/comments_44.html raw_input('Enter - ')
##
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
##tags = soup('span')
##for tag in tags:
##    if re.search('\S*\\span\S+',tag):
##        print tag
##    
##for line in html:
##    line = line.strip()
##    line = line.find('0-9')
##    if re.search('\S*\\span\S+',line):
##        print line
    
##------------------------
import urllib
import BeautifulSoup

page = urllib.urlopen(raw_input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

print(sum(numbers))
##----------------------
##from HTMLParser import HTMLParser
##
##
##HTMLParser.feed(http://www.python-data.dr-chuck.net/comments_44.html)






