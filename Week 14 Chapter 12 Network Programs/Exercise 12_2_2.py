import urllib

counts = 0
url = raw_input('Enter a url: ')
fhand = urllib.urlopen(url)

##print url

for line in fhand:
    words = line.strip()
    for word in words:
        counts[word] = counts.get[word,0] + 1

print counts
