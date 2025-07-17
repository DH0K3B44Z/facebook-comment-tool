from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        for filetype in ['tokens', 'messages', 'threads']:
            uploaded_file = request.files.get(filetype)
            if uploaded_file and uploaded_file.filename:
                uploaded_file.save(os.path.join(UPLOAD_FOLDER, f"{filetype}.txt"))
        message = '✅ Files uploaded successfully!'
    return render_template('index.html', message=message)

@app.route('/start')
def start():
    return '🚀 Started (Add your backend script logic here)'

@app.route('/stop')
def stop():
    return '🛑 Stopped (Add logic to stop your process)'

if __name__ == '__main__':
    app.run(debug=True)
