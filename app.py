from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Function to get list of PDF files
def get_pdf_files():
    pdf_files = []
    for filename in os.listdir('renamed_pages'):
        if filename.endswith('.pdf'):
            pdf_files.append(filename[:-4])  # Remove .pdf extension
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

if __name__ == '__main__':
    app.run(debug=True)

# Made by Zakariae EL harrak https://www.linkedin.com/in/zakaria-elharrak/
