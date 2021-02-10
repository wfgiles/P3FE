import urllib
from BeautifulSoup import *
import re

url = 'http://python-data.dr-chuck.net/comments_44.html'
##http://python-data.dr-chuck.net/comments_44.html raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
y = re.findall('[0-9]+','tags')

numbers = []
numbers = number
print y


##for line in url:
##    print line9
##tags = soup('span')
##
##
##for tag in tags:
##    atpos = html.find('/')
##    print atpos #81
##  
##spos = atpos -3

##print spos
##
##
##
##    
####    y = re.findall('[0-9]+', tags)
####    print y

##----------------------------
##import urllib
##from BeautifulSoup import *
####import re
##
##url = 'http://python-data.dr-chuck.net/comments_44.html'
####http://python-data.dr-chuck.net/comments_44.html raw_input('Enter - ')
##
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
##tags = soup('comments')
##
##for tag in tags:
##    print tag
##    .get('comments>'+2)
##
##                
####
####
####
####
####
####
####
####
####
####for tag in tags:
####    atpos = html.find('/')
####    print atpos #81
####  
####spos = atpos -3
####print spos
####
##
##
##    
####    y = re.findall('[0-9]+', tags)
####    print y
