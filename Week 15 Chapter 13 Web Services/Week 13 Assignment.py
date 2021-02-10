import urllib
import xml.etree.ElementTree as ET


address = 'http://python-data.dr-chuck.net/comments_42.xml'

url = urllib.urlopen(address).read()
##print url

tree = ET.fromstring(url)
counts = tree.findall('.//count')
print counts

print 'count', tree.find('count').text



lst = tree.findall('comments/comment/count')
print 'Comment count:', len(lst)

print counts
print 'counts'/count

##while True:
##    address = raw_input('Enter url: ')
##    if len(address) < 1 : break
##
##    url = urllib.urlopen(address)
##    
##    tree = ET.fromstring(url)
##    print 'count', tree.find('count').text
####

##urllib and ET to open the data in the example http, when I create a list and then "findall('comments/comment/count') where I have a problem is with the and then print 'Comment count:', len(lstI get the following error

##------------------



##print 'Name:', tree.find('name').text




##print 'count:', tree.find('count').get('count')


##commentinfo = ET.fromstring(address)
##lst = commentinfo.findall(











##uh = urllib.urlopen(url)
##print uh
##data = uh.read()
##print data
####tree = ET.fromstring(url)
##print tree
##print 'count:', tree.find('count').get('count')




