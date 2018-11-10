# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:20:21 2018

@author: yxz796
"""

# 13.1 Data on the web -web services

# Two types of serialization formats are XML adn JSON

# 13.2 XML

# eXtensible Markup Language

# Line ends do not matter. White space is generally discarded on text elements.
# We indent only to be readable.

# XML Basics

"""
<person>
 <name>Chunk</name>
 <phone type="intl">+1 216513216</phone>
 <email hide="yes"/>
</person>

"""

"""
Start Tag
    <person>
    <name>
    <phone type="intl">
End Tag
    </name>
    </phone>
    </person>
Text Content
    Chunk
    +1 216513216
Attribute
    hide="yes"
Self Closing Tag
    />
"""

"""
Tags 
    - indicate the beginning and ending of elements
Attributes 
    - Keyword/value pairs on the opening tag of XML
Serialize / De-Serialize 
    - Convert data in one program into a common format,
    that can be stored and/or transmitted between systems in a programming
    language-independent manner
"""

import xml.etree.ElementTree as ET
data = '''<person>
    <name>Eric</name>
    <phone type="intl">
        +44 07562 000000
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) 
# Why is it called fromstring?
# Because the data itself is a string! within triple quotes.
print('Name:', tree.find('name').text)
print('Atr:', tree.find('email').get('hide'))


import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input) # Stuff is a tree of information
lst = stuff.findall('users/user') # Search all user tags below users.
print(lst)
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
    
# Worked Exercise
# xml3.py

# 13.5 JavaScript Object Notation JSON
# A new serialization format.
print('http://jason.org')

# JSON represents data as nested lists and dictionaries.

import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

# JSON reads data with loads method.
# No start tags, no end tags and no attributes.
   
info = json.loads(data)
# info is a dictionary! with key-value pairs.
# Different from XML, json.loads(data) can be directly used in python.
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

# Example of a list

input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# 13.6 Service Oriented Approach
# Build a service layer to make data into one format for reuse in other service.
    
# 13.7 Using Application Programming Interfaces
# This is called API.
# API is the specification for what the URL patterns are, what the syntax of the data we are 
# supposed to send and what the syntax of data we can expect to get back,
    
# Example: Google Geocoding API
# https://developers.google.com/maps/documentation/geocoding/intro
    
# Example: geojson.py
    
# 13.8 Securing API Requests

# Google Geocoding API
# Twitter API
# Facebook API

# ===========
# Example: twitter2.py
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    # Because urllib eats the headers, so we need to get it from connection.
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']: 
        # js[users] is an array!!!
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
# ===========


# Example: hidden.py
# Example: twrul.py Twitter uses OAuth protocol for API Security.
        
# Quiz

"""
What library call do you make to append properly encoded parameters to the end of a URL like 
the following:

http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI   

ANSWER: urllib.parse.urlencode()

"""




