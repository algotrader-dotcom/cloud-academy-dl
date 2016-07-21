#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
print sys.argv
import requests
from lxml import html
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import urllib, urllib2, cookielib
from urlparse import urlparse
import os

###################################### Functions ######################################

# Make directory recursive
def mkdir_recursive(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

###################################### Functions ######################################
# Get URL Input
if (len(sys.argv) < 2 ):
	print "Usage: python2.7 cloud-dl.py https://cloudacademy.com/cloud-computing/introduction-to-devops-course"
	sys.exit()

URL = str(sys.argv[1])

# Declare global variables
BASE_DIR = "cloud-academy"
BASE_URL = "https://cloudacademy.com"
LIST = list() # List urls video lesson of course

USERNAME = "your-emaill@gmail.com"
PASSWORD = "*****"

LOGIN_URL = "https://cloudacademy.com/login/"
#URL = "https://cloudacademy.com/cloud-computing/introduction-to-devops-course"

parser = urlparse(URL)
COURSE_DIR = BASE_DIR + parser.path

print "Start creating directory course at: " + '"'+ COURSE_DIR + '"'
mkdir_recursive(COURSE_DIR)

# Initilize session login
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'email' : USERNAME, 'password' : PASSWORD})
opener.open('https://cloudacademy.com/login/', login_data)
resp = opener.open(URL)
html_page = resp.read()

# Process data response
soup = BeautifulSoup(html_page)
for div in soup.findAll('div', {'id': 'course-contents'}):
    for link in div.findAll('a'):
    	href = link.get('href')
    	if (href.endswith('.html')):
    		LIST.append(href)

for item in LIST:
    url = BASE_URL+item
    item_list = item.split('/')
    last_item = item_list[-1]
    filename = last_item[:-4] + 'mp4'


    resp = opener.open(url)
    html_page = resp.read()
    soup = BeautifulSoup(html_page)
    for source in soup.findAll('source', {'type': 'video/mp4', 'data-res': '720p'}):
	    print 'Start downloading file: ' + filename
	    full_filename = os.path.join(COURSE_DIR,filename)
	    urllib.urlretrieve(source['src'],full_filename)

    print '\n'
