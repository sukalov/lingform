import json
from flask import Flask
from flask import url_for, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rus')
def rus():
    return render_template('rus.html')

@app.route('/eng')
def eng():
    return render_template('eng.html')

if __name__ == '__main__':
    app.run()
