import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 1. Define the quote
    quote = "Happy Birthday, my favorite human! You’ve officially reached the age where wisdom and mischief meet perfectly... [rest of your quote]"
    
    # 2. Check if the file actually exists where Flask expects it
    expected_path = os.path.join(app.root_path, 'templates', 'index.html')
    
    if not os.path.exists(expected_path):
        return f"CRITICAL ERROR: I looked for the file at {expected_path} but it is NOT there. Check your folder names!"

    try:
        return render_template("index.html", quote=quote)
    except Exception as e:
        return f"SMART ERROR: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
