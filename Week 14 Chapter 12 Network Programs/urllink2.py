# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
##
##import urllib
##from BeautifulSoup import *
##
##url = raw_input('Enter - ')
##html = urllib.urlopen(url).read()
##soup = BeautifulSoup(html)
##
### Retrieve all of the anchor tags
##tags = soup('a')
##for tag in tags:
##    print tag.get('href', None)
##
##----------------------------
##find link at positon 3 - use split command
##follow link
##first name is 1
##repeat 4 times
##answer is last name retrieved

import urllib
from BeautifulSoup import *

count = 0
url = 'http://python-data.dr-chuck.net/known_by_Fikret.htmlraw_input'
##('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

##print soup
# Retrieve all of the anchor tags

tags = soup('a')
for tag in tags:
##    print tags[2]
        
    html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Fikret.html').read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
##        print tags[2]
        html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Fikret.html').read()
        soup = BeautifulSoup(html)
        print soup.get('href', None)

##tag 2 = http://python-data.dr-chuck.net/known_by_Montgomery.html







    
##print html


    
##    print tags[3]



    
##now just find names at position 3
##    count = count + 1
###    print count
##
##    if count < 5 :
##
##
####
##counts = dict()
##for line in html:
##    words = line.split()
##    print words
##    for word in words:
##        counts[word] = counts.get(word,0) + 1
##
##print counts


##    tag = tag.slice
##    print tag
####    print tag[1]


##Find the link at position 3 (the first name is 1). Follow that link.
##tags = soup('a')
##for tag in tags:
##    tag = tag.slice
##    print tag[1]
##    



##Extract the href= vaues from the anchor tags, scan for a tag
##that is in a particular position relative to the first name
##in the list, follow that link and repeat the process a number
##of times and report the last name you find.
##
##SAMPLE DATA
##http://python-data.dr-chuck.net/known_by_Fikret.html
##Find the link at position 3 (the first name is 1). Follow that link.
##Repeat this process 4 times. The answer is the last name that you retrieve.
##
##Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
##
##Last name in sequence: Anayah
##
##ASSIGNMENT DATA
##http://python-data.dr-chuck.net/known_by_Abar.html
##Find the link at position 18 (the first name is 1). Follow that link.
##Repeat this process 7 times. The answer is the last name that you retrieve.
##----------------
##Hint: The first character of the name of the last page that you will
##load is: C
    
##Strategy
##The web pages tweak the height between the links and hide the page after
##a few seconds to make it difficult for you to do the assignment without
##writing a Python program. But frankly with a little effort and patience
##you can overcome these attempts to make it a little harder to complete
##the assignment without writing a Python program. But that is not the point.
##The point is to write a clever Python program to solve the program.
##
##Sample execution
##
##Here is a sample execution of a solution:
##
##$ python solution.py 
##Enter URL: http://python-data.dr-chuck.net/known_by_Fikret.html
##Enter count: 4
##Enter position: 3
##Retrieving: http://python-data.dr-chuck.net/known_by_Fikret.html
##Retrieving: http://python-data.dr-chuck.net/known_by_Montgomery.html
##Retrieving: http://python-data.dr-chuck.net/known_by_Mhairade.html
##Retrieving: http://python-data.dr-chuck.net/known_by_Butchi.html
##Retrieving: http://python-data.dr-chuck.net/known_by_Anayah.html

