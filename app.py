from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import subprocess
import os.path
import time



app = Flask(__name__)

USERNAME = os.environ.get('MY_APP_USERNAME')
PASSWORD = os.environ.get('MY_APP_PASSWORD')

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
    last_lunch_time = get_last_lunch_time()
    return render_template('index.html', pdf_files=pdf_files, last_lunch_time=last_lunch_time)

def get_last_lunch_time():
    # Check if the timestamp file exists
    if os.path.exists('last_lunch.txt'):
        # If the file exists, read the last lunch time from it
        with open('last_lunch.txt', 'r') as file:
            last_lunch_time = file.read()
    else:
        # If the file does not exist, set the last lunch time to None
        last_lunch_time = None
    
    return last_lunch_time

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
    with open('last_lunch.txt', 'w') as file:
     file.write(time.strftime('%Y-%m-%d'))
    app.run(debug=True)
    

# Made by Zakariae EL harrak https://www.linkedin.com/in/zakaria-elharrak/
