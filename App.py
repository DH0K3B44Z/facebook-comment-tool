from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>𝗧𝗛𝟯 𝗟𝟯𝗝𝟯𝗡𝗗 𝗙𝗨𝗖𝗞𝟯𝗥 𝗦𝗔𝗜𝗜𝗠 <3</title>
    <style>
        body {
            background-image: url('https://i.pinimg.com/originals/54/94/66/5494660b8b139e5ef7e58e9286c1a570.jpg');
            background-size: cover;
            color: white;
            font-family: 'Courier New', monospace;
            text-shadow: 1px 1px 2px black;
        }
        .panel {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 20px;
            max-width: 600px;
            margin: 60px auto;
            box-shadow: 0 0 20px lime;
        }
        input[type="text"], input[type="url"], textarea {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid lime;
            border-radius: 5px;
            background: #111;
            color: #0f0;
        }
        button {
            padding: 10px 20px;
            background-color: lime;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            color: black;
            font-weight: bold;
        }
        h1 {
            text-align: center;
            font-size: 28px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="panel">
        <h1>𝗧𝗛𝟯 𝗟𝟯𝗝𝟯𝗡𝗗 𝗙𝗨𝗖𝗞𝟯𝗥 𝗦𝗔𝗜𝗜𝗠 &lt;3</h1>
        <form method="POST">
            <label>Facebook Token:</label>
            <input type="text" name="token" required>
            
            <label>Post Link:</label>
            <input type="url" name="post" required>
            
            <label>Comment Message:</label>
            <textarea name="message" rows="3" required></textarea>

            <label>Haters Name (Optional):</label>
            <input type="text" name="haters">
            
            <label>Delay Between Comments (seconds):</label>
            <input type="text" name="delay" value="60">
            
            <button type="submit">Start Commenting</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        token = request.form.get('token')
        post = request.form.get('post')
        message = request.form.get('message')
        haters = request.form.get('haters')
        delay = request.form.get('delay')

        print("=== Form Submitted ===")
        print("Token:", token)
        print("Post:", post)
        print("Message:", message)
        print("Haters:", haters)
        print("Delay:", delay)
        print("======================")

        return "Form submitted successfully at " + str(datetime.datetime.now())

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
