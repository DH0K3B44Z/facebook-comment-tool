from flask import Flask, render_template, request
import time
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    status = ""
    if request.method == 'POST':
        token = request.form.get('token')
        post_id = request.form.get('post_id')
        message = request.form.get('message')
        haters_name = request.form.get('haters_name')
        delay = float(request.form.get('delay') or 0)

        final_message = f"{message} {haters_name}"
        # Simulate sending
        status = f"✅ Comment sent to post ID: {post_id} with delay {delay}s and message: {final_message}"
        time.sleep(delay)

    return render_template('index.html', status=status)
