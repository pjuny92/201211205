
# coding: utf-8

# ## 11.02 MongoDB

# * client 만들기

# In[22]:

import pymongo
from pymongo import MongoClient
client=MongoClient('localhost:27017')


# In[11]:

from pymongo import MongoClient


# In[12]:

client=MongoClient('localhost:27017')


# In[23]:

db=client.Employees


# In[24]:

db.mytable.insert({
        "name":"jy"
    })


# In[32]:

empCol=db.mytable.find()


# In[33]:

type(empCol)


# In[34]:

for emp in empCol:
    print emp


# In[18]:

type(emp)


# In[19]:

emp['name']


# In[35]:

import os
KEY = "666568534139327035364559544c4c"
TYPE = 'json'
SERVICE = 'SearchSTNBySubwayLineService'
START_INDEX = '1'
END_INDEX = '10'
LINE_NUM = '2'


# In[36]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM


# In[37]:

import requests
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/SearchSTNBySubwayLineService/1/5/2/'
data=requests.get(myurl).text


# In[38]:

print data


# In[39]:

import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text


# In[40]:

import lxml
import lxml.etree
import StringIO

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text


# In[41]:

import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'


# In[42]:

_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    #print _api
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1

