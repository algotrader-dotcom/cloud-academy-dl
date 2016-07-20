#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import time 
import pprint

from BeautifulSoup import BeautifulSoup
import urllib2
import re

def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass

# Initialize Firefox Browser
driver = webdriver.Remote(command_executor='http://192.168.175.220:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)   

# Browser Maximize
# driver.maximize_window()

# Login
driver.get("https://cloudacademy.com/login/")
email = driver.find_element_by_id('email')
password  = driver.find_element_by_id('password')

## Fill email & password
email.send_keys("ninhthuan82us@gmail.com")
password.send_keys("khoican123")

## Submit login
form = driver.find_element_by_id('login-form')
form.submit()

## Go admin content
driver.get("https://cloudacademy.com/cloud-computing/introduction-to-devops-course/")

html_page = driver.page_source
print html_page

#soup = BeautifulSoup(html_page)
#for div in soup.findAll('div', {'class': 'accordion-group'}):
#    for link in div.findAll('a'):
#    	print link.prettify(), "\n----------------------------------------------------\n"

WebDriverWait(driver, 120).until(ajax_complete,  "Timeout waiting for page to load")
	
## Sleep
print "Waiting..."
time.sleep(5)

#html_page = driver.page_source.encode('utf-8')

driver.quit()

