from flask import Flask, render_template, request, jsonify
import requests, time, threading, random

app = Flask(__name__)
log_data = []

def send_comment(token, post_id, comment):
    try:
        graph_url = f"https://graph.facebook.com/{post_id}/comments"
        response = requests.post(graph_url, data={
            'message': comment,
            'access_token': token
        })
        if response.status_code == 200:
            return True, "Comment sent successfully"
        else:
            return False, response.json().get('error', {}).get('message', 'Unknown Error')
    except Exception as e:
        return False, str(e)

def comment_worker(tokens, comments, post_id, haters, interval):
    i = 0
    while True:
        token = tokens[i % len(tokens)]
        comment = random.choice(comments)
        success, message = send_comment(token, post_id, f"{haters} {comment}")
        log_data.append(f"Token: {token[:5]}... | Comment: {comment} | Status: {message}")
        time.sleep(interval)
        i += 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global log_data
    if request.method == 'POST':
        tokens_file = request.files['tokens']
        comments_file = request.files['comments']
        haters = request.form['haters']
        post_id = request.form['post']
        interval = int(request.form['interval'])

        tokens = tokens_file.read().decode().splitlines()
        comments = comments_file.read().decode().splitlines()

        log_data = []
        t = threading.Thread(target=comment_worker, args=(tokens, comments, post_id, haters, interval))
        t.daemon = True
        t.start()

        return render_template('index.html', started=True, log=log_data)
    return render_template('index.html', started=False, log=log_data)

@app.route
