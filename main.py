import json
import urllib
import time

USERID = 'subnaught'
POLL_INTERVAL = 60     #poll interval in seconds

QUERY_STRING = "https://hacker-news.firebaseio.com/v0/user/" + USERID + ".json"

while True:
  response = json.loads(urllib.urlopen(QUERY_STRING).read())
  karma = response['karma']
  print karma
  time.sleep(POLL_INTERVAL)    
