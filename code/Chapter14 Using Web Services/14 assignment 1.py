# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:20:01 2018

@author: yxz796
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url1 = 'http://py4e-data.dr-chuck.net/comments_42.html'
url2 = 'http://py4e-data.dr-chuck.net/comments_72113.html'
html = urlopen(url2, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('span', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    sum = sum + int(tag.contents[0])
print(sum)