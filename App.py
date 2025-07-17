from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    token_file = request.files['token_file']
    comment_file = request.files['comment_file']
    post_id = request.form['post_id']
    hater_name = request.form.get('hater_name', '')
    time_interval = int(request.form.get('time_interval', '30'))

    token_path = os.path.join(UPLOAD_FOLDER, 'tokens.txt')
    comment_path = os.path.join(UPLOAD_FOLDER, 'comments.txt')

    token_file.save(token_path)
    comment_file.save(comment_path)

    # ✅ You can print/log or pass these to your logic
    print("Post ID:", post_id)
    print("Hater Name:", hater_name)
    print("Interval:", time_interval)

    # Your comment-sending logic will go here...
    return f"Comments sent to Post ID {post_id} successfully."

if __name__ == '__main__':
    app.run(debug=True)
