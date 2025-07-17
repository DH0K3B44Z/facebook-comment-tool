from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Save haters name
        haters_name = request.form.get('hatersname')
        with open('hatersname.txt', 'w', encoding='utf-8') as f:
            f.write(haters_name)

        # Save time interval
        time_interval = request.form.get('timeinterval')
        with open('timeinterval.txt', 'w') as f:
            f.write(time_interval)

        # Save message file
        message_file = request.files.get('messages')
        if message_file:
            message_file.save('messages.txt')

        # Save post link
        post_link = request.form.get('postlink')
        with open('postlink.txt', 'w') as f:
            f.write(post_link)

        # Save token file
        token_file = request.files.get('tokens')
        if token_file:
            token_file.save('tokens.txt')

        return redirect(url_for('success'))

    return render_template('index.html')


@app.route('/success')
def success():
    return "✅ Data received successfully! You can now run your commenting tool."

if __name__ == '__main__':
    app.run(debug=True)
