from flask import Flask, url_for,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hahaha/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return "{}'s profile".format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile',username='Ganesh'))


with app.test_request_context():
    print(url_for('static', filename='style.css'))


