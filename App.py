from flask import Flask, render_template, request, redirect, url_for
import requests, time, random
from datetime import datetime
import threading

app = Flask(__name__)
LOGS = []

def comment_loop(token, post_id, messages, interval):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    while True:
        for msg in messages:
            data = {'message': msg}
            url = f"https://graph.facebook.com/v18.0/{post_id}/comments"
            res = requests.post(url, headers=headers, data=data)
            now = datetime.now().strftime('%H:%M:%S')
            if res.status_code == 200:
                LOGS.append((f"[{now}] ✅ Comment sent: {msg}", 'success'))
            else:
                LOGS.append((f"[{now}] ❌ Failed: {res.text}", 'fail'))
            time.sleep(interval)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        token = request.form['token']
        post_id = request.form['post_id']
        message = request.form['messages']
        interval = int(request.form['interval'])

        messages = message.splitlines()

        t = threading.Thread(target=comment_loop, args=(token, post_id, messages, interval))
        t.daemon = True
        t.start()

        return redirect(url_for('console'))
    return render_template('index.html')

@app.route('/console')
def console():
    return render_template('console.html', logs=LOGS[-50:])

if __name__ == '__main__':
    app.run(debug=True)
