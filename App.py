from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def control_panel():
    if request.method == 'POST':
        os.makedirs("files", exist_ok=True)

        with open("files/tokens.txt", "w") as f:
            f.write(request.form['tokens'])

        with open("files/thread.txt", "w") as f:
            f.write(request.form['thread'])

        with open("files/messages.txt", "w") as f:
            f.write(request.form['messages'])

        with open("files/time.txt", "w") as f:
            f.write(request.form['time_interval'])

        with open("files/haters.txt", "w") as f:
            f.write(request.form['haters_name'])

        return "✅ All files saved successfully. Tool can be launched now!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)
