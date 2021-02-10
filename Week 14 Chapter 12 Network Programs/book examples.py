import urllib
from BeautifulSoup import *

url = raw_input('Enter- ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    #Look for the parts of a tag
    print 'TAG:', tag
    print 'URL:', tag.get('href', None)
    print 'Content:',tag.contents[0]
    print 'Attrs:',tag.attrs
    
