import json
import urllib
import time
import rumps

USERID = 'subnaught'
POLL_INTERVAL = 60     #poll interval in seconds

QUERY_STRING = "https://hacker-news.firebaseio.com/v0/user/" + USERID + ".json"

class Narcissist(rumps.App):
    def __init__(self):
        super(Narcissist, self).__init__(type(self).__name__)

    @rumps.timer(POLL_INTERVAL)
    def poll_hn(sender, self):
        response = json.loads(urllib.urlopen(QUERY_STRING).read())
        karma = response['karma']
        sender.title = str(karma)
      
if __name__ == "__main__":
    Narcissist().run()

