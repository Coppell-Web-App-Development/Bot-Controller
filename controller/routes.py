from controller import app
from flask import render_template, request, jsonify
import controller.bot


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/post_message', methods=['POST'])
def post_message():
    if request.method == 'POST':
        message = request.form['message']
        try:
            twitter_status = controller.bot.post_message(msg=message)
            text = twitter_status.__dict__['text']
        except:
            return render_template('index.html', error=True)
        return render_template('index.html', success=True, msg=text)