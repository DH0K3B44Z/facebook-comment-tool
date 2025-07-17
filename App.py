from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    chat_link = request.form.get('chat_link')
    message_file = request.files['message_file']
    delay = request.form.get('delay')

    if message_file:
        messages = message_file.read().decode('utf-8').splitlines()
        with open("messages.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(messages))

    with open("config.txt", "w") as f:
        f.write(f"{chat_link}\n{delay}")

    return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
