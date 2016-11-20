
import os
import twitter
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

q = '#Seoul'
count = 10
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']

for i,tweet in enumerate(statuses):
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])