import twitter, os, json
import re
import random
from flask import Flask

class twitter_bot:
    def __init__(self, config_file="config.json"):
        self.config_path = config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_file)
        # self.config=None
        with open(self.config_path) as f:
            self.config = json.load(f)
        self.api = twitter.Api(
            consumer_key=self.config["consumer_key"], 
            consumer_secret=self.config["consumer_secret"], 
            access_token_key=self.config["access_token_key"], 
            access_token_secret=self.config["access_token_secret"]
        )
    def getTimeline(self,screen_name='potus'):
        user = self.api.GetUser(screen_name = screen_name)
        return [s.text for s in self.api.GetUserTimeline(user.id)]
    def postTweet(self,content):
        status = self.api.PostUpdate(content)
        return status
    def isVowel(self,t):
        return t.lower() == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u'
    def owoify(self,text):
        faces = ['OwO', 'UwU','>w<','^w^','-w-',';; w ;;']
        for c in range(len(text)-1):
            if(text[c].lower() == 'r' and isVowel(text[c+1])):
                text = text[:c] + 'w' + text[c+1:]
            elif((isVowel(text[c]) and text[c+1].lower() == 'r')):
                text = text[:c+1] + 'w' + text[c+2:]
            elif(text[c].lower() == 'n' and isVowel(text[c+1])):
                text = text[:c] + 'ny' + text[c+1:]
            elif(text[c].lower() == 'l'):
                text = text[:c] + 'w' + text[c+1:]
        return re.sub('!',' ' + faces[random.randint(0,len(faces)-1)],text) + ' nya~'

tb = twitter_bot()
