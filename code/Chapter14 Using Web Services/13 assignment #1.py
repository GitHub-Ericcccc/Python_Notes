# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:37:44 2018

@author: yxz796
"""

# 13 Assingment #1

import urllib.request, urllib.parse, urllib.error
import json
import ssl
import json

url0 = 'http://py4e-data.dr-chuck.net/comments_42.json'
url1 = 'http://py4e-data.dr-chuck.net/comments_72116.json'
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url1, context=ctx)
data = connection.read().decode()

js = json.loads(data)
for pair in js['comments']:
    num = pair['count']
    sum = sum + num

print(sum)
    
    