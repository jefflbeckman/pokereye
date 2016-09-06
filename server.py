import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename




UPLOAD_FOLDER = '/home/app/www-server/uploads' 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    #POST request, save the given file to the uploads directory
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                    secure_filename(file.filename))
            file.save(filename)
            upload_file.last_file = filename
            return card_string_from_picture(filename)

@app.route('/last_file')
def last_file():
    #GET request, return the last uploaded file
    if hasattr(upload_file, 'last_file') and \
               os.path.isfile(upload_file.last_file):
        last_filename = os.path.basename(upload_file.last_file)
        return redirect('/uploads/' + last_filename)
    
    #First GET request fails if there hasn't been an upload yet, so 
    return redirect('/')

def card_string_from_picture(filename):
    return 'succesfully got ' + filename + '''
<p>it's probably not a 4 of spades'''

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/uploads/<path:path>')
def send_pic(path):
    return send_from_directory('uploads', path)

##
##  Main
##
if __name__ == "__main__":
  port = int(os.getenv('PORT',8000))
  app.run(host='0.0.0.0', port=port, debug=True)




