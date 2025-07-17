from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        token_path = request.form.get('token_path')
        message_path = request.form.get('message_path')
        thread_path = request.form.get('thread_path')
        time_interval = request.form.get('time_interval')
        haters_name = request.form.get('haters_name')

        with open('files/token.txt', 'w') as f:
            f.write(token_path.strip())
        with open('files/message.txt', 'w') as f:
            f.write(message_path.strip())
        with open('files/thread.txt', 'w') as f:
            f.write(thread_path.strip())
        with open('files/time.txt', 'w') as f:
            f.write(time_interval.strip())
        with open('files/haters.txt', 'w') as f:
            f.write(haters_name.strip())

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return 'Files saved successfully! You can now close this tab.'

if __name__ == '__main__':
    if not os.path.exists('files'):
        os.makedirs('files')
    app.run(debug=True)
