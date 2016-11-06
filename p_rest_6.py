
# coding: utf-8

# ## REST-6 : 2013년 1년 동안 지하철역 승하차 인원
# 
# * 먼저 key값을 받아온다.

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


# In[49]:

import os
import requests

_url='http://openAPI.seoul.go.kr:8088/'
_key=key[ 'dataseoul' ]
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon) #datatype변환 casting


# In[50]:

print _api


# In[51]:

_maxIter=3
_iter=0
while _iter<_maxIter:
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
    response = requests.get(url).text
    print response
    START_INDEX= str(int(START_INDEX)+10)
    END_INDEX= str(int(END_INDEX)+10)
    _iter+=1

