import twitter, os, json

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

with open(config_path) as f:
    config = json.load(f)

api = twitter.Api(
    consumer_key=config["consumer_key"], 
    consumer_secret=config["consumer_secret"], 
    access_token_key=config["access_token_key"], 
    access_token_secret=config["access_token_secret"]
)