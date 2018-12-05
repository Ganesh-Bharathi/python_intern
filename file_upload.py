from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def samp():
    return "HIHIHI"
    
@app.route('/upload')
def upload():
    # return "welcomke"
        return (render_template("file_upload.html"))

@app.route('/uploader',methods=['GET','POST'])
def uploadsad():
    if request.method=='POST':
        f = request.files['file']
        f.save("D:/Python/flask_sample/uploads/"+secure_filename(f.filename))
    return "FILE UPLOADED"
