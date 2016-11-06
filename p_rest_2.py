
# coding: utf-8

# ## REST-2 : 키를 저장하고 읽기

# In[5]:

import os
keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','key.properties')
print keyPath


# In[6]:

f=open(keyPath,'r')
lines=f.readlines()
print lines


# In[7]:

d=dict()
for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()
print d


# In[9]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in lines:
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d


# In[10]:

keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','key.properties')
key=getKey(keyPath)


# In[13]:

print key['dataseoul']


# In[14]:

key['gokr']

