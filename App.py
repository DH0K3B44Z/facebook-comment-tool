from flask import Flask, render_template, request
import requests, time, random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hater = request.form["hater"]
        post_id = request.form["post_id"]
        delay = int(request.form["delay"])
        try:
            with open("comments.txt", "r") as f:
                comments = [c.strip() for c in f if c.strip()]
            with open("tokens.txt", "r") as f:
                tokens = [t.strip() for t in f if t.strip()]
        except:
            return "Error loading files."

        log = []
        token_index = 0
        for comment in comments:
            token = tokens[token_index % len(tokens)]
            url = f"https://graph.facebook.com/{post_id}/comments"
            headers = {"Authorization": f"Bearer {token}"}
            data = {"message": f"{comment} ~ {hater}"}
            r = requests.post(url, data=data, headers=headers)
            if r.status_code == 200:
                log.append(f"✅ Sent: {comment}")
            else:
                log.append(f"❌ Failed with token {token[:10]}...")

            token_index += 1
            time.sleep(delay)

        return "<br>".join(log)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
