
# coding: utf-8

# ## REST-4: 서울시 외국인 주민 자녀 국적취득 년도별 시군구 합계 구하기

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


# In[27]:

KEY=key['dataseoul']
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX='1'
END_INDEX='10'


# In[28]:

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


# In[29]:

import requests
data = requests.get(url).text


# In[30]:

import re
p=re.compile('<STATMAN>(.+?)</STATMAN>')
res=p.findall(data)
for item in res:
    print item

