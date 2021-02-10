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
##---------------------------
##RUBRIC TO SLOVING ASSIGNMANT 12.2
##once you have the value of tags[2]
##
##your urllib.urlopen line can go into your for loop
##
##acquire the value of the first desired tag
##
##printed that outside of the for loop
##
##then hand that value inside the for loop to the
##urllib.urlopen as you have above
##
##then repeate the process of reading the url, 
##
##passing it into BeautifulSoup, 
##
##looking for the 'a' tags, 
##
##reassigning that value as the new value of tags[2]
##
##then executing the 'someValue.get('href',None), where '
##someValue' is the new value of tags[2]. 
##
##print that out, and handed that url back into the
##urllib.urlopen function
##
##all within a 'for num in range(number)' loop, where number
##is the desired number of times for this to be performed.


##----------------------------


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

