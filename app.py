from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import subprocess


app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'password'

UPLOAD_FOLDER = 'main'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to get list of PDF files
def get_pdf_files():
    pdf_files = []
    for filename in os.listdir('renamed_pages'):
        if filename.endswith('.pdf'):
            pdf_files.append(filename[:-4])  # Remove .pdf extension
            pdf_files.sort()
    return pdf_files

@app.route('/renamed_pages', methods=['GET'])
def download_pdf():
    class_name = request.args.get('class_name')
    if class_name:
        filename = f"{class_name}.pdf"
        return send_from_directory('renamed_pages', filename, as_attachment=False)
    else:
        print("error")

@app.route('/')
def index():
    pdf_files = get_pdf_files()
    return render_template('index.html', pdf_files=pdf_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

@app.route('/run_scripts', methods=['POST'])
def run_scripts():
    # Execute clean.py
    subprocess.run(['python', 'clean.py'])

    # Execute split.py
    subprocess.run(['python', 'split.py'])
    
    # Execute rename.py
    subprocess.run(['python', 'rename.py'])
    
    print("scripts worked successfully")
    return render_template('admin.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            # If the username and password match, redirect to admin page
            return render_template('admin.html')
        else:
            # If the username and password don't match, redirect back to login page
            return render_template('login.html', message='Invalid username or password')
    else:
        # If it's a GET request, render the login page
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

# Made by Zakariae EL harrak https://www.linkedin.com/in/zakaria-elharrak/
