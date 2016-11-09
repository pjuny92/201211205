
# coding: utf-8

# ## T-1: Twitter에 'Hello World'를 쓴다.

# In[1]:

import os
keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','twitter4j.properties')
print keyPath


# In[2]:

f=open(keyPath,'r')
lines=f.readlines()
print lines


# In[3]:

d=dict()
for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()
print d


# In[4]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in lines:
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d


# * os.path.expanduser("~") 현재 home 디렉토리로 가는것이다.

# In[5]:

keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','twitter4j.properties')
key=getKey(keyPath)


# In[6]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[7]:

_client.statuses.update(status="My Exam Data 16.11.09")


# ## T-2: 자신의 타임라인 가져오기

# In[8]:

from pymongo import MongoClient
_mclient=MongoClient()


# * 저장할 DB를 만든다.

# In[9]:

_mclient['ds_twitter']


# In[10]:

_db=_mclient.ds_twitter
_col=_db.home_timeline


# In[11]:

home_timeline = _client.statuses.home_timeline()


# * 0번째 텍스트를 가져온다. 가장 최근에 올린것이 0번!! 
# * 숫자가 커질수록 내가 예전에 올렸던 글들이다.

# In[16]:

home_timeline[0]['text']


# * 지금 내 타임란인에 글이 몇개 있는지 알려준다.

# In[17]:

len(home_timeline)


# In[18]:

print home_timeline


# In[19]:

for tweet in home_timeline:
    print tweet['id'],tweet['text']


# In[20]:

for tweet in home_timeline:
    print tweet['id'],tweet['text']
    _col.insert_one(tweet)

