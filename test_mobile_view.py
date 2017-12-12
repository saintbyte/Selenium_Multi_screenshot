#!/usr/bin/env python
import urllib2 , urllib
import os
import lxml
from lxml import etree
from util import fullpage_screenshot
from selenium import webdriver
import time
mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities = chrome_options.to_capabilities())

url='http://xxxxxx.ru/sitemap.xml'
if not os.path.exists('sitemap.xml'):
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        fh = open('sitemap.xml','w')
        fh.write(data)
        fh.close()
    except:
        print 'cant download sitemap'
        quit()
tree = etree.parse('sitemap.xml')
for child in tree.getroot():
    print child[0].text
    url = child[0].text # may bugly please fix it
    if not (url[0:4].lower() == 'http'):
        print 'Error get url from element'
        continue
    filename = url
    filename = filename.replace('https://','')
    filename = filename.replace('http://','')
    filename = filename.replace('/','_')
    filename = filename.replace('?','_')
    filename = filename.replace('&','_')
    filename = filename.replace('.','_')
    filename = filename + '.png'
    driver.get(url)
    time.sleep(2)
    full_filename = os.path.join('screens',filename)
    fullpage_screenshot(driver, full_filename)
    time.sleep(2)
#print tree

