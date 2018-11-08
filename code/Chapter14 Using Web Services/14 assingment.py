# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:19:01 2018

@author: yxz796
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

position = input('Enter the position of the page - ') or 18
posit = 1
times = input('Enter the times to repeat - ') or 7

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

url = input('Enter the URL - ') or 'http://py4e-data.dr-chuck.net/known_by_Jamaal.html'

for i in range(times):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    
# Find the specific position
    for tag in tags:
        url = tag.get('href', None)
        posit = posit + 1
        if posit > position:
            print(tag.get_text())
            posit = 1
            break

  