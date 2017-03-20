import urllib2
import re
website  = urllib2.urlopen("https://dir.indiamart.com/impcat/mens-suits.html")
html = wesite.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)

//check
//checked working
print links

//for backup got the links in  the file
f = open("in_backup_links.txt", "w")
for i in links:
	f.write(str(i))
f.close()

//the func is not to be used in gen only once to be run  to create the backup


// parsing each link for data using beutiful soup

//import beatiful soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for i in links:
	print(soup.prettify())

