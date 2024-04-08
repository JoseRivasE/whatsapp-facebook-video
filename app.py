from flask import Flask, request, jsonify
from test import Ultrawebhook
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = Ultrawebhook(request.json)
        return bot.processing()

if(__name__) == '__main__':
    app.run()