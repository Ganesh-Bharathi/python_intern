from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/welcome', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['uname'],request.form['pas']):
            return (render_template("loggedin.html", name=request.form['uname']))
        else:
            return 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')

def valid_login(un,pa):
    if un=='ganeshbharathi1' and pa=="It'smypc":
        return True
    else:
        return False