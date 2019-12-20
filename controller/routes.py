from controller import app,bot
from flask import render_template,redirect

import random

b = bot.twitter_bot()

@app.route('/')
def index():
    return render_template('index.html',title='CWAD TWITTER BOT')

@app.route('/tweet')
def tweet():
    b.postTweet('This is a test %s' % random.randint(0,69))
    return redirect('/',code=302)
