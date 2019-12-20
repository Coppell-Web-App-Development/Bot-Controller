from controller import app,bot
from flask import render_template,redirect,request

import random

b = bot.twitter_bot()

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',title='CWAD TWITTER BOT')

@app.route('/tweet', methods=['POST'])
def tweet():
    if request.form.get('owoify'):
        b.postTweet(b.owoify(request.form['content']))
    else:
        b.postTweet(request.form['content'])
    return redirect('/',code=302)
