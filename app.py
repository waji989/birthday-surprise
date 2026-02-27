from flask import Flask, render_template, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    birthday_quote = (
        "Happy Birthday, my favorite human! You’ve officially reached the age where wisdom and mischief meet perfectly, "
        "and somehow, you still look ridiculously good doing it! 😎🎂 I love how you make me laugh at the silliest things, "
        "how you steal the blankets at night, and how you somehow know exactly what I’m thinking before I say a word. "
        "Life with you is never boring—it’s a beautiful mix of romance, chaos, laughter, and love. 🌈💫 Today is all about "
        "you—your smile, your laughter, and yes, your cake-eating skills 🍰😜. I hope you know that growing older doesn’t "
        "make you less amazing—it makes you even more irresistible, more inspiring, and more lovable. You are my heart, "
        "my home, and my happiness all rolled into one perfect human. So, let’s celebrate like there’s no tomorrow, "
        "eat cake until we regret it, laugh until our cheeks hurt, and love like we always do. Happy Birthday, my partner "
        "in crime and in love! 🥳❤️💌"
    )
    
    try:
        # Try to load your beautiful starry night template
        return render_template("index.html", quote=birthday_quote)
    except Exception as e:
        # If the template fails, show the quote on a plain background so the site doesn't crash
        return render_template_string(f"""
            <html>
                <body style="background: black; color: pink; font-family: sans-serif; padding: 50px; text-align: center;">
                    <h1>Oops! The styling didn't load, but the message is here:</h1>
                    <p style="font-size: 20px;">{birthday_quote}</p>
                    <p style="color: gray;">Error details: {str(e)}</p>
                </body>
            </html>
        """)

if __name__ == "__main__":
    app.run(debug=True)
