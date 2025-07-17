from flask import Flask, request, render_template_string
import requests, threading, time, random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>FB Post Commenter</title>
</head>
<body style="font-family:sans-serif;">
    <h2>Facebook Auto Commenter Tool</h2>
    <form method="POST">
        <label>Post ID (e.g. 1234567_89101112):</label><br>
        <input type="text" name="post_id" style="width: 400px;" required><br><br>

        <label>Access Tokens (one per line):</label><br>
        <textarea name="tokens" rows="6" cols="60" required></textarea><br><br>

        <label>Messages (one per line):</label><br>
        <textarea name="messages" rows="6" cols="60" required></textarea><br><br>

        <label>Time Delay (seconds):</label><br>
        <input type="number" name="delay" value="30" required><br><br>

        <input type="submit" value="Start Commenting">
    </form>
</body>
</html>
"""

success_page = """
<h3>✅ Comments started in background!</h3>
<p>You can close this tab. Tool is running...</p>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        post_id = request.form['post_id'].strip()
        tokens = [x.strip() for x in request.form['tokens'].splitlines() if x.strip()]
        messages = [x.strip() for x in request.form['messages'].splitlines() if x.strip()]
        delay = int(request.form['delay'])

        thread = threading.Thread(target=comment_loop, args=(post_id, tokens, messages, delay))
        thread.start()

        return success_page
    return render_template_string(HTML)

def comment_loop(post_id, tokens, messages, delay):
    index = 0
    while True:
        token = tokens[index % len(tokens)]
        message = random.choice(messages)
        url = f"https://graph.facebook.com/{post_id}/comments"
        payload = {
            'message': message,
            'access_token': token
        }
        try:
            r = requests.post(url, data=payload)
            res = r.json()
            if 'id' in res:
                print(f"[✓] Comment sent: {message}")
            else:
                print(f"[x] Failed with token: {token[:10]}... — {res}")
        except Exception as e:
            print(f"[!] Error: {e}")
        index += 1
        time.sleep(delay)

if __name__ == '__main__':
    app.run(debug=True)
