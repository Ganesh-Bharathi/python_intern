from flask import Flask, render_template, request, make_response, url_for, redirect
from werkzeug.utils import secure_filename
import os
import glob
import time
app = Flask(__name__)

# @app.route('/')
# def samp():
#     return "HIHIHI"
pathname = 'D:/Python/flask_sample/uploads/'

"""
THIS IS TYPE 1..........
USING COOKIES
"""


@app.route('/')
def red():
        return redirect('/upload')


@app.route('/upload')
def upload():
        return (render_template("file_upload.html"))


@app.route('/uploader', methods=['GET', 'POST'])
def uploadsad():
    if request.method == 'POST':
        f = request.files['file']
        nm = secure_filename(f.filename)
        f.save(pathname+nm)
        resp = make_response(render_template("file_details.html"))
        resp.set_cookie('name', nm)
        return resp


@app.route('/size', methods=['GET', 'POST'])
def d_size():
    if request.method == 'POST':
        os.chdir(pathname)
        nm = request.cookies.get('name')
        ob = os.stat(nm)
        s = ob.st_size
        size = " Size is "+str(s)+' Bytes'
        return size


@app.route('/date', methods=['GET', 'POST'])
def d_date():
    if request.method == 'POST':
        os.chdir(pathname)
        nm = request.cookies.get('name')
        ob = os.stat(nm)
        t = ob.st_mtime
        date_mod = " Date modified: {0}-{1}-{2}".format(str((time.localtime(t).tm_mday)), str((time.localtime(t).tm_mon)), str((time.localtime(t).tm_year)))
        return(date_mod)


@app.route('/lines', methods=['GET', 'POST'])
def d_lines():
    if request.method == 'POST':
        os.chdir(pathname)
        nm = request.cookies.get('name')
        lines = 0
        fob = open(nm, 'r')
        for i in fob:
            lines = lines+1
        return(" Lines: "+str(lines))


@app.route('/all', methods=['GET', 'POST'])
def d_all():
    if request.method == 'POST':
        return(d_date() + d_lines() + d_size())


# OR

"""
THIS IS TYPE 2..........
USING GLOBAL
"""

"""
@app.route('/upload')
def upload():
        return (render_template("file_upload.html"))


@app.route('/uploader',methods=['GET','POST'])
def uploadsad():
    if request.method=='POST':
        f = request.files['file']
        global nm
        nm=f.filename
        f.save(pathname+nm)
        return (render_template('file_details.html'))


@app.route('/size', methods=['GET','POST'])
def d_size():
    if request.method=='POST':
        os.chdir(pathname)
        ob=os.stat(nm)
        s = ob.st_size
        size = " Size is "+str(s)+' Bytes'
        return size
        

@app.route('/date',methods=['GET','POST'])
def d_date():
    if request.method=='POST':
        os.chdir(pathname)
        ob=os.stat(nm)
        t = ob.st_mtime
        date_mod = " Date modified: {0}-{1}-{2}".format(str((time.localtime(t).tm_mday)), str((time.localtime(t).tm_mon)), str((time.localtime(t).tm_year)))
        return(date_mod)


@app.route('/lines',methods=['GET','POST'])
def d_lines():
    if request.method=='POST':
        os.chdir(pathname)
        lines=0
        fob = open(nm,'r')
        for i in fob:
            lines=lines+1
        return(" Lines: "+str(lines))


@app.route('/all',methods=['GET','POST'])
def d_all():
    if request.method=='POST':
        return( d_date() + d_lines() + d_size() )
"""