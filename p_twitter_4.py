
import os
import twitter
import json

keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','twitter4j.properties')

f=open(keyPath,'r')
lines=f.readlines()

d=dict()
for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in lines:
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d
    
keyPath=os.path.join(os.getcwd(),'ProjectRoot\src','twitter4j.properties')
key=getKey(keyPath)

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)

q = '#seoul'
count = 200
max_id = '795328763802198017'
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']

f=open('ds_twitter_4.txt','w')
for i,tweet in enumerate(statuses):
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
    f.write("\n")
f.close()