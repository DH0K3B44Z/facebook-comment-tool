from flask import Flask, request, render_template
import os
from engine import start_commenting

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        token_file = request.files.get('token_file')
        comment_file = request.files.get('comment_file')
        hater = request.form.get('hater')
        post_id = request.form.get('post_id')
        delay = request.form.get('delay')

        if not all([token_file, comment_file, hater, post_id, delay]):
            message = "❌ Please fill all fields and upload both files!"
        else:
            token_path = os.path.join(app.config['UPLOAD_FOLDER'], token_file.filename)
            comment_path = os.path.join(app.config['UPLOAD_FOLDER'], comment_file.filename)
            token_file.save(token_path)
            comment_file.save(comment_path)

            # Start the background commenting engine
            start_commenting(token_path, comment_path, post_id, int(delay), hater)

            message = "✅ Commenting started in background!"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    # ✅ Deployment fix for Render / Railway / Fly.io
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
