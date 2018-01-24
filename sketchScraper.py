import requests
import urllib
import os
from bs4 import BeautifulSoup

home = os.getcwd()

print "[*] Fetching Page"
dpage = requests.get("https://www.sketchup.com/download/all")

if dpage.status_code / 100 != 2:
	print "boooooo wendy testaburger, request failed!"
else:
	print "[*] Request Successful\n"

soup = BeautifulSoup(dpage.content, 'html.parser')

print "[*] Scraping Relevant Content"

links = []
for link in soup.find_all('a'):
	if not link.get('href'):
		continue
	if '.dmg' in link.get('href') or '.exe' in link.get('href'):
		links.append(str(link.get('href')))

print "[*] Building Directory Structure"

for i in links:
	rel = i.split('dl.trimble.com')[1].split('/')
	rel.pop(0)
	curr_dir = ''
	for j in rel:
		print j
		curr_dir = os.path.join(curr_dir, j)
		print curr_dir
		if 'exe' in j or 'dmg' in j:
			urllib.urlretrieve(i, curr_dir)			
		else:
			if os.path.isdir(curr_dir):
				continue
			else:
				print "here*****"
				os.mkdir(curr_dir)	

print len(links)
