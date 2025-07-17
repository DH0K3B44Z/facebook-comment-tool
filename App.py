from flask import Flask, request, render_template_string, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    with open('index.html', 'r') as f:
        return render_template_string(f.read())

@app.route('/upload', methods=['POST'])
def upload():
    token = request.files['token_file']
    postid = request.files['postid_file']
    comment = request.files['comment_file']
    haters_name = request.form.get('haters_name', '').strip()
    interval = request.form.get('interval', '').strip()

    # Save files
    token.save(os.path.join(UPLOAD_FOLDER, 'tokens.txt'))
    postid.save(os.path.join(UPLOAD_FOLDER, 'postids.txt'))
    comment.save(os.path.join(UPLOAD_FOLDER, 'comments.txt'))

    # Save extra inputs
    with open(os.path.join(UPLOAD_FOLDER, 'hatersname.txt'), 'w') as f:
        f.write(haters_name if haters_name else 'None')

    with open(os.path.join(UPLOAD_FOLDER, 'interval.txt'), 'w') as f:
        f.write(interval if interval else '60')

    return '''
    <h2 style="text-align:center; color:lime;">✅ Submitted Successfully!</h2>
    <p style="text-align:center;"><a href="/">⬅️ Go Back</a></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
