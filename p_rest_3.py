
# coding: utf-8

# ## REST-3 : 서울시 노선별 지하철역 목록 구하기

# In[15]:

import os
KEY = "666568534139327035364559544c4c"
TYPE = 'json'
SERVICE = 'SearchSTNBySubwayLineService'
START_INDEX = '1'
END_INDEX = '10'
LINE_NUM = '2'


# In[16]:

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


# In[17]:

import requests
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/SearchSTNBySubwayLineService/1/5/2/'
data=requests.get(myurl).text


# In[18]:

print data


# In[19]:

import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text


# In[20]:

import lxml
import lxml.etree
import StringIO

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text

