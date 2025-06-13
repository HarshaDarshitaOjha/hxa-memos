from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    target_date = datetime(2025, 6, 28)
    today = datetime.now()
    days_left = (target_date - today).days

    love_reasons = [
        "You always know how to make me smile",
        "You support my dreams like they’re your own",
        "You make even boring days beautiful",
    ]

    return render_template("index.html", days_left=days_left, love_reasons=love_reasons)

if __name__ == '__main__':
    app.run(debug=True)