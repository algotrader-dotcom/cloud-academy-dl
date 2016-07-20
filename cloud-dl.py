#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import html
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import urllib, urllib2, cookielib
from urlparse import urlparse

# Declare variables
BASE_URL = "https://cloudacademy.com"
LIST = list()
USERNAME = "ninhthuan82us@gmail.com"
PASSWORD = "khoican123"

LOGIN_URL = "https://cloudacademy.com/login/"
URL = "https://cloudacademy.com/cloud-computing/introduction-to-devops-course/"

parser = urlparse(URL)
print parser

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
    		#print href
    		LIST.append(href)

for item in LIST:
    url = BASE_URL+item
    print item
    resp = opener.open(url)
    html_page = resp.read()
    soup = BeautifulSoup(html_page)
    for source in soup.findAll('source', {'type': 'video/mp4', 'data-res': '720p'}):
	    print source['src'] + '\n'