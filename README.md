# Bot-Controller
A controller interface for CWAD twitter bot.

# Tutorial

First thing to note is that this is just a like a console for you to post something on twitter remotely.
We will be using flask to do this relatively simple task. I have already uploaded a completed example in
the master branch so you can test it out. However, if you want to do it yourself, I suggest you start from
scratch by recreating the whole project structure. I want you to get used to the layout of this to get a 
better understanding of the back end code. Compare your code with master branch code. Please follow through
the master branch and understand what it does.

## Dependencies
pip3 install the following:
-flask
-python-twitter

## Project Structure

Make the project directory like this:

```

Project/

| --- controller/
|    | --- __init__.py 
|    | --- bot.py
|    | --- routes.py
|    | --- templates/
|    |    | --- index.html
|    | --- static/
|    |    | ---  style.css
| --- config.json
| --- run.py

```

## config.json

Contains API credentials for our bot. Go to developer.twitter.com, sign in as our bot account, go under 
Apps > Bot Controller > Keys and Tokens, and paste the credentials in the json file to access Twitter.
JSON files follow key-value pair notation. 
Ex: 

```
{
  "consumer_key": "paste in consumer key",
  "consumer_secret": "paste in consumer secret",
  ....
}
```

## run.py 

Our main starting place for the flask app. Just copy and paste from master branch. Execute this on
terminal to run the server.

## controller/

This is the main project python package.

## controller/__init__.py

Initializes the package when imported, copy content from master branch.

## controller/routes.py

Where the routes are defined and handles incoming requests. 

## bot.py 

Contains code for using Twitter's API. This is where you will define functions for use by routes.py
for interacting with the front end.

## controller/templates/

HTML files. Just copy from master branch.

## controller/static/

CSS, Javascripts, and other static files for reference by templates. Just copy from master branch.
