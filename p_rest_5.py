
# coding: utf-8

# ## REST-5: 2015년 서울시 지하철역별 월별 승하차인원 구하기

# In[21]:

import os
keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','key.properties')
print keyPath


# In[22]:

f=open(keyPath,'r')
lines=f.readlines()
print lines


# In[23]:

d=dict()
for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()
print d


# In[24]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in lines:
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d


# In[26]:

keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','key.properties')
key=getKey(keyPath)


# In[31]:

KEY=key['dataseoul']
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='10'
USE_MON='201512'


# In[32]:

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
url+=USE_MON


# In[37]:

import requests
import lxml
import lxml.etree
data = requests.get(url).text
tree=lxml.etree.fromstring(data.encode('utf-8'))
print data


# In[38]:

import re
p=re.compile('<SUB_STA_NM>(.+?)</SUB_STA_NM>')
res=p.findall(data)
for item in res:
    print item

