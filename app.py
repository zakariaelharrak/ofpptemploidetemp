from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/pdfs', methods=['GET'])
def download_pdf():
    class_name = request.args.get('class_name')
    if class_name:
        filename = f"{class_name}_idocc.pdf"
        return send_from_directory('pdfs', filename, as_attachment=False)
    else:
        print("error")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdfs/<class_name>')
def download_specific_pdf(class_name):
    filename = f"{class_name}_idocc.pdf"
    return send_from_directory('pdfs', filename, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
