##PRACTICE DATA
##
##import urllib
##from BeautifulSoup import *
##
##url = 'http://python-data.dr-chuck.net/comments_44.html'
####http://python-data.dr-chuck.net/comments_44.html raw_input('Enter - ')
##
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
##spans = soup('span')
##
##count = 0
##numbers = []
##
##for span in spans:
##    count = count + 1
##    numbers.append(int(span.string))
##
##print 'Count', count
##print 'Sum', sum(numbers)
##
##ANSWER:
##Enter - http://python-data.dr-chuck.net/comments_42.html
##Count 50
##Sum 2482
##
##----------------------------
##ACTUAL ASSIGNMENT DATA

##ANSWER:
##Enter - http://python-data.dr-chuck.net/comments_168750.html
##Count
##Sum (ENDS IN 19)
##
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
##http://python-data.dr-chuck.net/comments_44.html raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

spans = soup('span')

count = 0
numbers = []

for span in spans:
    count = count + 1
    numbers.append(int(span.string))

print 'Count', count
print 'Sum', sum(numbers)
##
##CORRECT!!!!!!!!!!!!!!!!!!!!!!!
##Count 50
##Sum 2319
