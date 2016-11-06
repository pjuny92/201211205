
# coding: utf-8

# ## REST-1 : ip주소에서 지역정보 알아내기

# In[1]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr


# In[2]:

import json
geojson=json.loads(geostr)
print "Whatis IP Address?"
print geojson['ip']


# In[3]:

country=geojson.get('country_code')
print "Whatis Country_Code?"
print country.decode('utf-8')


# In[4]:

for k,v in geojson.iteritems():
    print k,"\t: ",v

