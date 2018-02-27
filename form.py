import json
from flask import Flask
from flask import url_for, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ru')
def rus():
    return render_template('ru_private.html')

@app.route('/en')
def eng():
    return render_template('en_private.html')

if __name__ == '__main__':
    app.run()
