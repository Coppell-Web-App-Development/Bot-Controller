import twitter, os, json


# looks for config.json file for api credentials at root dir of project
# api credentials are on developer.twitter.com
# sign in as cwadbot and go under Apps > Bot Controller
# create config.json and store the credentials from "keys and tokens"
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

with open(config_path) as f:
    config = json.load(f)

api = twitter.Api(
    consumer_key=config["consumer_key"], 
    consumer_secret=config["consumer_secret"], 
    access_token_key=config["access_token_key"], 
    access_token_secret=config["access_token_secret"]
)

def post_message(msg):
    return api.PostUpdate(status=msg)