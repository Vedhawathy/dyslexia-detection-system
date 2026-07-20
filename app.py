from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('admin_login.html')

@app.route('/prediction')
def prediction():
    return render_template('webcam.html')

