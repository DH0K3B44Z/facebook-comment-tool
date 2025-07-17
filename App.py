from flask import Flask, render_template, request, redirect, url_for
import threading
import time
from datetime import datetime
from termcolor import colored
import random

app = Flask(__name__)

# Shared state
running = False
log_data = []

def log(message, status="info"):
    now = datetime.now().strftime("%H:%M:%S")
    color_map = {
        "success": "green",
        "error": "red",
        "info": "cyan",
        "warning": "yellow"
    }
    formatted = f"[{now}] {message}"
    log_data.append((formatted, color_map.get(status, "white")))
    print(colored(formatted, color_map.get(status, "white")))


def comment_worker():
    token_index = 0
    tokens = ["token1", "token2", "token3", "token4"]  # Dummy tokens
    messages = ["Nice post!", "Amazing!", "Loved it!", "🔥🔥🔥"]

    while running:
        token = tokens[token_index % len(tokens)]
        msg = random.choice(messages)

        try:
            log(f"Comment sent using Token #{token_index + 1} ({token[:5]}...)", status="success")
        except Exception as e:
            log(f"Failed to send comment with Token #{token_index + 1}: {e}", status="error")

        log("Waiting for next token rotation...", status="info")
        token_index += 1
        time.sleep(5)  # Simulate delay between comments


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start')
def start():
    global running
    if not running:
        running = True
        threading.Thread(target=comment_worker, daemon=True).start()
        log("Tool Started...", status="info")
    return redirect(url_for('index'))


@app.route('/stop')
def stop():
    global running
    running = False
    log("Tool Stopped.", status="warning")
    return redirect(url_for('index'))


@app.route('/console')
def console():
    return render_template("console.html", logs=log_data)


if __name__ == '__main__':
    app.run(debug=True)
