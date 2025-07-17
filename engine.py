import requests
import time
import threading
from datetime import datetime

def post_comment(token, post_id, message):
    url = f"https://graph.facebook.com/{post_id}/comments"
    payload = {
        'message': message,
        'access_token': token
    }
    try:
        r = requests.post(url, data=payload)
        return r.status_code == 200, r.text
    except Exception as e:
        return False, str(e)

def start_commenting(token_file, comment_file, post_id, delay, hater):
    def run():
        with open(token_file, 'r') as tf:
            tokens = [x.strip() for x in tf if x.strip()]

        with open(comment_file, 'r') as cf:
            comments = [x.strip() for x in cf if x.strip()]

        token_index = 0
        comment_index = 0

        while True:
            token = tokens[token_index % len(tokens)]
            comment = comments[comment_index % len(comments)]

            final_comment = f"{comment} 🤡 @{hater}"
            success, response = post_comment(token, post_id, final_comment)

            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"[{timestamp}] {'✅' if success else '❌'} {final_comment} → {response[:50]}...")

            token_index += 1
            comment_index += 1
            time.sleep(delay)

    threading.Thread(target=run, daemon=True).start()
