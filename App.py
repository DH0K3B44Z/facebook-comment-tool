from flask import Flask, render_template, request
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    token_file = request.files.get('token_file')
    comment_file = request.files.get('comment_file')
    post_id = request.form.get('post_id')
    hatername = request.form.get('hatername')
    interval = float(request.form.get('interval', 1))

    if not all([token_file, comment_file, post_id, hatername]):
        return "Missing input fields."

    # Save uploaded files temporarily
    token_path = 'token_temp.txt'
    comment_path = 'comment_temp.txt'
    token_file.save(token_path)
    comment_file.save(comment_path)

    with open(token_path, 'r') as tf:
        tokens = [line.strip() for line in tf if line.strip()]
    with open(comment_path, 'r') as cf:
        comments = [line.strip() for line in cf if line.strip()]

    os.remove(token_path)
    os.remove(comment_path)

    print(f"[LOG] Starting commenting on post ID: {post_id}")
    for token in tokens:
        for comment in comments:
            print(f"[{time.strftime('%H:%M:%S')}] Token: {token} ➜ {comment} [To: {hatername}]")
            time.sleep(interval)

    return "✅ Comments Sent Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
