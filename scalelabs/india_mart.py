import urllib2
import re
website  = urllib2.urlopen("https://dir.indiamart.com/impcat/mens-suits.html")
html = website.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)

#//check
#//checked working
print links

#//for backup got the links in  the file
f = open("in_backup_links.txt", "w")
for i in links:
	f.write(str(i))
f.close()

#//the func is not to be used in gen only once to be run  to create the backup


#// parsing each link for data using beutiful soup

#//import beatiful soup
from bs4 import BeautifulSoup

#soup = BeautifulSoup("<html>data</html>")
for i in links:
	soup = BeautifulSoup(urllib2.urlopen((str(i[0]))))
	#//print(soup.prettify())
	divs =soup.find_all("div", { "class" : "pr10 f1 fs18"})                                       
	for j in divs:
		print j


