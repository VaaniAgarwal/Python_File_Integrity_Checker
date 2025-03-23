import os
from flask import Flask,render_template,request,redirect,url_for,flash
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key='secret_key_of_the_person'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Oops! No file was selected. Please choose a file to upload.')
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename=='':
        flash('No file selected')
        return redirect(url_for('home'))
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    flash('file uploaded successfully')
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)