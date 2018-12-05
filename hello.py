from flask import Flask
app = Flask(__name__)

@app.route('/joker')
def hello_():
    return ('Hello, World hai!')