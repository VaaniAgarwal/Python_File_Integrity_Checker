import os
import psycopg2
import hashlib
from flask import Flask,render_template,request,redirect,url_for,flash
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key='secret_key_of_the_person'
DATABASE_URL="dbname=file_integrity_checker user=flask_user password=postgres host=localhost port=5432"
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
def get_db_connection():
    conn=psycopg2.connect(DATABASE_URL)
    return conn
def calculate_file_hash(file):
    hashes = hashlib.sha256()
    file.seek(0)
    for chunk in iter(lambda: file.read(4096),b""):
        hashes.update(chunk)
    file.seek(0)
    return hashes.hexdigest()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Oops! No file was selected. Please choose a file to upload.',category='error')
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename=='':
        flash('No file selected',category='error')
        return redirect(url_for('home'))
    file_hash = calculate_file_hash(file)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    try:
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("SELECT file_hash FROM file_hashes WHERE filename = %s", (file.filename,))
        existing_file = cur.fetchone()
        if existing_file:
            cur.execute("UPDATE file_hashes SET file_hash = %s, uploaded_at = CURRENT_TIMESTAMP WHERE filename = %s", (file_hash, file.filename))
            flash('File already existed, hash updated.',category='info')
        else:
            cur.execute("INSERT INTO file_hashes (filename, file_hash) values (%s, %s)", (file.filename, file_hash))
            flash('File uploaded and integrity check stored successfully.',category='success')
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        flash(f'Error storing file hash: {str(e)}',category='error')
    return redirect(url_for('home'))
@app.route('/check',methods=['POST'])
def check_integrity():
    if 'file' not in request.files:
        flash('Please select a file to check.',category='error')
        return redirect(url_for('home'))
    file=request.files['file']
    if file.filename=='':
        flash('No file selected',category='error')
        return redirect(url_for('home'))
    file_hash = calculate_file_hash(file)
    try:
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute("SELECT file_hash from file_hashes WHERE filename = %s",(file.filename,))
        result=cur.fetchone()
        cur.close()
        conn.close()
        if result:
            stored_hash=result[0]
            if file_hash==stored_hash:
                flash(f'Congrats!! File "{file.filename}" is unmodified.',category='success')
            else:
                flash(f'Danger!! File "{file.filename}" has been modified!',category='error')
        else:
            flash(f'No record found for "{file.filename}".',category='error')
    except Exception as e:
        flash(f'Error checking file integrity: {str(e)}',category='error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)