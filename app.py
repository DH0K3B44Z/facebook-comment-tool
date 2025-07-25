from flask import Flask, render_template_string, request, redirect, url_for
import threading
import time
import os

app = Flask(__name__)

is_running = False
comment_thread = None

# HTML UI
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Facebook Comment Tool</title>
</head>
<body style="font-family: Arial; text-align: center; padding: 40px;">
    <h1>📝 Facebook Auto Comment Tool</h1>
    {% if not is_running %}
    <form method="post" action="/start">
        <input type="text" name="access_token" placeholder="Access Token" required><br><br>
        <textarea name="message" placeholder="Enter your message..." rows="5" cols="40" required></textarea><br><br>
        <input type="submit" value="🚀 Start Commenting">
    </form>
    {% else %}
    <form method="post" action="/stop">
        <p><strong>Auto-commenting is running...</strong></p>
        <input type="submit" value="⛔ Stop">
    </form>
    {% endif %}
</body>
</html>
"""

# Fake commenting loop
def auto_comment(access_token, message):
    while is_running:
        print(f"[✔] Sending comment: '{message}' with token: {access_token[:10]}...")
        time.sleep(5)  # Simulated delay between comments

@app.route("/", methods=["GET"])
def index():
    return render_template_string(template, is_running=is_running)

@app.route("/start", methods=["POST"])
def start():
    global is_running, comment_thread

    access_token = request.form["access_token"]
    message = request.form["message"]

    if not is_running:
        is_running = True
        comment_thread = threading.Thread(target=auto_comment, args=(access_token, message))
        comment_thread.start()

    return redirect(url_for("index"))

@app.route("/stop", methods=["POST"])
def stop():
    global is_running
    is_running = False
    return redirect(url_for("index"))

# ✅ Deployment-friendly entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
