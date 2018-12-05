from flask import Flask,abort, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    print("shhhhhhhhhhhhhhhhhhhhhhh")
    abort(404)
    return "this_is_never_executed()"


@app.errorhandler(404)
def page_not_found(error):
    return "Page illa yaaeeeee", 404

@app.errorhandler(401)
def unauthorised(error):
    return "Die heyyyy", 401